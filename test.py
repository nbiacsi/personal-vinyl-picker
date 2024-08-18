from random import choice
import csv

vinyls = None
with open (r"vinyls.csv", "r") as sheet:
    reader = csv.reader(sheet)
    next(reader)
    vinyls = sorted(reader, key=lambda row: (row[1], row[0]))

print(choice(vinyls))