import csv

csv_file = open('./test.csv', 'r', newline='', encoding="UTF-8")
reader = csv.reader(csv_file)

for row in reader:
    print('----------------------------')
    for cell in row:
        print(cell)

csv_file.close()
