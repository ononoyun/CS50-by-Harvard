from cs50 import get_string
import string

# Get user input
text = get_string("Text: ")

# Initialize variables to keep count
letters = 0
words = 0
sentences = 0

# Calculate Coleman-Liau index = 0.0588 * L - 0.296 * S - 15.8
# L - average number of letters per 100 words in the text 
# S - average number of sentences per 100 words in the text 

for char in text:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1
    if char.isspace() == True:
    #FIX THIS
        words += 1
    if char == "." or char == "!" or char == "?":
        sentences += 1

print(f"Letters {letters}, words {words}, sentences {sentences}")
L = round((letters * 100 / words),2) 
S = round((sentences * 100 / words),2) 

print(f"L {L} , S {S}")

index = round((0.0588 * L - 0.296 * S - 15.8),2)
print(f"index {index}")

if 0 >= index: 
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+") 
else: 
    print(f"Grade {index}")