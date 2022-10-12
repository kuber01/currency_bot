import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f"Невозможно перевести одинаковые валюты {base}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")

        r = requests.get(f"https://api.currencyapi.com/v3/latest?apikey=KABveRgPl3paBrl7vFl5RnoYmgOvx80FqEMuUsf3&currencies={quote_ticker}&base_currency={base_ticker}")
        total_quote = json.loads(r.content)["data"][keys[quote]]["value"]

        return float(total_quote*amount)