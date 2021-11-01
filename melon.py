#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global mln_account_0_a
global mln_account_1_a
global mln_account_2_a
global mln_account_3_a
global mln_account_4_a
global mln_account_5_a
global mln_account_6_a
global mln_address
global mln_abi
global mln
global mln_call_0
global mln_call_1
global mln_call_2
global mln_call_3
global mln_call_4
global mln_call_5
global mln_call_6
global mln_call_ab
global mln_accounts
global mln_account_0_pw
global mln_account_1_pw
global mln_account_2_pw
global mln_account_3_pw
global mln_account_4_pw
global mln_account_5_pw
global mln_account_6_pw
global mln_account_0_n
global mln_account_1_n
global mln_account_2_n
global mln_account_3_n
global mln_account_4_n
global mln_account_5_n
global mln_account_6_n
global mln_account1pw
global mln_account2pw
global mln_account3pw
global mln_account4pw
global mln_account5pw
global mln_account6pw
global mln_last_price
global mln_accounts_range
global mln_tokenName
global mln_last_ethereum_price
global mln_unlockTime
global mln_balance
global mln_balanceOf
global mln_unlock
global mln_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
mln_token_d = 1e18
_e_d = 1e18
mln_accounts_range = '[0, 6]'
mln_unlock = web3.personal.unlockAccount
mln_last_ethereum_price = 370.00
mln_last_price = 81.61
mln_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
mln_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
mln_tokenName = 'Melon Token'
mln_unlockTime = hex(10000) # Must be hex()
mln_account_0_a = mln_accounts[0]
mln_account_1_a = mln_accounts[1]
mln_account_2_a = mln_accounts[2]
mln_account_3_a = mln_accounts[3]
mln_account_4_a = mln_accounts[4]
mln_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
mln_account_6_a = mln_accounts[6]
# Supply Unlock Passwords For Transactions Below
mln_account_0_pw = 'GuildSkrypt2017!@#'
mln_account_1_pw = ''
mln_account_2_pw = 'GuildSkrypt2017!@#'
mln_account_3_pw = ''
mln_account_4_pw = ''
mln_account_5_pw = ''
mln_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
mln_account_0_n = 'Skotys Bittrex Account'
mln_account_1_n = 'Jeffs Account'
mln_account_2_n = 'Skrypts Bittrex Account'
mln_account_3_n = 'Skotys Personal Account'
mln_account_4_n = 'Unknown'
mln_account_5_n = 'Watched \'Bittrex\' Account.'
mln_account_6_n = 'Watched Account (1)'
# Contract Information Below :
mln_address = '0xBEB9eF514a379B997e0798FDcC901Ee474B6D9A1'
mln_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minter","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newAddress","type":"address"}],"name":"changeMelonportAddress","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"sender","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"endTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"MAX_TOTAL_TOKEN_AMOUNT_OFFERED_TO_PUBLIC","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newAddress","type":"address"}],"name":"changeMintingAddress","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"lockedBalanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"startTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"mintIcedToken","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"mintLiquidToken","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"MAX_TOTAL_TOKEN_AMOUNT","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"}],"name":"unlockBalance","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"melonport","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"THAWING_DURATION","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"setMinter","type":"address"},{"name":"setMelonport","type":"address"},{"name":"setStartTime","type":"uint256"},{"name":"setEndTime","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
mln = web3.eth.contract(abi=mln_abi, address=mln_address)
mln_balanceOf = mln.call().balanceOf
# End Contract Information
def mln_update_accounts():
 global mln_account0
 global mln_account1
 global mln_account2
 global mln_account3
 global mln_account4
 global mln_account5
 global mln_account6
 global mln_account0_n
 global mln_account1_n
 global mln_account2_n
 global mln_account3_n
 global mln_account4_n
 global mln_account5_n
 global mln_account6_n
 global mln_account0pw
 global mln_account1pw
 global mln_account2pw
 global mln_account3pw
 global mln_account4pw
 global mln_account5pw
 global mln_account6pw
 mln_account0 = mln_account_0_a
 mln_account1 = mln_account_1_a
 mln_account2 = mln_account_2_a
 mln_account3 = mln_account_3_a
 mln_account4 = mln_account_4_a
 mln_account5 = mln_account_5_a
 mln_account6 = mln_account_6_a
 mln_account0_n = mln_account_0_n
 mln_account1_n = mln_account_1_n
 mln_account2_n = mln_account_2_n
 mln_account3_n = mln_account_3_n
 mln_account4_n = mln_account_4_n
 mln_account5_n = mln_account_5_n
 mln_account6_n = mln_account_6_n
 mln_account0pw = mln_account_0_pw
 mln_account1pw = mln_account_1_pw
 mln_account2pw = mln_account_2_pw
 mln_account3pw = mln_account_3_pw
 mln_account4pw = mln_account_4_pw
 mln_account5pw = mln_account_5_pw
 mln_account6pw = mln_account_6_pw
 print(mln_tokenName+' Accounts Updated.')
def mln_update_balances():
 global mln_call_0
 global mln_call_1
 global mln_call_2
 global mln_call_3
 global mln_call_4
 global mln_call_5
 global mln_call_6
 global mln_w_call_0
 global mln_w_call_1
 global mln_w_call_2
 global mln_w_call_3
 global mln_w_call_4
 global mln_w_call_5
 global mln_w_call_6
 mln_update_accounts()
 print('Updating '+mln_tokenName+' Balances Please Wait...')
 mln_call_0 = mln_balanceOf(mln_account0)
 mln_call_1 = mln_balanceOf(mln_account1)
 mln_call_2 = mln_balanceOf(mln_account2)
 mln_call_3 = mln_balanceOf(mln_account3)
 mln_call_4 = mln_balanceOf(mln_account4)
 mln_call_5 = mln_balanceOf(mln_account5)
 mln_call_6 = mln_balanceOf(mln_account6)
 mln_w_call_0 = mln_balance(mln_account0)
 mln_w_call_1 = mln_balance(mln_account1)
 mln_w_call_2 = mln_balance(mln_account2)
 mln_w_call_3 = mln_balance(mln_account3)
 mln_w_call_4 = mln_balance(mln_account4)
 mln_w_call_5 = mln_balance(mln_account5)
 mln_w_call_6 = mln_balance(mln_account6)
 print(mln_tokenName+' Balances Updated.')
def mln_list_all_accounts():
 mln_update_accounts()
 print(mln_tokenName+' '+mln_account0_n+': '+mln_account0)
 print(mln_tokenName+' '+mln_account1_n+': '+mln_account1)
 print(mln_tokenName+' '+mln_account2_n+': '+mln_account2)
 print(mln_tokenName+' '+mln_account3_n+': '+mln_account3)
 print(mln_tokenName+' '+mln_account4_n+': '+mln_account4)
 print(mln_tokenName+' '+mln_account5_n+': '+mln_account5)
 print(mln_tokenName+' '+mln_account6_n+': '+mln_account6)

def mln_account_balance(accountNumber):
 mln_update_balances()
 mln_ab_account_number = accountNumber
 mln_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if mln_ab_account_number == mln_ab_input[0]:
  print('Calling '+mln_account0_n+' '+mln_tokenName+' Balance: ')
  print(mln_account0_n+': '+mln_tokenName+' Balance: '+str(mln_call_0 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_0 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[1]:
  print('Calling '+mln_account1_n+' '+mln_tokenName+' Balance: ')
  print(mln_account1_n+': '+mln_tokenName+' Balance: '+str(mln_call_1 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_1 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[2]:
  print('Calling '+mln_account2_n+' '+mln_tokenName+' Balance: ')
  print(mln_account2_n+': '+mln_tokenName+' Balance: '+str(mln_call_2 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_2 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[3]:
  print('Calling '+mln_account3_n+' '+mln_tokenName+' Balance: ')
  print(mln_account3_n+': '+mln_tokenName+' Balance: '+str(mln_call_3 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_3 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[4]:
  print('Calling '+mln_account4_n+' '+mln_tokenName+' Balance: ')
  print(mln_account4_n+': '+mln_tokenName+' Balance: '+str(mln_call_4 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_4 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[5]:
  print('Calling '+mln_account5_n+' '+mln_tokenName+' Balance: ')
  print(mln_account5_n+': '+mln_tokenName+' Balance: '+str(mln_call_5 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_5 / mln_token_d * mln_last_price))
 if mln_ab_account_number == mln_ab_input[6]:
  print('Calling '+mln_account6_n+' '+mln_tokenName+' Balance: ')
  print(mln_account6_n+': '+mln_tokenName+' Balance: '+str(mln_call_6 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_6 / mln_token_d * mln_last_price))
 if mln_ab_account_number not in mln_ab_input:
  print('Must Integer Within Range '+mln_accounts_range+'.')

def mln_list_all_account_balances():
 mln_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+mln_tokenName+' Balance: ')
 print(mln_account0_n+': '+mln_tokenName+' Balance: '+str(mln_call_0 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_0 / mln_token_d * mln_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(mln_account0_n+': Ethereum Balance '+str(mln_w_call_0 / _e_d)+' $'+str(mln_w_call_0 / _e_d * mln_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+mln_tokenName+' Balance: ')
 print(mln_account1_n+': '+mln_tokenName+' Balance: '+str(mln_call_1 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_1 / mln_token_d * mln_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(mln_account1_n+': Ethereum Balance '+str(mln_w_call_1 / _e_d)+' $'+str(mln_w_call_1 / _e_d * mln_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+mln_tokenName+' Balance: ')
 print(mln_account2_n+': '+mln_tokenName+' Balance: '+str(mln_call_2 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_2 / mln_token_d * mln_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(mln_account2_n+': Ethereum Balance '+str(mln_w_call_2 / _e_d)+' $'+str(mln_w_call_2 / _e_d * mln_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+mln_tokenName+' Balance: ')
 print(mln_account3_n+': '+mln_tokenName+' Balance: '+str(mln_call_3 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_3 / mln_token_d * mln_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(mln_account3_n+': Ethereum Balance '+str(mln_w_call_3 / _e_d)+' $'+str(mln_w_call_3 / _e_d * mln_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+mln_tokenName+' Balance: ')
 print(mln_account4_n+': '+mln_tokenName+' Balance: '+str(mln_call_4 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_4 / mln_token_d * mln_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(mln_account4_n+': Ethereum Balance '+str(mln_w_call_4 / _e_d)+' $'+str(mln_w_call_4 / _e_d * mln_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+mln_tokenName+' Balance: ')
 print(mln_account5_n+': '+mln_tokenName+' Balance: '+str(mln_call_5 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_5 / mln_token_d * mln_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(mln_account5_n+': Ethereum Balance '+str(mln_w_call_5 / _e_d)+' $'+str(mln_w_call_5 /_e_d * mln_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+mln_tokenName+' Balance: ')
 print(mln_account6_n+': '+mln_tokenName+' Balance: '+str(mln_call_6 / mln_token_d)+' Usd/'+mln_tokenName+' Balance: $'+str(mln_call_6 / mln_token_d * mln_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(mln_account6_n+': Ethereum Balance '+str(mln_w_call_6 / _e_d)+' $'+str(mln_w_call_6 / _e_d * mln_last_ethereum_price))
def mln_unlock_all_accounts():
  mln_unlock_account_0()
  mln_unlock_account_1()
  mln_unlock_account_2()
  mln_unlock_account_3()
  mln_unlock_account_4()
  mln_unlock_account_5()
  mln_unlock_account_6()


def mln_unlock_account_0():
  global mln_account0pw
  global mln_account0
  global mln_account0_n
  mln_update_accounts()
  mln_u_a_0 = mln_w_unlock(mln_account0, mln_account0pw, mln_unlockTime)
  if mln_u_a_0 == False:
    if mln_account0pw == '':
     mln_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account0_n+' Passphrase Denied: '+mln_account0pw_r)
    elif mln_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mln_account0_n+' Passphrase Denied: '+mln_account0pw)
  if mln_u_a_0 == True:
   print(mln_account0_n+' Unlocked')

def mln_unlock_account_1():
  global mln_account1pw
  global mln_account1
  global mln_account1_n
  mln_update_accounts()
  mln_u_a_1 = mln_unlock(mln_account1, mln_account1pw, mln_unlockTime)
  if mln_u_a_1 == False:
    if mln_account1pw == '':
     mln_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account1_n+' Passphrase Denied: '+mln_account1pw_r)
    elif mln_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mln_account1_n+' Passphrase Denied: '+mln_account1pw)
  if mln_u_a_1 == True:
   print(mln_account1_n+' Unlocked')

def mln_unlock_account_2():
  global mln_account2pw
  global mln_account2
  global mln_account2_n
  mln_update_accounts()
  mln_u_a_2 = mln_unlock(mln_account2, mln_account2pw, mln_unlockTime)
  if mln_u_a_2 == False:
    if mln_account2pw == '':
     mln_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account2_n+' Passphrase Denied: '+mln_account2pw_r)
    elif mln_account2pw != '':
     print('Unlock Failure With Account '+mln_account2_n+' Passphrase Denied: '+mln_account2pw)
  if mln_u_a_2 == True:
   print(mln_account2_n+' Unlocked')

def mln_unlock_account_3():
  global mln_account3pw
  global mln_account3
  global mln_account3_n
  mln_update_accounts()
  mln_u_a_3 = mln_unlock(mln_account3, mln_account3pw, mln_unlockTime)
  if mln_u_a_3 == False:
    if mln_account3pw == '':
     mln_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account3_n+' Passphrase Denied: '+mln_account3pw_r)
    elif mln_account3pw != '':
     print('Unlock Failure With Account '+mln_account3_n+' Passphrase Denied: '+mln_account3pw)
  if mln_u_a_3 == True:
   print(mln_account3_n+' Unlocked')

def mln_unlock_account_4():
  global mln_account4pw
  global mln_account4
  global mln_account4_n
  mln_update_accounts()
  mln_u_a_4 = mln_unlock(mln_account4, mln_account4pw, mln_unlockTime)
  if mln_u_a_4 == False:
    if mln_account4pw == '':
     mln_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account4_n+' Passphrase Denied: '+mln_account4pw_r)
    elif mln_account4pw != '':
     print('Unlock Failure With Account '+mln_account4_n+' Passphrase Denied: '+mln_account4pw)
  if mln_u_a_4 == True:
   print(mln_account4_n+' Unlocked')

def mln_unlock_account_5():
  global mln_account5pw
  global mln_account5
  global mln_account5_n
  mln_update_accounts()
  mln_u_a_5 = mln_unlock(mln_account5, mln_account5pw, mln_unlockTime)
  if mln_u_a_5 == False:
    if mln_account5pw == '':
     mln_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account5_n+' Passphrase Denied: '+mln_account5pw_r)
    elif mln_account5pw != '':
     print('Unlock Failure With Account '+mln_account5_n+' Passphrase Denied: '+mln_account5pw)
  if mln_u_a_5 == True:
   print(mln_account5_n+' Unlocked')

def mln_unlock_account_6():
  global mln_account6pw
  global mln_account6
  global mln_account6_n
  mln_update_accounts()
  mln_u_a_6 = mln_unlock(mln_account6, mln_account6pw, mln_unlockTime)
  if mln_u_a_6 == False:
    if mln_account6pw == '':
     mln_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mln_account6_n+' Passphrase Denied: '+mln_account6pw_r)
    elif mln_account6pw != '':
     print('Unlock Failure With Account '+mln_account6_n+' Passphrase Denied: '+mln_account6pw)
  if mln_u_a_6 == True:
   print(mln_account6_n+' Unlocked')

def mln_unlock_account(mln_ua_accountNumber):
 mln_update_accounts()
 mln_ua_account_number = mln_ua_accountNumber
 mln_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if mln_ua_account_number == mln_ua_input[0]:
  mln_unlock_account_0()
 if mln_ua_account_number == mln_ua_input[1]:
  mln_unlock_account_1()
 if mln_ua_account_number == mln_ua_input[2]:
  mln_unlock_account_2()
 if mln_ua_account_number == mln_ua_input[3]:
  mln_unlock_account_3()
 if mln_ua_account_number == mln_ua_input[4]:
  mln_unlock_account_4()
 if mln_ua_account_number == mln_ua_input[5]:
  mln_unlock_account_5()
 if mln_ua_account_number == mln_ua_input[6]:
  mln_unlock_account_6()
 if mln_ua_account_number not in mln_ua_input:
  print('Must Integer Within Range '+mln_accounts_range+'.')
 

def mln_approve_between_accounts(fromAccount, toAccount, msgValue):
  mln_update_accounts()
  mln_a_0 = mln.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(mln_a_0)

def mln_approve(fromAccountNumber, toAddress, msgValue):
  mln_update_accounts()
  mln_unlock_account(fromAccountNumber)
  mln_a_1 = mln.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(mln_a_1)

def mln_transfer_between_accounts(fromAccount, toAccount, msgValue):
  mln_update_accounts()
  mln_unlock_account(fromAccount)
  mln_t_0 = mln.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(mln_t_0)

def mln_transfer(fromAccountNumber, toAddress, msgValue):
  mln_update_accounts()
  mln_unlock_account(fromAccountNumber)
  mln_t_1 = mln.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(mln_t_1)

def mln_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  mln_update_accounts()
  mln_unlock_account(callAccount)
  mln_tf_0 = mln.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(mln_tf_0)

def mln_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  mln_update_accounts()
  mln_unlock_account(callAccount)
  mln_tf_1 = mln.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(mln_tf_1)
  


def mln_help():
  print('Following Functions For '+mln_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * mln_unlock => web3.personal.unlockAccount
/ * mln_accounts => web3.personal.listAccounts
/ * mln_balance = web3.eth.getBalance
** mln => web3.eth.contract(abi=mln_abi, address=mln_address)
** / * mln_balanceOf => mln.call().balanceOf

~ Function Listing Below:
~ mln_update_accounts()
~ mln_update_balances() \n\r -- => mln_update_accounts()
~ mln_list_all_accounts() \n\r -- => mln_update_accounts()
~ mln_account_balance(accountNumber) \n\r -- => mln_update_balances() 
~ mln_list_all_account_balances() \n\r -- => mln_update_balances()
~ mln_unlock_all_accounts() \n\r -- => mln_unlock_account_0() \n\r -- => mln_unlock_account_1() \n\r -- => mln_unlock_account_2() \n\r -- => mln_unlock_account_3() \n\r -- => mln_unlock_account_4() \n\r -- => mln_unlock_account_5() \n\r -- => mln_unlock_account_6() 
~ mln_unlock_account_0() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account0, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_1() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account1, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_2() \n\r -- => mln_update_accounts() \n\r --/ *mln_w_unlock(mln_account2, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_3() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account3, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_4() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account4, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_5() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account5, mln_account0pw, mln_unlockTime)
~ mln_unlock_account_6() \n\r -- => mln_update_accounts() \n\r -- / *mln_w_unlock(mln_account6, mln_account0pw, mln_unlockTime)
~ mln_unlock_account(mln_ua_accountNumber) \n\r -- => mln_update_accounts() \n\r -- // mln_unlock_account_0() \n\r -- // mln_unlock_account_1() \n\r -- // mln_unlock_account_2() \n\r -- // mln_unlock_account_3() \n\r -- // mln_unlock_account_4() \n\r -- // mln_unlock_account_5() \n\r -- // mln_unlock_account_6()
~ mln_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(fromAccount) \n\r -- / ** mln.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mln_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(fromAccountNumber) \n\r -- / ** mln.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mln_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(fromAccount) \n\r -- / ** mln.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ mln_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(fromAccountNumber) \n\r -- / ** mln.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mln_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(callAccount) \n\r / ** mln.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mln_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mln_update_accounts() \n\r -- => mln_unlock_account(callAccount) \n\r -- / ** mln.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ mln_help() <-- You Are Here. ''')