#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global e_time_account_0_a
global e_time_account_1_a
global e_time_account_2_a
global e_time_account_3_a
global e_time_account_4_a
global e_time_account_5_a
global e_time_account_6_a
global e_time_address
global e_time_abi
global e_time
global e_time_call_0
global e_time_call_1
global e_time_call_2
global e_time_call_3
global e_time_call_4
global e_time_call_5
global e_time_call_6
global e_time_call_ab
global e_time_accounts
global e_time_account_0_pw
global e_time_account_1_pw
global e_time_account_2_pw
global e_time_account_3_pw
global e_time_account_4_pw
global e_time_account_5_pw
global e_time_account_6_pw
global e_time_account_0_n
global e_time_account_1_n
global e_time_account_2_n
global e_time_account_3_n
global e_time_account_4_n
global e_time_account_5_n
global e_time_account_6_n
global e_time_account1pw
global e_time_account2pw
global e_time_account3pw
global e_time_account4pw
global e_time_account5pw
global e_time_account6pw
global e_time_last_price
global e_time_accounts_range
global e_time_tokenName
global e_time_last_ethereum_price
global e_time_unlocke_time
global e_time_balance
global e_time_balanceOf
global e_time_unlock
global e_time_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
e_time_token_d = 1e8
_e_d = 1e18
e_time_accounts_range = '[0, 6]'
e_time_unlock = web3.personal.unlockAccount
e_time_last_ethereum_price = 370.00
e_time_last_price = 27.68
e_time_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
e_time_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
e_time_tokenName = 'e_time Token'
e_time_unlocke_time = hex(10000) # Must be hex()
e_time_account_0_a = e_time_accounts[0]
e_time_account_1_a = e_time_accounts[1]
e_time_account_2_a = e_time_accounts[2]
e_time_account_3_a = e_time_accounts[3]
e_time_account_4_a = e_time_accounts[4]
e_time_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
e_time_account_6_a = e_time_accounts[6]
# Supply Unlock Passwords For Transactions Below
e_time_account_0_pw = 'GuildSkrypt2017!@#'
e_time_account_1_pw = ''
e_time_account_2_pw = 'GuildSkrypt2017!@#'
e_time_account_3_pw = ''
e_time_account_4_pw = ''
e_time_account_5_pw = ''
e_time_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
e_time_account_0_n = 'Skotys Bittrex Account'
e_time_account_1_n = 'Jeffs Account'
e_time_account_2_n = 'Skrypts Bittrex Account'
e_time_account_3_n = 'Skotys Personal Account'
e_time_account_4_n = 'Unknown'
e_time_account_5_n = 'Watched \'Bittrex\' Account.'
e_time_account_6_n = 'Watched Account (1)'
# Contract Information Below :
e_time_address = '0x6531f133e6DeeBe7F2dcE5A0441aA7ef330B4e53'
e_time_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":false,"inputs":[{"name":"_for","type":"address"},{"name":"tokenCount","type":"uint256"}],"name":"issueTokens","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
e_time = web3.eth.contract(abi=e_time_abi, address=e_time_address)
e_time_balanceOf = e_time.call().balanceOf
# End Contract Information
def e_time_update_accounts():
 global e_time_account0
 global e_time_account1
 global e_time_account2
 global e_time_account3
 global e_time_account4
 global e_time_account5
 global e_time_account6
 global e_time_account0_n
 global e_time_account1_n
 global e_time_account2_n
 global e_time_account3_n
 global e_time_account4_n
 global e_time_account5_n
 global e_time_account6_n
 global e_time_account0pw
 global e_time_account1pw
 global e_time_account2pw
 global e_time_account3pw
 global e_time_account4pw
 global e_time_account5pw
 global e_time_account6pw
 e_time_account0 = e_time_account_0_a
 e_time_account1 = e_time_account_1_a
 e_time_account2 = e_time_account_2_a
 e_time_account3 = e_time_account_3_a
 e_time_account4 = e_time_account_4_a
 e_time_account5 = e_time_account_5_a
 e_time_account6 = e_time_account_6_a
 e_time_account0_n = e_time_account_0_n
 e_time_account1_n = e_time_account_1_n
 e_time_account2_n = e_time_account_2_n
 e_time_account3_n = e_time_account_3_n
 e_time_account4_n = e_time_account_4_n
 e_time_account5_n = e_time_account_5_n
 e_time_account6_n = e_time_account_6_n
 e_time_account0pw = e_time_account_0_pw
 e_time_account1pw = e_time_account_1_pw
 e_time_account2pw = e_time_account_2_pw
 e_time_account3pw = e_time_account_3_pw
 e_time_account4pw = e_time_account_4_pw
 e_time_account5pw = e_time_account_5_pw
 e_time_account6pw = e_time_account_6_pw
 print(e_time_tokenName+' Accounts Updated.')
