import json
import yaml

# Load type_names.yaml
with open('type_names.yaml') as f:
    type_names = yaml.safe_load(f)

# Create a dictionary to store the smallest prices
smallest_prices = {}

# Load combined_orders_sell.json
with open('combined_orders_sell.json') as f:
    combined_orders_sell = json.load(f)

    # Iterate over each item in type_names.yaml
    for type_id, item_name in type_names.items():
        # Initialize the minimum price for the current item
        min_price = float('inf')

        # Iterate over each dictionary in combined_orders_sell.json
        for order in combined_orders_sell:
            # Check if the dictionary corresponds to the current item and location_id is 60003760
            if order['type_id'] == int(type_id) and order['location_id'] == 60003760:
                # Update the minimum price if a smaller price is found
                if order['price'] < min_price:
                    min_price = order['price']

        # Store the smallest price for the current item
        smallest_prices[item_name] = min_price

# Save the smallest prices in a new JSON file
with open('smallest_prices.json', 'w') as f:
    json.dump(smallest_prices, f, indent=2)
