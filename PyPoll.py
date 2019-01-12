

#Create a python script to analyze polling results

# import operating system & csv file
import os
import csv
from collections import Counter

# tell python where to find the csv file
csvpath = os.path.join('', "Downloads", "election_data.csv")

# open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#have a place to store information
    votes_count = Counter() 
    candidates = [] 
    percentage = []

#get totals      
    for row in csvreader: 
        candidates.append(row[2])
        total_votes = len(candidates)
    
#add votes to each candidate
    for candidate in candidates: 
        votes_count[candidate] += 1

#connect the vote count to the candidate count
    candidates = tuple(votes_count.keys())
    votes = tuple(votes_count.values())

#determine the winner
    winner = max(zip(votes_count.values(), votes_count.keys()))

#determine the percent votes
    for x in votes:
        percentage.append(round(int(x)/total_votes*100,2))

        percent_formatted = ['{}%'.format(p) for p in percentage]


#print the results
    print("Election Results")
    print("------------------------")
    print ("total votes:", (total_votes))

    print(list(zip(candidates, votes, percentage)))
    print("------------------------")
    print("Winner:",winner)
    print("------------------------")
