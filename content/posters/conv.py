#!/usr/bin/python3
import pandas as pd

print("# Posters")
print("")

i = 0
df = pd.read_csv('apsys24posters-data.csv')
for row in df.itertuples():
    i = i + 1
    id = row[1]
    title = row[2]
    authors = row[5]
    print("###### (%d) %s" % (i, title))
    print("<p>%s<br>" % (authors))
    print("[<a href=\"apsys24posters-paper%d.pdf\">Abstract</a>]</p>\n" % (id))
