# -*- coding: utf-8 -*-
import csv
with open('_team_.tsv', encoding='utf8') as f:
    reader = csv.DictReader(f)
    print ('\t'.join(reader.fieldnames))
    for r in reader:
        print ('\t'.join([r[k] for k in reader.fieldnames]) )
