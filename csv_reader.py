import csv

temp_list = []

with open('IGGIELGN_PipeSegments.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        temp_list .append(row)


import ast
#dictionary erstellen, um nur deutsche pipelines zu haben
germany = {}
germany['intern']={}
for row in temp_list:
    #filtern nach nur deutschen pipelines
    if row[6][2:4] == 'DE' and row[6][8:10] == 'DE':
        name = row[0]
        temp_dict = ast.literal_eval(row[8])
        print(temp_dict)
        print(temp_dict['diameter_mm'])
        print(name)
        germany['intern'][name] = {}
        germany['intern'][name]['diameter_mm'] = temp_dict['diameter_mm']
        germany['intern'][name]['length_km'] = temp_dict['length_km']


import json
out_file = open("germany.json", "w")

json.dump(germany, out_file)#, indent=6)




