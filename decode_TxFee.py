import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data['bitcoin']['usd']
    return price

def get_bitcoin_transactions(address, price):
    # Request URL
    url = f'https://mempool.space/api/address/{address}/txs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    # Sending the request and loading data
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)

    # Processing each transaction
    for item in data:
        print("Transaction Details:")
        # Transaction input details
        vin_length = len(item["vin"])
        for i in range(vin_length):
            txid = item["vin"][0]['txid']
            if item["vin"][i]["prevout"]["scriptpubkey_address"]==address:
                in_value = item["vin"][i]["prevout"]["value"]
            else:
                continue
            print(f"Input Transaction ID: {txid}")
            print(f"Input Value: {in_value} satoshis")

        # Transaction output details
        out_length = len(item["vout"])
        for i in range(out_length):
            if item["vout"][i]["scriptpubkey_address"] == address:
                print(f"Output Transaction Index: {i}")
                out_value = item["vout"][i]["value"]
                cost = in_value - out_value
                print(f"Output Value: {out_value} satoshis")
            else:
                cost = in_value

        # Convert Satoshis to Bitcoins
        btc_amount = cost / 100000000
        print(f"Cost value: {cost} satoshis")
        print(f"Bitcoin Current Price: ${price}")
        print(f"Transaction Fee Equals: ${price*btc_amount:.2f}")
        print("\n")

def main():
    # Example usage
    my_address = txid = os.environ.get("my_address")
    price = get_bitcoin_price()
    get_bitcoin_transactions(my_address, price)

if __name__ == "__main__":
    main()
