#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global mgo_account_0_a
global mgo_account_1_a
global mgo_account_2_a
global mgo_account_3_a
global mgo_account_4_a
global mgo_account_5_a
global mgo_account_6_a
global mgo_address
global mgo_abi
global mgo
global mgo_call_0
global mgo_call_1
global mgo_call_2
global mgo_call_3
global mgo_call_4
global mgo_call_5
global mgo_call_6
global mgo_call_ab
global mgo_accounts
global mgo_account_0_pw
global mgo_account_1_pw
global mgo_account_2_pw
global mgo_account_3_pw
global mgo_account_4_pw
global mgo_account_5_pw
global mgo_account_6_pw
global mgo_account_0_n
global mgo_account_1_n
global mgo_account_2_n
global mgo_account_3_n
global mgo_account_4_n
global mgo_account_5_n
global mgo_account_6_n
global mgo_account1pw
global mgo_account2pw
global mgo_account3pw
global mgo_account4pw
global mgo_account5pw
global mgo_account6pw
global mgo_last_price
global mgo_accounts_range
global mgo_tokenName
global mgo_last_ethereum_price
global mgo_unlockTime
global mgo_balance
global mgo_balanceOf
global mgo_unlock
global mgo_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
mgo_token_d = 1e8
_e_d = 1e18
mgo_accounts_range = '[0, 6]'
mgo_unlock = web3.personal.unlockAccount
mgo_last_ethereum_price = 370.00
mgo_last_price = 0.88
mgo_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
mgo_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
mgo_tokenName = 'MobileGo Token'
mgo_unlockTime = hex(10000) # Must be hex()
mgo_account_0_a = mgo_accounts[0]
mgo_account_1_a = mgo_accounts[1]
mgo_account_2_a = mgo_accounts[2]
mgo_account_3_a = mgo_accounts[3]
mgo_account_4_a = mgo_accounts[4]
mgo_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
mgo_account_6_a = mgo_accounts[6]
# Supply Unlock Passwords For Transactions Below
mgo_account_0_pw = 'GuildSkrypt2017!@#'
mgo_account_1_pw = ''
mgo_account_2_pw = 'GuildSkrypt2017!@#'
mgo_account_3_pw = ''
mgo_account_4_pw = ''
mgo_account_5_pw = ''
mgo_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
mgo_account_0_n = 'Skotys Bittrex Account'
mgo_account_1_n = 'Jeffs Account'
mgo_account_2_n = 'Skrypts Bittrex Account'
mgo_account_3_n = 'Skotys Personal Account'
mgo_account_4_n = 'Unknown'
mgo_account_5_n = 'Watched \'Bittrex\' Account.'
mgo_account_6_n = 'Watched Account (1)'
# Contract Information Below :
mgo_address = '0x40395044Ac3c0C57051906dA938B54BD6557F212'
mgo_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"name","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_allowance","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"decimals","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"amountBurned","outputs":[{"name":"amountBurned","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_address","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"currentSupply","outputs":[{"name":"currentSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"symbol","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"_currentSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"_initialSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"burn","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"amount","type":"uint256"},{"indexed":false,"name":"currentSupply","type":"uint256"},{"indexed":false,"name":"data","type":"bytes"}],"name":"Burn","type":"event"}]
mgo = web3.eth.contract(abi=mgo_abi, address=mgo_address)
mgo_balanceOf = mgo.call().balanceOf
# End Contract Information
def mgo_update_accounts():
 global mgo_account0
 global mgo_account1
 global mgo_account2
 global mgo_account3
 global mgo_account4
 global mgo_account5
 global mgo_account6
 global mgo_account0_n
 global mgo_account1_n
 global mgo_account2_n
 global mgo_account3_n
 global mgo_account4_n
 global mgo_account5_n
 global mgo_account6_n
 global mgo_account0pw
 global mgo_account1pw
 global mgo_account2pw
 global mgo_account3pw
 global mgo_account4pw
 global mgo_account5pw
 global mgo_account6pw
 mgo_account0 = mgo_account_0_a
 mgo_account1 = mgo_account_1_a
 mgo_account2 = mgo_account_2_a
 mgo_account3 = mgo_account_3_a
 mgo_account4 = mgo_account_4_a
 mgo_account5 = mgo_account_5_a
 mgo_account6 = mgo_account_6_a
 mgo_account0_n = mgo_account_0_n
 mgo_account1_n = mgo_account_1_n
 mgo_account2_n = mgo_account_2_n
 mgo_account3_n = mgo_account_3_n
 mgo_account4_n = mgo_account_4_n
 mgo_account5_n = mgo_account_5_n
 mgo_account6_n = mgo_account_6_n
 mgo_account0pw = mgo_account_0_pw
 mgo_account1pw = mgo_account_1_pw
 mgo_account2pw = mgo_account_2_pw
 mgo_account3pw = mgo_account_3_pw
 mgo_account4pw = mgo_account_4_pw
 mgo_account5pw = mgo_account_5_pw
 mgo_account6pw = mgo_account_6_pw
 print(mgo_tokenName+' Accounts Updated.')
