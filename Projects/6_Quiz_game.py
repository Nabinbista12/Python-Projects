import requests
import time
import random

url = 'https://the-trivia-api.com/v2/questions/'
ques_no = 1
score = 0

print("----------------------------------------------------------------")
print("-------------------------Welcome to-----------------------------")
print("-------------------------QUIZ GAME------------------------------")
print("----------------------------------------------------------------")
while True:
    print()
    print("--------------------------Press Any Key to continue-----------------")
    print()
    print()
    prompt = input("Enter 'q' to quit the program or press any key to play quiz: ")
    print()
    
    if prompt == 'q':
        break
    else:
        print("Question no:", ques_no)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            li = []
            for x in data:
                li.append(x['category'])
            
            print("Category: ")
            for key, value in enumerate(li):
                print(str(key) + ":", value)
            print()
            
            val = int(input("Choose number to choose which category you want to play: "))
            print()
            question = data[val]["question"]["text"]
            print(question)
            print()
            
            options = [data[val]['correctAnswer']]
            for x in data[val]['incorrectAnswers']:
                options.append(x)

            # print(options)
            random.shuffle(options)
            for key, value in enumerate(options, start=0):
                print(str(key) + ":", value)
                
            print()
            answer = int(input("Enter correct option: "))
            print(options[answer])
            
            if options[answer] == data[val]['correctAnswer']:
                print("You were correct.")
                print("The correct answer is:", data[val]['correctAnswer'])
                score += 1
                print("Your Score:", score)
                ques_no += 1
                print()
                print()
            else:
                print("You were wrong.")
                print("The correct answer is:", data[val]['correctAnswer'])
                print("Your Score:", score)
                ques_no += 1
            
            time.sleep(2)
                
        else:
            print("Falied to fetch data")
    
# while True:
#     prompt = input("Enter 'q' to quit or press any key to press: ")
[{'category': 'geography', 'id': '622a1c357cc59eab6f94ffd8', 'correctAnswer': 'Australia', 'incorrectAnswers': ['Hawaii', 'Cuba', 'Madagascar'], 'question': {'text': 'Which island country lies to the East of Mauritius?'}, 'tags': ['countries', 'geography'], 'type': 'text_choice', 'difficulty': 'medium', 'regions': [], 'isNiche': False}, 
 {'category': 'music', 'id': '622a1c347cc59eab6f94fb95', 'correctAnswer': '"Jumpin\', Jumpin\'" by Destiny\'s Child', 'incorrectAnswers': ['"A Thousand Miles" by Vanessa Carlton', '"Baby Got Back" by Sir Mix-a-Lot', '"Hurt" by Nine Inch Nails'], 'question': {'text': 'Which song begins with the lyrics: "Ladies leave your man at home, the club is full of ballers and their pockets full grown."?'}, 'tags': ['lyrics', 'music'], 'type': 'text_choice', 'difficulty': 'hard', 'regions': [], 'isNiche': False}, 
 {'category': 'geography', 'id': '622a1c357cc59eab6f94fe5b', 'correctAnswer': 'Afghanistan\xa0', 'incorrectAnswers': ['Iraq', 'Bangladesh', 'Sri Lanka'], 'question': {'text': 'In which Asian country is the Hindu Kush mountain range?'}, 'tags': ['asia', 'mountains', 'geography'], 'type': 'text_choice', 'difficulty': 'hard', 'regions': [], 'isNiche': False}, 
 {'category': 'history', 'id': '645c9f8742ea81e2554c5f41', 'correctAnswer': 'Hawaii', 'incorrectAnswers': ['Alaska', 'Puerto Rico', 'Guam'], 'question': {'text': 'Which U.S. territory was attacked 18 years before it became a state in 1959?'}, 'tags': ['usa', 'us_states', "1950's"], 'type': 'text_choice', 'difficulty': 'medium', 'regions': [], 'isNiche': False}, 
 {'category': 'geography', 'id': '6237403bcb85f7ce9e949ce9', 'correctAnswer': 'Dominica', 'incorrectAnswers': ['Romania', 'Sierra Leone', 'Antigua and Barbuda'], 'question': {'text': 'Roseau is the capital city of which country?'}, 'tags': ['capital_cities', 'cities', 'geography'], 'type': 'text_choice', 'difficulty': 'hard', 'regions': [], 'isNiche': False}, 
 {'category': 'music', 'id': '622a1c357cc59eab6f94feb0', 'correctAnswer': 'Beyoncé', 'incorrectAnswers': ['Madonna', 'Drake', 'Nicki Minaj'], 'question': {'text': "Which American singer, actress and record producer released the song 'Lift Off'?"}, 'tags': ['songs', 'music'], 'type': 'text_choice', 'difficulty': 'medium', 'regions': [], 'isNiche': False}, 
 {'category': 'history', 'id': '65056f817a97013de78b5461', 'correctAnswer': 'Vladimir Putin', 'incorrectAnswers': ['Boris Yeltsin', 'Dmitry Medvedev', 'Mikhail Gorbachev'], 'question': {'text': 'Who became president of Russia in 2012?'}, 'tags': ['history', 'world_leaders', 'politics', 'russia', "2010's"], 'type': 'text_choice', 'difficulty': 'easy', 'regions': [], 'isNiche': False},
 {'category': 'music', 'id': '622a1c357cc59eab6f94fd97', 'correctAnswer': 'Mariah Carey', 'incorrectAnswers': ['Rihanna', 'Beyonce', 'Christina Aguilera'], 'question': {'text': 'Which Singing Diva Flopped At The Box Office With Her Debut Movie “Glitter”?'}, 'tags': ['people', 'music'], 'type': 'text_choice', 'difficulty': 'hard', 'regions': [], 'isNiche': False}, 
 {'category': 'geography', 'id': '622a1c357cc59eab6f94fdeb', 'correctAnswer': 'Nevada', 'incorrectAnswers': ['Arizona', 'Colorado', 'Alaska'], 'question': {'text': 'Which U.S. state has the least rainfall?'}, 'tags': ['us_states', 'usa', 'meteorology', 'geography'], 'type': 'text_choice', 'difficulty': 'hard', 'regions': [], 'isNiche': False}, 
 {'category': 'society_and_culture', 'id': '645cb1627d263fd5097043bf', 'correctAnswer': 'Alpha & Omega', 'incorrectAnswers': ['Beta & Gamma', 'Sigma & Tau', 'Delta & Epsilon'], 'question': {'text': 'What are the first and last letters of the Greek alphabet?'}, 'tags': ['alphabet', 'society_and_culture', 'ancient_greece'], 'type': 'text_choice', 'difficulty': 'medium', 'regions': [], 'isNiche': False}]