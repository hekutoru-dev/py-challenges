# Dependencies
import csv
import os

# Get file.
election_data = os.path.join(".", "Resources", "election_data.csv")

with open(election_data, "r") as data:

    reader = csv.reader(data)
    header = next(reader)

    # Initial values: votes, candidate name.
    total_votes = 0
    candidates = []
    candidate_votes = {}

    winning_votes = 0

    for row in reader:

        # Add votes to total count.        
        total_votes += 1

        # Get the name
        candidate_name = row[2]

        # Check if candidate has already been counted.
        if candidate_name not in candidates:

            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Sum candidate votes
        candidate_votes[candidate_name] += 1
    
    print(f'\n\n    Election Results') 
    print(f'--------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'--------------------------')    
    
    # Iterate through candidates
    for candidate in candidate_votes:

        # Get votes for each candidate.
        votes = candidate_votes[candidate]
        votes_percentage = votes/total_votes * 100

        candidate_output = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        print(candidate_output, end="")

        # Find winner candidate.
        if votes > winning_votes:
            winning_votes = votes
            winner_candidate = candidate
    
    print(f'--------------------------')
    print(f'Winner: {winner_candidate}')
    print(f'--------------------------')

print('\n')