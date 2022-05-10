import json
import csv

list_of_writers = json.load(open('ps_nominees_2019-2021.json', 'r'))

lista_scrittori = open('ps_nominees_2019-2021.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(lista_scrittori)

count = 0

for name in list_of_writers:
    if count == 0:
        header = name.keys()
        csv_writer.writerow(header)

        count += 1

    csv_writer.writerow(name.values())

lista_scrittori.close()