from flask import Flask, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Question
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brainquest.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        category = request.form.get('category')
        difficulty = request.form.get('difficulty')
        questions = Question.query.filter_by(category=category, difficulty=difficulty).all()
        return render_template('quiz.html', questions=questions)
    return render_template('quiz.html')

@app.route('/leaderboard')
def leaderboard():
    users = User.query.order_by(User.score.desc()).all()
    return render_template('leaderboard.html', users=users)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    score = 0
    for question_id in request.form:
        question = Question.query.get(question_id)
        if question and request.form[question_id] == question.answer:
            score += 1

    user = User.query.get(user_id)
    user.score += score
    db.session.commit()
    flash(f'Your score: {score}', 'success')
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)