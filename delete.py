alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
direction=input("Type 'encode' to encrypt and 'decode' to decrypt \n").lower()
text=input("Type your message:\n").lower()
shift=int(input('type the shift number:    '))

def encrypt(original_text,shift_number):
    position=0
    encrypted_text=""
    for x in original_text:
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
            position=alphabet.index(x)
            position-=shift_amount
            decrypt=alphabet[position]
            
            
            decrypted_text+=decrypt    
        
        print(f"Here is your decrypted text: {decrypted_text}")   
        
def caesar(direction,original_text,shift_number):        
    if direction=="encode":
        
        encrypt(original_text=text,shift_number=shift) 
    if direction=="decode":
        decrypt(encrypt_text=text,shift_amount=shift)      
    
       
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

print(student_scores)
for i in student_scores:
    score=student_scores[i]
    if score==88:
        score="good"
    elif score==95:
        score="great"
    else:
        score="good try"
    print(i,score)    
  
  
              