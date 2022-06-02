#!/usr/bin/python3
import coinmarketcapapi, json, os
path = os.path.dirname(os.path.realpath(__file__))

print("Loading config.json")
with open(f"{path}/config.json") as handle:
    config = json.loads(handle.read())

cmc = coinmarketcapapi.CoinMarketCapAPI(config['apiKey'])
r = cmc.cryptocurrency_quotes_latest(symbol='SCP', convert='USD')
price = r.data['SCP']['quote']['USD']['price']
minPrice = config['target'] #price per TB in USD
coins =  minPrice / (price / 100) / 100
#Failsafe
#Don't go below 3
if coins < 3: coins = 3
#Format
coins = "{:.2f}".format(coins)
print(f"Setting {coins}")
os.system(f"current/spc host config minstorageprice {coins}SCP")
os.system(f"current/spc host config collateral {coins}SCP")