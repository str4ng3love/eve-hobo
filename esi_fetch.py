import json
import requests

# Function for fetching prices from the endpoint (order type eather sell or buy - all small letters)


def get_orders(page_nr, order_type):

    url = f"https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=&{order_type}page={page_nr}"

    # Set your User-Agent header to identify your application
    headers = {"User-Agent": "eve-hobo"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if an HTTP error occurs

        orders = response.json()
        with open(f"orders_{order_type}.json", "a") as file:
            json.dump(orders, file)
        return orders

    except requests.exceptions.RequestException as e:
        print("Error occurred during the API request:", e)
        return None


# Example usage
for i in range(1, 353):
    get_orders(i, "buy")
