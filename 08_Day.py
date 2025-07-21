# Caesar Cipher 
# Separate encrypt & decrypt function

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message1, shift1):
    encrypt_text = ""
    for i in message1:
        shifted_index = alphabet.index(i) + shift1
        shifted_index %= len(alphabet)
        encrypt_text += alphabet[shifted_index]
    print(encrypt_text)

def decrypt(message1, shift1):
    plain_text = ""
    for i in message1:
        shifted_index = alphabet.index(i) - shift1
        shifted_index %= len(alphabet)
        plain_text += alphabet[shifted_index]
    print(plain_text)

direction = input("Encode or Decode: ").lower()
if direction == "encode":
    message = input("Enter message: ").lower()
    shift = int(input("Enter shift number: "))
    encrypt(message, shift)
elif direction == "decode":
    message = input("Enter message: ").lower()
    shift = int(input("Enter shift number: "))
    decrypt(message, shift)
else:
    print("Please choose correct option.")

# Common function with UI improvement

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message1, shift1, direction1):
    text = ""
    if direction1 == "decode":
        shift1 *= -1

    for i in message1:
        shifted_index = alphabet.index(i) + shift1
        shifted_index %= len(alphabet)
        text += alphabet[shifted_index]
    print(text)

caesar_status = True
while caesar_status:
    direction = input("Encode or Decode: ").lower()

    if direction == "encode" or direction == "decode":
        message = input("Enter message: ").lower()
        shift = int(input("Enter shift number: "))
        caesar(message, shift, direction)
        user_response = input("Do you wanna continue?(Yes or No)\n").lower()
        if user_response == "no":
            caesar_status = False
    else:
        caesar_status = False
        print("Please choose correct option.")
        break

#--------------------------------------------------------art.py--------------------------------------------------------#

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

