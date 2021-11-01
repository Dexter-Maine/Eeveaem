#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global bnt_account_0_a
global bnt_account_1_a
global bnt_account_2_a
global bnt_account_3_a
global bnt_account_4_a
global bnt_account_5_a
global bnt_account_6_a
global bnt_address
global bnt_abi
global bnt
global bnt_call_0
global bnt_call_1
global bnt_call_2
global bnt_call_3
global bnt_call_4
global bnt_call_5
global bnt_call_6
global bnt_call_ab
global bnt_accounts
global bnt_account_0_pw
global bnt_account_1_pw
global bnt_account_2_pw
global bnt_account_3_pw
global bnt_account_4_pw
global bnt_account_5_pw
global bnt_account_6_pw
global bnt_account_0_n
global bnt_account_1_n
global bnt_account_2_n
global bnt_account_3_n
global bnt_account_4_n
global bnt_account_5_n
global bnt_account_6_n
global bnt_account1pw
global bnt_account2pw
global bnt_account3pw
global bnt_account4pw
global bnt_account5pw
global bnt_account6pw
global bnt_last_price
global bnt_accounts_range
global bnt_tokenName
global bnt_last_ethereum_price
global bnt_unlockTime
global bnt_balance
global bnt_balanceOf
global bnt_unlock
global bnt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
bnt_token_d = 1e2
_e_d = 1e18
bnt_accounts_range = '[0, 6]'
bnt_unlock = web3.personal.unlockAccount
bnt_last_ethereum_price = 370.00
bnt_last_price = 3.18
bnt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
bnt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
bnt_tokenName = 'Bancor Token'
bnt_unlockTime = hex(10000) # Must be hex()
bnt_account_0_a = bnt_accounts[0]
bnt_account_1_a = bnt_accounts[1]
bnt_account_2_a = bnt_accounts[2]
bnt_account_3_a = bnt_accounts[3]
bnt_account_4_a = bnt_accounts[4]
bnt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
bnt_account_6_a = bnt_accounts[6]
# Supply Unlock Passwords For Transactions Below
bnt_account_0_pw = 'GuildSkrypt2017!@#'
bnt_account_1_pw = ''
bnt_account_2_pw = 'GuildSkrypt2017!@#'
bnt_account_3_pw = ''
bnt_account_4_pw = ''
bnt_account_5_pw = ''
bnt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
bnt_account_0_n = 'Skotys Bittrex Account'
bnt_account_1_n = 'Jeffs Account'
bnt_account_2_n = 'Skrypts Bittrex Account'
bnt_account_3_n = 'Skotys Personal Account'
bnt_account_4_n = 'Unknown'
bnt_account_5_n = 'Watched \'Bittrex\' Account.'
bnt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
bnt_address = '0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C'
bnt_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_disable","type":"bool"}],"name":"disableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"withdrawTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroy","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint8"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_token","type":"address"}],"name":"NewSmartToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Issuance","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Destruction","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_prevOwner","type":"address"},{"indexed":false,"name":"_newOwner","type":"address"}],"name":"OwnerUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
bnt = web3.eth.contract(abi=bnt_abi, address=bnt_address)
bnt_balanceOf = bnt.call().balanceOf
# End Contract Information
def bnt_update_accounts():
 global bnt_account0
 global bnt_account1
 global bnt_account2
 global bnt_account3
 global bnt_account4
 global bnt_account5
 global bnt_account6
 global bnt_account0_n
 global bnt_account1_n
 global bnt_account2_n
 global bnt_account3_n
 global bnt_account4_n
 global bnt_account5_n
 global bnt_account6_n
 global bnt_account0pw
 global bnt_account1pw
 global bnt_account2pw
 global bnt_account3pw
 global bnt_account4pw
 global bnt_account5pw
 global bnt_account6pw
 bnt_account0 = bnt_account_0_a
 bnt_account1 = bnt_account_1_a
 bnt_account2 = bnt_account_2_a
 bnt_account3 = bnt_account_3_a
 bnt_account4 = bnt_account_4_a
 bnt_account5 = bnt_account_5_a
 bnt_account6 = bnt_account_6_a
 bnt_account0_n = bnt_account_0_n
 bnt_account1_n = bnt_account_1_n
 bnt_account2_n = bnt_account_2_n
 bnt_account3_n = bnt_account_3_n
 bnt_account4_n = bnt_account_4_n
 bnt_account5_n = bnt_account_5_n
 bnt_account6_n = bnt_account_6_n
 bnt_account0pw = bnt_account_0_pw
 bnt_account1pw = bnt_account_1_pw
 bnt_account2pw = bnt_account_2_pw
 bnt_account3pw = bnt_account_3_pw
 bnt_account4pw = bnt_account_4_pw
 bnt_account5pw = bnt_account_5_pw
 bnt_account6pw = bnt_account_6_pw
 print(bnt_tokenName+' Accounts Updated.')
