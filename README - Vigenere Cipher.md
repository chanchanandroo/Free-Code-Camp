# Vigenère Cipher – Encryption & Decryption

This is a beginner-friendly Python implementation of the **Vigenère cipher**, upgraded from the earlier Caesar cipher.  
It was built as part of the [freeCodeCamp](https://www.freecodecamp.org/) **Scientific Computing with Python** course.

---

## Overview

The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword.  
This script allows you to:

- Encrypt a message using a custom keyword.
- Decrypt the encrypted message using the same keyword.

---

## Example

**Message:** `freecodecamp is awesome`  
**Key:** `happycoding`  

**Encrypted:** `mrttaqrhknsw ih puggur`  
**Decrypted:** `freecodecamp is awesome`

---

## How to Use

1. Clone this repo or copy the `vigenere.py` file.
2. Modify the `text` and `custom_key` variables at the top of the file.
3. Run the script in Python 3 to see the encryption and decryption in action.

---

## Author

Created by [Andrew Chan] as part of a personal learning journey in cybersecurity, programming, and AI development.

---

## Explanation of how cipher works:

text = 'mrttaqrhknsw ih puggrur'  #encrypted text we are trying to decode
custom_key = 'happycoding'       #answer key that shifts the encrypted text in the right sequence to unlock the hidden message

def vigenere(message, key, direction=1):     #defining the vigenere function
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'   #using the alphabet as our database
    final_message = ''

    for char in message.lower():           #changes the message into lower case to get around case sensitivity

        # Append any non-letter character to the message
        if not char.isalpha():    #saying if character is not letters add final_message to the characters and store in final_message
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]   
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')