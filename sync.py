#!/usr/bin/python3
import coinmarketcapapi, json, os

cmc = coinmarketcapapi.CoinMarketCapAPI('YOURKEY')
r = cmc.cryptocurrency_quotes_latest(symbol='SCP', convert='USD')
price = r.data['SCP']['quote']['USD']['price']
minPrice = 3 #price per TB in USD
print(price)
coins =  minPrice / (price / 100) / 100
#Failsafe
#Suggest by scprime dev's max at 15
if coins > 15: coins = 15
#Don't go below 1
if coins < 1: coins = 1
#Format
coins = "{:.2f}".format(coins)
print(f"Setting {coins}")
os.system(f"ScPrime-v1.6.0-linux-amd64/spc host config minstorageprice {coins}SCP")