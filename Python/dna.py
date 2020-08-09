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

        #Create a list of lists from the csv file
        data = [row for row in reader]
        print(f"Original: {data}")

        # Create a list to store the returned values from "count" function
        newlist = []
        for n in range (1, len(i), 1):
            newlist.append(count(i[n]))
        print(f"New: {newlist}")

        result = check(i, data, newlist)
        if result == None:
            print("No match")
        else:
            print(result)

def check(i, data, newlist):
    length = len(data)
    for e in range(len(data)):
        for x in range(len(i)-2):
            if int(data[e][1+x]) == newlist[0+x]:
                if x == len(i)-3:
                    return data[e][0]
                else:
                    continue
            else:
                break

# Count STRs in the text file. Compute the longest run of consecutive repeats for each STR in the sequence
def count(string):
    with open(argv[2],'r') as sequence:
        dna = sequence.read()
        consq = 0
        index = 0
        while index < len(dna):
            index = dna.find(string, index)
            if index == -1:
                break
            else:
                consq = 1
                #compare the column name with DNA sequence
                while dna[(index+len(string)) : (index+len(string)+len(string))] == string:
                    consq += 1
                    index += len(string)
        return consq

main()
