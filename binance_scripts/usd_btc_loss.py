import requests
import sys

#Set Binance API Key and Payloads
api_key = '5jGzsCwL5NqVB6rlk0hYqvIPftxj5075fDcEJ9dhrkISltUYeSQgZm9eqYM2k7MJ'
binance_base = 'https://api.binance.com'
ark_payload ={'symbol':'ARKBTC'}
eth_payload = {'symbol' : 'ETHBTC'}

#Get current price of BTC from Coinbase
cb_btc_url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
res = requests.get(cb_btc_url)
json_obj = res.json()
data = json_obj['data']
symbol_btc = data['base']
btc_price = data['amount']
print("Current: " + symbol_btc + " " + btc_price)


#Prompt for Old BTC Price
btc_old_price = input("Old BTC Price: ")

#Prompt for USD Principle
usd_value = input("USD Amount: ")

#Get Current BTC-USD Satoshi
usd_btc_value = float(usd_value) / float(btc_price)
#print('BTC = ',end='')
#print(round(float(usd_btc_value),8))

#Get Old BTC-USD Satoshi
usd_btc_value_old = float(usd_value) / float(btc_old_price)
#print('Old BTC = ',end='')
#print(round(float(usd_btc_value_old),8))

#Differential
diff_btc = abs(float(usd_btc_value) - float(usd_btc_value_old))
print('USD Loss = ',end='')
print(round(float(diff_btc) * float(btc_price),8))

#Get ARK Values
res = requests.get(binance_base+'/api/v3/ticker/price',params=ark_payload)
ark_price = res.json()['price']
usd_ark_value = (float(ark_price) * float(btc_price))
print('ARK = $',end='')
print(round(usd_ark_value,2))

#Get ETH values
res = requests.get(binance_base+'/api/v3/ticker/price',params=eth_payload)
eth_price = res.json()['price']
usd_eth_value = (float(eth_price) * float(btc_price))
print('ETH = $',end='')
print(round(usd_eth_value,2))
