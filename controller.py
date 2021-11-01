from bittrex import *
bittrex = Bittrex("457a3ef1d2b84cde86b822d46e726125", "b7f944e24a5443c2b061c55d34604c21")
global eth_invest_int
global eth_exchange_int
global eth_buyorder_min
global eth_sellorder_min
global raw_eth_buy_price
global raw_eth_sell_price
global raw_doge_buy_price
global raw_doge_sell_price
global doge_invest_int
global doge_exchange_int
global doge_buyorder_min
global doge_sellorder_min
global trade_doge
global trade_btc
global orders_taken
global orders_taken2
global doge_sell_price
global doge_buy_price
global balance_dogecoin
global eth_sell_price
global eth_buy_price
global balance_ether
global balance_bitc
global btc_doge_ticker
global btc_eth_ticker
global test
global Trade_Eth
global Sell_Eth

orders_taken = 0
orders_taken2 = 0

trade_doge = True
trade_btc = False
btc_doge_ticker = bittrex.get_ticker('BTC-DOGE')
btc_eth_ticker = bittrex.get_ticker('BTC-ETH')
doge_sell_price = float(btc_doge_ticker['result']['Bid']) * 100000000
doge_buy_price = float(btc_doge_ticker['result']['Ask']) * 100000000
raw_doge_sell_price = float(btc_doge_ticker['result']['Bid'])
raw_doge_buy_price = float(btc_doge_ticker['result']['Ask'])
balance_dogecoin = bittrex.get_balance('DOGE')['result']['Balance']

eth_sell_price = float(btc_eth_ticker['result']['Bid']) * 100000000
eth_buy_price = float(btc_eth_ticker['result']['Ask']) * 100000000
raw_eth_sell_price = float(btc_eth_ticker['result']['Bid'])
raw_eth_buy_price = float(btc_eth_ticker['result']['Ask'])
balance_ether = bittrex.get_balance('ETH')['result']['Balance']

balance_bitc = bittrex.get_balance('BTC')['result']['Balance']


eth_invest_int = 8129999
eth_exchange_int = 8140000
eth_buyorder_min = 0.00050000 / raw_eth_buy_price
eth_sellorder_min = 0.00050000 / raw_eth_sell_price

doge_invest_int = doge_sell_price
doge_exchange_int = doge_buy_price
doge_buyorder_min = 0.00050000 / raw_doge_buy_price
doge_sellorder_min = 0.00050000 / raw_doge_sell_price


yes = True

test = 'test'

def balance_eth():
  global balance_ether
  balance_ether = bittrex.get_balance('ETH')['result']['Balance']

def eth_sell():
  global eth_sell_price
  global raw_eth_sell_price
  eth_sell_price = float(btc_eth_ticker['result']['Bid']) * 100000000
  raw_eth_sell_price = float(btc_eth_ticker['result']['Bid'])

def eth_buy():
  global eth_buy_price
  global raw_eth_buy_price
  eth_buy_price = float(btc_eth_ticker['result']['Ask']) * 100000000
  raw_eth_buy_price = float(btc_eth_ticker['result']['Ask'])


def balance_btc():
  global balance_bitc
  balance_bitc = bittrex.get_balance('BTC')['result']['Balance']







def balance_doge():
  global balance_dogecoin
  balance_dogecoin = bittrex.get_balance('DOGE')['result']['Balance']

def doge_sell():
  global doge_sell_price
  global raw_doge_sell_price
  doge_sell_price = float(btc_doge_ticker['result']['Bid']) * 100000000
  raw_doge_sell_price = float(btc_doge_ticker['result']['Bid'])

def doge_buy():
  global doge_buy_price
  global raw_doge_buy_price
  doge_buy_price = float(btc_doge_ticker['result']['Ask']) * 100000000
  raw_doge_buy_price = float(btc_doge_ticker['result']['Ask'])


Trade_Eth = True
Sell_Eth = False

while True:
 if yes == True:
  eth_buy()
  balance_btc()
  if eth_buy_price <= eth_invest_int and Trade_Eth == True and orders_taken <= 10:
   bittrex.buy_limit('BTC-ETH', float(eth_buyorder_min), float(raw_eth_buy_price))
   print('Bought ETH, Remaining Bitcoin Balance : '+str(balance_bitc))
   orders_taken += 1
   orders_taken2 += 1
   Trade_Eth = False
   Sell_Eth = True
 if yes == True and Sell_Eth == True and orders_taken <= 10:
  eth_sell()
  balance_eth()
  if eth_sell_price >= eth_exchange_int:
   bittrex.sell_limit('BTC-ETH', float(eth_sellorder_min), float(raw_eth_sell_price))
   balance_eth()
   print('Sold ETH, Remaining Balance : '+str(balance_ether))
   orders_taken += 1
   orders_taken2 += 1
   Sell_Eth = False
   Trade_Eth = True
 if yes == True and orders_taken >= 10:
   orders_taken = 0
   print("Made "+str(orders_taken2)+' Trades So Far. Here Are Eth/Btc Balances')
   balance_eth()
   balance_btc()
   print('Bittrex Bitcoin Balance : '+str(balance_bitc))
   print('Bittrex ETH Balance : '+str(balance_ether))
 if yes == False:
  print('Test Complete Changing "yes" to "None"')
  yes = None
 if yes == None:
  break
 else:
  yes = True

 if test == True:
  balance_eth()
  eth_buy()
  eth_sell()
  print('Ether Balance: '+str(balance_ether))
  print('Ether Ask Satoshi : '+str(eth_buy_price))
  print('Ether Bid Satoshi : '+str(eth_sell_price))
  test = False