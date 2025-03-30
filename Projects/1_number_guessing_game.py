import random
import time

print("Hello, Welcome to the Number guessing game")
computer_guess = random.randint(1, 100)

print("Enter 'q' to quit the game wherever you want: ")

while True:
    ask_user_prompt = input("Guess the Number: ")
    if (ask_user_prompt == 'q'):
        print("...")
        time.sleep(2)
        quit_show = "Quitting the game..."
        for char in quit_show:
            print(char, end='')
            time.sleep(.1)
        break
    else:
        while True:
            if not (int(ask_user_prompt.isdigit())):
                print("Please enter a number not a character: ")
                ask_user_prompt = input("Guess the number: ")
            else:
                break
            
        ask_user_prompt = int(ask_user_prompt)

        if ask_user_prompt == computer_guess:
            print("Congratulation! You won")
            show_prompt = f"Computer Guess: {computer_guess}."
            for char in show_prompt:
                print(char, end="")
                time.sleep(.1)

            show_prompt = f"Your Guess: {ask_user_prompt}."
            for char in show_prompt:
                print(char, end="")
                time.sleep(.1)

            print()

            show_prompt = "Play Again"
            print("Play Again")
            for char in show_prompt:
                print(char, end="")
                time.sleep(.1)
            print()

            ask_user = input("Enter 'q' to quit and press any key to play again: ")
            if ask_user == 'q':
                print("...")
                time.sleep(2)
                quit_show = "Quitting the game..."
                for char in quit_show:
                    print(char, end='')
                    time.sleep(.1)
                break
            else:
                computer_guess = random.randint(1, 100)
        elif ask_user_prompt < computer_guess:
            print(f"Your guess: {ask_user_prompt}")
            print("Guess Bigger Number")
        elif ask_user_prompt > computer_guess:
            print(f"Your guess: {ask_user_prompt}")
            print("Guess Smaller Number")

