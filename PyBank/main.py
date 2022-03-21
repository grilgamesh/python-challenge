import os
import csv
import statistics

#T H E   B A N K   J O B
#direct python to the input file
bankpath = os.path.join("Resources", "budget_data.csv")

#instantiate variable: list to drop monthly data into.
monthlyProf = []

#open the file as bankdata
with open(bankpath, encoding='utf') as csvfile:
    bankdata = csv.reader(csvfile, delimiter=",")

    #read in and store the header
    header = next(bankdata)
    
    #loop through the rest of the rows and read in data
    for row in bankdata:
        monthlyProf.append(int(row[1]))
            
# create output string
output = [f"Financial Analysis",
          f"------------------",
          f"Total Months: {len(monthlyProf)}",
          f"Total: {sum(monthlyProf)}",
          f"Average Change: {round(statistics.mean(monthlyProf), 2)}", 
          f"Greatest Increase in Profits: {max(monthlyProf)}",
          f"Greatest Decrease in Profits: {min(monthlyProf)}"]

#print output string    
for i in output:
    print(i)

#write output txt file
fapath = os.path.join("analysis", "Financial Analysis.txt")
with open(fapath, 'w') as fa:
    fa.write('\n'.join(output))


