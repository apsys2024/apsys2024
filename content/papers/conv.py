#!/usr/bin/python
import csv
import pprint

with open('apsys24-data.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print('###### ' + row[1] + "<br>\n<p>" + row[3] + "</p>\n")
