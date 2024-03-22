import csv

# Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)

    # Write a header row
    csvwriter.writerow(['Name', 'Age', 'Occupation'])

    # Write some data rows
    csvwriter.writerow(['John', '30', 'Software Engineer'])
    csvwriter.writerow(['Jane', '25', 'Teacher'])
    csvwriter.writerow(['Bob', '40', 'Doctor'])
