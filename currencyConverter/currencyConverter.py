import json
import requests


API_KEY = 'cur_live_sRtZSbMWTI3rBfacFWGVe0gF5bDSC2PyZnIeYKSO'
BASE_URL = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_sRtZSbMWTI3rBfacFWGVe0gF5bDSC2PyZnIeYKSO'

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)

    payload = {
        'access_key': API_KEY
    }

    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data


# print (get_rates(mock=True))


def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        rates.get(currency)
    else:
        raise ValueError(f'{currency} is not a valid currency.')


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print (f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')
    return conversion


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    convert_currency(100, 'EUR', 'JPY', rates=rates)


if __name__ == '__main__':
    main()



# Potential add-ons
  # 1. Enter base currency
  # 2. Enter conversion currency
  # 3. Enter value
  # 4. Errors for currency and amount (value)