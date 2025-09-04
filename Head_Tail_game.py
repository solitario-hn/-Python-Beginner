#CREATING HEAD OR TAIL GENERATOR
import random
a=random.randint(1,100)
if a%2==0:
    print("HEADS!!")
else:
    print("TAILS!!")
print(f"your lucky number was {a}")    
    
#CREATING HEAD TAIL GENERATOR USING LISTS
coinside=list(("HEADS","TAILS"))
print(random.choice(coinside))

#CREATING A ROCK PAPER SCISSORS GAME
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("WELCOME TO THE ROCK PAPER SCISSORS GAME RULES:\n1.Rock crushes Scissors\n2.Scissors cut Paper\n3.Paper covers Rock")
print("CHOOSE '1' FOR ROCK , '2' FOR PAPER '3' FOR SCISSORS")
game_images=list((rock,paper,scissors))
computer=random.randint(1,3)
you=int(input("ENTER YOUR CHOICE:  "))
if you==computer:
    print(f"YOUR CHOICE:\n " , game_images[you])
    print(f"COMPUTER CHOICE:\n{game_images[computer]}\n")
    print("IT'S A DRAW")
elif you==1 and computer==2:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")
    print("OOPS YOU LOSE!")
elif you==2 and computer==1:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")
    print(f"YOU WON!!")
elif you==3 and computer==1:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")
    print(f"YOU WON!!")
elif you==1 and computer==2:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")
    print("YOU LOSE!!")
elif you==1 and computer==3:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")
    print("YOU LOSE!!")
elif you==2 and computer==3:
    print(f"your choice:\n{game_images[you -1]}")
    print(f"computer choice:\n{game_images[computer -1]}")    
    print("YOU LOSE!!")
else:
    print("YOU BROKE THE GAME!")
    
        
         
            