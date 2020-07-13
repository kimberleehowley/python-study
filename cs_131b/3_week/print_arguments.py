"""
This program prints out the unique command line arguments it receives, in alphabetical order and without duplicates.
"""
# Importing sys, library to get command line arguments 
import sys 

# Empty dict, to hold future values  
# I'm choosing a dictionary because I want duplicates to be automatically taken care of 
dictionary = {} 

# Variable to hold string of arguments passed to command line 
arguments = sys.argv

# Loop through arguments passed
# Add each to the empty dictionary as a key 
# Add n as the place of the argument as the value  
for arg in arguments: 
    n = 1
    dictionary[arg] = n
    n = n + 1

# Tell the user what the program does 
print("\nThis program prints out the unique command line arguments it read, in alphabetical order.\n")
# Display the output
print("The command line arguments you typed, in order, without duplicates, were:")
print(sorted(dictionary))
# Prompt the user to keep testing 
print("\nTo test this program again, type words after the file name.\nTry duplicate words to be sure there are no duplicates!")