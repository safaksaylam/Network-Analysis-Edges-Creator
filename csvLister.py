import csv

categoryList = []

with open('stack3[Nodes].csv', "rt") as f:
    with open('stack3[Edges].csv', 'w') as w:
        r = csv.DictReader(f)
        writer = csv.writer(w)
        writer.writerow((
            'Source',
            'Target',
            'Type',
            'id',
            'label',
            'timeset',
            'weight'
        ))


        for row in r:
            with open('stack3[Nodes]2.csv', "rt") as f2:
                r2 = csv.DictReader(f2)
                for row2 in r2:
                    if row['category'] in row2['category']:
                        writer.writerow((
                            row['id'],
                            row2['id'],
                            'Directed',
                            '0',
                            '',
                            '',
                            '1.0'
                        ))
