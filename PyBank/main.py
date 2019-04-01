import os
import csv
from collections import Counter

BOB = os.path.join("/Users/matthewpetroff/WORKSPACE/unc/02-homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
#print("good path")

#with open(csv, 'r') as csvfile:
with open(BOB) as csvfile:

    #reader open
    reader = csv.reader(csvfile)


    #The total number of months included in the dataset
    data = list(reader)
    row_count = len(data)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" ,(row_count - 1))
#The net total amount of "Profit/Losses" over the entire period
with open(BOB) as fin:
    reader = csv.reader(fin)
    header = next(reader)

    for row in reader:
        total = sum(int(float(r[1])) for r in csv.reader(fin))
        print ("NET Total Profit & Loss: $", total)

    average = 0.0
    maxt = 0.0
    mint = 0.0
    for line in fin:
        try:
            p = float(line.split(",")[1])
            average += p
            total += 1
            maxt = max(maxt,p)
            mint = min(mint,p)
        except:
            pass

    average = average / float(total)

    print("Average:", average)
    print("Maximum:", maxt)
    print("Mimimum:", mint)
