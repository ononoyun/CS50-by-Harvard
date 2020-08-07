from sys import argv, exit
from cs50 import get_string
import csv 

def main():
# Check if user provided a command line argument
    if len(argv) != 3:
        print("Missing command-line argument.")
        print("Usage: file.csv file.txt")
        exit(1)

# Open the CSV file for reading

    with open(argv[1],"r") as database: 
        reader = csv.reader(database)
        i = next(reader)
        for x in range (0, len(i), 1):
            check(i[x])

def check(string):
    with open(argv[2],'r') as sequence:
        #compare the column name with DNA sequence
        if sequence.find(string) != -1:
            print(f"{string} found.")
        else:
            print("not found")

main()
#sequence = open(argv[2], "r")

#with file:
#    reader = csv.DictReader(file)
#    for row in reader:
#        print(row['AATG'])
# Create a dictionary  name,AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
#dictionary = {
#    "name": "string in the first column"
#   "AGATC": "number"
#    "TTTTTTCT": "number"
#    "ATTG": "number"
#    "TCTAG": "number"
#    "GATA": "number"
#    "TATC": "number"
#   "GAAA": "number"
#    "TCTG": "number"
#}

# Open the text file

# Count STRs in the text file. Compute the longest run of consecitive repeats for each STR in the sequence
#sequence = {

#}
# Check the dictionary for a match
