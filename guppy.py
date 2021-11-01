#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global guppy_account_0_a
global guppy_account_1_a
global guppy_account_2_a
global guppy_account_3_a
global guppy_account_4_a
global guppy_account_5_a
global guppy_account_6_a
global guppy_address
global guppy_abi
global guppy
global guppy_call_0
global guppy_call_1
global guppy_call_2
global guppy_call_3
global guppy_call_4
global guppy_call_5
global guppy_call_6
global guppy_call_ab
global guppy_accounts
global guppy_account_0_pw
global guppy_account_1_pw
global guppy_account_2_pw
global guppy_account_3_pw
global guppy_account_4_pw
global guppy_account_5_pw
global guppy_account_6_pw
global guppy_account_0_n
global guppy_account_1_n
global guppy_account_2_n
global guppy_account_3_n
global guppy_account_4_n
global guppy_account_5_n
global guppy_account_6_n
global guppy_account1pw
global guppy_account2pw
global guppy_account3pw
global guppy_account4pw
global guppy_account5pw
global guppy_account6pw
global guppy_last_price
global guppy_accounts_range
global guppy_tokenName
global guppy_last_ethereum_price
global guppy_unlockTime
global guppy_balance
global guppy_balanceOf
global guppy_unlock
global guppy_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
guppy_token_d = 1e3
_e_d = 1e18
guppy_accounts_range = '[0, 6]'
guppy_unlock = web3.personal.unlockAccount
guppy_last_ethereum_price = 370.00
guppy_last_price = 0.26
guppy_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
guppy_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
guppy_tokenName = 'Guppy Token'
guppy_unlockTime = hex(10000) # Must be hex()
guppy_account_0_a = guppy_accounts[0]
guppy_account_1_a = guppy_accounts[1]
guppy_account_2_a = guppy_accounts[2]
guppy_account_3_a = guppy_accounts[3]
guppy_account_4_a = guppy_accounts[4]
guppy_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
guppy_account_6_a = guppy_accounts[6]
# Supply Unlock Passwords For Transactions Below
guppy_account_0_pw = 'GuildSkrypt2017!@#'
guppy_account_1_pw = ''
guppy_account_2_pw = 'GuildSkrypt2017!@#'
guppy_account_3_pw = ''
guppy_account_4_pw = ''
guppy_account_5_pw = ''
guppy_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
guppy_account_0_n = 'Skotys Bittrex Account'
guppy_account_1_n = 'Jeffs Account'
guppy_account_2_n = 'Skrypts Bittrex Account'
guppy_account_3_n = 'Skotys Personal Account'
guppy_account_4_n = 'Unknown'
guppy_account_5_n = 'Watched \'Bittrex\' Account.'
guppy_account_6_n = 'Watched Account (1)'
# Contract Information Below :
guppy_address = '0xf7B098298f7C69Fc14610bf71d5e02c60792894C'
guppy_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minter","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"o_success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_value","type":"uint256"}],"name":"createIlliquidToken","outputs":[{"name":"o_success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_recipient","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"o_success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"endMintingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_value","type":"uint256"}],"name":"createToken","outputs":[{"name":"o_success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"illiquidBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"o_success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"LOCKOUT_PERIOD","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"o_remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"makeLiquid","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_minter","type":"address"},{"name":"_endMintingTime","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_recipient","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
guppy = web3.eth.contract(abi=guppy_abi, address=guppy_address)
guppy_balanceOf = guppy.call().balanceOf
# End Contract Information
def guppy_update_accounts():
 global guppy_account0
 global guppy_account1
 global guppy_account2
 global guppy_account3
 global guppy_account4
 global guppy_account5
 global guppy_account6
 global guppy_account0_n
 global guppy_account1_n
 global guppy_account2_n
 global guppy_account3_n
 global guppy_account4_n
 global guppy_account5_n
 global guppy_account6_n
 global guppy_account0pw
 global guppy_account1pw
 global guppy_account2pw
 global guppy_account3pw
 global guppy_account4pw
 global guppy_account5pw
 global guppy_account6pw
 guppy_account0 = guppy_account_0_a
 guppy_account1 = guppy_account_1_a
 guppy_account2 = guppy_account_2_a
 guppy_account3 = guppy_account_3_a
 guppy_account4 = guppy_account_4_a
 guppy_account5 = guppy_account_5_a
 guppy_account6 = guppy_account_6_a
 guppy_account0_n = guppy_account_0_n
 guppy_account1_n = guppy_account_1_n
 guppy_account2_n = guppy_account_2_n
 guppy_account3_n = guppy_account_3_n
 guppy_account4_n = guppy_account_4_n
 guppy_account5_n = guppy_account_5_n
 guppy_account6_n = guppy_account_6_n
 guppy_account0pw = guppy_account_0_pw
 guppy_account1pw = guppy_account_1_pw
 guppy_account2pw = guppy_account_2_pw
 guppy_account3pw = guppy_account_3_pw
 guppy_account4pw = guppy_account_4_pw
 guppy_account5pw = guppy_account_5_pw
 guppy_account6pw = guppy_account_6_pw
 print(guppy_tokenName+' Accounts Updated.')
def guppy_update_balances():
 global guppy_call_0
 global guppy_call_1
 global guppy_call_2
 global guppy_call_3
 global guppy_call_4
 global guppy_call_5
 global guppy_call_6
 global guppy_w_call_0
 global guppy_w_call_1
 global guppy_w_call_2
 global guppy_w_call_3
 global guppy_w_call_4
 global guppy_w_call_5
 global guppy_w_call_6
 guppy_update_accounts()
 print('Updating '+guppy_tokenName+' Balances Please Wait...')
 guppy_call_0 = guppy_balanceOf(guppy_account0)
 guppy_call_1 = guppy_balanceOf(guppy_account1)
 guppy_call_2 = guppy_balanceOf(guppy_account2)
 guppy_call_3 = guppy_balanceOf(guppy_account3)
 guppy_call_4 = guppy_balanceOf(guppy_account4)
 guppy_call_5 = guppy_balanceOf(guppy_account5)
 guppy_call_6 = guppy_balanceOf(guppy_account6)
 guppy_w_call_0 = guppy_balance(guppy_account0)
 guppy_w_call_1 = guppy_balance(guppy_account1)
 guppy_w_call_2 = guppy_balance(guppy_account2)
 guppy_w_call_3 = guppy_balance(guppy_account3)
 guppy_w_call_4 = guppy_balance(guppy_account4)
 guppy_w_call_5 = guppy_balance(guppy_account5)
 guppy_w_call_6 = guppy_balance(guppy_account6)
 print(guppy_tokenName+' Balances Updated.')
def guppy_list_all_accounts():
 guppy_update_accounts()
 print(guppy_tokenName+' '+guppy_account0_n+': '+guppy_account0)
 print(guppy_tokenName+' '+guppy_account1_n+': '+guppy_account1)
 print(guppy_tokenName+' '+guppy_account2_n+': '+guppy_account2)
 print(guppy_tokenName+' '+guppy_account3_n+': '+guppy_account3)
 print(guppy_tokenName+' '+guppy_account4_n+': '+guppy_account4)
 print(guppy_tokenName+' '+guppy_account5_n+': '+guppy_account5)
 print(guppy_tokenName+' '+guppy_account6_n+': '+guppy_account6)

def guppy_account_balance(accountNumber):
 guppy_update_balances()
 guppy_ab_account_number = accountNumber
 guppy_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if guppy_ab_account_number == guppy_ab_input[0]:
  print('Calling '+guppy_account0_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account0_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_0 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_0 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[1]:
  print('Calling '+guppy_account1_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account1_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_1 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_1 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[2]:
  print('Calling '+guppy_account2_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account2_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_2 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_2 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[3]:
  print('Calling '+guppy_account3_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account3_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_3 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_3 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[4]:
  print('Calling '+guppy_account4_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account4_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_4 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_4 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[5]:
  print('Calling '+guppy_account5_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account5_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_5 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_5 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number == guppy_ab_input[6]:
  print('Calling '+guppy_account6_n+' '+guppy_tokenName+' Balance: ')
  print(guppy_account6_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_6 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_6 / guppy_token_d * guppy_last_price))
 if guppy_ab_account_number not in guppy_ab_input:
  print('Must Integer Within Range '+guppy_accounts_range+'.')

def guppy_list_all_account_balances():
 guppy_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+guppy_tokenName+' Balance: ')
 print(guppy_account0_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_0 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_0 / guppy_token_d * guppy_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(guppy_account0_n+': Ethereum Balance '+str(guppy_w_call_0 / _e_d)+' $'+str(guppy_w_call_0 / _e_d * guppy_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+guppy_tokenName+' Balance: ')
 print(guppy_account1_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_1 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_1 / guppy_token_d * guppy_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(guppy_account1_n+': Ethereum Balance '+str(guppy_w_call_1 / _e_d)+' $'+str(guppy_w_call_1 / _e_d * guppy_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+guppy_tokenName+' Balance: ')
 print(guppy_account2_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_2 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_2 / guppy_token_d * guppy_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(guppy_account2_n+': Ethereum Balance '+str(guppy_w_call_2 / _e_d)+' $'+str(guppy_w_call_2 / _e_d * guppy_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+guppy_tokenName+' Balance: ')
 print(guppy_account3_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_3 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_3 / guppy_token_d * guppy_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(guppy_account3_n+': Ethereum Balance '+str(guppy_w_call_3 / _e_d)+' $'+str(guppy_w_call_3 / _e_d * guppy_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+guppy_tokenName+' Balance: ')
 print(guppy_account4_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_4 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_4 / guppy_token_d * guppy_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(guppy_account4_n+': Ethereum Balance '+str(guppy_w_call_4 / _e_d)+' $'+str(guppy_w_call_4 / _e_d * guppy_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+guppy_tokenName+' Balance: ')
 print(guppy_account5_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_5 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_5 / guppy_token_d * guppy_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(guppy_account5_n+': Ethereum Balance '+str(guppy_w_call_5 / _e_d)+' $'+str(guppy_w_call_5 /_e_d * guppy_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+guppy_tokenName+' Balance: ')
 print(guppy_account6_n+': '+guppy_tokenName+' Balance: '+str(guppy_call_6 / guppy_token_d)+' Usd/'+guppy_tokenName+' Balance: $'+str(guppy_call_6 / guppy_token_d * guppy_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(guppy_account6_n+': Ethereum Balance '+str(guppy_w_call_6 / _e_d)+' $'+str(guppy_w_call_6 / _e_d * guppy_last_ethereum_price))
def guppy_unlock_all_accounts():
  guppy_unlock_account_0()
  guppy_unlock_account_1()
  guppy_unlock_account_2()
  guppy_unlock_account_3()
  guppy_unlock_account_4()
  guppy_unlock_account_5()
  guppy_unlock_account_6()


def guppy_unlock_account_0():
  global guppy_account0pw
  global guppy_account0
  global guppy_account0_n
  guppy_update_accounts()
  guppy_u_a_0 = guppy_w_unlock(guppy_account0, guppy_account0pw, guppy_unlockTime)
  if guppy_u_a_0 == False:
    if guppy_account0pw == '':
     guppy_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account0_n+' Passphrase Denied: '+guppy_account0pw_r)
    elif guppy_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+guppy_account0_n+' Passphrase Denied: '+guppy_account0pw)
  if guppy_u_a_0 == True:
   print(guppy_account0_n+' Unlocked')

def guppy_unlock_account_1():
  global guppy_account1pw
  global guppy_account1
  global guppy_account1_n
  guppy_update_accounts()
  guppy_u_a_1 = guppy_unlock(guppy_account1, guppy_account1pw, guppy_unlockTime)
  if guppy_u_a_1 == False:
    if guppy_account1pw == '':
     guppy_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account1_n+' Passphrase Denied: '+guppy_account1pw_r)
    elif guppy_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+guppy_account1_n+' Passphrase Denied: '+guppy_account1pw)
  if guppy_u_a_1 == True:
   print(guppy_account1_n+' Unlocked')

def guppy_unlock_account_2():
  global guppy_account2pw
  global guppy_account2
  global guppy_account2_n
  guppy_update_accounts()
  guppy_u_a_2 = guppy_unlock(guppy_account2, guppy_account2pw, guppy_unlockTime)
  if guppy_u_a_2 == False:
    if guppy_account2pw == '':
     guppy_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account2_n+' Passphrase Denied: '+guppy_account2pw_r)
    elif guppy_account2pw != '':
     print('Unlock Failure With Account '+guppy_account2_n+' Passphrase Denied: '+guppy_account2pw)
  if guppy_u_a_2 == True:
   print(guppy_account2_n+' Unlocked')

def guppy_unlock_account_3():
  global guppy_account3pw
  global guppy_account3
  global guppy_account3_n
  guppy_update_accounts()
  guppy_u_a_3 = guppy_unlock(guppy_account3, guppy_account3pw, guppy_unlockTime)
  if guppy_u_a_3 == False:
    if guppy_account3pw == '':
     guppy_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account3_n+' Passphrase Denied: '+guppy_account3pw_r)
    elif guppy_account3pw != '':
     print('Unlock Failure With Account '+guppy_account3_n+' Passphrase Denied: '+guppy_account3pw)
  if guppy_u_a_3 == True:
   print(guppy_account3_n+' Unlocked')

def guppy_unlock_account_4():
  global guppy_account4pw
  global guppy_account4
  global guppy_account4_n
  guppy_update_accounts()
  guppy_u_a_4 = guppy_unlock(guppy_account4, guppy_account4pw, guppy_unlockTime)
  if guppy_u_a_4 == False:
    if guppy_account4pw == '':
     guppy_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account4_n+' Passphrase Denied: '+guppy_account4pw_r)
    elif guppy_account4pw != '':
     print('Unlock Failure With Account '+guppy_account4_n+' Passphrase Denied: '+guppy_account4pw)
  if guppy_u_a_4 == True:
   print(guppy_account4_n+' Unlocked')

def guppy_unlock_account_5():
  global guppy_account5pw
  global guppy_account5
  global guppy_account5_n
  guppy_update_accounts()
  guppy_u_a_5 = guppy_unlock(guppy_account5, guppy_account5pw, guppy_unlockTime)
  if guppy_u_a_5 == False:
    if guppy_account5pw == '':
     guppy_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account5_n+' Passphrase Denied: '+guppy_account5pw_r)
    elif guppy_account5pw != '':
     print('Unlock Failure With Account '+guppy_account5_n+' Passphrase Denied: '+guppy_account5pw)
  if guppy_u_a_5 == True:
   print(guppy_account5_n+' Unlocked')

def guppy_unlock_account_6():
  global guppy_account6pw
  global guppy_account6
  global guppy_account6_n
  guppy_update_accounts()
  guppy_u_a_6 = guppy_unlock(guppy_account6, guppy_account6pw, guppy_unlockTime)
  if guppy_u_a_6 == False:
    if guppy_account6pw == '':
     guppy_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+guppy_account6_n+' Passphrase Denied: '+guppy_account6pw_r)
    elif guppy_account6pw != '':
     print('Unlock Failure With Account '+guppy_account6_n+' Passphrase Denied: '+guppy_account6pw)
  if guppy_u_a_6 == True:
   print(guppy_account6_n+' Unlocked')

def guppy_unlock_account(guppy_ua_accountNumber):
 guppy_update_accounts()
 guppy_ua_account_number = guppy_ua_accountNumber
 guppy_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if guppy_ua_account_number == guppy_ua_input[0]:
  guppy_unlock_account_0()
 if guppy_ua_account_number == guppy_ua_input[1]:
  guppy_unlock_account_1()
 if guppy_ua_account_number == guppy_ua_input[2]:
  guppy_unlock_account_2()
 if guppy_ua_account_number == guppy_ua_input[3]:
  guppy_unlock_account_3()
 if guppy_ua_account_number == guppy_ua_input[4]:
  guppy_unlock_account_4()
 if guppy_ua_account_number == guppy_ua_input[5]:
  guppy_unlock_account_5()
 if guppy_ua_account_number == guppy_ua_input[6]:
  guppy_unlock_account_6()
 if guppy_ua_account_number not in guppy_ua_input:
  print('Must Integer Within Range '+guppy_accounts_range+'.')
 

def guppy_approve_between_accounts(fromAccount, toAccount, msgValue):
  guppy_update_accounts()
  guppy_a_0 = guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(guppy_a_0)

def guppy_approve(fromAccountNumber, toAddress, msgValue):
  guppy_update_accounts()
  guppy_unlock_account(fromAccountNumber)
  guppy_a_1 = guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(guppy_a_1)

def guppy_transfer_between_accounts(fromAccount, toAccount, msgValue):
  guppy_update_accounts()
  guppy_unlock_account(fromAccount)
  guppy_t_0 = guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(guppy_t_0)

def guppy_transfer(fromAccountNumber, toAddress, msgValue):
  guppy_update_accounts()
  guppy_unlock_account(fromAccountNumber)
  guppy_t_1 = guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(guppy_t_1)

def guppy_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  guppy_update_accounts()
  guppy_unlock_account(callAccount)
  guppy_tf_0 = guppy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(guppy_tf_0)

def guppy_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  guppy_update_accounts()
  guppy_unlock_account(callAccount)
  guppy_tf_1 = guppy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(guppy_tf_1)
  


def guppy_help():
  print('Following Functions For '+guppy_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * guppy_unlock => web3.personal.unlockAccount
/ * guppy_accounts => web3.personal.listAccounts
/ * guppy_balance = web3.eth.getBalance
** guppy => web3.eth.contract(abi=guppy_abi, address=guppy_address)
** / * guppy_balanceOf => guppy.call().balanceOf

~ Function Listing Below:
~ guppy_update_accounts()
~ guppy_update_balances() \n\r -- => guppy_update_accounts()
~ guppy_list_all_accounts() \n\r -- => guppy_update_accounts()
~ guppy_account_balance(accountNumber) \n\r -- => guppy_update_balances() 
~ guppy_list_all_account_balances() \n\r -- => guppy_update_balances()
~ guppy_unlock_all_accounts() \n\r -- => guppy_unlock_account_0() \n\r -- => guppy_unlock_account_1() \n\r -- => guppy_unlock_account_2() \n\r -- => guppy_unlock_account_3() \n\r -- => guppy_unlock_account_4() \n\r -- => guppy_unlock_account_5() \n\r -- => guppy_unlock_account_6() 
~ guppy_unlock_account_0() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account0, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_1() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account1, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_2() \n\r -- => guppy_update_accounts() \n\r --/ *guppy_w_unlock(guppy_account2, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_3() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account3, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_4() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account4, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_5() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account5, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account_6() \n\r -- => guppy_update_accounts() \n\r -- / *guppy_w_unlock(guppy_account6, guppy_account0pw, guppy_unlockTime)
~ guppy_unlock_account(guppy_ua_accountNumber) \n\r -- => guppy_update_accounts() \n\r -- // guppy_unlock_account_0() \n\r -- // guppy_unlock_account_1() \n\r -- // guppy_unlock_account_2() \n\r -- // guppy_unlock_account_3() \n\r -- // guppy_unlock_account_4() \n\r -- // guppy_unlock_account_5() \n\r -- // guppy_unlock_account_6()
~ guppy_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(fromAccount) \n\r -- / ** guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ guppy_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(fromAccountNumber) \n\r -- / ** guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ guppy_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(fromAccount) \n\r -- / ** guppy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ guppy_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(fromAccountNumber) \n\r -- / ** guppy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ guppy_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(callAccount) \n\r / ** guppy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ guppy_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => guppy_update_accounts() \n\r -- => guppy_unlock_account(callAccount) \n\r -- / ** guppy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ guppy_help() <-- You Are Here. ''')