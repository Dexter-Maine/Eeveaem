#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global sngls_account_0_a
global sngls_account_1_a
global sngls_account_2_a
global sngls_account_3_a
global sngls_account_4_a
global sngls_account_5_a
global sngls_account_6_a
global sngls_address
global sngls_abi
global sngls
global sngls_call_0
global sngls_call_1
global sngls_call_2
global sngls_call_3
global sngls_call_4
global sngls_call_5
global sngls_call_6
global sngls_call_ab
global sngls_accounts
global sngls_account_0_pw
global sngls_account_1_pw
global sngls_account_2_pw
global sngls_account_3_pw
global sngls_account_4_pw
global sngls_account_5_pw
global sngls_account_6_pw
global sngls_account_0_n
global sngls_account_1_n
global sngls_account_2_n
global sngls_account_3_n
global sngls_account_4_n
global sngls_account_5_n
global sngls_account_6_n
global sngls_account1pw
global sngls_account2pw
global sngls_account3pw
global sngls_account4pw
global sngls_account5pw
global sngls_account6pw
global sngls_last_price
global sngls_accounts_range
global sngls_tokenName
global sngls_last_ethereum_price
global sngls_unlockTime
global sngls_balance
global sngls_balanceOf
global sngls_unlock
global sngls_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
sngls_token_d = 1e0
_e_d = 1e18
sngls_accounts_range = '[0, 6]'
sngls_unlock = web3.personal.unlockAccount
sngls_last_ethereum_price = 370.00
sngls_last_price = 0.16
sngls_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
sngls_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
sngls_tokenName = 'Singular Token'
sngls_unlockTime = hex(10000) # Must be hex()
sngls_account_0_a = sngls_accounts[0]
sngls_account_1_a = sngls_accounts[1]
sngls_account_2_a = sngls_accounts[2]
sngls_account_3_a = sngls_accounts[3]
sngls_account_4_a = sngls_accounts[4]
sngls_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
sngls_account_6_a = sngls_accounts[6]
# Supply Unlock Passwords For Transactions Below
sngls_account_0_pw = 'GuildSkrypt2017!@#'
sngls_account_1_pw = ''
sngls_account_2_pw = 'GuildSkrypt2017!@#'
sngls_account_3_pw = ''
sngls_account_4_pw = ''
sngls_account_5_pw = ''
sngls_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
sngls_account_0_n = 'Skotys Bittrex Account'
sngls_account_1_n = 'Jeffs Account'
sngls_account_2_n = 'Skrypts Bittrex Account'
sngls_account_3_n = 'Skotys Personal Account'
sngls_account_4_n = 'Unknown'
sngls_account_5_n = 'Watched \'Bittrex\' Account.'
sngls_account_6_n = 'Watched Account (1)'
# Contract Information Below :
sngls_address = '0xaeC2E87E0A235266D9C5ADc9DEb4b2E29b54D009'
sngls_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":false,"inputs":[{"name":"_for","type":"address"},{"name":"tokenCount","type":"uint256"}],"name":"issueTokens","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
sngls = web3.eth.contract(abi=sngls_abi, address=sngls_address)
sngls_balanceOf = sngls.call().balanceOf
# End Contract Information
def sngls_update_accounts():
 global sngls_account0
 global sngls_account1
 global sngls_account2
 global sngls_account3
 global sngls_account4
 global sngls_account5
 global sngls_account6
 global sngls_account0_n
 global sngls_account1_n
 global sngls_account2_n
 global sngls_account3_n
 global sngls_account4_n
 global sngls_account5_n
 global sngls_account6_n
 global sngls_account0pw
 global sngls_account1pw
 global sngls_account2pw
 global sngls_account3pw
 global sngls_account4pw
 global sngls_account5pw
 global sngls_account6pw
 sngls_account0 = sngls_account_0_a
 sngls_account1 = sngls_account_1_a
 sngls_account2 = sngls_account_2_a
 sngls_account3 = sngls_account_3_a
 sngls_account4 = sngls_account_4_a
 sngls_account5 = sngls_account_5_a
 sngls_account6 = sngls_account_6_a
 sngls_account0_n = sngls_account_0_n
 sngls_account1_n = sngls_account_1_n
 sngls_account2_n = sngls_account_2_n
 sngls_account3_n = sngls_account_3_n
 sngls_account4_n = sngls_account_4_n
 sngls_account5_n = sngls_account_5_n
 sngls_account6_n = sngls_account_6_n
 sngls_account0pw = sngls_account_0_pw
 sngls_account1pw = sngls_account_1_pw
 sngls_account2pw = sngls_account_2_pw
 sngls_account3pw = sngls_account_3_pw
 sngls_account4pw = sngls_account_4_pw
 sngls_account5pw = sngls_account_5_pw
 sngls_account6pw = sngls_account_6_pw
 print(sngls_tokenName+' Accounts Updated.')
