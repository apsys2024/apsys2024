#!/usr/bin/python3
import pandas as pd

print("# Posters")
print("")

i = 0
df = pd.read_csv('apsys24posters-data.csv')
for row in df.itertuples():
    i = i + 1
    print("###### (%d) %s" % (i, row[2]))
    print("<p>%s</p>\n" % (row[5]))
