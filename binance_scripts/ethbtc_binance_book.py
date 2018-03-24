import requests
import sys
from time import sleep
from termcolor import *

#All endpoints return either a JSON object or array.
#4XX return = malformed request
#429 return = breaking a request rate limit
#418 return = IP is auto-banned for too much 429 
#5XX return = internal error on Binance side
#504 return = API success but NO RESPONSE
#res = requests.get(base+'/api/v1/ping') #Used for testing API connectivity

api_key = '5jGzsCwL5NqVB6rlk0hYqvIPftxj5075fDcEJ9dhrkISltUYeSQgZm9eqYM2k7MJ'
base = 'https://api.binance.com'
ark_payload = {'symbol' : 'ARKBTC'}
eth_payload = {'symbol' : 'ETHBTC'}

res = requests.get(base+'/api/v3/ticker/price',params=ark_payload)
ark_price = res.json()['price']
#usd_ark_value = (float(ark_price) * float(usd_btc_value))
#print(usd_ark_value)

#bookTicker
i = 0
end = 10000
while(i != end):
	sleep(0.5)
	res = requests.get(base+'/api/v3/ticker/bookTicker',params=eth_payload)

	jobj = res.json()
	symbol = jobj['symbol']
	bidQty = jobj['bidQty']
	bidPrice = jobj['bidPrice']
	askQty = jobj['askQty']
	askPrice = jobj['askPrice']
	
	bidQty = round(float(bidQty),2)
	askQty = round(float(askQty),2)
	
	bidQty = str(bidQty)
	askQty = str(askQty)
		
	cprint('\u2666 ' + bidQty + ' | ' + '\u20BF ' + bidPrice, 'green', end='')
	cprint('      ' + '\u2666 ' + askQty + ' | ' + '\u20BF ' + askPrice, 'red')
	
	i = i+1
	if(i == end):
		break

#res = requests.get(base+'/api/v3/ticker/bookTicker',params=ark_payload)
#res = requests.get(base+'/api/v3/ticker/price',params=eth_payload)
#eth_price = res.json()['price']


