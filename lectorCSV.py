import csv
import random
 
def sorteador():
    with open('paises.csv', 'r') as csv_file:
        # Crea un lector CSV
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader)
        lista = list(csv_reader)
        random_number = random.randint(0, len(lista))
        return lista[random_number][0], lista[random_number][3]