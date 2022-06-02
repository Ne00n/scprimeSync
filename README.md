# scprimeSync
Sync your Node pricing with current SCP listed Price

**Dependencies**<br />
```
apt-get install -y git python3 python3-pip && pip3 install python-coinmarketcap
```

**API Key**<br />
https://coinmarketcap.com/api/</br>
Free up to 10k/req per month</br>
```
git clone https://github.com/Ne00n/scprimeSync.git && cd scprimeSync
cp config.example.json config.json
sed -i -e 's/xxxx-xxxx-xxxx-xxxx/YOURKEY/g' config.json
sed -i -e 's/4.0/TARGETPRICE/g' config.json
```
As of today you can go up to 4$ per TB

**Test**<br />
```
python3 sync.py
```