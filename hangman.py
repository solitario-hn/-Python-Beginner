import random
from logo import word_list,HANGMAN_STAGES,hangman_logo


print("WELCOME TO \n",hangman_logo)

choose_word = random.choice(word_list)
placeholder=""
for letter in choose_word:
    placeholder+="_"
print(placeholder)

lives=6
game=False
correct_letters=""
while game!=True:
    display=""
    guess=input("guess a letter?\n").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")


    for letter in choose_word:
        if letter==guess:
            display+=letter
            correct_letters+=letter
        elif letter in correct_letters:
            display+=letter  
        else:
            display+="_" 
        
    print(display)
           
            

                       
    if guess not in choose_word:
        lives-=1
        print(f"OOPS!! {guess} not in the word , YOU LOSE A LIFE!")
        if lives==0:
            print("GAMEOVER1!1!1")
            print(f"YOU WERE TRYING TO GUESS {choose_word}")
            game=False
            break
    if lives<6:    
        print(HANGMAN_STAGES[6-lives]) 
        print(f"LIVES LEFT {lives}")   
    if "_" not in display:
        game=True 
        print(f"YOU GUESSED  {choose_word} CORRECT")
        print("YOU WIN THE GAME!")       
            
               

