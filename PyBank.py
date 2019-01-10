#import csv file
import os
import csv

Mycsvfile = os.path.join('', 'Downloads', 'budget_data.csv')

with open(Mycsvfile, 'r') as csvfile:


    reader = csv.reader(csvfile, delimiter = ',')
# Files to load (Remember to change these)

    # use of next to skip first title row in csv file
    next(reader) 
    record_count = 0
    netRev = 0
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0
    

    for row in reader:

        revenue.append(int(row[1]))
        date.append(row[0])


    for row in reader:
        record_count = record_count +1
        if record_count > 0:
            netRev = netRev + int(row[1])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))
    #print("My way: ", netRev)


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Average Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
