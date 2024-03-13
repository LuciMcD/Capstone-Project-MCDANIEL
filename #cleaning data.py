
import csv

with open('2005.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)
    
#rounding the numbers to 2 decimal places for easier reading
for row in data:
    try:
        value4 = float(row[4])
        formatted_value4 = f"{value4:.2f}"
        row[4] = formatted_value4
        value7 = float(row[7])
        formatted_value7 = f"{value7:.2f}"
        row[7] = formatted_value7

    except ValueError:
        pass
with open('edited2005.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