def bnt_update_balances():
 global bnt_call_0
 global bnt_call_1
 global bnt_call_2
 global bnt_call_3
 global bnt_call_4
 global bnt_call_5
 global bnt_call_6
 global bnt_w_call_0
 global bnt_w_call_1
 global bnt_w_call_2
 global bnt_w_call_3
 global bnt_w_call_4
 global bnt_w_call_5
 global bnt_w_call_6
 bnt_update_accounts()
 print('Updating '+bnt_tokenName+' Balances Please Wait...')
 bnt_call_0 = bnt_balanceOf(bnt_account0)
 bnt_call_1 = bnt_balanceOf(bnt_account1)
 bnt_call_2 = bnt_balanceOf(bnt_account2)
 bnt_call_3 = bnt_balanceOf(bnt_account3)
 bnt_call_4 = bnt_balanceOf(bnt_account4)
 bnt_call_5 = bnt_balanceOf(bnt_account5)
 bnt_call_6 = bnt_balanceOf(bnt_account6)
 bnt_w_call_0 = bnt_balance(bnt_account0)
 bnt_w_call_1 = bnt_balance(bnt_account1)
 bnt_w_call_2 = bnt_balance(bnt_account2)
 bnt_w_call_3 = bnt_balance(bnt_account3)
 bnt_w_call_4 = bnt_balance(bnt_account4)
 bnt_w_call_5 = bnt_balance(bnt_account5)
 bnt_w_call_6 = bnt_balance(bnt_account6)
 print(bnt_tokenName+' Balances Updated.')
def bnt_list_all_accounts():
 bnt_update_accounts()
 print(bnt_tokenName+' '+bnt_account0_n+': '+bnt_account0)
 print(bnt_tokenName+' '+bnt_account1_n+': '+bnt_account1)
 print(bnt_tokenName+' '+bnt_account2_n+': '+bnt_account2)
 print(bnt_tokenName+' '+bnt_account3_n+': '+bnt_account3)
 print(bnt_tokenName+' '+bnt_account4_n+': '+bnt_account4)
 print(bnt_tokenName+' '+bnt_account5_n+': '+bnt_account5)
 print(bnt_tokenName+' '+bnt_account6_n+': '+bnt_account6)

