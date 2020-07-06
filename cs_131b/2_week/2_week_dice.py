"""
This program simulates throwing two 900-sided dice, then indicates whether or not the sum of the results is divisible by three.

I am assuming that I will not ask for user input, and the user will run the program directly from the terminal to throw the dice. 

I am also deciding that my 900-sided dice include the options 1-900, inclusive. 
"""
import random 

# Gets random numbers between 1 and 900 (dice faces)
first_die = random.randint(1,900) # .randint will include both 1 and 900
second_die = random.randint(1,900)

# Adds those numbers together
total = first_die + second_die 

# Determines whether that sum is divisible by three
# Conditional stores a string that will be used in output
if total % 3 == 0: 
    divisible = "is divisible by 3."
else: 
    divisible = "is NOT divisible 3."

# Tell the user what they rolled, and the outcome.  
print("\nWelcome! By running this program, you simulated rolling two 900 sided dice 🎲✨.\n")
print("Your first die rolled", first_die)
print("And, your second rolled", second_die)
print("Their total sum of", total, divisible,"\n")