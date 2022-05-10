import csv
import json

list_of_winners = json.load(open('ps_allscraped_2022.json', 'r'))

lista_di_vincitori = open('ps_allscraped_2022.csv', 'w')

csv_writer = csv.writer(lista_di_vincitori)

count = 0

for book in list_of_winners:
    if count == 0:
        header = book.keys()
        csv_writer.writerow(header)

        count += 1

    csv_writer.writerow(book.values())

lista_di_vincitori.close()