import os
import csv

totalvotes = 0
candidates ={}
#establish the csv pathway
csvpath = os.path.join('election_data.csv')
#open the file from the pathway
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)
    #establish the headers (Ballot ID, County, Candidate)
    csvheader = next(csvreader)
    print(f"Election Results")

    for row in csvreader:
        #calculate total votes
        totalvotes += 1
        #calculate total votes for each candidate
        if row[2] not in candidates: 
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
    print(f"Total Votes: {totalvotes}")    
    #calculate the percent of votes for each candidate
    for candidate in candidates:
        votepercent = round(candidates[candidate] / totalvotes * 100, 3)
        totalcandidatevotes = candidates[candidate]
        print(f"{candidate}: {votepercent}% ({totalcandidatevotes})")
    #calculate winner
    winner = max(candidates, key=candidates.get)
    print(f"Winner: {winner}")


#open with text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write(f"-------------------------\n")
    for candidate in candidates:
        votepercent = round(candidates[candidate] / totalvotes * 100, 3)
        totalcandidatevotes = candidates[candidate]
        txtfile.write(f"{candidate}: {votepercent}% ({totalcandidatevotes})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")