def e_time_update_balances():
 global e_time_call_0
 global e_time_call_1
 global e_time_call_2
 global e_time_call_3
 global e_time_call_4
 global e_time_call_5
 global e_time_call_6
 global e_time_w_call_0
 global e_time_w_call_1
 global e_time_w_call_2
 global e_time_w_call_3
 global e_time_w_call_4
 global e_time_w_call_5
 global e_time_w_call_6
 e_time_update_accounts()
 print('Updating '+e_time_tokenName+' Balances Please Wait...')
 e_time_call_0 = e_time_balanceOf(e_time_account0)
 e_time_call_1 = e_time_balanceOf(e_time_account1)
 e_time_call_2 = e_time_balanceOf(e_time_account2)
 e_time_call_3 = e_time_balanceOf(e_time_account3)
 e_time_call_4 = e_time_balanceOf(e_time_account4)
 e_time_call_5 = e_time_balanceOf(e_time_account5)
 e_time_call_6 = e_time_balanceOf(e_time_account6)
 e_time_w_call_0 = e_time_balance(e_time_account0)
 e_time_w_call_1 = e_time_balance(e_time_account1)
 e_time_w_call_2 = e_time_balance(e_time_account2)
 e_time_w_call_3 = e_time_balance(e_time_account3)
 e_time_w_call_4 = e_time_balance(e_time_account4)
 e_time_w_call_5 = e_time_balance(e_time_account5)
 e_time_w_call_6 = e_time_balance(e_time_account6)
 print(e_time_tokenName+' Balances Updated.')
def e_time_list_all_accounts():
 e_time_update_accounts()
 print(e_time_tokenName+' '+e_time_account0_n+': '+e_time_account0)
 print(e_time_tokenName+' '+e_time_account1_n+': '+e_time_account1)
 print(e_time_tokenName+' '+e_time_account2_n+': '+e_time_account2)
 print(e_time_tokenName+' '+e_time_account3_n+': '+e_time_account3)
 print(e_time_tokenName+' '+e_time_account4_n+': '+e_time_account4)
 print(e_time_tokenName+' '+e_time_account5_n+': '+e_time_account5)
 print(e_time_tokenName+' '+e_time_account6_n+': '+e_time_account6)