def sngls_update_balances():
 global sngls_call_0
 global sngls_call_1
 global sngls_call_2
 global sngls_call_3
 global sngls_call_4
 global sngls_call_5
 global sngls_call_6
 global sngls_w_call_0
 global sngls_w_call_1
 global sngls_w_call_2
 global sngls_w_call_3
 global sngls_w_call_4
 global sngls_w_call_5
 global sngls_w_call_6
 sngls_update_accounts()
 print('Updating '+sngls_tokenName+' Balances Please Wait...')
 sngls_call_0 = sngls_balanceOf(sngls_account0)
 sngls_call_1 = sngls_balanceOf(sngls_account1)
 sngls_call_2 = sngls_balanceOf(sngls_account2)
 sngls_call_3 = sngls_balanceOf(sngls_account3)
 sngls_call_4 = sngls_balanceOf(sngls_account4)
 sngls_call_5 = sngls_balanceOf(sngls_account5)
 sngls_call_6 = sngls_balanceOf(sngls_account6)
 sngls_w_call_0 = sngls_balance(sngls_account0)
 sngls_w_call_1 = sngls_balance(sngls_account1)
 sngls_w_call_2 = sngls_balance(sngls_account2)
 sngls_w_call_3 = sngls_balance(sngls_account3)
 sngls_w_call_4 = sngls_balance(sngls_account4)
 sngls_w_call_5 = sngls_balance(sngls_account5)
 sngls_w_call_6 = sngls_balance(sngls_account6)
 print(sngls_tokenName+' Balances Updated.')
def sngls_list_all_accounts():
 sngls_update_accounts()
 print(sngls_tokenName+' '+sngls_account0_n+': '+sngls_account0)
 print(sngls_tokenName+' '+sngls_account1_n+': '+sngls_account1)
 print(sngls_tokenName+' '+sngls_account2_n+': '+sngls_account2)
 print(sngls_tokenName+' '+sngls_account3_n+': '+sngls_account3)
 print(sngls_tokenName+' '+sngls_account4_n+': '+sngls_account4)
 print(sngls_tokenName+' '+sngls_account5_n+': '+sngls_account5)
 print(sngls_tokenName+' '+sngls_account6_n+': '+sngls_account6)

