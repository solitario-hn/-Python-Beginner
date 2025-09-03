from logo import AUCTION_LOGO_BANNER
print(AUCTION_LOGO_BANNER)
print("                WELCOME TO THE BLIND AUCTION \n")
bidding={}
winning=[]          #creating an empty list in order to compare highest int bid later
option=True
while option==True:                       #so loop doesn't stop till option is false (user says no)
    
    name=input("Please Enter your name: ").capitalize()
    bid_amt=int(input("Please Enter the amount you'd like to bid:$"))
    bidding[name]=bid_amt
    choice=input("Are there any other users wanting to bid?  'yes' or 'no' ").lower()
    if choice=='no':
        option=False
        
        for user in bidding:
            win=bidding[user]
            winning.append(win)                    #creating a list with integers to compare max value
            
        winner=max(winning)           #max func to take out max value from list    
        winn=list(bidding.keys())[list(bidding.values()).index(winner)]
        print('\n'*50)    
        print("The bidding has been over\nHere are your results:")   
        print(f"The winner of this blind auction is {winn} with highest bidding of ${winner}")
    else:
        print("\n"*100)                             #subscripting by individually converting 
                                                    #keys and values into list and using index funciton
        
        
        
