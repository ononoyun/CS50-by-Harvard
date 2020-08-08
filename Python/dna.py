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

        #Create a list of dictionaries from the csv file
        data = [row for row in reader]
        print(f"Original: {data}")

        # Create a dictionary to store the returned values
        newlist = []
        #d = {}
        for n in range (1, len(i), 1):
            #d = {i[n] : count(i[n])}
            newlist.append(count(i[n]))
        print(f"New: {newlist}")

        print(data[1][1])
        print(newlist[0])


def compare(data, newlist):
    return

# Count STRs in the text file. Compute the longest run of consecitive repeats for each STR in the sequence
def count(string):
    with open(argv[2],'r') as sequence:
        dna = sequence.read()
        consq = 0
        if string in dna:
            index = dna.find(string)
            #print(index)
            if index > -1:
                consq = 1
            #compare the column name with DNA sequence
                while dna[(index+len(string)) : (index+len(string)+len(string))] == string:
                    consq += 1
                    index += len(string)
        return consq

main()
