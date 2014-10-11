# Python 2.7.6. WBN Calling exchange APIs. original github.com/wobine/blackboard101
import time, json, requests
import urllib2, urllib, cookielib
from time import gmtime, strftime
"""
Some other api pages
doge/btc http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132 
doge/ltc http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=135
doge/cny http://api.btc38.com/v1/ticker.php?c=dog&mk_type=cny
doge/btc http://api.btc38.com/v1/ticker.php?c=dog&mk_type=btc
all http://data.bter.com/api/1/pairs
doge/cny http://data.bter.com/api/1/ticker/doge_cny
doge/btc http://data.bter.com/api/1/ticker/doge_btc
btc/doge https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-doge
btc/doge https://api.vircurex.com/api/get_last_trade.json?base=DOGE&alt=BTC
https://www.btc100.com/apidata/getdata.json
"""

def crypa():
    cryptsyBtc = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
    return cryptsyBtc.json()['return']['markets']['DOGE']['lasttradeprice']
def crypb():
    cryptsyLtc = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=135')
    return cryptsyLtc.json()['return']['markets']['DOGE']['lasttradeprice']
def crypc():
    cryptsyUsd = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=182')
    return cryptsyUsd.json()['return']['markets']['DOGE']['lasttradeprice']

def btera():
    bterBtc = requests.get('http://data.bter.com/api/1/ticker/doge_btc')
    return bterBtc.json()['last']
def bterb():
    bterCny = requests.get('http://data.bter.com/api/1/ticker/doge_cny')
    return bterCny.json()['last']
def bterc():
    bterUsd = requests.get('http://data.bter.com/api/1/ticker/doge_usd')
    return bterUsd.json()['last']

def bittrexa():
    bittCny = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-doge')
    return bittCny.json()['result'][0]['Last']

def vircua():
    vircuBtc = requests.get('https://api.vircurex.com/api/get_last_trade.json?base=DOGE&alt=BTC')
    return vircuBtc.json()['value']

def btc100a():
    btc100Doge = requests.get('https://www.btc100.com/apidata/getdata.json', verify=False)
    return btc100Doge.json()[0]['dic']

btc38a= "http://api.btc38.com/v1/ticker.php?c=dog&mk_type=cny"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
req = urllib2.Request(btc38a, headers=hdr)
page = urllib2.urlopen(req)
btc38resCNY = page.read()

btc38b= "http://api.btc38.com/v1/ticker.php?c=dog&mk_type=btc"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
req = urllib2.Request(btc38b, headers=hdr)
page = urllib2.urlopen(req)
btc38resBTC = page.read()

while True:
    CryptsyBTCLive = float(crypa())
    CryptsyLTCLive = crypb() 
    CryptsyUSDLive = crypc()
    bterBTCLive = float(btera())
    bterCNYLive = bterb()
    bterUSDLive = bterc()
    VircurexBTCLive = float(vircua()) 
    Btc100CNYLive = btc100a()
    btc38resCNYLive = btc38resCNY
    btc38resBTCLive = btc38resBTC

    #convert to sat
    CryptsyBTCLive2 = int(CryptsyBTCLive * 100000000)
    bterBTCLive2 = int(bterBTCLive * 100000000)
    VircurexBTCLive2 = int(VircurexBTCLive * 100000000)
    bittrexBTCLive = int(bittrexa() * 100000000)

    print "-=-=-=", strftime("%H:%M:%S"),"=-=-=-"
    print "       Doge/BTC"
    print "Cryptsy  =", CryptsyBTCLive2 ,"sat"
    print "Btc38    =", btc38resBTCLive[45:51]
    print "Bter     =", bterBTCLive2 ,"sat"
    print "Bittrex  =", bittrexBTCLive ,"sat"
    print "Vircurex =", VircurexBTCLive2 ,"sat"
    print "       Doge/USD"
    print "Cryptsy  =", CryptsyUSDLive
    print "Bter     =", bterUSDLive
    print "       Doge/CNY"
    print "Btc38    =", btc38resCNYLive[46:53]
    print "Bter     =", bterCNYLive
    print "Btc100   =", Btc100CNYLive
    print "       Doge/LTC"
    print "Cryptsy  =", CryptsyLTCLive
    time.sleep(20) # 120 equals two minutes
  
