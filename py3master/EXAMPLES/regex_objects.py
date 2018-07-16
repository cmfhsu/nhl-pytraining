#!/usr/bin/env python
import re

r = re.compile(r"\d{2,}")  # match 2 or more digits

with open("../DATA/spam.txt","r") as SPAM:
    for line in SPAM:
        if r.search(line):
            print(line, end=' ')
