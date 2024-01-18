import csv

data = csv.DictReader(open('Resources/election_data.csv'))
my_report = open('Analysis/Election_Report.txt','w')

total = 0
candidates = {}

for row in data:
    total += 1
    candidate = row["Candidate"]

    if candidate not in candidates.keys():
        candidates[candidate] = 0
    
    candidates[candidate]+=1

output = f'''
Election Results
-------------------------
Total Votes: {total:,}
-------------------------
'''

winner = ['',0]

for candidate in candidates.keys():
    votes = candidates[candidate]
    
    if votes > winner[1]:
        winner[0] = candidate
        winner[1] = votes

    output += f'{candidate}: {votes/total*100:.3f} ({votes})\n'

output += f'-------------------------\nWinner: {winner[0]}\n-------------------------'

print(output)
my_report.write(output)