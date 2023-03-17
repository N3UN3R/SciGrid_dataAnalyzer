import json

with open('IGGIELGN_PipeSegments.geojson') as file:
    data = json.load(file)


german_features = []
counter = 0
for i in data['features']:
    country1 = data['features'][counter]['properties']['country_code'][0]
    country2 = data['features'][counter]['properties']['country_code'][1]

    counter +=1

    if country1 == 'DE' and country2 == 'DE':
        print("Hier")
        german_features.append(i)


data['features']
new_dic = {}
new_dic['type'] = data['type']
new_dic['features'] = german_features

import json
out_file = open("geotest.json", "w")
json.dump(new_dic, out_file)