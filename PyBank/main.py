import csv

input_file = "Resources/budget_data.csv"

total_month = 0
total_value = 0
pre_rev = 0
total_ch = 0
inc = ['',0]
decr = ['',0]

with open (input_file) as infile:
    rows = csv.reader(infile)
    next(rows)

    for row in rows:
        rev = int(row[1])
        total_month = total_month + 1 # total_month += 1
        total_value = total_value + rev

        # Average Change
        ch = rev - pre_rev
        if pre_rev == 0:
            ch = 0

        total_ch += ch

        # Greatest Increase
        if ch > inc[1]:
            inc[0] = row[0]
            inc[1] = ch

        #Greatest Decrease
        if ch < decr[1]:
            decr[0] = row[0]
            decr[1] = ch

        # Reset Area
        pre_rev = rev
       

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_value:,}
Average Change: ${total_ch/(total_month-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {decr[0]} (${decr[1]:,})
"""

print(output)

with open ("Analysis/PyPoll_Analysis.txt","w") as outfile:
    outfile.write (output)