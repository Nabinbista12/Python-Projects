import random
import time

def rock_paper_scissor():
    print("---------------------------------Welcome Rock-Paper-Scissor-----------------------------------")
    print()
    while True:
        li = ['rock', 'paper', 'scissor']
        computer_guess = random.choice(li)
        computer_num = li.index(computer_guess)

        ask_user = input("Enter 'q' to quit the program\nEnter '0' for 'rock'\nEnter '1' for 'paper'\nEnter '2' for 'scissor'\nYour Guess:  ")
        print()

        if ask_user == 'q':
            print()
            text = "Thanks for playing rock-paper-scissor games."
            for char in text:
                print(char, end='', flush=True)
                time.sleep(.1)
            print()
            break
        else:
            try:
                ask_user = int(ask_user)
                prompt_val = li[ask_user]

                if (ask_user == computer_num):
                    print("This is draw.")
                    print(f"You both has guess {prompt_val}.")
                    print()

                elif (ask_user == 0 and computer_guess == 'scissor') or (ask_user == 1 and computer_guess == 'rock') or (ask_user == 2 and computer_guess == 'paper'):
                    print("You won the game.")
                    print("Your Guess: ", prompt_val)
                    print("Computer Guess: ", computer_guess)
                    time.sleep(1)
                    print()
                
                else:
                    print("You lose the game.")
                    print("Your Guess: ", prompt_val)
                    print("Computer Guess: ", computer_guess)
                    time.sleep(1)
                    print()
            except:
                print("Please enter a correct option.")
                time.sleep(1)
                print()
            
            
                
rock_paper_scissor()
