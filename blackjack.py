import random
def add(n1,n2):
    return n1+n2


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
wish=input("Do you wish to play a blackjack game 'y' or 'n' ")

your_first_deck=random.choices(cards,k=2)
print(f"Your cards:{your_first_deck}\n")
your_score=add(your_first_deck[0],your_first_deck[1])
print(f"Your score:{your_score}\n")

computer_first_deck=random.choices(cards,k=2)
print(f"Computer's First card:{computer_first_deck[0]}")
computer_score=add(computer_first_deck[0],computer_first_deck[1])

if your_score==computer_score==21:
    print("It's a Draw")
elif your_score==21:
    print("You won")
elif computer_score==21:
    print("You lose")

   
if your_score>21:
    if 11 in your_first_deck:
        your_score+=1
        
            