def e_time_account_balance(accountNumber):
 e_time_update_balances()
 e_time_ab_account_number = accountNumber
 e_time_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if e_time_ab_account_number == e_time_ab_input[0]:
  print('Calling '+e_time_account0_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account0_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_0 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_0 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[1]:
  print('Calling '+e_time_account1_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account1_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_1 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_1 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[2]:
  print('Calling '+e_time_account2_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account2_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_2 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_2 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[3]:
  print('Calling '+e_time_account3_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account3_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_3 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_3 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[4]:
  print('Calling '+e_time_account4_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account4_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_4 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_4 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[5]:
  print('Calling '+e_time_account5_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account5_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_5 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_5 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number == e_time_ab_input[6]:
  print('Calling '+e_time_account6_n+' '+e_time_tokenName+' Balance: ')
  print(e_time_account6_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_6 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_6 / e_time_token_d * e_time_last_price))
 if e_time_ab_account_number not in e_time_ab_input:
  print('Must Integer Within Range '+e_time_accounts_range+'.')

def e_time_list_all_account_balances():
 e_time_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+e_time_tokenName+' Balance: ')
 print(e_time_account0_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_0 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_0 / e_time_token_d * e_time_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(e_time_account0_n+': Ethereum Balance '+str(e_time_w_call_0 / _e_d)+' $'+str(e_time_w_call_0 / _e_d * e_time_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+e_time_tokenName+' Balance: ')
 print(e_time_account1_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_1 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_1 / e_time_token_d * e_time_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(e_time_account1_n+': Ethereum Balance '+str(e_time_w_call_1 / _e_d)+' $'+str(e_time_w_call_1 / _e_d * e_time_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+e_time_tokenName+' Balance: ')
 print(e_time_account2_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_2 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_2 / e_time_token_d * e_time_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(e_time_account2_n+': Ethereum Balance '+str(e_time_w_call_2 / _e_d)+' $'+str(e_time_w_call_2 / _e_d * e_time_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+e_time_tokenName+' Balance: ')
 print(e_time_account3_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_3 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_3 / e_time_token_d * e_time_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(e_time_account3_n+': Ethereum Balance '+str(e_time_w_call_3 / _e_d)+' $'+str(e_time_w_call_3 / _e_d * e_time_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+e_time_tokenName+' Balance: ')
 print(e_time_account4_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_4 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_4 / e_time_token_d * e_time_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(e_time_account4_n+': Ethereum Balance '+str(e_time_w_call_4 / _e_d)+' $'+str(e_time_w_call_4 / _e_d * e_time_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+e_time_tokenName+' Balance: ')
 print(e_time_account5_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_5 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_5 / e_time_token_d * e_time_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(e_time_account5_n+': Ethereum Balance '+str(e_time_w_call_5 / _e_d)+' $'+str(e_time_w_call_5 /_e_d * e_time_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+e_time_tokenName+' Balance: ')
 print(e_time_account6_n+': '+e_time_tokenName+' Balance: '+str(e_time_call_6 / e_time_token_d)+' Usd/'+e_time_tokenName+' Balance: $'+str(e_time_call_6 / e_time_token_d * e_time_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(e_time_account6_n+': Ethereum Balance '+str(e_time_w_call_6 / _e_d)+' $'+str(e_time_w_call_6 / _e_d * e_time_last_ethereum_price))
def e_time_unlock_all_accounts():
  e_time_unlock_account_0()
  e_time_unlock_account_1()
  e_time_unlock_account_2()
  e_time_unlock_account_3()
  e_time_unlock_account_4()
  e_time_unlock_account_5()
  e_time_unlock_account_6()


def e_time_unlock_account_0():
  global e_time_account0pw
  global e_time_account0
  global e_time_account0_n
  e_time_update_accounts()
  e_time_u_a_0 = e_time_w_unlock(e_time_account0, e_time_account0pw, e_time_unlocke_time)
  if e_time_u_a_0 == False:
    if e_time_account0pw == '':
     e_time_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account0_n+' Passphrase Denied: '+e_time_account0pw_r)
    elif e_time_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+e_time_account0_n+' Passphrase Denied: '+e_time_account0pw)
  if e_time_u_a_0 == True:
   print(e_time_account0_n+' Unlocked')

def e_time_unlock_account_1():
  global e_time_account1pw
  global e_time_account1
  global e_time_account1_n
  e_time_update_accounts()
  e_time_u_a_1 = e_time_unlock(e_time_account1, e_time_account1pw, e_time_unlocke_time)
  if e_time_u_a_1 == False:
    if e_time_account1pw == '':
     e_time_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account1_n+' Passphrase Denied: '+e_time_account1pw_r)
    elif e_time_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+e_time_account1_n+' Passphrase Denied: '+e_time_account1pw)
  if e_time_u_a_1 == True:
   print(e_time_account1_n+' Unlocked')

def e_time_unlock_account_2():
  global e_time_account2pw
  global e_time_account2
  global e_time_account2_n
  e_time_update_accounts()
  e_time_u_a_2 = e_time_unlock(e_time_account2, e_time_account2pw, e_time_unlocke_time)
  if e_time_u_a_2 == False:
    if e_time_account2pw == '':
     e_time_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account2_n+' Passphrase Denied: '+e_time_account2pw_r)
    elif e_time_account2pw != '':
     print('Unlock Failure With Account '+e_time_account2_n+' Passphrase Denied: '+e_time_account2pw)
  if e_time_u_a_2 == True:
   print(e_time_account2_n+' Unlocked')

def e_time_unlock_account_3():
  global e_time_account3pw
  global e_time_account3
  global e_time_account3_n
  e_time_update_accounts()
  e_time_u_a_3 = e_time_unlock(e_time_account3, e_time_account3pw, e_time_unlocke_time)
  if e_time_u_a_3 == False:
    if e_time_account3pw == '':
     e_time_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account3_n+' Passphrase Denied: '+e_time_account3pw_r)
    elif e_time_account3pw != '':
     print('Unlock Failure With Account '+e_time_account3_n+' Passphrase Denied: '+e_time_account3pw)
  if e_time_u_a_3 == True:
   print(e_time_account3_n+' Unlocked')

def e_time_unlock_account_4():
  global e_time_account4pw
  global e_time_account4
  global e_time_account4_n
  e_time_update_accounts()
  e_time_u_a_4 = e_time_unlock(e_time_account4, e_time_account4pw, e_time_unlocke_time)
  if e_time_u_a_4 == False:
    if e_time_account4pw == '':
     e_time_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account4_n+' Passphrase Denied: '+e_time_account4pw_r)
    elif e_time_account4pw != '':
     print('Unlock Failure With Account '+e_time_account4_n+' Passphrase Denied: '+e_time_account4pw)
  if e_time_u_a_4 == True:
   print(e_time_account4_n+' Unlocked')

def e_time_unlock_account_5():
  global e_time_account5pw
  global e_time_account5
  global e_time_account5_n
  e_time_update_accounts()
  e_time_u_a_5 = e_time_unlock(e_time_account5, e_time_account5pw, e_time_unlocke_time)
  if e_time_u_a_5 == False:
    if e_time_account5pw == '':
     e_time_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account5_n+' Passphrase Denied: '+e_time_account5pw_r)
    elif e_time_account5pw != '':
     print('Unlock Failure With Account '+e_time_account5_n+' Passphrase Denied: '+e_time_account5pw)
  if e_time_u_a_5 == True:
   print(e_time_account5_n+' Unlocked')

def e_time_unlock_account_6():
  global e_time_account6pw
  global e_time_account6
  global e_time_account6_n
  e_time_update_accounts()
  e_time_u_a_6 = e_time_unlock(e_time_account6, e_time_account6pw, e_time_unlocke_time)
  if e_time_u_a_6 == False:
    if e_time_account6pw == '':
     e_time_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+e_time_account6_n+' Passphrase Denied: '+e_time_account6pw_r)
    elif e_time_account6pw != '':
     print('Unlock Failure With Account '+e_time_account6_n+' Passphrase Denied: '+e_time_account6pw)
  if e_time_u_a_6 == True:
   print(e_time_account6_n+' Unlocked')

def e_time_unlock_account(e_time_ua_accountNumber):
 e_time_update_accounts()
 e_time_ua_account_number = e_time_ua_accountNumber
 e_time_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if e_time_ua_account_number == e_time_ua_input[0]:
  e_time_unlock_account_0()
 if e_time_ua_account_number == e_time_ua_input[1]:
  e_time_unlock_account_1()
 if e_time_ua_account_number == e_time_ua_input[2]:
  e_time_unlock_account_2()
 if e_time_ua_account_number == e_time_ua_input[3]:
  e_time_unlock_account_3()
 if e_time_ua_account_number == e_time_ua_input[4]:
  e_time_unlock_account_4()
 if e_time_ua_account_number == e_time_ua_input[5]:
  e_time_unlock_account_5()
 if e_time_ua_account_number == e_time_ua_input[6]:
  e_time_unlock_account_6()
 if e_time_ua_account_number not in e_time_ua_input:
  print('Must Integer Within Range '+e_time_accounts_range+'.')
 

def e_time_approve_between_accounts(fromAccount, toAccount, msgValue):
  e_time_update_accounts()
  e_time_a_0 = e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(e_time_a_0)

def e_time_approve(fromAccountNumber, toAddress, msgValue):
  e_time_update_accounts()
  e_time_unlock_account(fromAccountNumber)
  e_time_a_1 = e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(e_time_a_1)

def e_time_transfer_between_accounts(fromAccount, toAccount, msgValue):
  e_time_update_accounts()
  e_time_unlock_account(fromAccount)
  e_time_t_0 = e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(e_time_t_0)

def e_time_transfer(fromAccountNumber, toAddress, msgValue):
  e_time_update_accounts()
  e_time_unlock_account(fromAccountNumber)
  e_time_t_1 = e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(e_time_t_1)

def e_time_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  e_time_update_accounts()
  e_time_unlock_account(callAccount)
  e_time_tf_0 = e_time.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(e_time_tf_0)

def e_time_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  e_time_update_accounts()
  e_time_unlock_account(callAccount)
  e_time_tf_1 = e_time.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(e_time_tf_1)
  


def e_time_help():
  print('Following Functions For '+e_time_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * e_time_unlock => web3.personal.unlockAccount
/ * e_time_accounts => web3.personal.listAccounts
/ * e_time_balance = web3.eth.getBalance
** e_time => web3.eth.contract(abi=e_time_abi, address=e_time_address)
** / * e_time_balanceOf => e_time.call().balanceOf

~ Function Listing Below:
~ e_time_update_accounts()
~ e_time_update_balances() \n\r -- => e_time_update_accounts()
~ e_time_list_all_accounts() \n\r -- => e_time_update_accounts()
~ e_time_account_balance(accountNumber) \n\r -- => e_time_update_balances() 
~ e_time_list_all_account_balances() \n\r -- => e_time_update_balances()
~ e_time_unlock_all_accounts() \n\r -- => e_time_unlock_account_0() \n\r -- => e_time_unlock_account_1() \n\r -- => e_time_unlock_account_2() \n\r -- => e_time_unlock_account_3() \n\r -- => e_time_unlock_account_4() \n\r -- => e_time_unlock_account_5() \n\r -- => e_time_unlock_account_6() 
~ e_time_unlock_account_0() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account0, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_1() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account1, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_2() \n\r -- => e_time_update_accounts() \n\r --/ *e_time_w_unlock(e_time_account2, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_3() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account3, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_4() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account4, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_5() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account5, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account_6() \n\r -- => e_time_update_accounts() \n\r -- / *e_time_w_unlock(e_time_account6, e_time_account0pw, e_time_unlocke_time)
~ e_time_unlock_account(e_time_ua_accountNumber) \n\r -- => e_time_update_accounts() \n\r -- // e_time_unlock_account_0() \n\r -- // e_time_unlock_account_1() \n\r -- // e_time_unlock_account_2() \n\r -- // e_time_unlock_account_3() \n\r -- // e_time_unlock_account_4() \n\r -- // e_time_unlock_account_5() \n\r -- // e_time_unlock_account_6()
~ e_time_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(fromAccount) \n\r -- / ** e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ e_time_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(fromAccountNumber) \n\r -- / ** e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ e_time_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(fromAccount) \n\r -- / ** e_time.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ e_time_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(fromAccountNumber) \n\r -- / ** e_time.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ e_time_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(callAccount) \n\r / ** e_time.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ e_time_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => e_time_update_accounts() \n\r -- => e_time_unlock_account(callAccount) \n\r -- / ** e_time.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ e_time_help() <-- You Are Here. ''')