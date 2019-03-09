import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read header row
    header = next(csvreader) 
     
    print(total_months)
    print(header)
    
    firstrow = next(csvreader)
    total_months = total_months + 1
    print(firstrow)
    print(total_months)

    for row in csvreader:
        total_months = total_months + 1
        print(row,total_months)

    print("The total amount of months is:")
    print(total_months)

print("finishingmain.py")

