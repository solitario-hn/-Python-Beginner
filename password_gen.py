    #password genrator project
import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
specialchar=['@','#','$','%','&','!','^']
print("WELCOME TO PYPASSSWORD GENERATOR\n")
nr_letters=int(input("How many letters do you want in your password?\n"))
nr_numbers=int(input("How many numbers you want in your password?\n"))
nr_specialchar=int(input("How mnay special characters do you want in your password?\n"))

password=[]
for char in range(0,nr_letters):
    password.append(random.choice(letters))
for x in range(0,nr_numbers):
    password.append(random.choice(numbers))
for y in range(0,nr_specialchar): 
    password.append(random.choice(specialchar))   

print(len(password))  
key=len(password)     
print(password)  
new_password=random.choices(password,k=key)
print(new_password)
random.shuffle(password)
print(password)

passcode=""
for char in password:
    passcode+=char
print("YOUR NEW PASSWORD IS :", passcode) 




