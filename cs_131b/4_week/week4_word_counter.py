"""
This program estimates the number of unique words in the text file: '/users/abrick/resources/urantia.txt'.
"""

# File path stored as a variable. 
# Instructions specify the program *only* needs to read this file, no others. Therefore, variable! 
file_path = '/users/abrick/resources/urantia.txt'

# Variable holds a word count we keep adding to 
word_count = 0 

# Open the file, store as lines 
try: 
    file = open(file_path).readlines()
# Prepare for cases when file not found or permission denied 
except FileNotFoundError: 
    print('File not found.')
except PermissionError: 
    print('File not readable (permissions error).')
# But if everything goes okay...
else: 
# Assume a new word starts every time there is a space. 
# Use .split to identify each word in a line.
# Place that line.split in a set to get unique words only. 
# Add the number of those words to the word_count 
    for line in file: 
        line_count += 1
        word_count += len(set(line.split()))
# Subtract the number of line breaks from the word count  
line_breaks = len(file) - file.count('\n')
word_count = word_count - line_breaks 

# Print an estimate of a number of words 
print('Subtracting estimated new line breaks, we estimate that this file contains', word_count,'distinct words.')