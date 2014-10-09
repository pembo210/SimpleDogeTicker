# Python 2.7.6. WBN Calling exchange APIs. original github.com/wobine/blackboard101
import time, json, requests
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
"""
 
def crypa():
    cryptsyBtc = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
    return cryptsyBtc.json()['return']['markets']['DOGE']['lasttradeprice']

def crypb():
    cryptsyLtc = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=135')
    return cryptsyLtc.json()['return']['markets']['DOGE']['lasttradeprice']

def btera():
    bterBtc = requests.get('http://data.bter.com/api/1/ticker/doge_btc')
    return bterBtc.json()['last']

def bterb():
    bterCny = requests.get('http://data.bter.com/api/1/ticker/doge_cny')
    return bterCny.json()['last']

def bittrexa():
    bittCny = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-doge')
    return bittCny.json()['result'][0]['Last']

def vircua():
    vircuBtc = requests.get('https://api.vircurex.com/api/get_last_trade.json?base=DOGE&alt=BTC')
    return vircuBtc.json()['value']

while True:
    CryptsyBTCLive = float(crypa())
    CryptsyLTCLive = crypb() 
    bterBTCLive = float(btera())
    bterCNYLive = bterb()
    bittrexBTCLive = int(bittrexa() * 100000000)
    VircurexBTCLive = float(vircua()) 

    #convert to sat
    CryptsyBTCLive2 = int(CryptsyBTCLive * 100000000)
    bterBTCLive2 = int(bterBTCLive * 100000000)
    VircurexBTCLive2 = int(VircurexBTCLive * 100000000)

    print "Doge/BTC"
    print "Cryptsy  =", CryptsyBTCLive2 ,"sat"
    print "Bter     =", bterBTCLive2 ,"sat"
    print "Bittrex  =", bittrexBTCLive ,"sat"
    print "Vircurex =", VircurexBTCLive2 ,"sat"
    print;
    print "Doge/LTC"
    print "Cryptsy =", CryptsyLTCLive
    print;
    print "Doge/CNY"
    print "Bter =", bterCNYLive
    print; print "=-=-=-=-=-=-=--=-="; print;
    time.sleep(10) # 120 equals two minutes
  
