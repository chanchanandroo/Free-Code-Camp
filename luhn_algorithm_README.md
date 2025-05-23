This is the Luhn Algorithm created by following the instructions created by freecodecamp's Scientific Computing with Python. 

I made this project as part of my self-learning journey in learning Python. 

You can run this project by downloading the repo and running it in python by running python luhn_algorithm.py

The Luhn Algorithm is a validation tool used to check long strings of data i.e. account numbers / credit card numbers. It works by doubling every second digit starting from the right (excluding the last digit, that's the number the system checks against).

If any doubled number is greater than 9, the numbers are split into single digits and added together i.e. 9*2 = 18 = 1+8

Add to the sum of the untouched digits (digits that didn't double), take total sum. The total sum % 10 = 0, the number is valid. If not, the check fails, and the number input is invalid. The check failing could mean the number is invalid, human error i.e. mistyping the number in, or the number corrupting and changing. 

Here's a run through of what the code does line by line:

def verify_card_number(card_number):  #def function
    sum_of_odd_digits = 0   # what we compare to in the end i.e. % 10 = 0
    card_number_reversed = card_number[::-1] #setting up our list in reverse
    odd_digits = card_number_reversed[::2] #looking at our reversed card number, every 2nd digit

    for digit in odd_digits:     #a for in loop to loop the logic for every digit
        sum_of_odd_digits += int(digit) # making the sum of the odd digits ana integer since everything defaults as strings

    sum_of_even_digits = 0  #same idea as odd digits, check is %10 = 0.
    even_digits = card_number_reversed[1::2] #start index 1 where the first even digit is, every 2nd digit, already reversed
    for digit in even_digits:
        number = int(digit) * 2 #integer even digits are doubled 
        if number >= 10: #doubled if greater than or equal to 10 i.e. bigger than 9.
            number = (number // 10) + (number % 10) # // symbol divides for numbers in the 10's column, % gets remainder in 1's column
        sum_of_even_digits += number #sum of even digits
    total = sum_of_odd_digits + sum_of_even_digits #checking total sum: even and odd together
    print(total)
    return total % 10 == 0 #checking if valid or invalid. 

def main(): #def second function to check numbers
    card_number = '4111-1111-4555-1142' #number we want to check (it is valid)
    card_translation = str.maketrans({'-': '', ' ': ''}) #follows the above formatting list and runs through the for loop
    translated_card_number = card_number.translate(card_translation) #end result check against = 0 or not

    if verify_card_number(translated_card_number):
        print('VALID!') #if equal to 0 prints valid, otherwise prints invalid
    else:
        print('INVALID!')

main()