import requests
import sys
import json

api_key = ''

def main():
    if len(sys.argv) == 1:
        sys.exit('Missing commad-line argument')
    elif len(sys.argv) == 2:
        try:
            print(f'${get_price(api_key)*float(sys.argv[1]):,.4f}')
        except ValueError:
            sys.exit('Commad-line argument is not a number')
    else:
        sys.exit('Commad-line argument is not a number')

def get_price(key):
    try:
         response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey=' + key)
    except requests.RequestException:
        sys.exit('Bad connection')

    return float(response.json()['data']['priceUsd'])

main()
