import os
import csv
import statistics




#T H E   E L E C T I O N   J O B
#direct python to the input file
pollpath = os.path.join("Resources", "election_data.csv")

#instantiate variables: 
results = {}

#open the file as polldata
with open(pollpath, encoding='utf') as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")

    #read in and store the header
    header = next(polldata)
    
    #loop through the rest of the rows and add the vote to the results dictionary
    for row in polldata:
        candidate = row[2]
        if candidate in results:
            #add 1 to the current value;
            results[candidate] = results[candidate]+1
        else:
            #create a new dictionary entry with 1 vote.
            results[candidate] = 1

    votesCast = sum(results.values())

    #calculate the winner:
    winner = ""
    winningvotes = 0
    for candy in results:
        if results[candy] > winningvotes:
            winner = candy
            winningvotes = results[candy]
    
    #write out summary
    output = [f""
                f"Election Results",
                f"----------------", 
                f"Total votes cast: {votesCast}", 
                f"----------------"]

    for foo in results:
        # for each entry in results, append the key and count to the output, and format correctly.
        output.append(f"{foo}: {round((results[foo]/votesCast * 100), 2)}% ({results[foo]})")

    output.append(f"----------------")
    output.append(f"The winner is: {winner}. Congratulations to them.")

#print output string 
print()   
for i in output:
    print(i)
    
#write output txt file
electionpath = os.path.join("analysis", "Election Analysis.txt")
with open(electionpath, 'w') as ea:
    ea.write('\n'.join(output))
