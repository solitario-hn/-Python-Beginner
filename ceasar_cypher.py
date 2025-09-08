import random
import logo

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
        



