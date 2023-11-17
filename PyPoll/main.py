import csv
import os

# Set the path to your election_data.csv file
csvpath = r'C:\Users\User\Documents\GitHub\pythonChallenge\PyPoll\Resources\election_data.csv'

# Begin variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract data from the row
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner
winner = max(candidates, key=candidates.get)

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Set the path to save the results text file
csvpath = r'C:\Users\User\Documents\GitHub\pythonChallenge\PyPoll\Resources\election_data.csv'

# Export the results to a text file
with open(csvpath, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print(f"Results have been saved to: {csvpath}")






