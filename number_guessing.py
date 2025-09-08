from logo import number_guess
import random


def game_mode(mode):
    if level=='hard':
        points=5
        print("You have 5 attempts to make the guess")
    elif level=='easy':
        points=10
        print("You have 10 attempts to make the guess")
    else:
        print("Wrong choice , ERROR!")

    for i in range(0,points):
        user_choice=int(input("Make a guess:  "))
        if points==0:
            print(f"0 points left the correct guess was {computer_guess} . \n Game over! YOU LOSE! \n Re-run the program to play again.")
        if user_choice<computer_guess:
            print("Too low\nGuess again.")
            points-=1
            print(f'Oops you only have {points} remaining.')
        elif user_choice>computer_guess:
            print("Too high\nGuess again")
            points-=1
            print(f"Oops you only have {points} remaining.")
        elif user_choice==computer_guess:
            print("HURRAY YOU WON!! GUESSED CORRECTLY")
            break

chance=1  
while chance==1:    
    print(number_guess)
    print("WELCOME TO THE NUMBER GUESSING GAME!!\nI'm thinking of a number between 1 and 100\nGUESS WISELY!!\n")

    computer_guess=random.randint(1,100)
    level=input("Choose a playing mode 'easy' or 'hard': ")
    game_mode(mode=level)
    choice=input("Do you wish to replay the game? 'y' or 'n' ")   
    if choice=='y':
        chance=1
    else:
        chance=0 


    