def mgo_update_balances():
 global mgo_call_0
 global mgo_call_1
 global mgo_call_2
 global mgo_call_3
 global mgo_call_4
 global mgo_call_5
 global mgo_call_6
 global mgo_w_call_0
 global mgo_w_call_1
 global mgo_w_call_2
 global mgo_w_call_3
 global mgo_w_call_4
 global mgo_w_call_5
 global mgo_w_call_6
 mgo_update_accounts()
 print('Updating '+mgo_tokenName+' Balances Please Wait...')
 mgo_call_0 = mgo_balanceOf(mgo_account0)
 mgo_call_1 = mgo_balanceOf(mgo_account1)
 mgo_call_2 = mgo_balanceOf(mgo_account2)
 mgo_call_3 = mgo_balanceOf(mgo_account3)
 mgo_call_4 = mgo_balanceOf(mgo_account4)
 mgo_call_5 = mgo_balanceOf(mgo_account5)
 mgo_call_6 = mgo_balanceOf(mgo_account6)
 mgo_w_call_0 = mgo_balance(mgo_account0)
 mgo_w_call_1 = mgo_balance(mgo_account1)
 mgo_w_call_2 = mgo_balance(mgo_account2)
 mgo_w_call_3 = mgo_balance(mgo_account3)
 mgo_w_call_4 = mgo_balance(mgo_account4)
 mgo_w_call_5 = mgo_balance(mgo_account5)
 mgo_w_call_6 = mgo_balance(mgo_account6)
 print(mgo_tokenName+' Balances Updated.')
def mgo_list_all_accounts():
 mgo_update_accounts()
 print(mgo_tokenName+' '+mgo_account0_n+': '+mgo_account0)
 print(mgo_tokenName+' '+mgo_account1_n+': '+mgo_account1)
 print(mgo_tokenName+' '+mgo_account2_n+': '+mgo_account2)
 print(mgo_tokenName+' '+mgo_account3_n+': '+mgo_account3)
 print(mgo_tokenName+' '+mgo_account4_n+': '+mgo_account4)
 print(mgo_tokenName+' '+mgo_account5_n+': '+mgo_account5)
 print(mgo_tokenName+' '+mgo_account6_n+': '+mgo_account6)

