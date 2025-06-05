# Snake Case Converter (From Pascal Case or Camel Case)

This is a simple converter made from python that chanages pascal case: Words Like This (each word's first letter capitialized), or camel case: worDsliKethEse(like a camel, capitals in the middle) to snake case: i_am_a_snake_case.

I completed this assignment as part of my self-learning journey in **Python**, **AI**, and **Cybersecurity**. This assignment was FreeCodeCamp's scientific computing with Python course. 

# How to Run This Code?

Once downloaded, use the terminal and bash in python snake_case_converter.py

Then you can change the print(convert_to_snake_case("change_String_Here)) to play around with the converter.

# Code Breakdown

def convert_to_snake_case(pascal_or_camel_cased_string): #defining the function and our parameters

    snake_cased_char_list = [ #making a list, inside the list characters are changed to lower case, isupper() is used to detect all uppercase letters 
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string #we keep the first letter upper case
    ]

    return ''.join(snake_cased_char_list).strip('_') # we convert to snake case with _ in between each letter

def main():
    print(convert_to_snake_case('IAmAPascalCasedString')) # print the converted words onto console 

    

main() #calling main so it works