from app import app, db
from models import Question

# Sample questions to add
sample_questions = [
    # General Knowledge
    {
        'category': 'General Knowledge',
        'difficulty': 'easy',
        'question_text': 'What is the capital of France?',
        'answer': 'Paris',
        'options': 'Paris,London,Berlin,Madrid'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'easy',
        'question_text': 'What is the largest ocean on Earth?',
        'answer': 'Pacific Ocean',
        'options': 'Pacific Ocean,Atlantic Ocean,Indian Ocean,Arctic Ocean'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'easy',
        'question_text': 'Who wrote "Hamlet"?',
        'answer': 'William Shakespeare',
        'options': 'William Shakespeare,Charles Dickens,Mark Twain,J.K. Rowling'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'easy',
        'question_text': 'What is the currency of Japan?',
        'answer': 'Yen',
        'options': 'Yen,Dollar,Euro,Pound'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'easy',
        'question_text': 'What planet is known as the Red Planet?',
        'answer': 'Mars',
        'options': 'Mars,Venus,Jupiter,Saturn'
    },
    # Medium
    {
        'category': 'General Knowledge',
        'difficulty': 'medium',
        'question_text': 'Who painted the Mona Lisa?',
        'answer': 'Leonardo da Vinci',
        'options': 'Leonardo da Vinci,Picasso,Van Gogh,Rembrandt'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'medium',
        'question_text': 'What is the smallest country in the world?',
        'answer': 'Vatican City',
        'options': 'Vatican City,Monaco,Nauru,Malta'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'medium',
        'question_text': 'In which year did the Titanic sink?',
        'answer': '1912',
        'options': '1912,1914,1916,1918'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'medium',
        'question_text': 'What is the longest river in the world?',
        'answer': 'Nile',
        'options': 'Nile,Amazone,Yangtze,Mississippi'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'medium',
        'question_text': 'Who was the first person to walk on the moon?',
        'answer': 'Neil Armstrong',
        'options': 'Neil Armstrong,Buzz Aldrin,Michael Collins,Yuri Gagarin'
    },
    # Hard
    {
        'category': 'General Knowledge',
        'difficulty': 'hard',
        'question_text': 'What is the capital of Bhutan?',
        'answer': 'Thimphu',
        'options': 'Thimphu,Katmandu,Delhi,Colombo'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'hard',
        'question_text': 'Who discovered penicillin?',
        'answer': 'Alexander Fleming',
        'options': 'Alexander Fleming,Marie Curie,Louis Pasteur,Joseph Lister'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'hard',
        'question_text': 'What is the main ingredient in traditional Japanese miso soup?',
        'answer': 'Miso',
        'options': 'Miso,Soy Sauce,Tofu,Rice'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'hard',
        'question_text': 'Who was the first female Prime Minister of the UK?',
        'answer': 'Margaret Thatcher',
        'options': 'Margaret Thatcher,Theresa May,Angela Merkel,Indira Gandhi'
    },
    {
        'category': 'General Knowledge',
        'difficulty': 'hard',
        'question_text': 'What is the hardest natural substance on Earth?',
        'answer': 'Diamond',
        'options': 'Diamond,Gold,Iron,Quartz'
    },
    
    # Science
    {
        'category': 'Science',
        'difficulty': 'easy',
        'question_text': 'What is the chemical symbol for water?',
        'answer': 'H2O',
        'options': 'H2O,O2,CO2,N2'
    },
    {
        'category': 'Science',
        'difficulty': 'easy',
        'question_text': 'What planet is known for its rings?',
        'answer': 'Saturn',
        'options': 'Saturn,Jupiter,Earth,Mars'
    },
    {
        'category': 'Science',
        'difficulty': 'easy',
        'question_text': 'What gas do plants absorb from the atmosphere?',
        'answer': 'Carbon Dioxide',
        'options': 'Carbon Dioxide,Oxygen,Nitrogen,Hydrogen'
    },
    {
        'category': 'Science',
        'difficulty': 'easy',
        'question_text': 'What is the powerhouse of the cell?',
        'answer': 'Mitochondria',
        'options': 'Mitochondria,Nucleus,Ribosome,Chloroplast'
    },
    {
        'category': 'Science',
        'difficulty': 'easy',
        'question_text': 'What is the boiling point of water?',
        'answer': '100°C',
        'options': '100°C,90°C,80°C,110°C'
    },
    # Medium
    {
        'category': 'Science',
        'difficulty': 'medium',
        'question_text': 'What is the speed of light?',
        'answer': '299792458 m/s',
        'options': '299792458 m/s,150000000 m/s,300000000 m/s,100000000 m/s'
    },
    {
        'category': 'Science',
        'difficulty': 'medium',
        'question_text': 'What is the most abundant gas in the Earth\'s atmosphere?',
        'answer': 'Nitrogen',
        'options': 'Nitrogen,Oxygen,Carbon Dioxide,Argon'
    },
    {
        'category': 'Science',
        'difficulty': 'medium',
        'question_text': 'What is the process by which plants make their food?',
        'answer': 'Photosynthesis',
        'options': 'Photosynthesis,Respiration,Transpiration,Digestion'
    },
    {
        'category': 'Science',
        'difficulty': 'medium',
        'question_text': 'What is the chemical formula for table salt?',
        'answer': 'NaCl',
        'options': 'NaCl,KCl,CaCl2,MgCl2'
    },
    {
        'category': 'Science',
        'difficulty': 'medium',
        'question_text': 'What is the main organ of the circulatory system?',
        'answer': 'Heart',
        'options': 'Heart,Lungs,Liver,Kidneys'
    },
    # Hard
    {
        'category': 'Science',
        'difficulty': 'hard',
        'question_text': 'What is the pH level of pure water?',
        'answer': '7',
        'options': '7,6,8,5'
    },
    {
        'category': 'Science',
        'difficulty': 'hard',
        'question_text': 'What is the name of the first artificial satellite launched into space?',
        'answer': 'Sputnik',
        'options': 'Sputnik,Explorer 1,Apollo 11,Mir'
    },
    {
        'category': 'Science',
        'difficulty': 'hard',
        'question_text': 'What is the theory that explains the origin of the universe?',
        'answer': 'Big Bang Theory',
        'options': 'Big Bang Theory,Steady State Theory,Quantum Theory,Relativity'
    },
    {
        'category': 'Science',
        'difficulty': 'hard',
        'question_text': 'What is the most common isotope of carbon?',
        'answer': 'Carbon-12',
        'options': 'Carbon-12,Carbon-13,Carbon-14,Carbon-15'
    },
    {
        'category': 'Science',
        'difficulty': 'hard',
        'question_text': 'What is the name of the process by which a solid turns directly into a gas?',
        'answer': 'Sublimation',
        'options': 'Sublimation,Evaporation,Condensation,Deposition'
    },
    
    # History
    {
        'category': 'History',
        'difficulty': 'easy',
        'question_text': 'Who was the first President of the United States?',
        'answer': 'George Washington',
        'options': 'George Washington,Thomas Jefferson,Abraham Lincoln,John Adams'
    },
    {
        'category': 'History',
        'difficulty': 'easy',
        'question_text': 'In which year did World War II end?',
        'answer': '1945',
        'options': '1945,1944,1946,1947'
    },
    {
        'category': 'History',
        'difficulty': 'easy',
        'question_text': 'Who was known as the Iron Lady?',
        'answer': 'Margaret Thatcher',
        'options': 'Margaret Thatcher,Angela Merkel,Indira Gandhi,Golda Meir'
    },
    {
        'category': 'History',
        'difficulty': 'easy',
        'question_text': 'What ancient civilization built the pyramids?',
        'answer': 'Egyptians',
        'options': 'Egyptians,Greeks,Romans,Mayans'
    },
    {
        'category': 'History',
        'difficulty': 'easy',
        'question_text': 'Who was the first man to circumnavigate the globe?',
        'answer': 'Ferdinand Magellan',
        'options': 'Ferdinand Magellan,Christopher Columbus,James Cook,Marco Polo'
    },
    # Medium
    {
        'category': 'History',
        'difficulty': 'medium',
        'question_text': 'What year did the Berlin Wall fall?',
        'answer': '1989',
        'options': '1989,1990,1988,1987'
    },
    {
        'category': 'History',
        'difficulty': 'medium',
        'question_text': 'Who was the first female Prime Minister of India?',
        'answer': 'Indira Gandhi',
        'options': 'Indira Gandhi,Sonia Gandhi,Pratibha Patil,Meira Kumar'
    },
    {
        'category': 'History',
        'difficulty': 'medium',
        'question_text': 'What was the main cause of the American Civil War?',
        'answer': 'Slavery',
        'options': 'Slavery,Taxation,States Rights,Expansion'
    },
    {
        'category': 'History',
        'difficulty': 'medium',
        'question_text': 'In which year did the Titanic sink?',
        'answer': '1912',
        'options': '1912,1914,1916,1918'
    },
    {
        'category': 'History',
        'difficulty': 'medium',
        'question_text': 'Who was the first woman to fly solo across the Atlantic?',
        'answer': 'Amelia Earhart',
        'options': 'Amelia Earhart,Bessie Coleman,Harriet Quimby,Jacqueline Cochran'
    },
    # Hard
    {
        'category': 'History',
        'difficulty': 'hard',
        'question_text': 'What year did the French Revolution begin?',
        'answer': '1789',
        'options': '1789,1792,1787,1791'
    },
    {
        'category': 'History',
        'difficulty': 'hard',
        'question_text': 'Who was the last Emperor of Russia?',
        'answer': 'Nicholas II',
        'options': 'Nicholas II,Alexander III,Peter the Great,Catherine the Great'
    },
    {
        'category': 'History',
        'difficulty': 'hard',
        'question_text': 'What was the main event that triggered World War I?',
        'answer': 'Assassination of Archduke Franz Ferdinand',
        'options': 'Assassination of Archduke Franz Ferdinand,Invasion of Poland,Attack on Pearl Harbor,The sinking of the Lusitania'
    },
    {
        'category': 'History',
        'difficulty': 'hard',
        'question_text': 'Who was the first President of South Africa after apartheid?',
        'answer': 'Nelson Mandela',
        'options': 'Nelson Mandela,Thabo Mbeki,F.W. de Klerk,Jacob Zuma'
    },
    {
        'category': 'History',
        'difficulty': 'hard',
        'question_text': 'What was the name of the ship that brought the Pilgrims to America?',
        'answer': 'Mayflower',
        'options': 'Mayflower,Discovery,Santa Maria,Endeavour'
    },
    
    # Sports
    {
        'category': 'Sports',
        'difficulty': 'easy',
        'question_text': 'What sport is known as "the beautiful game"?',
        'answer': 'Soccer',
        'options': 'Soccer,Basketball,Tennis,Baseball'
    },
    {
        'category': 'Sports',
        'difficulty': 'easy',
        'question_text': 'How many players are there in a football team?',
        'answer': '11',
        'options': '11,9,7,13'
    },
    {
        'category': 'Sports',
        'difficulty': 'easy',
        'question_text': 'In which sport do players use a racket?',
        'answer': 'Tennis',
        'options': 'Tennis,Basketball,Football,Hockey'
    },
    {
        'category': 'Sports',
        'difficulty': 'easy',
        'question_text': 'What is the national sport of Canada?',
        'answer': 'Lacrosse',
        'options': 'Lacrosse,Hockey,Baseball,Football'
    },
    {
        'category': 'Sports',
        'difficulty': 'easy',
        'question_text': 'Which country hosted the 2016 Summer Olympics?',
        'answer': 'Brazil',
        'options': 'Brazil,China,USA,UK'
    },
    # Medium
    {
        'category': 'Sports',
        'difficulty': 'medium',
        'question_text': 'Who holds the record for the most goals in World Cup history?',
        'answer': 'Marta',
        'options': 'Marta,Pele,Diego Maradona,Cristiano Ronaldo'
    },
    {
        'category': 'Sports',
        'difficulty': 'medium',
        'question_text': 'In which sport is the term "home run" used?',
        'answer': 'Baseball',
        'options': 'Baseball,Football,Basketball,Hockey'
    },
    {
        'category': 'Sports',
        'difficulty': 'medium',
        'question_text': 'Which country won the FIFA World Cup in 2018?',
        'answer': 'France',
        'options': 'France,Germany,Brazil,Argentina'
    },
    {
        'category': 'Sports',
        'difficulty': 'medium',
        'question_text': 'What is the maximum score in a game of ten-pin bowling?',
        'answer': '300',
        'options': '300,200,150,100'
    },
    {
        'category': 'Sports',
        'difficulty': 'medium',
        'question_text': 'Which sport is known as the "king of sports"?',
        'answer': 'Football',
        'options': 'Football,Basketball,Tennis,Cricket'
    },
    # Hard
    {
        'category': 'Sports',
        'difficulty': 'hard',
        'question_text': 'Who was the first athlete to win six Olympic gold medals in a single Games?',
        'answer': 'Mark Spitz',
        'options': 'Mark Spitz,Michael Phelps,Bobby Fischer,Usain Bolt'
    },
    {
        'category': 'Sports',
        'difficulty': 'hard',
        'question_text': 'What is the only sport to have been played on the moon?',
        'answer': 'Golf',
        'options': 'Golf,Tennis,Basketball,Baseball'
    },
    {
        'category': 'Sports',
        'difficulty': 'hard',
        'question_text': 'Which country has won the most Rugby World Cups?',
        'answer': 'New Zealand',
        'options': 'New Zealand,Australia,South Africa,England'
    },
    {
        'category': 'Sports',
        'difficulty': 'hard',
        'question_text': 'What is the highest possible break in snooker?',
        'answer': '147',
        'options': '147,155,140,150'
    },
    {
        'category': 'Sports',
        'difficulty': 'hard',
        'question_text': 'Who is the only player to have played in every World Cup since its inception?',
        'answer': 'Pele',
        'options': 'Pele,Diego Maradona,Cristiano Ronaldo,Lionel Messi'
    },
    
    # Technology
    {
        'category': 'Technology',
        'difficulty': 'easy',
        'question_text': 'What does CPU stand for?',
        'answer': 'Central Processing Unit',
        'options': 'Central Processing Unit,Computer Personal Unit,Central Program Unit,Computer Processing Unit'
    },
    {
        'category': 'Technology',
        'difficulty': 'easy',
        'question_text': 'What is the main function of an operating system?',
        'answer': 'Manage computer hardware and software',
        'options': 'Manage computer hardware and software,Run applications,Store data,Connect to the internet'
    },
    {
        'category': 'Technology',
        'difficulty': 'easy',
        'question_text': 'Which company developed the iPhone?',
        'answer': 'Apple',
        'options': 'Apple,Samsung,Nokia,Microsoft'
    },
    {
        'category': 'Technology',
        'difficulty': 'easy',
        'question_text': 'What does Wi-Fi stand for?',
        'answer': 'Wireless Fidelity',
        'options': 'Wireless Fidelity,Wireless Functionality,Wireless Frequency,Wireless Fiber'
    },
    {
        'category': 'Technology',
        'difficulty': 'easy',
        'question_text': 'What is the most widely used programming language?',
        'answer': 'JavaScript',
        'options': 'JavaScript,Python,Java,C++'
    },
    # Medium
    {
        'category': 'Technology',
        'difficulty': 'medium',
        'question_text': 'What is the primary language used for web development?',
        'answer': 'HTML',
        'options': 'HTML,CSS,JavaScript,PHP'
    },
    {
        'category': 'Technology',
        'difficulty': 'medium',
        'question_text': 'What does HTTP stand for?',
        'answer': 'HyperText Transfer Protocol',
        'options': 'HyperText Transfer Protocol,HyperText Transmission Protocol,HyperText Transport Protocol,HyperText Transfer Process'
    },
    {
        'category': 'Technology',
        'difficulty': 'medium',
        'question_text': 'Which company is known for its search engine?',
        'answer': 'Google',
        'options': 'Google,Bing,Yahoo,Ask'
    },
    {
        'category': 'Technology',
        'difficulty': 'medium',
        'question_text': 'What is the name of the first electronic computer?',
        'answer': 'ENIAC',
        'options': 'ENIAC,UNIVAC,IBM 701,Colossus'
    },
    {
        'category': 'Technology',
        'difficulty': 'medium',
        'question_text': 'What is the main purpose of a firewall?',
        'answer': 'To protect a network from unauthorized access',
        'options': 'To protect a network from unauthorized access,To speed up internet connection,To store data,To manage network traffic'
    },
    # Hard
    {
        'category': 'Technology',
        'difficulty': 'hard',
        'question_text': 'What is the name of the first computer virus?',
        'answer': 'Creeper',
        'options': 'Creeper,Brain,ILOVEYOU,Morris'
    },
    {
        'category': 'Technology',
        'difficulty': 'hard',
        'question_text': 'What is the primary function of a router?',
        'answer': 'To forward data packets between computer networks',
        'options': 'To forward data packets between computer networks,To store data,To connect devices,To manage traffic'
    },
    {
        'category': 'Technology',
        'difficulty': 'hard',
        'question_text': 'What does the term "cloud computing" refer to?',
        'answer': 'Storing and accessing data over the internet',
        'options': 'Storing and accessing data over the internet,Using local servers,Storing data on hard drives,Using USB drives'
    },
    {
        'category': 'Technology',
        'difficulty': 'hard',
        'question_text': 'What is the main purpose of an API?',
        'answer': 'To allow different software applications to communicate',
        'options': 'To allow different software applications to communicate,To store data,To manage user interfaces,To enhance security'
    },
    {
        'category': 'Technology',
        'difficulty': 'hard',
        'question_text': 'What programming language is primarily used for Android app development?',
        'answer': 'Java',
        'options': 'Java,Kotlin,C#,Swift'
    }
]

# Function to add questions to the database
def add_sample_questions():
    with app.app_context():
        for question in sample_questions:
            new_question = Question(
                category=question['category'],
                difficulty=question['difficulty'],
                question_text=question['question_text'],
                answer=question['answer'],
                options=question['options']  # Ensure options are included
            )
            db.session.add(new_question)
        db.session.commit()
        print("Sample questions added successfully!")

if __name__ == '__main__':
    add_sample_questions()