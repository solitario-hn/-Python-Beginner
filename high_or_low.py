from logo import highlow_logo , data
import random

def get_values(choice):
    selected_keys=["name", "description","country"]
    result=""
    for key, value in choice.items():                                #using for loop and selected keys condition to get the desired values printed out of the dict.
        if key in selected_keys:
            result+=f"{key}:{value}\n"
    return result   


def high_or_low():  
    print(highlow_logo)
    print("Hey! Ready to play a cool game? Let's start\nYou lose , game restarts so make sure you score a hatrick!\n")

    user_score=0
    win=1
    while win==1:               #using while loop so scores keep adding up until user loses i.e. win=0.
        
        Choice_A=random.choice(data)
        print(f"COMPARE A: {get_values(Choice_A)}")

        A=Choice_A["follower_count"]  
        
        data.remove(Choice_A)
        Choice_B=random.choice(data)
        print(f"AGAINST B: {get_values(Choice_B)}")
        B=Choice_B["follower_count"]
        print(f"Your current Score:{user_score}")
        user_choice=input("Who do you think has more instagram followers? Type 'A' or 'B' to choose: ").upper()

        def score(choice):
            win=1
            if choice=='A' and A>B:
                print("Hurray you won!")
                return 1 ,win               #using return to keep adding 1-1 points in user_score.
            elif choice=='B' and B>A:
                print("Hurray you won!")
                return 1 ,win
            else:
                print("You lost the streak.\nGAME OVER!")
                win=0
                return 0 , win
                

        points,win=score(choice=user_choice)               #returning two values from the score function and storing it under two variables win,points.
        user_score+=points                                 #using points obtained after calling score function to add in user_score
        
        if win==0:
            print("\n"*100)          
            print(f"Better Luck Next time\nYour final score:{user_score}")


high_or_low()
will=input("DO YOU WISH TO PLAY ONE MORE ROUND , TYPE 'Y' OR 'N':").upper()
if will=='Y':
    high_or_low()                                    #used recursion after asking user input.
elif will=='N':
    print("SEE YOU NEXT TIME....")








      
        


