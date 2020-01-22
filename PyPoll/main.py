#Modules
import os
import csv

# Open Reader
pybank_file = os.path.join('Resources', 'election_data.csv')
with open(pybank_file, 'r', newline='') as pybank_csv:
    csv_reader = csv.reader(pybank_csv, delimiter=",")
    next(csv_reader, None)

    voterCount = 0
    candidates = []

# * The total number of votes cast
    for row in csv_reader:
        voterCount = voterCount + 1

    # Reset
    pybank_csv.seek(0)
    next(pybank_csv, None)

# * A complete list of candidates who received votes
    for row in csv_reader: 
        if row[2] not in candidates:
            candidates.append(row[2])

    # Reset
    pybank_csv.seek(0)
    next(pybank_csv, None)

# * The total number of votes each candidate won
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    otooleyVotes = 0
    for row in csv_reader:
        if row[2] == candidates[0]:
            khanVotes = khanVotes + 1
        elif row[2] == candidates[1]:
            correyVotes = correyVotes + 1
        elif row[2] == candidates[2]:
            liVotes = liVotes + 1
        elif row[2] == candidates[3]:
            otooleyVotes = otooleyVotes + 1
allVotes = {
    khanVotes : "Khan",
    correyVotes : "Correy",
    liVotes : "Li",
    otooleyVotes: "O'Tooley"
}

# * The percentage of votes each candidate won
khanPercent = round((khanVotes / voterCount)*100, 3)
correyPercent = round((correyVotes / voterCount)*100, 3)
liPercent = round((liVotes / voterCount)*100, 3)
otooleyPercent = round((otooleyVotes / voterCount)*100, 3)

# * The winner of the election based on popular vote.
winner = allVotes[max(allVotes)]

# Text file with results
text_file = open("election_results.txt", "w")
text_file.write(
    "Election Results \n ----- \n" +
    "Total Votes: " + str(voterCount) + "\n ----- \n" +
    "Khan: " + str(khanPercent) + "% (" + str(khanVotes) + ") \n" +
    "Correy: " + str(correyPercent) + "% (" + str(correyVotes) + ") \n" +
    "Li: " + str(liPercent) + "% (" + str(liVotes) + ") \n" + 
    "O'Tooley: " + str(otooleyPercent) + "% (" + str(otooleyVotes) + ") \n" +
    " ---- \n" +
    "Winner: " + str(winner) + "\n ----"
)