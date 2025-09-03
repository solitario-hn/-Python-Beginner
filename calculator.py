from logo import calculator_logo #imporitng a calculator logo from our logo file
#creating individual functions for each opertaion
def add(n1,n2):
    '''add both the argument digits'''
    result=n1+n2
    return result

def subtract(n1,n2):
    '''subtract the second argument from first argument digit'''
    result=n1-n2
    return result

def divide(n1,n2):
    '''divide the first arguemnts digit by second digit'''
    result=n1/n2
    return result

def multiply(n1,n2):
    '''multiply both the argument digit'''
    result=n1*n2
    return result




#taking user input
def calculator():
    print(calculator_logo)
    print('''                 WELCOME TO THE PYTHON CALCULATOR                    ''')
    print("You can perform various mathematical opertaions , all you need to start is enter your digits and then choose the operation you wish to perform on it.")
    new_number=''
    x=True
    number_1=float(input("Enter the first digit: "))    #writing it outside the loop as we do not wish to take two inputs again and again
    while x==True:
        number_2=float(input("Enter the second digit:"))                       
        choice=input("Pick up an operation you'd like to perform on \n1.'+'  (for addition)\n2.'-'  (for subtraction)\n3.'*'  (for multiplication)\n4.'/' (for divide)\n")
        if choice=='+':
            new_number=add(number_1,number_2)
            print(f"Your result is {new_number}")
        elif choice=='-':
            new_number=subtract(n1=number_1,n2=number_2)
            print(f"Your result is {new_number}")
        elif choice=='/':
            new_number=divide(n1=number_1,n2=number_2)
            print(f"Your result is {new_number}")
        elif choice=='*':
            new_number=multiply(n1=number_1,n2=number_2)
            print(f"Your result is {new_number}")
        else:
            print("you chose an undefined digit ,hence result is 0")
            new_number=0

        will=input(f"Type 'y' to continue calculating with {new_number} or 'n' to start a new calculation  ")
        if will=='y':
            number_1=new_number
            x=True
        elif will=='n':
            x=False     #exiting the existing calculaton
            print("\n"*20)
            calculator()
        else:
            print("Error!!!")


calculator()                #RECURSION: a process in which a function calls itself directly or indirectly in order to solve a problem.