def sngls_account_balance(accountNumber):
 sngls_update_balances()
 sngls_ab_account_number = accountNumber
 sngls_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if sngls_ab_account_number == sngls_ab_input[0]:
  print('Calling '+sngls_account0_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account0_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_0 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_0 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[1]:
  print('Calling '+sngls_account1_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account1_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_1 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_1 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[2]:
  print('Calling '+sngls_account2_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account2_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_2 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_2 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[3]:
  print('Calling '+sngls_account3_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account3_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_3 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_3 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[4]:
  print('Calling '+sngls_account4_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account4_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_4 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_4 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[5]:
  print('Calling '+sngls_account5_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account5_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_5 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_5 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number == sngls_ab_input[6]:
  print('Calling '+sngls_account6_n+' '+sngls_tokenName+' Balance: ')
  print(sngls_account6_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_6 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_6 / sngls_token_d * sngls_last_price))
 if sngls_ab_account_number not in sngls_ab_input:
  print('Must Integer Within Range '+sngls_accounts_range+'.')

def sngls_list_all_account_balances():
 sngls_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+sngls_tokenName+' Balance: ')
 print(sngls_account0_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_0 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_0 / sngls_token_d * sngls_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(sngls_account0_n+': Ethereum Balance '+str(sngls_w_call_0 / _e_d)+' $'+str(sngls_w_call_0 / _e_d * sngls_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+sngls_tokenName+' Balance: ')
 print(sngls_account1_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_1 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_1 / sngls_token_d * sngls_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(sngls_account1_n+': Ethereum Balance '+str(sngls_w_call_1 / _e_d)+' $'+str(sngls_w_call_1 / _e_d * sngls_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+sngls_tokenName+' Balance: ')
 print(sngls_account2_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_2 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_2 / sngls_token_d * sngls_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(sngls_account2_n+': Ethereum Balance '+str(sngls_w_call_2 / _e_d)+' $'+str(sngls_w_call_2 / _e_d * sngls_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+sngls_tokenName+' Balance: ')
 print(sngls_account3_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_3 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_3 / sngls_token_d * sngls_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(sngls_account3_n+': Ethereum Balance '+str(sngls_w_call_3 / _e_d)+' $'+str(sngls_w_call_3 / _e_d * sngls_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+sngls_tokenName+' Balance: ')
 print(sngls_account4_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_4 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_4 / sngls_token_d * sngls_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(sngls_account4_n+': Ethereum Balance '+str(sngls_w_call_4 / _e_d)+' $'+str(sngls_w_call_4 / _e_d * sngls_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+sngls_tokenName+' Balance: ')
 print(sngls_account5_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_5 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_5 / sngls_token_d * sngls_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(sngls_account5_n+': Ethereum Balance '+str(sngls_w_call_5 / _e_d)+' $'+str(sngls_w_call_5 /_e_d * sngls_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+sngls_tokenName+' Balance: ')
 print(sngls_account6_n+': '+sngls_tokenName+' Balance: '+str(sngls_call_6 / sngls_token_d)+' Usd/'+sngls_tokenName+' Balance: $'+str(sngls_call_6 / sngls_token_d * sngls_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(sngls_account6_n+': Ethereum Balance '+str(sngls_w_call_6 / _e_d)+' $'+str(sngls_w_call_6 / _e_d * sngls_last_ethereum_price))
def sngls_unlock_all_accounts():
  sngls_unlock_account_0()
  sngls_unlock_account_1()
  sngls_unlock_account_2()
  sngls_unlock_account_3()
  sngls_unlock_account_4()
  sngls_unlock_account_5()
  sngls_unlock_account_6()


def sngls_unlock_account_0():
  global sngls_account0pw
  global sngls_account0
  global sngls_account0_n
  sngls_update_accounts()
  sngls_u_a_0 = sngls_w_unlock(sngls_account0, sngls_account0pw, sngls_unlockTime)
  if sngls_u_a_0 == False:
    if sngls_account0pw == '':
     sngls_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account0_n+' Passphrase Denied: '+sngls_account0pw_r)
    elif sngls_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+sngls_account0_n+' Passphrase Denied: '+sngls_account0pw)
  if sngls_u_a_0 == True:
   print(sngls_account0_n+' Unlocked')

def sngls_unlock_account_1():
  global sngls_account1pw
  global sngls_account1
  global sngls_account1_n
  sngls_update_accounts()
  sngls_u_a_1 = sngls_unlock(sngls_account1, sngls_account1pw, sngls_unlockTime)
  if sngls_u_a_1 == False:
    if sngls_account1pw == '':
     sngls_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account1_n+' Passphrase Denied: '+sngls_account1pw_r)
    elif sngls_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+sngls_account1_n+' Passphrase Denied: '+sngls_account1pw)
  if sngls_u_a_1 == True:
   print(sngls_account1_n+' Unlocked')

def sngls_unlock_account_2():
  global sngls_account2pw
  global sngls_account2
  global sngls_account2_n
  sngls_update_accounts()
  sngls_u_a_2 = sngls_unlock(sngls_account2, sngls_account2pw, sngls_unlockTime)
  if sngls_u_a_2 == False:
    if sngls_account2pw == '':
     sngls_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account2_n+' Passphrase Denied: '+sngls_account2pw_r)
    elif sngls_account2pw != '':
     print('Unlock Failure With Account '+sngls_account2_n+' Passphrase Denied: '+sngls_account2pw)
  if sngls_u_a_2 == True:
   print(sngls_account2_n+' Unlocked')

def sngls_unlock_account_3():
  global sngls_account3pw
  global sngls_account3
  global sngls_account3_n
  sngls_update_accounts()
  sngls_u_a_3 = sngls_unlock(sngls_account3, sngls_account3pw, sngls_unlockTime)
  if sngls_u_a_3 == False:
    if sngls_account3pw == '':
     sngls_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account3_n+' Passphrase Denied: '+sngls_account3pw_r)
    elif sngls_account3pw != '':
     print('Unlock Failure With Account '+sngls_account3_n+' Passphrase Denied: '+sngls_account3pw)
  if sngls_u_a_3 == True:
   print(sngls_account3_n+' Unlocked')

def sngls_unlock_account_4():
  global sngls_account4pw
  global sngls_account4
  global sngls_account4_n
  sngls_update_accounts()
  sngls_u_a_4 = sngls_unlock(sngls_account4, sngls_account4pw, sngls_unlockTime)
  if sngls_u_a_4 == False:
    if sngls_account4pw == '':
     sngls_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account4_n+' Passphrase Denied: '+sngls_account4pw_r)
    elif sngls_account4pw != '':
     print('Unlock Failure With Account '+sngls_account4_n+' Passphrase Denied: '+sngls_account4pw)
  if sngls_u_a_4 == True:
   print(sngls_account4_n+' Unlocked')

def sngls_unlock_account_5():
  global sngls_account5pw
  global sngls_account5
  global sngls_account5_n
  sngls_update_accounts()
  sngls_u_a_5 = sngls_unlock(sngls_account5, sngls_account5pw, sngls_unlockTime)
  if sngls_u_a_5 == False:
    if sngls_account5pw == '':
     sngls_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account5_n+' Passphrase Denied: '+sngls_account5pw_r)
    elif sngls_account5pw != '':
     print('Unlock Failure With Account '+sngls_account5_n+' Passphrase Denied: '+sngls_account5pw)
  if sngls_u_a_5 == True:
   print(sngls_account5_n+' Unlocked')

def sngls_unlock_account_6():
  global sngls_account6pw
  global sngls_account6
  global sngls_account6_n
  sngls_update_accounts()
  sngls_u_a_6 = sngls_unlock(sngls_account6, sngls_account6pw, sngls_unlockTime)
  if sngls_u_a_6 == False:
    if sngls_account6pw == '':
     sngls_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+sngls_account6_n+' Passphrase Denied: '+sngls_account6pw_r)
    elif sngls_account6pw != '':
     print('Unlock Failure With Account '+sngls_account6_n+' Passphrase Denied: '+sngls_account6pw)
  if sngls_u_a_6 == True:
   print(sngls_account6_n+' Unlocked')

def sngls_unlock_account(sngls_ua_accountNumber):
 sngls_update_accounts()
 sngls_ua_account_number = sngls_ua_accountNumber
 sngls_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if sngls_ua_account_number == sngls_ua_input[0]:
  sngls_unlock_account_0()
 if sngls_ua_account_number == sngls_ua_input[1]:
  sngls_unlock_account_1()
 if sngls_ua_account_number == sngls_ua_input[2]:
  sngls_unlock_account_2()
 if sngls_ua_account_number == sngls_ua_input[3]:
  sngls_unlock_account_3()
 if sngls_ua_account_number == sngls_ua_input[4]:
  sngls_unlock_account_4()
 if sngls_ua_account_number == sngls_ua_input[5]:
  sngls_unlock_account_5()
 if sngls_ua_account_number == sngls_ua_input[6]:
  sngls_unlock_account_6()
 if sngls_ua_account_number not in sngls_ua_input:
  print('Must Integer Within Range '+sngls_accounts_range+'.')
 

def sngls_approve_between_accounts(fromAccount, toAccount, msgValue):
  sngls_update_accounts()
  sngls_a_0 = sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(sngls_a_0)

def sngls_approve(fromAccountNumber, toAddress, msgValue):
  sngls_update_accounts()
  sngls_unlock_account(fromAccountNumber)
  sngls_a_1 = sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(sngls_a_1)

def sngls_transfer_between_accounts(fromAccount, toAccount, msgValue):
  sngls_update_accounts()
  sngls_unlock_account(fromAccount)
  sngls_t_0 = sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(sngls_t_0)

def sngls_transfer(fromAccountNumber, toAddress, msgValue):
  sngls_update_accounts()
  sngls_unlock_account(fromAccountNumber)
  sngls_t_1 = sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(sngls_t_1)

def sngls_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  sngls_update_accounts()
  sngls_unlock_account(callAccount)
  sngls_tf_0 = sngls.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(sngls_tf_0)

def sngls_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  sngls_update_accounts()
  sngls_unlock_account(callAccount)
  sngls_tf_1 = sngls.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(sngls_tf_1)
  


def sngls_help():
  print('Following Functions For '+sngls_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * sngls_unlock => web3.personal.unlockAccount
/ * sngls_accounts => web3.personal.listAccounts
/ * sngls_balance = web3.eth.getBalance
** sngls => web3.eth.contract(abi=sngls_abi, address=sngls_address)
** / * sngls_balanceOf => sngls.call().balanceOf

~ Function Listing Below:
~ sngls_update_accounts()
~ sngls_update_balances() \n\r -- => sngls_update_accounts()
~ sngls_list_all_accounts() \n\r -- => sngls_update_accounts()
~ sngls_account_balance(accountNumber) \n\r -- => sngls_update_balances() 
~ sngls_list_all_account_balances() \n\r -- => sngls_update_balances()
~ sngls_unlock_all_accounts() \n\r -- => sngls_unlock_account_0() \n\r -- => sngls_unlock_account_1() \n\r -- => sngls_unlock_account_2() \n\r -- => sngls_unlock_account_3() \n\r -- => sngls_unlock_account_4() \n\r -- => sngls_unlock_account_5() \n\r -- => sngls_unlock_account_6() 
~ sngls_unlock_account_0() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account0, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_1() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account1, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_2() \n\r -- => sngls_update_accounts() \n\r --/ *sngls_w_unlock(sngls_account2, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_3() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account3, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_4() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account4, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_5() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account5, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account_6() \n\r -- => sngls_update_accounts() \n\r -- / *sngls_w_unlock(sngls_account6, sngls_account0pw, sngls_unlockTime)
~ sngls_unlock_account(sngls_ua_accountNumber) \n\r -- => sngls_update_accounts() \n\r -- // sngls_unlock_account_0() \n\r -- // sngls_unlock_account_1() \n\r -- // sngls_unlock_account_2() \n\r -- // sngls_unlock_account_3() \n\r -- // sngls_unlock_account_4() \n\r -- // sngls_unlock_account_5() \n\r -- // sngls_unlock_account_6()
~ sngls_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(fromAccount) \n\r -- / ** sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ sngls_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(fromAccountNumber) \n\r -- / ** sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ sngls_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(fromAccount) \n\r -- / ** sngls.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ sngls_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(fromAccountNumber) \n\r -- / ** sngls.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ sngls_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(callAccount) \n\r / ** sngls.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ sngls_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => sngls_update_accounts() \n\r -- => sngls_unlock_account(callAccount) \n\r -- / ** sngls.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ sngls_help() <-- You Are Here. ''')