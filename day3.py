        
#MAKING A PIZZA DELIVERY PROGRAM todo:workout their total bill based on all of their preferences
print("WELCOME TO DANGO PIZZA DELIVERY\nWHAT WOULD YOU LIKE TO ORDER TODAY?")
size=input("CHOOSE 'C' FOR A CLASSIC , 'M' FOR A MEDIUM , AND 'P' PARTY PACK FOR LARGE ")
bill=0
Choice="no"
if size=='C':
    bill=100
    print("you would have to pay rs.100")
elif size=='M':
    bill=150
    print("you would have to pay RS.150")
elif size=="P":
    bill=200
    print("you would have to pay rs.200")
else:
    print("choose a correct size")
toppings=input("DO YOU WISH TO ADD ANY EXTRA TOPPING , CHOOSE 'YES' OR 'NO'.")
if toppings=='YES':
        print("EACH EXTRA TOPPING WOULD COST YOU RS.30")
        bill+=30
        choice=input("which topping would you like to choose \n1.mushrooms\n2.capsicum\n3.onion\n4.pepperoni\n")
        Choice=choice
        print(f"we've added {Choice} to your pizza")
else:
        print(f"you've not chosen any extra toppings")
        
cheese=input("DO YOU WANT EXTRA CHEESE? IT COSTS RS.20 PER PIZZA , 'Yes' FOR YES 'No' FOR No.")   
if cheese=='Yes':
        bill+=20
        print("we've added extra cheese to your pizza")
else:
        print("no cheese")
amt=int(input("How many pizza do you want?  "))        
total_bill=bill*amt
print(f"you've opted for {size} size pizza with {Choice} toppings and {cheese} for cheese.\n your total bill is {total_bill}")    
        
       
print("WELCOME TO THE TREASURE LAND \n YOUR MISSION IS TO FIND THE TREAURE!!")
your_way=input("AHA CHOOSE YOUR WAY WISELY! LEFT OR RIGHT?\n")
if your_way=="LEFT":
    nextstep=input("DO YOU WISH TO SWIM OR WAIT FOR THE BOAT\n")
    if nextstep=="WAIT":
        print("HURRAY YOU TOOK THE RIGHT STEP!\nNOW YOU HAVE THREE DOORS IN FRONT OF YOU,WHICH ONE WILL YOU CHOOSE?\n")
        door=(input("1.RED\n2.BLUE\n3.YELLOW\n"))
        if door=="RED":
            print("Game Over!")
        elif door=="BLUE":
            print("GAME OVER!")
        elif door=="YELLOW":
            print("HURRAYYYY YOU WIN!!")
        else:
            print("You broke the game")
    else :
        print("oops the crocodiles ate you.")            
else:
        print("GAME OVER!")    
                
