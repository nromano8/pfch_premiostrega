import csv
import json

list_of_winners = json.load(open('ps_all_1947-2018.json', 'r'))

lista_di_vincitori = open('ps_all_1947-2018.csv', 'w')

csv_writer = csv.writer(lista_di_vincitori)

count = 0

for book in list_of_winners:
    if count == 0:
        header = book.keys()
        csv_writer.writerow(header)

        count += 1

    csv_writer.writerow(book.values())

lista_di_vincitori.close()