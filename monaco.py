#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global mco_account_0_a
global mco_account_1_a
global mco_account_2_a
global mco_account_3_a
global mco_account_4_a
global mco_account_5_a
global mco_account_6_a
global mco_address
global mco_abi
global mco
global mco_call_0
global mco_call_1
global mco_call_2
global mco_call_3
global mco_call_4
global mco_call_5
global mco_call_6
global mco_call_ab
global mco_accounts
global mco_account_0_pw
global mco_account_1_pw
global mco_account_2_pw
global mco_account_3_pw
global mco_account_4_pw
global mco_account_5_pw
global mco_account_6_pw
global mco_account_0_n
global mco_account_1_n
global mco_account_2_n
global mco_account_3_n
global mco_account_4_n
global mco_account_5_n
global mco_account_6_n
global mco_account1pw
global mco_account2pw
global mco_account3pw
global mco_account4pw
global mco_account5pw
global mco_account6pw
global mco_last_price
global mco_accounts_range
global mco_tokenName
global mco_last_ethereum_price
global mco_unlockTime
global mco_balance
global mco_balanceOf
global mco_unlock
global mco_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
mco_token_d = 1e8
_e_d = 1e18
mco_accounts_range = '[0, 6]'
mco_unlock = web3.personal.unlockAccount
mco_last_ethereum_price = 370.00
mco_last_price = 13.95
mco_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
mco_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
mco_tokenName = 'Monaco Token'
mco_unlockTime = hex(10000) # Must be hex()
mco_account_0_a = mco_accounts[0]
mco_account_1_a = mco_accounts[1]
mco_account_2_a = mco_accounts[2]
mco_account_3_a = mco_accounts[3]
mco_account_4_a = mco_accounts[4]
mco_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
mco_account_6_a = mco_accounts[6]
# Supply Unlock Passwords For Transactions Below
mco_account_0_pw = 'GuildSkrypt2017!@#'
mco_account_1_pw = ''
mco_account_2_pw = 'GuildSkrypt2017!@#'
mco_account_3_pw = ''
mco_account_4_pw = ''
mco_account_5_pw = ''
mco_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
mco_account_0_n = 'Skotys Bittrex Account'
mco_account_1_n = 'Jeffs Account'
mco_account_2_n = 'Skrypts Bittrex Account'
mco_account_3_n = 'Skotys Personal Account'
mco_account_4_n = 'Unknown'
mco_account_5_n = 'Watched \'Bittrex\' Account.'
mco_account_6_n = 'Watched Account (1)'
# Contract Information Below :
mco_address = '0xB63B606Ac810a52cCa15e44bB630fd42D8d1d83d'
mco_abi = [{"constant":true,"inputs":[],"name":"mcoFundDeposit","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"mcoFund","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenExchangeRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationCap","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isFinalized","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingEndBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ethFundDeposit","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"createTokens","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationMin","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingStartBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"_ethFundDeposit","type":"address"},{"name":"_mcoFundDeposit","type":"address"},{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingEndBlock","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"LogRefund","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Createmco","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
mco = web3.eth.contract(abi=mco_abi, address=mco_address)
mco_balanceOf = mco.call().balanceOf
# End Contract Information
def mco_update_accounts():
 global mco_account0
 global mco_account1
 global mco_account2
 global mco_account3
 global mco_account4
 global mco_account5
 global mco_account6
 global mco_account0_n
 global mco_account1_n
 global mco_account2_n
 global mco_account3_n
 global mco_account4_n
 global mco_account5_n
 global mco_account6_n
 global mco_account0pw
 global mco_account1pw
 global mco_account2pw
 global mco_account3pw
 global mco_account4pw
 global mco_account5pw
 global mco_account6pw
 mco_account0 = mco_account_0_a
 mco_account1 = mco_account_1_a
 mco_account2 = mco_account_2_a
 mco_account3 = mco_account_3_a
 mco_account4 = mco_account_4_a
 mco_account5 = mco_account_5_a
 mco_account6 = mco_account_6_a
 mco_account0_n = mco_account_0_n
 mco_account1_n = mco_account_1_n
 mco_account2_n = mco_account_2_n
 mco_account3_n = mco_account_3_n
 mco_account4_n = mco_account_4_n
 mco_account5_n = mco_account_5_n
 mco_account6_n = mco_account_6_n
 mco_account0pw = mco_account_0_pw
 mco_account1pw = mco_account_1_pw
 mco_account2pw = mco_account_2_pw
 mco_account3pw = mco_account_3_pw
 mco_account4pw = mco_account_4_pw
 mco_account5pw = mco_account_5_pw
 mco_account6pw = mco_account_6_pw
 print(mco_tokenName+' Accounts Updated.')
def mco_update_balances():
 global mco_call_0
 global mco_call_1
 global mco_call_2
 global mco_call_3
 global mco_call_4
 global mco_call_5
 global mco_call_6
 global mco_w_call_0
 global mco_w_call_1
 global mco_w_call_2
 global mco_w_call_3
 global mco_w_call_4
 global mco_w_call_5
 global mco_w_call_6
 mco_update_accounts()
 print('Updating '+mco_tokenName+' Balances Please Wait...')
 mco_call_0 = mco_balanceOf(mco_account0)
 mco_call_1 = mco_balanceOf(mco_account1)
 mco_call_2 = mco_balanceOf(mco_account2)
 mco_call_3 = mco_balanceOf(mco_account3)
 mco_call_4 = mco_balanceOf(mco_account4)
 mco_call_5 = mco_balanceOf(mco_account5)
 mco_call_6 = mco_balanceOf(mco_account6)
 mco_w_call_0 = mco_balance(mco_account0)
 mco_w_call_1 = mco_balance(mco_account1)
 mco_w_call_2 = mco_balance(mco_account2)
 mco_w_call_3 = mco_balance(mco_account3)
 mco_w_call_4 = mco_balance(mco_account4)
 mco_w_call_5 = mco_balance(mco_account5)
 mco_w_call_6 = mco_balance(mco_account6)
 print(mco_tokenName+' Balances Updated.')
def mco_list_all_accounts():
 mco_update_accounts()
 print(mco_tokenName+' '+mco_account0_n+': '+mco_account0)
 print(mco_tokenName+' '+mco_account1_n+': '+mco_account1)
 print(mco_tokenName+' '+mco_account2_n+': '+mco_account2)
 print(mco_tokenName+' '+mco_account3_n+': '+mco_account3)
 print(mco_tokenName+' '+mco_account4_n+': '+mco_account4)
 print(mco_tokenName+' '+mco_account5_n+': '+mco_account5)
 print(mco_tokenName+' '+mco_account6_n+': '+mco_account6)

def mco_account_balance(accountNumber):
 mco_update_balances()
 mco_ab_account_number = accountNumber
 mco_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if mco_ab_account_number == mco_ab_input[0]:
  print('Calling '+mco_account0_n+' '+mco_tokenName+' Balance: ')
  print(mco_account0_n+': '+mco_tokenName+' Balance: '+str(mco_call_0 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_0 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[1]:
  print('Calling '+mco_account1_n+' '+mco_tokenName+' Balance: ')
  print(mco_account1_n+': '+mco_tokenName+' Balance: '+str(mco_call_1 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_1 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[2]:
  print('Calling '+mco_account2_n+' '+mco_tokenName+' Balance: ')
  print(mco_account2_n+': '+mco_tokenName+' Balance: '+str(mco_call_2 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_2 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[3]:
  print('Calling '+mco_account3_n+' '+mco_tokenName+' Balance: ')
  print(mco_account3_n+': '+mco_tokenName+' Balance: '+str(mco_call_3 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_3 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[4]:
  print('Calling '+mco_account4_n+' '+mco_tokenName+' Balance: ')
  print(mco_account4_n+': '+mco_tokenName+' Balance: '+str(mco_call_4 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_4 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[5]:
  print('Calling '+mco_account5_n+' '+mco_tokenName+' Balance: ')
  print(mco_account5_n+': '+mco_tokenName+' Balance: '+str(mco_call_5 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_5 / mco_token_d * mco_last_price))
 if mco_ab_account_number == mco_ab_input[6]:
  print('Calling '+mco_account6_n+' '+mco_tokenName+' Balance: ')
  print(mco_account6_n+': '+mco_tokenName+' Balance: '+str(mco_call_6 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_6 / mco_token_d * mco_last_price))
 if mco_ab_account_number not in mco_ab_input:
  print('Must Integer Within Range '+mco_accounts_range+'.')

def mco_list_all_account_balances():
 mco_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+mco_tokenName+' Balance: ')
 print(mco_account0_n+': '+mco_tokenName+' Balance: '+str(mco_call_0 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_0 / mco_token_d * mco_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(mco_account0_n+': Ethereum Balance '+str(mco_w_call_0 / _e_d)+' $'+str(mco_w_call_0 / _e_d * mco_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+mco_tokenName+' Balance: ')
 print(mco_account1_n+': '+mco_tokenName+' Balance: '+str(mco_call_1 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_1 / mco_token_d * mco_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(mco_account1_n+': Ethereum Balance '+str(mco_w_call_1 / _e_d)+' $'+str(mco_w_call_1 / _e_d * mco_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+mco_tokenName+' Balance: ')
 print(mco_account2_n+': '+mco_tokenName+' Balance: '+str(mco_call_2 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_2 / mco_token_d * mco_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(mco_account2_n+': Ethereum Balance '+str(mco_w_call_2 / _e_d)+' $'+str(mco_w_call_2 / _e_d * mco_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+mco_tokenName+' Balance: ')
 print(mco_account3_n+': '+mco_tokenName+' Balance: '+str(mco_call_3 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_3 / mco_token_d * mco_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(mco_account3_n+': Ethereum Balance '+str(mco_w_call_3 / _e_d)+' $'+str(mco_w_call_3 / _e_d * mco_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+mco_tokenName+' Balance: ')
 print(mco_account4_n+': '+mco_tokenName+' Balance: '+str(mco_call_4 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_4 / mco_token_d * mco_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(mco_account4_n+': Ethereum Balance '+str(mco_w_call_4 / _e_d)+' $'+str(mco_w_call_4 / _e_d * mco_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+mco_tokenName+' Balance: ')
 print(mco_account5_n+': '+mco_tokenName+' Balance: '+str(mco_call_5 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_5 / mco_token_d * mco_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(mco_account5_n+': Ethereum Balance '+str(mco_w_call_5 / _e_d)+' $'+str(mco_w_call_5 /_e_d * mco_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+mco_tokenName+' Balance: ')
 print(mco_account6_n+': '+mco_tokenName+' Balance: '+str(mco_call_6 / mco_token_d)+' Usd/'+mco_tokenName+' Balance: $'+str(mco_call_6 / mco_token_d * mco_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(mco_account6_n+': Ethereum Balance '+str(mco_w_call_6 / _e_d)+' $'+str(mco_w_call_6 / _e_d * mco_last_ethereum_price))
def mco_unlock_all_accounts():
  mco_unlock_account_0()
  mco_unlock_account_1()
  mco_unlock_account_2()
  mco_unlock_account_3()
  mco_unlock_account_4()
  mco_unlock_account_5()
  mco_unlock_account_6()


def mco_unlock_account_0():
  global mco_account0pw
  global mco_account0
  global mco_account0_n
  mco_update_accounts()
  mco_u_a_0 = mco_w_unlock(mco_account0, mco_account0pw, mco_unlockTime)
  if mco_u_a_0 == False:
    if mco_account0pw == '':
     mco_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account0_n+' Passphrase Denied: '+mco_account0pw_r)
    elif mco_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mco_account0_n+' Passphrase Denied: '+mco_account0pw)
  if mco_u_a_0 == True:
   print(mco_account0_n+' Unlocked')

def mco_unlock_account_1():
  global mco_account1pw
  global mco_account1
  global mco_account1_n
  mco_update_accounts()
  mco_u_a_1 = mco_unlock(mco_account1, mco_account1pw, mco_unlockTime)
  if mco_u_a_1 == False:
    if mco_account1pw == '':
     mco_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account1_n+' Passphrase Denied: '+mco_account1pw_r)
    elif mco_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mco_account1_n+' Passphrase Denied: '+mco_account1pw)
  if mco_u_a_1 == True:
   print(mco_account1_n+' Unlocked')

def mco_unlock_account_2():
  global mco_account2pw
  global mco_account2
  global mco_account2_n
  mco_update_accounts()
  mco_u_a_2 = mco_unlock(mco_account2, mco_account2pw, mco_unlockTime)
  if mco_u_a_2 == False:
    if mco_account2pw == '':
     mco_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account2_n+' Passphrase Denied: '+mco_account2pw_r)
    elif mco_account2pw != '':
     print('Unlock Failure With Account '+mco_account2_n+' Passphrase Denied: '+mco_account2pw)
  if mco_u_a_2 == True:
   print(mco_account2_n+' Unlocked')

def mco_unlock_account_3():
  global mco_account3pw
  global mco_account3
  global mco_account3_n
  mco_update_accounts()
  mco_u_a_3 = mco_unlock(mco_account3, mco_account3pw, mco_unlockTime)
  if mco_u_a_3 == False:
    if mco_account3pw == '':
     mco_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account3_n+' Passphrase Denied: '+mco_account3pw_r)
    elif mco_account3pw != '':
     print('Unlock Failure With Account '+mco_account3_n+' Passphrase Denied: '+mco_account3pw)
  if mco_u_a_3 == True:
   print(mco_account3_n+' Unlocked')

def mco_unlock_account_4():
  global mco_account4pw
  global mco_account4
  global mco_account4_n
  mco_update_accounts()
  mco_u_a_4 = mco_unlock(mco_account4, mco_account4pw, mco_unlockTime)
  if mco_u_a_4 == False:
    if mco_account4pw == '':
     mco_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account4_n+' Passphrase Denied: '+mco_account4pw_r)
    elif mco_account4pw != '':
     print('Unlock Failure With Account '+mco_account4_n+' Passphrase Denied: '+mco_account4pw)
  if mco_u_a_4 == True:
   print(mco_account4_n+' Unlocked')

def mco_unlock_account_5():
  global mco_account5pw
  global mco_account5
  global mco_account5_n
  mco_update_accounts()
  mco_u_a_5 = mco_unlock(mco_account5, mco_account5pw, mco_unlockTime)
  if mco_u_a_5 == False:
    if mco_account5pw == '':
     mco_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account5_n+' Passphrase Denied: '+mco_account5pw_r)
    elif mco_account5pw != '':
     print('Unlock Failure With Account '+mco_account5_n+' Passphrase Denied: '+mco_account5pw)
  if mco_u_a_5 == True:
   print(mco_account5_n+' Unlocked')

def mco_unlock_account_6():
  global mco_account6pw
  global mco_account6
  global mco_account6_n
  mco_update_accounts()
  mco_u_a_6 = mco_unlock(mco_account6, mco_account6pw, mco_unlockTime)
  if mco_u_a_6 == False:
    if mco_account6pw == '':
     mco_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mco_account6_n+' Passphrase Denied: '+mco_account6pw_r)
    elif mco_account6pw != '':
     print('Unlock Failure With Account '+mco_account6_n+' Passphrase Denied: '+mco_account6pw)
  if mco_u_a_6 == True:
   print(mco_account6_n+' Unlocked')

def mco_unlock_account(mco_ua_accountNumber):
 mco_update_accounts()
 mco_ua_account_number = mco_ua_accountNumber
 mco_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if mco_ua_account_number == mco_ua_input[0]:
  mco_unlock_account_0()
 if mco_ua_account_number == mco_ua_input[1]:
  mco_unlock_account_1()
 if mco_ua_account_number == mco_ua_input[2]:
  mco_unlock_account_2()
 if mco_ua_account_number == mco_ua_input[3]:
  mco_unlock_account_3()
 if mco_ua_account_number == mco_ua_input[4]:
  mco_unlock_account_4()
 if mco_ua_account_number == mco_ua_input[5]:
  mco_unlock_account_5()
 if mco_ua_account_number == mco_ua_input[6]:
  mco_unlock_account_6()
 if mco_ua_account_number not in mco_ua_input:
  print('Must Integer Within Range '+mco_accounts_range+'.')
 

def mco_approve_between_accounts(fromAccount, toAccount, msgValue):
  mco_update_accounts()
  mco_a_0 = mco.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(mco_a_0)

def mco_approve(fromAccountNumber, toAddress, msgValue):
  mco_update_accounts()
  mco_unlock_account(fromAccountNumber)
  mco_a_1 = mco.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(mco_a_1)

def mco_transfer_between_accounts(fromAccount, toAccount, msgValue):
  mco_update_accounts()
  mco_unlock_account(fromAccount)
  mco_t_0 = mco.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(mco_t_0)

def mco_transfer(fromAccountNumber, toAddress, msgValue):
  mco_update_accounts()
  mco_unlock_account(fromAccountNumber)
  mco_t_1 = mco.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(mco_t_1)

def mco_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  mco_update_accounts()
  mco_unlock_account(callAccount)
  mco_tf_0 = mco.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(mco_tf_0)

def mco_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  mco_update_accounts()
  mco_unlock_account(callAccount)
  mco_tf_1 = mco.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(mco_tf_1)
  


def mco_help():
  print('Following Functions For '+mco_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * mco_unlock => web3.personal.unlockAccount
/ * mco_accounts => web3.personal.listAccounts
/ * mco_balance = web3.eth.getBalance
** mco => web3.eth.contract(abi=mco_abi, address=mco_address)
** / * mco_balanceOf => mco.call().balanceOf

~ Function Listing Below:
~ mco_update_accounts()
~ mco_update_balances() \n\r -- => mco_update_accounts()
~ mco_list_all_accounts() \n\r -- => mco_update_accounts()
~ mco_account_balance(accountNumber) \n\r -- => mco_update_balances() 
~ mco_list_all_account_balances() \n\r -- => mco_update_balances()
~ mco_unlock_all_accounts() \n\r -- => mco_unlock_account_0() \n\r -- => mco_unlock_account_1() \n\r -- => mco_unlock_account_2() \n\r -- => mco_unlock_account_3() \n\r -- => mco_unlock_account_4() \n\r -- => mco_unlock_account_5() \n\r -- => mco_unlock_account_6() 
~ mco_unlock_account_0() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account0, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_1() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account1, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_2() \n\r -- => mco_update_accounts() \n\r --/ *mco_w_unlock(mco_account2, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_3() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account3, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_4() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account4, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_5() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account5, mco_account0pw, mco_unlockTime)
~ mco_unlock_account_6() \n\r -- => mco_update_accounts() \n\r -- / *mco_w_unlock(mco_account6, mco_account0pw, mco_unlockTime)
~ mco_unlock_account(mco_ua_accountNumber) \n\r -- => mco_update_accounts() \n\r -- // mco_unlock_account_0() \n\r -- // mco_unlock_account_1() \n\r -- // mco_unlock_account_2() \n\r -- // mco_unlock_account_3() \n\r -- // mco_unlock_account_4() \n\r -- // mco_unlock_account_5() \n\r -- // mco_unlock_account_6()
~ mco_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(fromAccount) \n\r -- / ** mco.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mco_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(fromAccountNumber) \n\r -- / ** mco.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mco_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(fromAccount) \n\r -- / ** mco.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ mco_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(fromAccountNumber) \n\r -- / ** mco.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mco_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(callAccount) \n\r / ** mco.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mco_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mco_update_accounts() \n\r -- => mco_unlock_account(callAccount) \n\r -- / ** mco.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ mco_help() <-- You Are Here. ''')