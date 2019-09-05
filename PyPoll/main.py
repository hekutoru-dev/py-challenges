# Dependencies
import os
import csv

# Import file.
csvpath = os.path.join(".", "", "election_data.csv")

# Auxiliary Lists
total_candidate_votes = []
unique_candidate_list = []

# Initialize Votes per Candidate
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open File and read it.
with open(csvpath, newline='') as election:
    reader = csv.reader(election, delimiter=',')
    csv_header = next(reader)    

    # Get unique candidates and a list with all votes    
    for row in reader:
        total_candidate_votes.append(row[2])
        if row[2] not in unique_candidate_list:
            unique_candidate_list.append(row[2])
        
        #Get total votes for each candidate                        
        if row[2] == 'Khan':     khan_votes += 1
        elif row[2] == 'Correy': correy_votes += 1
        elif row[2] == 'Li':     li_votes += 1
        else:                    otooley_votes += 1
    
    # PERFORM calculations
    total_votes = len(total_candidate_votes)
    votes_per_candidate = [khan_votes, correy_votes, li_votes, otooley_votes]
    percentage_votes = [(div / total_votes)*100 for div in votes_per_candidate]
    
    # GET Winner
    max_votes = max(votes_per_candidate)        
    winner = unique_candidate_list[ votes_per_candidate.index(max_votes) ]        

    # PRINT results to Terminal
    print ("")
    print ('Election Results')
    print ('---------------------------')
    print (f'Total Votes: {total_votes}')
    print (f'Khan: {votes_per_candidate[0]} {percentage_votes[0]} %')
    print (f'Correy: {votes_per_candidate[1]} {percentage_votes[1]} %')
    print (f'Li: {votes_per_candidate[2]} {percentage_votes[2]} %')
    print (f"O'Tooley: {votes_per_candidate[3]} {percentage_votes[3]} %")
    print ('---------------------------')
    print (f'Winner is: {winner}')

# Define an Output path and a filename for that output.
output_file = os.path.join(".", "", "Election_Results.txt")


with open(output_file,"w") as file:
    
    # Write methods to print to Financial Analysis.
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write(f'Khan: {votes_per_candidate[0]} {percentage_votes[0]} %\n')
    file.write(f'Correy: {votes_per_candidate[1]} {percentage_votes[1]} %\n')
    file.write(f'Li: {votes_per_candidate[2]} {percentage_votes[2]} %\n')
    file.write(f"O'Tooley: {votes_per_candidate[3]} {percentage_votes[3]} %\n")
    file.write("----------------------------\n")
    file.write(f'Winner is: {winner}')    