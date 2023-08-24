import random
import string

#list of characters used for encryption
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
keys = char.copy()

#using random to encrypt
random.shuffle(keys)

#encryption
user_input = input("Enter some text to be encrypted: ")
Cipher = ""

for letter in user_input:
    index = char.index(letter)
    Cipher += keys[index]

print(f"Encrypted message between arrows: >>>{Cipher}<<<")


#decryption
Cipher = input("Enter some text to be decrypted (copy and paste the encrypted message here): ")
user_input = ""

for letter in Cipher:
    index = keys.index(letter)
    user_input += char[index]

print(f"\nDecrypted message here: >>>{user_input}<<<")

print("\nHow Does this work?:\nThis encryption method uses a list of letters/digits/special characters and takes your text and changes it to these charcters. This list is randomized eveyrtime\n\nHow does Decryption work?:\nDecryption works the same way, it takes your encrypted text and compares it to the list of original characters that we randomized and checks if they match, these characters are then changed back to the letters used in your input.")

#source used: https://youtu.be/vsLBErLWBhA?si=OMrJ6vaUB5J8eBwb