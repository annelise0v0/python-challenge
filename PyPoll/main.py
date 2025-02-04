# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
election_data_csv = os.path.join("Resources", "election_data.csv")  # Input file path
election_analysis = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
vote_counts = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = "" 
winning_votes = 0

# Open the CSV file and process it
with open(election_data_csv) as election_data:
    reader = csv.reader(election_data)
    
    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            vote_counts[candidate_name] = 0
        # Add a vote to the candidate's count
        vote_counts[candidate_name] += 1


# Open a text file to save the output
with open(election_analysis, "w") as txt_file:

    # Print the total vote count (to terminal)
    results = (
        f"Election Results\n\n"
        f"-------------------------\n\n"
        f"Total Votes: {total_votes}\n\n"
        f"-------------------------\n\n"
        )
    print(results)

    # Write the total vote count to the text file
    txt_file.write(results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_counts:
        votes = vote_counts[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_votes:
            winning_votes = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n"
    )

    # Save the winning candidate summary to the text file
    print(winning_summary)
    txt_file.write(winning_summary)
