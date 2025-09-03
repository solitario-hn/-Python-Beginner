#testing out print function , + , \n method
print("Marvel is the peak \n jaat said no\n But he is a liar")
print("yo" + "he"+ " gay")                     #\n not /n , + works #line continuation char works only in string not separately
print("nidhi + patel")                          #but + acts like a string if in comma \n needs to be in string

#using  int , input and print function 
Username=input("What is your name?\n")
password=int(input("Use a strong password:\n"))
print("CONGRATS!\nYOUR ","Username=",Username,"and","password=",password,"has been saved."+"\nThankyou")
xyz="YOUR USERNAME IS: "
print(len(Username))
print(len(Username)+len(xyz))
#recalling needs only naming and no "" otherwise behaves as a string + can't be used in a "" behvaes as a strng value , int used to take base 10 decimal value just add besides input
#add comma while recalling otherwise print shows error or any term besides string
#input function runs first then print
#len fucntion doesn't works on integer values , neither on print , only use in string


#Exercise - to take username and find lenght
user_name=input("HEY DEAR , WHAT IS YOUR NAME?\n")
Length=print("The number of characters in your name present are: ",len(user_name))

#Always use a comma after strings if using any function + or len() like.

#DAY1 BAND NAME GENERATOR PROJECT 
print("WELCOME TO EXQUISITE BAND NAME GENERATOR")
name=input("What's the name of the city you grew in?\n")
favourite_snack=input("What's your favourite snack?\n")
lucky_number=int(input("Enter your lucky number:\n"))
print("YOUR BAND NAME COULD BE:",name + "" + favourite_snack,lucky_number)
print(name,user_name+"1233")

#,VARIABLE, ADDS A SPACE BY DEFAULT NO NEED TO USE VARIABLE AND + AS SHOWS EERROR + FUCNTION ONLY IS USED TO SUM TWO STRNGS or one string one var NOT two VARIABLES.
#ANOTHER WAY TO USE + AND VAR TOGETHER IS TO ADD A BLANK STRING BEFORE IN B/W ADDING TWO VAR TOGETHER LIKE VAR1 + ""+ VAR2 THIS WILL PREVENT TWO VAR ADD ERROR.
