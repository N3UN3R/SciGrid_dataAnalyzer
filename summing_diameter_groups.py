import json
import ast

with open('germany.json') as file:
    data = json.load(file)

print(data)

diameter_groups = {}
diameter_groups['bis500'] = []
diameter_groups['500bis900'] = []
diameter_groups['900plus'] = []

for k in data['intern'].keys():
    print(k)
    diameter = data['intern'][k]['diameter_mm']
    length = data['intern'][k]['length_km']

    if diameter <= 500:
        diameter_groups['bis500'].append(length)

    if 500 < diameter < 900:
        diameter_groups['500bis900'].append(length)

    if diameter >= 900:
        diameter_groups['900plus'].append(length)

print(diameter_groups)

total_length = []

german_groups = {}
german_groups['bis500'] = []
german_groups['500bis900'] = []
german_groups['900plus'] = []

for k,v in diameter_groups.items():
    print(k)
    print(sum(v))
    total_length.append(sum(v))
    german_groups[k].append(sum(v))

print(total_length)

print(sum(total_length))

print(german_groups)



import json
out_file = open("germany_diameter_group_sums.json", "w")

json.dump(german_groups, out_file)
