from sys import argv, exit
from cs50 import get_string
import csv

def main():
# Check if user provided a command line argument
    if len(argv) != 3:
        print("Missing command-line argument.")
        print("Usage: file.csv file.txt")
        exit(1)

# Open the CSV file for reading and extract STR names from columns
    with open(argv[1],"r") as database:
        reader = csv.reader(database)
        i = next(reader)
        sequences = {rows[0]:rows[len(i)-2] for rows in reader} # Need to figure out how to create a dictionary
        print(sequences)
        for x in range (1, len(i), 1):
            print(f"{i[x]}")
            print(f"{count(i[x])}")



# Count STRs in the text file. Compute the longest run of consecitive repeats for each STR in the sequence
def count(string):
    with open(argv[2],'r') as sequence:
        dna = sequence.read()
        consq = 0
        if string in dna:
            index = dna.find(string)
            print(index)
            if index > -1:
                consq = 1
            #compare the column name with DNA sequence
                while dna[(index+len(string)) : (index+len(string)+len(string))] == string:
                    consq += 1
                    index += len(string)
        return consq

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


#sequence = {

#}
# Check the dictionary for a match
