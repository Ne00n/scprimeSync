# scprimeSync
Sync your Node pricing with current SCP listed Price

**Dependencies**<br />
```
apt-get install -y python3 python3-pip
pip3 install python-coinmarketcap
```

**API Key**<br />
https://coinmarketcap.com/api/</br>
Free up to 10k/req per month</br>
```
cp config.example.json config.json
sed -i -e 's/YOURKEY/xxxx-xxxx-xxxx-xxxx/g' config.json
sed -i -e 's/TARGETPRICE/4.0/g' config.json
```
As of today you can go up to 4$ per TB

**Test**<br />
```
scprimeSync/sync.py
```