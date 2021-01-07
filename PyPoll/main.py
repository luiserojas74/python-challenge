# Import the os module
# This will allow me to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Import Counter. It will allow me to create dictionary that counts records
from collections import Counter

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# List used to store the monthy results
monthly_result_list = []
# List used to store the monthy changes
change_list = []

# Reading using CSV module
with open(csvpath, encoding="utf8") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents  = ['Voter ID', 'County', 'Candidate']
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    poll_data_list = list(csvreader)
    # Get the number of votes cast
    total_votes = len(poll_data_list)

# Print the analysis to the terminal
print ("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")

# Concurrently export the analysis to a text file with the results
# Save the output file path
output_file = os.path.join('.', 'analysis', 'output.txt')
# Open the output file and then write the  object to the txt
with open(output_file, "w", newline='') as datafile:
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write("----------------------------\n")

    # Zip the original list in order to transpose values and manipulate Candidate rows
    zipped_poll_data_list = zip(*poll_data_list)
    # Convert to list
    candidates_list = list(zipped_poll_data_list)[2]
    # Count votes and create a dictionary with a key (name) and a value (votes)
    candidates_dict = Counter(candidates_list)
    # Create a list with unique candidate names
    candidates_names_list =list(candidates_dict.keys())
    # Create a list with votes per candidate
    candidates_votes_list =list(candidates_dict.values())
    # For loop to output candidates, votes and percentages
    for i in range(len(candidates_dict)):
        candidate_name = candidates_names_list[i]
        candidate_votes = float(candidates_votes_list[i])
        if total_votes > 0:
            candidate_percent = candidate_votes / total_votes
        else:
            candidate_percent = 0
        # Format numbers accordingly
        candidate_percent = "{:.3%}".format(candidate_percent)
        candidate_votes = "{:.0f}".format(candidate_votes)
        print(f'{candidate_name}: {candidate_percent} ({candidate_votes })')
        datafile.write(f'{candidate_name}: {candidate_percent} ({candidate_votes })\n')
    print("-------------------------")
    datafile.write("----------------------------\n")
    # Get the winner
    max_votes = max(candidates_votes_list)
    winner = candidates_names_list[candidates_votes_list.index(max_votes)]
    print(f'Winner: {winner}')
    datafile.write(f'Winner: {winner}\n')
    print("-------------------------")
    datafile.write("----------------------------")
