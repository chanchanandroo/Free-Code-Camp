# What is this?

This is following FreeCodeCamp's instructions in building a script that finds the square root of a number by using the bisection method. This is part of my self learning journey in **Python**, **AI**, and **Cybersecurity**. 

# How to Run This Code?

Download and then bash in the terminal: python bisection_method_squareroot.py

You can then change the N variable to be different numbers and the function will find the square root whether it's doable or not. If it can't find it, it'll throw an error message. 

# Code Walkthrough

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0: #if number is negative make it print an error message
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1 #giving it absolute values of 1 and 0
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target) #guessing range between 0 and the target number
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2 #finding the midpoint of the squareroot
            square_mid = mid**2 #square rooting 

            if abs(square_mid - square_target) < tolerance: #check how close the guess is
                root = mid
                break

            elif square_mid < square_target: #if guess was too low
                low = mid
            else:
                high = mid #ig guess was too high

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root #found root or failed to converge. 

N = 16 #target square root number
square_root_bisection(N)
