import random
import logo

def life_in_weeks(age):
    assumed_total_lifepan=90
    total_weeks=90*52
    age_left=total_weeks-52*age
    print(f"You have {age_left} weeks left")
    num=age_left*7
    print(f"you have {num} days left")

#print("WELCOME TO LIFESPAN CALCULATOR\n")
#current_age=int(input("Please enter your current age:   "))   
#life_in_weeks(current_age)


def greet_with(name,location,day):
    print(f"I actually met {name}")
    print(f"in {location}")
    print(f"on {day}")


#greet_with("Om","Karnataka","Monday")
#greet_with(location="chennai",day="tuesday",name="jack")
 
#print("WELCOME TO THE LOVE CALCULATOR\n")

def calculate_love_score(name1,name2):
    word1="TRUE"
    word2="LOVE"
    match1=0
    match2=0
    for name in name1:
        for word in word1:
            if name==word:
                match1+=1
        for word in word2:
            if name==word:
                match1+=1 
    for name in name2:
        for word in word1:
            if name==word:
                match2+=1
        for word in word2:
            if name==word:
                match2+=1                 
    str(match1)
    str(match2)
    print(f"Your love score is :{match1}{match2}")                     
           
#name1=input("Enter the first person name:      ").upper()
#name2=input("Enter the second person name:     ").upper()
#calculate_love_score(name1,name2)

      



def encrypt(original_text,shift_number):
    position=0
    encrypted_text=""
    for x in original_text:
        if x not in alphabet:
            encrypted_text+=x
        else:
            position=alphabet.index(x)
            position+=shift_number
            if position<26:
                encrypt=alphabet[position]
            else:
                encrypt=alphabet[position-26]    
        
            encrypted_text+=encrypt
        
    print(f"Here is the encrypted text:{encrypted_text}")
    
 
    
def decrypt(encrypt_text,shift_amount):
        position=0
        decrypted_text=""
        for x in encrypt_text:
            if x not in alphabet:
                decrypted_text+=x
            else:
                position=alphabet.index(x)
                position-=shift_amount
                decrypt=alphabet[position]
            
            
                decrypted_text+=decrypt    
        
        print(f"Here is your decrypted text: {decrypted_text}")   
        



def caesar(direction,text,shift):        
    if direction=="encode":
        encrypt(original_text=text,shift_number=shift) 
    if direction=="decode":
        decrypt(encrypt_text=text,shift_amount=shift)       
    


print(logo.logo)
print("               -CAESAR CYPHER BY NIDHI-                   ")


x=True
while x==True:
    
    alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
    direction=input("Type 'encode' to encrypt and 'decode' to decrypt \n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input('type the shift number:    '))
    caesar(direction,text,shift)

    option=input("Do you want to encrypt or decrypt more messages?\nType 'yes' or 'no'          ").lower()
    if option=='no':
        x=False
        print("GOODBYE....")
        


    
    
    



