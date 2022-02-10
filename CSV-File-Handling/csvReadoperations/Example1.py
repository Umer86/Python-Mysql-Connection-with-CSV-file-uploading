import csv

with open('country.csv', mode='r', encoding='utf8') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