def bnt_account_balance(accountNumber):
 bnt_update_balances()
 bnt_ab_account_number = accountNumber
 bnt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if bnt_ab_account_number == bnt_ab_input[0]:
  print('Calling '+bnt_account0_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account0_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_0 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_0 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[1]:
  print('Calling '+bnt_account1_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account1_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_1 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_1 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[2]:
  print('Calling '+bnt_account2_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account2_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_2 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_2 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[3]:
  print('Calling '+bnt_account3_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account3_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_3 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_3 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[4]:
  print('Calling '+bnt_account4_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account4_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_4 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_4 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[5]:
  print('Calling '+bnt_account5_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account5_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_5 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_5 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number == bnt_ab_input[6]:
  print('Calling '+bnt_account6_n+' '+bnt_tokenName+' Balance: ')
  print(bnt_account6_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_6 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_6 / bnt_token_d * bnt_last_price))
 if bnt_ab_account_number not in bnt_ab_input:
  print('Must Integer Within Range '+bnt_accounts_range+'.')

def bnt_list_all_account_balances():
 bnt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+bnt_tokenName+' Balance: ')
 print(bnt_account0_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_0 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_0 / bnt_token_d * bnt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(bnt_account0_n+': Ethereum Balance '+str(bnt_w_call_0 / _e_d)+' $'+str(bnt_w_call_0 / _e_d * bnt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+bnt_tokenName+' Balance: ')
 print(bnt_account1_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_1 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_1 / bnt_token_d * bnt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(bnt_account1_n+': Ethereum Balance '+str(bnt_w_call_1 / _e_d)+' $'+str(bnt_w_call_1 / _e_d * bnt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+bnt_tokenName+' Balance: ')
 print(bnt_account2_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_2 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_2 / bnt_token_d * bnt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(bnt_account2_n+': Ethereum Balance '+str(bnt_w_call_2 / _e_d)+' $'+str(bnt_w_call_2 / _e_d * bnt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+bnt_tokenName+' Balance: ')
 print(bnt_account3_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_3 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_3 / bnt_token_d * bnt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(bnt_account3_n+': Ethereum Balance '+str(bnt_w_call_3 / _e_d)+' $'+str(bnt_w_call_3 / _e_d * bnt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+bnt_tokenName+' Balance: ')
 print(bnt_account4_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_4 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_4 / bnt_token_d * bnt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(bnt_account4_n+': Ethereum Balance '+str(bnt_w_call_4 / _e_d)+' $'+str(bnt_w_call_4 / _e_d * bnt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+bnt_tokenName+' Balance: ')
 print(bnt_account5_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_5 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_5 / bnt_token_d * bnt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(bnt_account5_n+': Ethereum Balance '+str(bnt_w_call_5 / _e_d)+' $'+str(bnt_w_call_5 /_e_d * bnt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+bnt_tokenName+' Balance: ')
 print(bnt_account6_n+': '+bnt_tokenName+' Balance: '+str(bnt_call_6 / bnt_token_d)+' Usd/'+bnt_tokenName+' Balance: $'+str(bnt_call_6 / bnt_token_d * bnt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(bnt_account6_n+': Ethereum Balance '+str(bnt_w_call_6 / _e_d)+' $'+str(bnt_w_call_6 / _e_d * bnt_last_ethereum_price))
def bnt_unlock_all_accounts():
  bnt_unlock_account_0()
  bnt_unlock_account_1()
  bnt_unlock_account_2()
  bnt_unlock_account_3()
  bnt_unlock_account_4()
  bnt_unlock_account_5()
  bnt_unlock_account_6()


def bnt_unlock_account_0():
  global bnt_account0pw
  global bnt_account0
  global bnt_account0_n
  bnt_update_accounts()
  bnt_u_a_0 = bnt_w_unlock(bnt_account0, bnt_account0pw, bnt_unlockTime)
  if bnt_u_a_0 == False:
    if bnt_account0pw == '':
     bnt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account0_n+' Passphrase Denied: '+bnt_account0pw_r)
    elif bnt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bnt_account0_n+' Passphrase Denied: '+bnt_account0pw)
  if bnt_u_a_0 == True:
   print(bnt_account0_n+' Unlocked')

def bnt_unlock_account_1():
  global bnt_account1pw
  global bnt_account1
  global bnt_account1_n
  bnt_update_accounts()
  bnt_u_a_1 = bnt_unlock(bnt_account1, bnt_account1pw, bnt_unlockTime)
  if bnt_u_a_1 == False:
    if bnt_account1pw == '':
     bnt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account1_n+' Passphrase Denied: '+bnt_account1pw_r)
    elif bnt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bnt_account1_n+' Passphrase Denied: '+bnt_account1pw)
  if bnt_u_a_1 == True:
   print(bnt_account1_n+' Unlocked')

def bnt_unlock_account_2():
  global bnt_account2pw
  global bnt_account2
  global bnt_account2_n
  bnt_update_accounts()
  bnt_u_a_2 = bnt_unlock(bnt_account2, bnt_account2pw, bnt_unlockTime)
  if bnt_u_a_2 == False:
    if bnt_account2pw == '':
     bnt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account2_n+' Passphrase Denied: '+bnt_account2pw_r)
    elif bnt_account2pw != '':
     print('Unlock Failure With Account '+bnt_account2_n+' Passphrase Denied: '+bnt_account2pw)
  if bnt_u_a_2 == True:
   print(bnt_account2_n+' Unlocked')

def bnt_unlock_account_3():
  global bnt_account3pw
  global bnt_account3
  global bnt_account3_n
  bnt_update_accounts()
  bnt_u_a_3 = bnt_unlock(bnt_account3, bnt_account3pw, bnt_unlockTime)
  if bnt_u_a_3 == False:
    if bnt_account3pw == '':
     bnt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account3_n+' Passphrase Denied: '+bnt_account3pw_r)
    elif bnt_account3pw != '':
     print('Unlock Failure With Account '+bnt_account3_n+' Passphrase Denied: '+bnt_account3pw)
  if bnt_u_a_3 == True:
   print(bnt_account3_n+' Unlocked')

def bnt_unlock_account_4():
  global bnt_account4pw
  global bnt_account4
  global bnt_account4_n
  bnt_update_accounts()
  bnt_u_a_4 = bnt_unlock(bnt_account4, bnt_account4pw, bnt_unlockTime)
  if bnt_u_a_4 == False:
    if bnt_account4pw == '':
     bnt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account4_n+' Passphrase Denied: '+bnt_account4pw_r)
    elif bnt_account4pw != '':
     print('Unlock Failure With Account '+bnt_account4_n+' Passphrase Denied: '+bnt_account4pw)
  if bnt_u_a_4 == True:
   print(bnt_account4_n+' Unlocked')

def bnt_unlock_account_5():
  global bnt_account5pw
  global bnt_account5
  global bnt_account5_n
  bnt_update_accounts()
  bnt_u_a_5 = bnt_unlock(bnt_account5, bnt_account5pw, bnt_unlockTime)
  if bnt_u_a_5 == False:
    if bnt_account5pw == '':
     bnt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account5_n+' Passphrase Denied: '+bnt_account5pw_r)
    elif bnt_account5pw != '':
     print('Unlock Failure With Account '+bnt_account5_n+' Passphrase Denied: '+bnt_account5pw)
  if bnt_u_a_5 == True:
   print(bnt_account5_n+' Unlocked')

def bnt_unlock_account_6():
  global bnt_account6pw
  global bnt_account6
  global bnt_account6_n
  bnt_update_accounts()
  bnt_u_a_6 = bnt_unlock(bnt_account6, bnt_account6pw, bnt_unlockTime)
  if bnt_u_a_6 == False:
    if bnt_account6pw == '':
     bnt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bnt_account6_n+' Passphrase Denied: '+bnt_account6pw_r)
    elif bnt_account6pw != '':
     print('Unlock Failure With Account '+bnt_account6_n+' Passphrase Denied: '+bnt_account6pw)
  if bnt_u_a_6 == True:
   print(bnt_account6_n+' Unlocked')

def bnt_unlock_account(bnt_ua_accountNumber):
 bnt_update_accounts()
 bnt_ua_account_number = bnt_ua_accountNumber
 bnt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if bnt_ua_account_number == bnt_ua_input[0]:
  bnt_unlock_account_0()
 if bnt_ua_account_number == bnt_ua_input[1]:
  bnt_unlock_account_1()
 if bnt_ua_account_number == bnt_ua_input[2]:
  bnt_unlock_account_2()
 if bnt_ua_account_number == bnt_ua_input[3]:
  bnt_unlock_account_3()
 if bnt_ua_account_number == bnt_ua_input[4]:
  bnt_unlock_account_4()
 if bnt_ua_account_number == bnt_ua_input[5]:
  bnt_unlock_account_5()
 if bnt_ua_account_number == bnt_ua_input[6]:
  bnt_unlock_account_6()
 if bnt_ua_account_number not in bnt_ua_input:
  print('Must Integer Within Range '+bnt_accounts_range+'.')
 

def bnt_approve_between_accounts(fromAccount, toAccount, msgValue):
  bnt_update_accounts()
  bnt_a_0 = bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(bnt_a_0)

def bnt_approve(fromAccountNumber, toAddress, msgValue):
  bnt_update_accounts()
  bnt_unlock_account(fromAccountNumber)
  bnt_a_1 = bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(bnt_a_1)

def bnt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  bnt_update_accounts()
  bnt_unlock_account(fromAccount)
  bnt_t_0 = bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(bnt_t_0)

def bnt_transfer(fromAccountNumber, toAddress, msgValue):
  bnt_update_accounts()
  bnt_unlock_account(fromAccountNumber)
  bnt_t_1 = bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(bnt_t_1)

def bnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  bnt_update_accounts()
  bnt_unlock_account(callAccount)
  bnt_tf_0 = bnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(bnt_tf_0)

def bnt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  bnt_update_accounts()
  bnt_unlock_account(callAccount)
  bnt_tf_1 = bnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(bnt_tf_1)
  


def bnt_help():
  print('Following Functions For '+bnt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * bnt_unlock => web3.personal.unlockAccount
/ * bnt_accounts => web3.personal.listAccounts
/ * bnt_balance = web3.eth.getBalance
** bnt => web3.eth.contract(abi=bnt_abi, address=bnt_address)
** / * bnt_balanceOf => bnt.call().balanceOf

~ Function Listing Below:
~ bnt_update_accounts()
~ bnt_update_balances() \n\r -- => bnt_update_accounts()
~ bnt_list_all_accounts() \n\r -- => bnt_update_accounts()
~ bnt_account_balance(accountNumber) \n\r -- => bnt_update_balances() 
~ bnt_list_all_account_balances() \n\r -- => bnt_update_balances()
~ bnt_unlock_all_accounts() \n\r -- => bnt_unlock_account_0() \n\r -- => bnt_unlock_account_1() \n\r -- => bnt_unlock_account_2() \n\r -- => bnt_unlock_account_3() \n\r -- => bnt_unlock_account_4() \n\r -- => bnt_unlock_account_5() \n\r -- => bnt_unlock_account_6() 
~ bnt_unlock_account_0() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account0, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_1() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account1, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_2() \n\r -- => bnt_update_accounts() \n\r --/ *bnt_w_unlock(bnt_account2, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_3() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account3, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_4() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account4, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_5() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account5, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account_6() \n\r -- => bnt_update_accounts() \n\r -- / *bnt_w_unlock(bnt_account6, bnt_account0pw, bnt_unlockTime)
~ bnt_unlock_account(bnt_ua_accountNumber) \n\r -- => bnt_update_accounts() \n\r -- // bnt_unlock_account_0() \n\r -- // bnt_unlock_account_1() \n\r -- // bnt_unlock_account_2() \n\r -- // bnt_unlock_account_3() \n\r -- // bnt_unlock_account_4() \n\r -- // bnt_unlock_account_5() \n\r -- // bnt_unlock_account_6()
~ bnt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(fromAccount) \n\r -- / ** bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bnt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(fromAccountNumber) \n\r -- / ** bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bnt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(fromAccount) \n\r -- / ** bnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ bnt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(fromAccountNumber) \n\r -- / ** bnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(callAccount) \n\r / ** bnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bnt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bnt_update_accounts() \n\r -- => bnt_unlock_account(callAccount) \n\r -- / ** bnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ bnt_help() <-- You Are Here. ''')