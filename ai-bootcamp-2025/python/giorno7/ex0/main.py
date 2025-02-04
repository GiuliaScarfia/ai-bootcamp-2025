#Ordino per Cognome

import csv

data =[]

with open("data.csv", encoding="utf-8") as fd:
    reader = csv.reader(fd)
    header = next(reader)

    for line in reader:
        data.append(line)

data.sort(key=lambda x: x[1].lower())

for i, line in enumerate(data, start=1):
    print([i]+line)

with open("data2.csv", mode="w", encoding="utf-8") as fd:
    writer = csv.writer(fd)
    writer.writerow(header)
    writer.writerows(data)

# Bonus: Ordino per Cognome e Nome
# Chiave da usare: key=lambda x: (x[1].lower(), x[0].lower())
