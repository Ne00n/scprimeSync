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
sed -i -e 's/YOURKEY/xxx-xxxx-xxxx-xxx-xxxx/g' scprimeSync/sync.py
```

**Test**<br />
```
scprimeSync/sync.py
```