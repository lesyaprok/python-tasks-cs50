import requests
import sys

def main():
    bitcoins = get_bitcoins()
    print(convert_bitcoin_to_usd(bitcoins))

def get_bitcoins():
    args = sys.argv[1:]
    try:
        bitcoins = float(args[0])
        return bitcoins
    except ValueError:
        sys.exit("Command-line argument is not a number!")
    except IndexError:
        sys.exit("Missing command-line argument")

def convert_bitcoin_to_usd(bitcoin):
    try:
        api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(api_url).json()
        rate = float(response["bpi"]["USD"]["rate"].replace(",",""))
        return f"${(bitcoin * rate):,.4f}"
    except requests.RequestException:
         sys.exit("Unable to get rate info")

main()