import sys
import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            btc_quantity = float(sys.argv[1])
            print(get_btc_price(btc_quantity))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Invalid command-line argument")


def get_btc_price(quantity):
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
        price_per_coin = response["bpi"]["USD"]["rate_float"]
        total_price = price_per_coin * quantity
        return f"${total_price:,.4f}"
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
