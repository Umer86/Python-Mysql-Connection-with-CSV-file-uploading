import csv

with open('country.csv', encoding='utf-8', mode='r') as file:
    reader = csv.reader(file)
    # To separate the header and data,
    # use the enumerate() function to get the index of each line:

    for line_no, line in enumerate(reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data
