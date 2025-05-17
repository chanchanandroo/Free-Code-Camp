# Caesar Cipher – Beginner Python Project

This is a beginner-friendly Caesar cipher script written in Python. I built it while following [freeCodeCamp’s Scientific Computing with Python](https://www.freecodecamp.org/learn/) course as part of my self-taught learning journey.

The Caesar cipher is a simple encryption technique where each letter in a message is shifted by a set number of positions.

---

## What This Project Taught Me

- How to follow logic step-by-step
- Using `.lower()` and string indexing
- Writing `for` loops and using `if` statements
- Managing code with Git and GitHub

---

## How to Run It

```bash
git clone https://github.com/chanchanandroo/Free-Code-Camp.git
cd Free-Code-Camp
python "caesar cipher.py"
------------------------------------------------------------------------------------------------------------------------------------


text = 'Hello Zaira' #text we are shifting by 3 spaces
shift = 3           #normal amount that we shift in a Caesar cipher i.e. A -> D, B ->E, etc. 

def caesar(message, offset):                   #define a funtion called caesar, passing 2 parameters: message and offset

    alphabet = 'abcdefghijklmnopqrstuvwxyz'    #alphabet key for the caesar cipher i.e. convert letters ->index->letters

    encrypted_text = ''           #keeps the spaces in the printed message

    for char in message.lower():   #changes the message i.e. text to lowercase so it doesn't conflict with lowercase alphabet
        if char == ' ':
            encrypted_text += char  #adds encrypted_text aka blank space to char another ' ' then stores it in encrypted_text
        else:
            index = alphabet.find(char)  #uses index of alphabet letter and changes it back to corresponding letter i.e. index H = 7

            new_index = (index + offset) % len(alphabet) #modulates back to beginning of alphabet by dividing by alphabet sequence

            encrypted_text += alphabet[new_index] #encrypts original text with shifted value
    print('plain text:', message) #prints shifted text messeage 
    print('encrypted text:', encrypted_text) #prints the encrypted shifted text message

caesar(text, shift) #calling the function to work and shifting 'Hello Zaira' 
caesar(text, 13) # shift it by 13 instetad of 3