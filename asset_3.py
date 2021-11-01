# Skryptek Asset_3.py For Bittrex Auto-Trader (Don't Fuck With My Squishy!)
# V1.10
# asset_3 = reddcoin (base = BTC)
from bittrex import * # Imports our bittrex client
from account_setup import * # Imports user account setup to allow multi-account usage
bittrex = Bittrex(asset_3_api_key, asset_3_api_secret) # Sets our api key/secret for the currency being traded

# Global definitions for variable usage (allows updating within a function for the entire program)
global raw_asset_3_buy_price # The checksum for (Ask) price for currency as a float
global raw_asset_3_sell_price # The checksum for (Bid) price for currency as a float
global asset_3_invest_int # The integar used to determine rate trade occurs
global asset_3_exchange_int # The integar used to determine rate exchange occurs
global asset_3_buyorder_min # The integar used to determine quantity of trade
global asset_3_sellorder_min # The integar used to determine quantity of exchange
global asset_3_orders_taken # Checksum used for trades refresh / counter
global asset_3_orders_taken2 # Checksum used for trades display / counter
global asset_3_sell_price # Checksum used for (Bid) function
global asset_3_buy_price # Checksum used for (Ask) function
global asset_3_balance # Checksum used for (Balance) function
global base_balance # Checksum used for (Balance) function (BTC)
global base_asset_3_ticker # Checksum used for (Ticker, Call) from client
global test # Skryptek 'Test' Trigger, This is my squishy don't fuck with it
global asset_3_buy # Boolean to trigger exchange
global asset_3_sell # Boolean to trigger trade
global asset_3 # Koin type for trading/exchange
global asset_3_short # Koin short for api reference

# Variable assignment
base = 'BTC'
asset_3 = 'ReddCoin'
asset_3_short = 'RDD'
asset_3_orders_taken = 0 # Checksum used for trades refresh / counter
asset_3_orders_taken2 = 0 # Checksum used for trades display / counter
asset_3_buy = False # Boolean to trigger exchange
asset_3_sell = True # Boolean to trigger trade
base_asset_3_ticker = bittrex.get_ticker(base+'-'+asset_3_short) # Checksum used for (Ticker, Call) from client
asset_3_sell_price = float(base_asset_3_ticker['result']['Bid']) * 100000000 # Checksum used for (Bid) function
asset_3_buy_price = float(base_asset_3_ticker['result']['Ask']) * 100000000 # Checksum used for (Ask) function
raw_asset_3_sell_price = float(base_asset_3_ticker['result']['Bid']) # The checksum for (Bid) price for currency as a float
raw_asset_3_buy_price = float(base_asset_3_ticker['result']['Ask']) # The checksum for (Ask) price for currency as a float
asset_3_balance = bittrex.get_balance(asset_3_short)['result']['Balance'] # Checksum used for (Balance) function


base_balance = bittrex.get_balance(base)['result']['Balance'] # Checksum used for (Balance) function (BTC)

asset_3_invest_base = 50000 # How many satoshi's per trade are you investing?
asset_3_invest_int = 77 # The base investment rate for trade period
asset_3_exchange_int = 78 # The base exchange rate for exchange period
asset_3_buyorder_min = asset_3_invest_base / asset_3_buy_price # The base investment int for minimum trade utilizing (invest_base)
asset_3_sellorder_min = asset_3_invest_base /asset_3_sell_price # The base devestment int for minimum exchange utilizing (invest_base)

yes = True #Trigger for while true that is no longer being used, along with 'Test' which is my squishy


def base_balance_SF(): # Base Balance Checksum Function, Grabs Global Base (I.E. Bittrex (Bitcoin/BTC)) Balance.
  global base_balance # Assigns the variable as global for other functions to utilize
  base_balance = bittrex.get_balance(base)['result']['Balance'] # Uses Bittrex Restful APi To Obtain Account Balance Information

def asset_3_balance_SF(): # Asset_2 Balance Checksum Function, Grabs Global Asset_2 (I.E. First Trade Option/ 'Doge') Balance
  global asset_2_balance # Assigns the variable as global for other functions to utilize
  asset_3_balance = bittrex.get_balance(asset_2_short)['result']['Balance'] # Uses Bittrex Restful APi to obtain balance for Asset_1

def asset_3_sell_price_SF(): # Asset_2 Sell (Bid) Checksum Function, Obtains Last Bid Option For Asset Via Bittrex APi Information.
  global asset_3_sell_price 
  global raw_asset_3_sell_price
  asset_3_sell_price = float(base_asset_3_ticker['result']['Bid']) * 100000000
  raw_asset_3_sell_price = float(base_asset_3_ticker['result']['Bid'])

def asset_3_buy_price_SF():
  global asset_3_buy_price
  global raw_asset_3_buy_price
  asset_3_buy_price = float(base_asset_3_ticker['result']['Ask']) * 100000000
  raw_asset_3_buy_price = float(base_asset_3_ticker['result']['Ask'])

def asset_3_buy_SF():
  asset_3_buy_price_SF()
  base_balance_SF()
  if asset_3_buy_price <= asset_3_invest_int:
   bittrex.buy_limit(str(base)+'-'+str(asset_3_short), float(asset_3_buyorder_min), float(raw_asset_3_buy_price))
   base_balance_SF()
   print('Bought '+asset_3_short+', Remaining '+str(base)+' Balance : '+str(base_balance))
   asset_3_orders_taken += 1
   asset_3_orders_taken2 += 1
   asset_3_buy = False
   asset_3_sell = True

def asset_3_sell_SF():
  asset_3_sell_price_SF()
  asset_3_balance_SF()
  if asset_3_sell_price >= asset_3_exchange_int:
   bittrex.sell_limit(base+'-'+asset_3_short, float(asset_3_sellorder_min), float(raw_asset_3_sell_price))
   asset_3_balance_SF()
   print('Sold '+str(asset_3)+', Remaining '+str(asset_3_short)+' Balance : '+str(asset_3_balance))
   asset_3_orders_taken += 1
   asset_3_orders_taken2 += 1
   asset_3_sell = False
   asset_3_buy = True


def asset_3_orders_taken_SF():
   asset_3_orders_taken = 0
   print("Made "+str(asset_3_orders_taken2)+' Trades So Far. Here Are '+str(base)+'/'+str(asset_3)+' Balances:')
   asset_3_balance_SF()
   base_balance_SF()
   print('Bittrex '+str(base)+' Balance : '+str(base_balance))
   print('Bittrex '+str(asset_1)+' Balance : '+str(asset_3_balance))
