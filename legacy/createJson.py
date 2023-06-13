import yaml
import json
with open('IndustryTypeMaterials.json', 'r') as data:
    materialTypes = json.load(data)


with open ('type_names.yaml', 'r') as f:
    stuff = yaml.load(f, yaml.FullLoader)
l = 75677

result = []
while l > 0:
    
    if l in stuff:
        result.append({'type_id':l, 'name': stuff[l]})
        l-=1
    else:
        l-=1



l = 75677

for m in materialTypes:
    for r in result:
        if r['type_id'] == m[0]:
            r['reprocess'] = m[1]


with open('result.json', 'w') as file:
    json.dump(result, file)