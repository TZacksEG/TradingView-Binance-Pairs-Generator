import requests

print("Welcome to ZCrypto Binance Pairs Generator\n")
question = int(input("What Market do you want?\n"
                     "type 1 for USDT OR 2 For BNB OR 3 for ETH OR 4 for BTC\n"))

if question == 1:
    base = "USDT"
elif question == 2:
    base = "BNB"
elif question == 3:
    base = "ETH"
elif question == 4:
    base = "BTC"
else:
    print("fetching All Markets")
    base = ""

link = "https://api.binance.com/api/v1/exchangeInfo"

results = requests.get(link).json()

pair_list = []


def getcoins():
    for x in range(len(results["symbols"])):
        status = results["symbols"][x]["status"]
        coin = results["symbols"][x]["symbol"]
        if status != "TRADING":
            continue
        if not coin.endswith(base):
            continue

        if (
                ("UP" in coin)
                or ("DOWN" in coin)
                or ("BULL" in coin)
                or ("BEAR" in coin)
        ):
            continue
        pair_list.append(f"BINANCE:{coin},\n")
    sorted_coins = (''.join(sorted(pair_list)))
    return sorted_coins


with open(f"pairs{base}.txt", "w") as file:
    for line in getcoins():
        file.write(line)
    file.close()
    print(f"{len(pair_list)} Pairs has been written into pairs{base}.txt")
