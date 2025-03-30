from faker import Faker
import time

fake = Faker()

def measure_typing():
    try:
        inp = int(input("Enter how much text you want to try: "))
        all_text = ""
        for _ in range(1):
            given_typing = fake.paragraph(nb_sentences=inp)
            all_text += given_typing
        print(all_text)
        print()
        print("Start typing")
        print()
        start = time.time()
        user_typing = input()
        end = time.time()

        acc = 0
        for i in range(len(all_text)):
            try:
                if all_text[i] == user_typing[i]:
                    acc += 1
            except:
                break

        typing_accuracy = (acc * 100) / len(all_text) 
        typing_speed = (len(user_typing) / (end - start)) * 60
        print(f"Your typing speed is {typing_speed} kpm with {typing_accuracy} accuracy.")
    except Exception as err:
        print("Some exception occured", err)


measure_typing()

