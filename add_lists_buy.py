import json

# Read the original JSON file as a string
with open('orders_buy.json', 'r') as file:
    json_string = file.read()

# Extract individual JSON objects or arrays from the string
json_objects = []
start_index = 0

while start_index < len(json_string):
    try:
        json_object, end_index = json.JSONDecoder(
        ).raw_decode(json_string[start_index:])
        json_objects.append(json_object)
        start_index += end_index
    except json.JSONDecodeError:
        start_index += 1

# Combine the extracted JSON objects or arrays into a list
combined_data = []
for obj in json_objects:
    if isinstance(obj, dict):
        combined_data.append(obj)
    elif isinstance(obj, list):
        combined_data.extend(obj)

# Write the combined data to a new JSON file
with open('combined_orders_buy.json', 'w') as file:
    json.dump(combined_data, file)
