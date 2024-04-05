import requests

kartoshka = "https://nbu.uz/uz/exchange-rates/json/"

response = requests.get(kartoshka)

data = response.json()

for x in data:
    # if x["code"] == "RUB":
    #     print(x)
    print(x)


