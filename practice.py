#using dictionaries in python

student={}
option=True

while option == True:
    student_name=input("Enter the student name:   ")
    student_score=int(input("Enter the student score:   "))
    if  90<student_score<100:             #giving regards according to percentage using if elif for conditions
        student_score='Outstanding'
    elif 80<student_score<90:
        student_score='Exceeds Expectations'
    elif 70<student_score<80:
        student_score='Acceptable'
    else:
        student_score='Fail'
    student[student_name]=student_score
    choice=input("Do you want to add more entries? 'yes' or 'no'\n")
    if choice=='no':
        option=False
        print(student)
    
    
#trying to curate nested lists in dictionary and taking it out using funcitons.

travel_log={
    "New Delhi":["Lodhi garden","Humayun Tomb", "Dlf Mall","Chandni Chowk"],
    "Mumbai":["Bandra","Sea Beach","B-town"]
}

print(travel_log["New Delhi"][2])                    #using subscripting as we use in lists double -accesses New Delhi and then gives value present at index '2'


#nesting and accessing elements in the nested list in dict.        
for i in travel_log:
    cor=travel_log[i]        #goes out into dictionary key names one by one and prints value
    print(cor)
    core=len(cor)                                 #using len func on list inside dict.(len counts the value length of each key)
    for key in range(0,core):
        sys=travel_log[i][key]                    #using range funct after using len(using double subscripting-first goes into keys -then into values -then accessing individual list values by using their index in particulr list)
        print(sys)
    for i in cor:
        print(i)                                   #using another loop after accessing cor=whole lists of each key



bidding={"hey":90,
         "hello":89,
         "jiyun":66,
}
winner=66
winn=list(bidding.keys())[list(bidding.values()).index(winner)]  #subscripting by individually converting keys and values into list and using index funciton
print(winn)



#a diiferent way of using max function
fruits={
    "banana":90,
    'oranges':89,
    "apple":67,
    'grapes':92
}

c=max(fruits,key=fruits.get)
print(c)

#getting the max value , using a for loop 
high_amt=0
fruit=""
for i in fruits:
    wgt=fruits[i]
    if wgt>high_amt:
        high_amt=wgt
        fruit=i
        
print(f'Highest amont of {fruit} with {high_amt} packets is present in home. ')    
    
    
#using dictionaries and assigning name to a funciton or making a variable act as a function

def quotient(n1,n2):
    '''divides n1 by n2 and puts out the quotient'''
    result=n1//n2
    return result
def power(n1,n2):
    '''n2 acts as exponent power to n1'''
    result=n1**n2
    return result

operations={                                          #  "**"=power, since we using dictionary use : to assing values
    "**":power,                                       # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
    "//":quotient
}

v=operations["**"](2,3)
print(v)
print(operations["//"](18,9))
#operations=["**"==power,"//"==quotient]       #cannot use this method to assign functions in lists , shows boolean error
#print(operations[1](9,2))
# operations=["sahara"==power,"nahara"==quotient]       #you cannot assign literal values inside a list, you need to predefined variable as function name using = and then use it in string.

sahara=power
nahara=quotient
operations=[sahara,nahara]
print(operations[1](9,2))

#Learning about scope , global variables through the project
enemies=10                                      #here we defined the namespace

def kill():
    enemies=7
    print(f"inside function:{enemies}")
    
kill()                                                      #7 enemies is a local scope inside a defined function.
print(f"outside function:{enemies}") 
#10 because uses the glocalscope of enemies



#Global scope and Local scope 

game_point=33                   #global scope non indented outside every function and loop.


    
def game_score():
    game_point=game_point-10 #again shows an error as game_point is still not defined nor any value is set as parameter for the same so we cannot perform mathematical opertaions on it 
    print(game_point)
     
def gamekill():
    def gamepoint():
        print(game_point)

game_score()         #prints 33-10=23(first line first print) and then 9 (as gamepoint is now a new local variable defined inside game_score)
# game_point()      shows an error as gamepoint is in local space defined (inside the gamekill func so we have to call game kill function first.)    
print(game_point)     #would print 10 as it access global variable scope .
a=gamekill()
print(a)


nisha=10

def name():
    global nisha
    nisha+=10           #by using global it would now consider the nisha defined outside the function and modifying the variable is now possible!
     