import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalVotes = 0
    cadidates = []
    cadidateVotes = {}
    # Read each row of data after the header
    for row in csvreader:
        
        
        
        print(row)




totalVWon

winPop = 