def mgo_account_balance(accountNumber):
 mgo_update_balances()
 mgo_ab_account_number = accountNumber
 mgo_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if mgo_ab_account_number == mgo_ab_input[0]:
  print('Calling '+mgo_account0_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account0_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_0 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_0 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[1]:
  print('Calling '+mgo_account1_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account1_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_1 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_1 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[2]:
  print('Calling '+mgo_account2_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account2_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_2 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_2 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[3]:
  print('Calling '+mgo_account3_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account3_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_3 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_3 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[4]:
  print('Calling '+mgo_account4_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account4_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_4 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_4 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[5]:
  print('Calling '+mgo_account5_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account5_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_5 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_5 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number == mgo_ab_input[6]:
  print('Calling '+mgo_account6_n+' '+mgo_tokenName+' Balance: ')
  print(mgo_account6_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_6 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_6 / mgo_token_d * mgo_last_price))
 if mgo_ab_account_number not in mgo_ab_input:
  print('Must Integer Within Range '+mgo_accounts_range+'.')

def mgo_list_all_account_balances():
 mgo_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+mgo_tokenName+' Balance: ')
 print(mgo_account0_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_0 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_0 / mgo_token_d * mgo_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(mgo_account0_n+': Ethereum Balance '+str(mgo_w_call_0 / _e_d)+' $'+str(mgo_w_call_0 / _e_d * mgo_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+mgo_tokenName+' Balance: ')
 print(mgo_account1_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_1 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_1 / mgo_token_d * mgo_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(mgo_account1_n+': Ethereum Balance '+str(mgo_w_call_1 / _e_d)+' $'+str(mgo_w_call_1 / _e_d * mgo_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+mgo_tokenName+' Balance: ')
 print(mgo_account2_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_2 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_2 / mgo_token_d * mgo_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(mgo_account2_n+': Ethereum Balance '+str(mgo_w_call_2 / _e_d)+' $'+str(mgo_w_call_2 / _e_d * mgo_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+mgo_tokenName+' Balance: ')
 print(mgo_account3_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_3 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_3 / mgo_token_d * mgo_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(mgo_account3_n+': Ethereum Balance '+str(mgo_w_call_3 / _e_d)+' $'+str(mgo_w_call_3 / _e_d * mgo_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+mgo_tokenName+' Balance: ')
 print(mgo_account4_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_4 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_4 / mgo_token_d * mgo_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(mgo_account4_n+': Ethereum Balance '+str(mgo_w_call_4 / _e_d)+' $'+str(mgo_w_call_4 / _e_d * mgo_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+mgo_tokenName+' Balance: ')
 print(mgo_account5_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_5 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_5 / mgo_token_d * mgo_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(mgo_account5_n+': Ethereum Balance '+str(mgo_w_call_5 / _e_d)+' $'+str(mgo_w_call_5 /_e_d * mgo_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+mgo_tokenName+' Balance: ')
 print(mgo_account6_n+': '+mgo_tokenName+' Balance: '+str(mgo_call_6 / mgo_token_d)+' Usd/'+mgo_tokenName+' Balance: $'+str(mgo_call_6 / mgo_token_d * mgo_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(mgo_account6_n+': Ethereum Balance '+str(mgo_w_call_6 / _e_d)+' $'+str(mgo_w_call_6 / _e_d * mgo_last_ethereum_price))
def mgo_unlock_all_accounts():
  mgo_unlock_account_0()
  mgo_unlock_account_1()
  mgo_unlock_account_2()
  mgo_unlock_account_3()
  mgo_unlock_account_4()
  mgo_unlock_account_5()
  mgo_unlock_account_6()


def mgo_unlock_account_0():
  global mgo_account0pw
  global mgo_account0
  global mgo_account0_n
  mgo_update_accounts()
  mgo_u_a_0 = mgo_w_unlock(mgo_account0, mgo_account0pw, mgo_unlockTime)
  if mgo_u_a_0 == False:
    if mgo_account0pw == '':
     mgo_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account0_n+' Passphrase Denied: '+mgo_account0pw_r)
    elif mgo_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mgo_account0_n+' Passphrase Denied: '+mgo_account0pw)
  if mgo_u_a_0 == True:
   print(mgo_account0_n+' Unlocked')

def mgo_unlock_account_1():
  global mgo_account1pw
  global mgo_account1
  global mgo_account1_n
  mgo_update_accounts()
  mgo_u_a_1 = mgo_unlock(mgo_account1, mgo_account1pw, mgo_unlockTime)
  if mgo_u_a_1 == False:
    if mgo_account1pw == '':
     mgo_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account1_n+' Passphrase Denied: '+mgo_account1pw_r)
    elif mgo_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mgo_account1_n+' Passphrase Denied: '+mgo_account1pw)
  if mgo_u_a_1 == True:
   print(mgo_account1_n+' Unlocked')

def mgo_unlock_account_2():
  global mgo_account2pw
  global mgo_account2
  global mgo_account2_n
  mgo_update_accounts()
  mgo_u_a_2 = mgo_unlock(mgo_account2, mgo_account2pw, mgo_unlockTime)
  if mgo_u_a_2 == False:
    if mgo_account2pw == '':
     mgo_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account2_n+' Passphrase Denied: '+mgo_account2pw_r)
    elif mgo_account2pw != '':
     print('Unlock Failure With Account '+mgo_account2_n+' Passphrase Denied: '+mgo_account2pw)
  if mgo_u_a_2 == True:
   print(mgo_account2_n+' Unlocked')

def mgo_unlock_account_3():
  global mgo_account3pw
  global mgo_account3
  global mgo_account3_n
  mgo_update_accounts()
  mgo_u_a_3 = mgo_unlock(mgo_account3, mgo_account3pw, mgo_unlockTime)
  if mgo_u_a_3 == False:
    if mgo_account3pw == '':
     mgo_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account3_n+' Passphrase Denied: '+mgo_account3pw_r)
    elif mgo_account3pw != '':
     print('Unlock Failure With Account '+mgo_account3_n+' Passphrase Denied: '+mgo_account3pw)
  if mgo_u_a_3 == True:
   print(mgo_account3_n+' Unlocked')

def mgo_unlock_account_4():
  global mgo_account4pw
  global mgo_account4
  global mgo_account4_n
  mgo_update_accounts()
  mgo_u_a_4 = mgo_unlock(mgo_account4, mgo_account4pw, mgo_unlockTime)
  if mgo_u_a_4 == False:
    if mgo_account4pw == '':
     mgo_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account4_n+' Passphrase Denied: '+mgo_account4pw_r)
    elif mgo_account4pw != '':
     print('Unlock Failure With Account '+mgo_account4_n+' Passphrase Denied: '+mgo_account4pw)
  if mgo_u_a_4 == True:
   print(mgo_account4_n+' Unlocked')

def mgo_unlock_account_5():
  global mgo_account5pw
  global mgo_account5
  global mgo_account5_n
  mgo_update_accounts()
  mgo_u_a_5 = mgo_unlock(mgo_account5, mgo_account5pw, mgo_unlockTime)
  if mgo_u_a_5 == False:
    if mgo_account5pw == '':
     mgo_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account5_n+' Passphrase Denied: '+mgo_account5pw_r)
    elif mgo_account5pw != '':
     print('Unlock Failure With Account '+mgo_account5_n+' Passphrase Denied: '+mgo_account5pw)
  if mgo_u_a_5 == True:
   print(mgo_account5_n+' Unlocked')

def mgo_unlock_account_6():
  global mgo_account6pw
  global mgo_account6
  global mgo_account6_n
  mgo_update_accounts()
  mgo_u_a_6 = mgo_unlock(mgo_account6, mgo_account6pw, mgo_unlockTime)
  if mgo_u_a_6 == False:
    if mgo_account6pw == '':
     mgo_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mgo_account6_n+' Passphrase Denied: '+mgo_account6pw_r)
    elif mgo_account6pw != '':
     print('Unlock Failure With Account '+mgo_account6_n+' Passphrase Denied: '+mgo_account6pw)
  if mgo_u_a_6 == True:
   print(mgo_account6_n+' Unlocked')

def mgo_unlock_account(mgo_ua_accountNumber):
 mgo_update_accounts()
 mgo_ua_account_number = mgo_ua_accountNumber
 mgo_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if mgo_ua_account_number == mgo_ua_input[0]:
  mgo_unlock_account_0()
 if mgo_ua_account_number == mgo_ua_input[1]:
  mgo_unlock_account_1()
 if mgo_ua_account_number == mgo_ua_input[2]:
  mgo_unlock_account_2()
 if mgo_ua_account_number == mgo_ua_input[3]:
  mgo_unlock_account_3()
 if mgo_ua_account_number == mgo_ua_input[4]:
  mgo_unlock_account_4()
 if mgo_ua_account_number == mgo_ua_input[5]:
  mgo_unlock_account_5()
 if mgo_ua_account_number == mgo_ua_input[6]:
  mgo_unlock_account_6()
 if mgo_ua_account_number not in mgo_ua_input:
  print('Must Integer Within Range '+mgo_accounts_range+'.')
 

def mgo_approve_between_accounts(fromAccount, toAccount, msgValue):
  mgo_update_accounts()
  mgo_a_0 = mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(mgo_a_0)

def mgo_approve(fromAccountNumber, toAddress, msgValue):
  mgo_update_accounts()
  mgo_unlock_account(fromAccountNumber)
  mgo_a_1 = mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(mgo_a_1)

def mgo_transfer_between_accounts(fromAccount, toAccount, msgValue):
  mgo_update_accounts()
  mgo_unlock_account(fromAccount)
  mgo_t_0 = mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(mgo_t_0)

def mgo_transfer(fromAccountNumber, toAddress, msgValue):
  mgo_update_accounts()
  mgo_unlock_account(fromAccountNumber)
  mgo_t_1 = mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(mgo_t_1)

def mgo_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  mgo_update_accounts()
  mgo_unlock_account(callAccount)
  mgo_tf_0 = mgo.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(mgo_tf_0)

def mgo_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  mgo_update_accounts()
  mgo_unlock_account(callAccount)
  mgo_tf_1 = mgo.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(mgo_tf_1)
  


def mgo_help():
  print('Following Functions For '+mgo_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * mgo_unlock => web3.personal.unlockAccount
/ * mgo_accounts => web3.personal.listAccounts
/ * mgo_balance = web3.eth.getBalance
** mgo => web3.eth.contract(abi=mgo_abi, address=mgo_address)
** / * mgo_balanceOf => mgo.call().balanceOf

~ Function Listing Below:
~ mgo_update_accounts()
~ mgo_update_balances() \n\r -- => mgo_update_accounts()
~ mgo_list_all_accounts() \n\r -- => mgo_update_accounts()
~ mgo_account_balance(accountNumber) \n\r -- => mgo_update_balances() 
~ mgo_list_all_account_balances() \n\r -- => mgo_update_balances()
~ mgo_unlock_all_accounts() \n\r -- => mgo_unlock_account_0() \n\r -- => mgo_unlock_account_1() \n\r -- => mgo_unlock_account_2() \n\r -- => mgo_unlock_account_3() \n\r -- => mgo_unlock_account_4() \n\r -- => mgo_unlock_account_5() \n\r -- => mgo_unlock_account_6() 
~ mgo_unlock_account_0() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account0, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_1() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account1, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_2() \n\r -- => mgo_update_accounts() \n\r --/ *mgo_w_unlock(mgo_account2, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_3() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account3, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_4() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account4, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_5() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account5, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account_6() \n\r -- => mgo_update_accounts() \n\r -- / *mgo_w_unlock(mgo_account6, mgo_account0pw, mgo_unlockTime)
~ mgo_unlock_account(mgo_ua_accountNumber) \n\r -- => mgo_update_accounts() \n\r -- // mgo_unlock_account_0() \n\r -- // mgo_unlock_account_1() \n\r -- // mgo_unlock_account_2() \n\r -- // mgo_unlock_account_3() \n\r -- // mgo_unlock_account_4() \n\r -- // mgo_unlock_account_5() \n\r -- // mgo_unlock_account_6()
~ mgo_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(fromAccount) \n\r -- / ** mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mgo_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(fromAccountNumber) \n\r -- / ** mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mgo_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(fromAccount) \n\r -- / ** mgo.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ mgo_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(fromAccountNumber) \n\r -- / ** mgo.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mgo_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(callAccount) \n\r / ** mgo.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mgo_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mgo_update_accounts() \n\r -- => mgo_unlock_account(callAccount) \n\r -- / ** mgo.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ mgo_help() <-- You Are Here. ''')