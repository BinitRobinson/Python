import random
import string

chars=" "+string.punctuation + string.digits + string.ascii_letters
chars=list(chars)

key=chars.copy()

random.shuffle(key)

#print(f"chars:{chars}")
#print(f"key:{key}")

#Encryption
print("Encryption")

Plain_text=input("Enter your message here : ")
Cipher_text=""

for letter in Plain_text:
    index=chars.index(letter)
    Cipher_text+=key[index]

print(f"Plain text : {Plain_text}")
print(f"Encrypted text : {Cipher_text}")


print("----------------------------------------------------------------------")

#Decryption

print("Decryption")
Secret_text=input("Enter your secret message here : ")
simple_text=""

for letter in Secret_text:
    index=key.index(letter)
    simple_text+=chars[index]

print(f"Cipher text : {Secret_text}")
print(f"Plain text : {simple_text}")
