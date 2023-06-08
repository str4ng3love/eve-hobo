import json
import yaml


with open('type_names.yaml') as f:
    type_names = yaml.safe_load(f)


smallest_prices = {}


with open('combined_orders_sell.json') as f:
    combined_orders_sell = json.load(f)

    for type_id, item_name in type_names.items():

        min_price = float('inf')

        for order in combined_orders_sell:

            if order['type_id'] == int(type_id):

                if order['price'] < min_price:
                    min_price = order['price']

        smallest_prices[item_name] = min_price


with open('smallest_prices.json', 'w') as f:
    json.dump(smallest_prices, f, indent=2)
