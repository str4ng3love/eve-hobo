import json

with open('mini.json') as json_file:
    data = json.load(json_file)
    result = []
    ri = 0
    for i in data:
        if len(result) == 0:
           newEntry = i['typeID'], {i['materialTypeID']: i['quantity']}
           print(newEntry)
           result.append(newEntry)
          
        elif result[ri][0] == i['typeID']:
         
           result[ri][1][i['materialTypeID']] = i['quantity']
           
        else:
            newEntry = i['typeID'], {i['materialTypeID']: i['quantity']}
            result.append(newEntry)
            ri+=1



with open('IndustryTypeMaterials.json', 'w') as f:
    json.dump(result, f, indent=2)