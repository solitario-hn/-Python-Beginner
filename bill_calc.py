print("day2.py")
#, using strings integeres _ and , in integers , boolean and float #exercise to count letters in your name
#using if else to show error 
name=(input('PLEASE ENTER YOUR NAME :'))
if type(name) == str :
    length=len(name)
    print("number of characters in your name:",length)
else:
    print("ERROR ONLY ALPHABETS!!")
#using type() function to know datatype 
print(type("hello"),"\n",type(1234),"\n",type(123.789),"\n",type(False))       #, is enoughN777788

#using fstring and using {} to insert in variables in an ongoing string , subscripting
user_name=input("ENTER YOUR USERNAME: ")
Height=int(input("Enter your height: "))
Weight=(input("Your weight in kg:\n"))
print(f"Your name is {user_name} \n Your height is {Height} \n Your weight is {Weight}")
print(type(Weight))


#   DAY2 PROJECT BILL CALCULATOR ONLY WANT TWO DECIMAL POINTS 
print("WELCOME TO YOUR BILL BUDDY")
bill=float(input("What is the total bill?\n"))
tip=int(input("How much tip would you like to give?\n"))
split=int(input("How many people are there to split the bill?\n"))
aftertip= bill/100*tip 
bill+=aftertip
pay=bill/split
print(f"Each person should pay:{round(pay,2)}")



