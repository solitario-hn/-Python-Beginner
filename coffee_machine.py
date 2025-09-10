#TODO:1.creating a welcome screen for the coffee machine





menu = {
    "espresso": {
        "ingredients": {
            "water": 50,      # in ml
            "milk": 0,        # in ml
            "coffee": 18,     # in grams
            "sugar": 5        # in grams
        },
        "cost": 1.5          # in dollars
    },
    "cappuccino": {
        "ingredients": {
            "water": 30,
            "milk": 80,
            "coffee": 18,
            "sugar": 5
        },
        "cost": 2.5
    },
    "latte": {
        "ingredients": {
            "water": 20,
            "milk": 100,
            "coffee": 18,
            "sugar": 5
        },
        "cost": 3
    },
    "americano": {
        "ingredients": {
            "water": 100,
            "milk": 0,
            "coffee": 18,
            "sugar": 5
        },
        "cost": 3.5
    }
}



coffee_logo = r"""
       ( (
        ) )
     ........
     |      |]
     \      /
      `----'
   _Coffee Machine_
"""


welcome=''' 
▄█     █▄     ▄████████  ▄█        ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████      
███     ███   ███    ███ ███       ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      
███     ███   ███    █▀  ███       ███    █▀  ███    ███ ███   ███   ███   ███    █▀       
███     ███  ▄███▄▄▄     ███       ███        ███    ███ ███   ███   ███  ▄███▄▄▄          
███     ███ ▀▀███▀▀▀     ███       ███        ███    ███ ███   ███   ███ ▀▀███▀▀▀          
███     ███   ███    █▄  ███       ███    █▄  ███    ███ ███   ███   ███   ███    █▄       
███ ▄█▄ ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███   ███   ███   ███    ███      
 ▀███▀███▀    ██████████ █████▄▄██ ████████▀   ▀██████▀   ▀█   ███   █▀    ██████████      
                         ▀                                                                 
                                                                                            '''
                                                                                            



cup='''☕'''                                                                                        
                
print(coffee_logo)
print(welcome,cup*50)

profit=0
resources={
    'water':300,
    'milk':200,
    'coffee':100,
    'sugar':100
}

def is_resource_sufficient(order_ingredients):
    '''Returns if there is sufficient ingredients in machine or not'''
    for items in order_ingredients:
        if order_ingredients[items]>=resources[items]:
            print(f"Sorry there's not sufficient {items} in machine.")
            return False
        else:
            return True
                
def process_coins():
    '''Returns total calculated coins'''
    print("Please insert coins.")                         #we can also use direct total assigning value in python since it executes line by line and perform mathematical operations on it line by line.
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received,cost):
    '''Return True if transaction is successful and False if it is unsuccessful'''
    if money_received>=cost:
        change=round(money_received-cost,2)
        global profit
        profit+=money_received
        print(f"Thankyou so much , here is your change ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money has been refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    '''dedcuts the resources used in the process'''
    for items in order_ingredients:
        global resources
        resources[items]-=order_ingredients[items]
    print(f"Here is your {drink_name} enjoy your coffee\nHave a great day!")
    
is_on=True
while is_on:
    user_choice=input("What would you like to have? Options:\n1.espresso\n2.cappuccino\n3.latte\n4.americano\n").lower()
    if user_choice=='off':
        is_on=False
        
    elif user_choice=='report':
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"sugar:90{resources['sugar']}g")
        print(f"coffee:8{resources['coffee']}g")
        print(f"Money:${profit}")
    elif user_choice=='latte' or 'espresso' or 'cappuccino' or 'americano':
        drink=menu[user_choice]
        condition=is_resource_sufficient(drink['ingredients'])
        if condition==True:
            money=process_coins()
            costing=menu[user_choice]['cost']
            if is_transaction_successful(money_received=money,cost=costing):  #this will return true and statemnt would run if false then stops.
                ingredients=menu[user_choice]
                make_coffee(user_choice,ingredients['ingredients'])           
            
            
            
         
            
            
            
        
        
        
                
  
        
    