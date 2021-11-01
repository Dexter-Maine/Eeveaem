#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global gno_account_0_a
global gno_account_1_a
global gno_account_2_a
global gno_account_3_a
global gno_account_4_a
global gno_account_5_a
global gno_account_6_a
global gno_address
global gno_abi
global gno
global gno_call_0
global gno_call_1
global gno_call_2
global gno_call_3
global gno_call_4
global gno_call_5
global gno_call_6
global gno_call_ab
global gno_accounts
global gno_account_0_pw
global gno_account_1_pw
global gno_account_2_pw
global gno_account_3_pw
global gno_account_4_pw
global gno_account_5_pw
global gno_account_6_pw
global gno_account_0_n
global gno_account_1_n
global gno_account_2_n
global gno_account_3_n
global gno_account_4_n
global gno_account_5_n
global gno_account_6_n
global gno_account1pw
global gno_account2pw
global gno_account3pw
global gno_account4pw
global gno_account5pw
global gno_account6pw
global gno_last_price
global gno_accounts_range
global gno_tokenName
global gno_last_ethereum_price
global gno_unlockTime
global gno_balance
global gno_balanceOf
global gno_unlock
global gno_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
gno_token_d = 1e18
_e_d = 1e18
gno_accounts_range = '[0, 6]'
gno_unlock = web3.personal.unlockAccount
gno_last_ethereum_price = 370.00
gno_last_price = 179.42
gno_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
gno_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
gno_tokenName = 'Gnosis Token'
gno_unlockTime = hex(10000) # Must be hex()
gno_account_0_a = gno_accounts[0]
gno_account_1_a = gno_accounts[1]
gno_account_2_a = gno_accounts[2]
gno_account_3_a = gno_accounts[3]
gno_account_4_a = gno_accounts[4]
gno_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
gno_account_6_a = gno_accounts[6]
# Supply Unlock Passwords For Transactions Below
gno_account_0_pw = 'GuildSkrypt2017!@#'
gno_account_1_pw = ''
gno_account_2_pw = 'GuildSkrypt2017!@#'
gno_account_3_pw = ''
gno_account_4_pw = ''
gno_account_5_pw = ''
gno_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
gno_account_0_n = 'Skotys Bittrex Account'
gno_account_1_n = 'Jeffs Account'
gno_account_2_n = 'Skrypts Bittrex Account'
gno_account_3_n = 'Skotys Personal Account'
gno_account_4_n = 'Unknown'
gno_account_5_n = 'Watched \'Bittrex\' Account.'
gno_account_6_n = 'Watched Account (1)'
# Contract Information Below :
gno_address = '0x6810e776880C02933D47DB1b9fc05908e5386b96'
gno_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"dutchAuction","type":"address"},{"name":"owners","type":"address[]"},{"name":"tokens","type":"uint256[]"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
gno = web3.eth.contract(abi=gno_abi, address=gno_address)
gno_balanceOf = gno.call().balanceOf
# End Contract Information
def gno_update_accounts():
 global gno_account0
 global gno_account1
 global gno_account2
 global gno_account3
 global gno_account4
 global gno_account5
 global gno_account6
 global gno_account0_n
 global gno_account1_n
 global gno_account2_n
 global gno_account3_n
 global gno_account4_n
 global gno_account5_n
 global gno_account6_n
 global gno_account0pw
 global gno_account1pw
 global gno_account2pw
 global gno_account3pw
 global gno_account4pw
 global gno_account5pw
 global gno_account6pw
 gno_account0 = gno_account_0_a
 gno_account1 = gno_account_1_a
 gno_account2 = gno_account_2_a
 gno_account3 = gno_account_3_a
 gno_account4 = gno_account_4_a
 gno_account5 = gno_account_5_a
 gno_account6 = gno_account_6_a
 gno_account0_n = gno_account_0_n
 gno_account1_n = gno_account_1_n
 gno_account2_n = gno_account_2_n
 gno_account3_n = gno_account_3_n
 gno_account4_n = gno_account_4_n
 gno_account5_n = gno_account_5_n
 gno_account6_n = gno_account_6_n
 gno_account0pw = gno_account_0_pw
 gno_account1pw = gno_account_1_pw
 gno_account2pw = gno_account_2_pw
 gno_account3pw = gno_account_3_pw
 gno_account4pw = gno_account_4_pw
 gno_account5pw = gno_account_5_pw
 gno_account6pw = gno_account_6_pw
 print(gno_tokenName+' Accounts Updated.')
def gno_update_balances():
 global gno_call_0
 global gno_call_1
 global gno_call_2
 global gno_call_3
 global gno_call_4
 global gno_call_5
 global gno_call_6
 global gno_w_call_0
 global gno_w_call_1
 global gno_w_call_2
 global gno_w_call_3
 global gno_w_call_4
 global gno_w_call_5
 global gno_w_call_6
 gno_update_accounts()
 print('Updating '+gno_tokenName+' Balances Please Wait...')
 gno_call_0 = gno_balanceOf(gno_account0)
 gno_call_1 = gno_balanceOf(gno_account1)
 gno_call_2 = gno_balanceOf(gno_account2)
 gno_call_3 = gno_balanceOf(gno_account3)
 gno_call_4 = gno_balanceOf(gno_account4)
 gno_call_5 = gno_balanceOf(gno_account5)
 gno_call_6 = gno_balanceOf(gno_account6)
 gno_w_call_0 = gno_balance(gno_account0)
 gno_w_call_1 = gno_balance(gno_account1)
 gno_w_call_2 = gno_balance(gno_account2)
 gno_w_call_3 = gno_balance(gno_account3)
 gno_w_call_4 = gno_balance(gno_account4)
 gno_w_call_5 = gno_balance(gno_account5)
 gno_w_call_6 = gno_balance(gno_account6)
 print(gno_tokenName+' Balances Updated.')
def gno_list_all_accounts():
 gno_update_accounts()
 print(gno_tokenName+' '+gno_account0_n+': '+gno_account0)
 print(gno_tokenName+' '+gno_account1_n+': '+gno_account1)
 print(gno_tokenName+' '+gno_account2_n+': '+gno_account2)
 print(gno_tokenName+' '+gno_account3_n+': '+gno_account3)
 print(gno_tokenName+' '+gno_account4_n+': '+gno_account4)
 print(gno_tokenName+' '+gno_account5_n+': '+gno_account5)
 print(gno_tokenName+' '+gno_account6_n+': '+gno_account6)

def gno_account_balance(accountNumber):
 gno_update_balances()
 gno_ab_account_number = accountNumber
 gno_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if gno_ab_account_number == gno_ab_input[0]:
  print('Calling '+gno_account0_n+' '+gno_tokenName+' Balance: ')
  print(gno_account0_n+': '+gno_tokenName+' Balance: '+str(gno_call_0 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_0 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[1]:
  print('Calling '+gno_account1_n+' '+gno_tokenName+' Balance: ')
  print(gno_account1_n+': '+gno_tokenName+' Balance: '+str(gno_call_1 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_1 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[2]:
  print('Calling '+gno_account2_n+' '+gno_tokenName+' Balance: ')
  print(gno_account2_n+': '+gno_tokenName+' Balance: '+str(gno_call_2 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_2 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[3]:
  print('Calling '+gno_account3_n+' '+gno_tokenName+' Balance: ')
  print(gno_account3_n+': '+gno_tokenName+' Balance: '+str(gno_call_3 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_3 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[4]:
  print('Calling '+gno_account4_n+' '+gno_tokenName+' Balance: ')
  print(gno_account4_n+': '+gno_tokenName+' Balance: '+str(gno_call_4 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_4 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[5]:
  print('Calling '+gno_account5_n+' '+gno_tokenName+' Balance: ')
  print(gno_account5_n+': '+gno_tokenName+' Balance: '+str(gno_call_5 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_5 / gno_token_d * gno_last_price))
 if gno_ab_account_number == gno_ab_input[6]:
  print('Calling '+gno_account6_n+' '+gno_tokenName+' Balance: ')
  print(gno_account6_n+': '+gno_tokenName+' Balance: '+str(gno_call_6 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_6 / gno_token_d * gno_last_price))
 if gno_ab_account_number not in gno_ab_input:
  print('Must Integer Within Range '+gno_accounts_range+'.')

def gno_list_all_account_balances():
 gno_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+gno_tokenName+' Balance: ')
 print(gno_account0_n+': '+gno_tokenName+' Balance: '+str(gno_call_0 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_0 / gno_token_d * gno_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(gno_account0_n+': Ethereum Balance '+str(gno_w_call_0 / _e_d)+' $'+str(gno_w_call_0 / _e_d * gno_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+gno_tokenName+' Balance: ')
 print(gno_account1_n+': '+gno_tokenName+' Balance: '+str(gno_call_1 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_1 / gno_token_d * gno_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(gno_account1_n+': Ethereum Balance '+str(gno_w_call_1 / _e_d)+' $'+str(gno_w_call_1 / _e_d * gno_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+gno_tokenName+' Balance: ')
 print(gno_account2_n+': '+gno_tokenName+' Balance: '+str(gno_call_2 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_2 / gno_token_d * gno_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(gno_account2_n+': Ethereum Balance '+str(gno_w_call_2 / _e_d)+' $'+str(gno_w_call_2 / _e_d * gno_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+gno_tokenName+' Balance: ')
 print(gno_account3_n+': '+gno_tokenName+' Balance: '+str(gno_call_3 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_3 / gno_token_d * gno_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(gno_account3_n+': Ethereum Balance '+str(gno_w_call_3 / _e_d)+' $'+str(gno_w_call_3 / _e_d * gno_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+gno_tokenName+' Balance: ')
 print(gno_account4_n+': '+gno_tokenName+' Balance: '+str(gno_call_4 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_4 / gno_token_d * gno_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(gno_account4_n+': Ethereum Balance '+str(gno_w_call_4 / _e_d)+' $'+str(gno_w_call_4 / _e_d * gno_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+gno_tokenName+' Balance: ')
 print(gno_account5_n+': '+gno_tokenName+' Balance: '+str(gno_call_5 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_5 / gno_token_d * gno_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(gno_account5_n+': Ethereum Balance '+str(gno_w_call_5 / _e_d)+' $'+str(gno_w_call_5 /_e_d * gno_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+gno_tokenName+' Balance: ')
 print(gno_account6_n+': '+gno_tokenName+' Balance: '+str(gno_call_6 / gno_token_d)+' Usd/'+gno_tokenName+' Balance: $'+str(gno_call_6 / gno_token_d * gno_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(gno_account6_n+': Ethereum Balance '+str(gno_w_call_6 / _e_d)+' $'+str(gno_w_call_6 / _e_d * gno_last_ethereum_price))
def gno_unlock_all_accounts():
  gno_unlock_account_0()
  gno_unlock_account_1()
  gno_unlock_account_2()
  gno_unlock_account_3()
  gno_unlock_account_4()
  gno_unlock_account_5()
  gno_unlock_account_6()


def gno_unlock_account_0():
  global gno_account0pw
  global gno_account0
  global gno_account0_n
  gno_update_accounts()
  gno_u_a_0 = gno_w_unlock(gno_account0, gno_account0pw, gno_unlockTime)
  if gno_u_a_0 == False:
    if gno_account0pw == '':
     gno_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account0_n+' Passphrase Denied: '+gno_account0pw_r)
    elif gno_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+gno_account0_n+' Passphrase Denied: '+gno_account0pw)
  if gno_u_a_0 == True:
   print(gno_account0_n+' Unlocked')

def gno_unlock_account_1():
  global gno_account1pw
  global gno_account1
  global gno_account1_n
  gno_update_accounts()
  gno_u_a_1 = gno_unlock(gno_account1, gno_account1pw, gno_unlockTime)
  if gno_u_a_1 == False:
    if gno_account1pw == '':
     gno_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account1_n+' Passphrase Denied: '+gno_account1pw_r)
    elif gno_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+gno_account1_n+' Passphrase Denied: '+gno_account1pw)
  if gno_u_a_1 == True:
   print(gno_account1_n+' Unlocked')

def gno_unlock_account_2():
  global gno_account2pw
  global gno_account2
  global gno_account2_n
  gno_update_accounts()
  gno_u_a_2 = gno_unlock(gno_account2, gno_account2pw, gno_unlockTime)
  if gno_u_a_2 == False:
    if gno_account2pw == '':
     gno_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account2_n+' Passphrase Denied: '+gno_account2pw_r)
    elif gno_account2pw != '':
     print('Unlock Failure With Account '+gno_account2_n+' Passphrase Denied: '+gno_account2pw)
  if gno_u_a_2 == True:
   print(gno_account2_n+' Unlocked')

def gno_unlock_account_3():
  global gno_account3pw
  global gno_account3
  global gno_account3_n
  gno_update_accounts()
  gno_u_a_3 = gno_unlock(gno_account3, gno_account3pw, gno_unlockTime)
  if gno_u_a_3 == False:
    if gno_account3pw == '':
     gno_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account3_n+' Passphrase Denied: '+gno_account3pw_r)
    elif gno_account3pw != '':
     print('Unlock Failure With Account '+gno_account3_n+' Passphrase Denied: '+gno_account3pw)
  if gno_u_a_3 == True:
   print(gno_account3_n+' Unlocked')

def gno_unlock_account_4():
  global gno_account4pw
  global gno_account4
  global gno_account4_n
  gno_update_accounts()
  gno_u_a_4 = gno_unlock(gno_account4, gno_account4pw, gno_unlockTime)
  if gno_u_a_4 == False:
    if gno_account4pw == '':
     gno_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account4_n+' Passphrase Denied: '+gno_account4pw_r)
    elif gno_account4pw != '':
     print('Unlock Failure With Account '+gno_account4_n+' Passphrase Denied: '+gno_account4pw)
  if gno_u_a_4 == True:
   print(gno_account4_n+' Unlocked')

def gno_unlock_account_5():
  global gno_account5pw
  global gno_account5
  global gno_account5_n
  gno_update_accounts()
  gno_u_a_5 = gno_unlock(gno_account5, gno_account5pw, gno_unlockTime)
  if gno_u_a_5 == False:
    if gno_account5pw == '':
     gno_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account5_n+' Passphrase Denied: '+gno_account5pw_r)
    elif gno_account5pw != '':
     print('Unlock Failure With Account '+gno_account5_n+' Passphrase Denied: '+gno_account5pw)
  if gno_u_a_5 == True:
   print(gno_account5_n+' Unlocked')

def gno_unlock_account_6():
  global gno_account6pw
  global gno_account6
  global gno_account6_n
  gno_update_accounts()
  gno_u_a_6 = gno_unlock(gno_account6, gno_account6pw, gno_unlockTime)
  if gno_u_a_6 == False:
    if gno_account6pw == '':
     gno_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gno_account6_n+' Passphrase Denied: '+gno_account6pw_r)
    elif gno_account6pw != '':
     print('Unlock Failure With Account '+gno_account6_n+' Passphrase Denied: '+gno_account6pw)
  if gno_u_a_6 == True:
   print(gno_account6_n+' Unlocked')

def gno_unlock_account(gno_ua_accountNumber):
 gno_update_accounts()
 gno_ua_account_number = gno_ua_accountNumber
 gno_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if gno_ua_account_number == gno_ua_input[0]:
  gno_unlock_account_0()
 if gno_ua_account_number == gno_ua_input[1]:
  gno_unlock_account_1()
 if gno_ua_account_number == gno_ua_input[2]:
  gno_unlock_account_2()
 if gno_ua_account_number == gno_ua_input[3]:
  gno_unlock_account_3()
 if gno_ua_account_number == gno_ua_input[4]:
  gno_unlock_account_4()
 if gno_ua_account_number == gno_ua_input[5]:
  gno_unlock_account_5()
 if gno_ua_account_number == gno_ua_input[6]:
  gno_unlock_account_6()
 if gno_ua_account_number not in gno_ua_input:
  print('Must Integer Within Range '+gno_accounts_range+'.')
 

def gno_approve_between_accounts(fromAccount, toAccount, msgValue):
  gno_update_accounts()
  gno_a_0 = gno.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(gno_a_0)

def gno_approve(fromAccountNumber, toAddress, msgValue):
  gno_update_accounts()
  gno_unlock_account(fromAccountNumber)
  gno_a_1 = gno.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(gno_a_1)

def gno_transfer_between_accounts(fromAccount, toAccount, msgValue):
  gno_update_accounts()
  gno_unlock_account(fromAccount)
  gno_t_0 = gno.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(gno_t_0)

def gno_transfer(fromAccountNumber, toAddress, msgValue):
  gno_update_accounts()
  gno_unlock_account(fromAccountNumber)
  gno_t_1 = gno.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(gno_t_1)

def gno_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  gno_update_accounts()
  gno_unlock_account(callAccount)
  gno_tf_0 = gno.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(gno_tf_0)

def gno_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  gno_update_accounts()
  gno_unlock_account(callAccount)
  gno_tf_1 = gno.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(gno_tf_1)
  


def gno_help():
  print('Following Functions For '+gno_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * gno_unlock => web3.personal.unlockAccount
/ * gno_accounts => web3.personal.listAccounts
/ * gno_balance = web3.eth.getBalance
** gno => web3.eth.contract(abi=gno_abi, address=gno_address)
** / * gno_balanceOf => gno.call().balanceOf

~ Function Listing Below:
~ gno_update_accounts()
~ gno_update_balances() \n\r -- => gno_update_accounts()
~ gno_list_all_accounts() \n\r -- => gno_update_accounts()
~ gno_account_balance(accountNumber) \n\r -- => gno_update_balances() 
~ gno_list_all_account_balances() \n\r -- => gno_update_balances()
~ gno_unlock_all_accounts() \n\r -- => gno_unlock_account_0() \n\r -- => gno_unlock_account_1() \n\r -- => gno_unlock_account_2() \n\r -- => gno_unlock_account_3() \n\r -- => gno_unlock_account_4() \n\r -- => gno_unlock_account_5() \n\r -- => gno_unlock_account_6() 
~ gno_unlock_account_0() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account0, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_1() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account1, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_2() \n\r -- => gno_update_accounts() \n\r --/ *gno_w_unlock(gno_account2, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_3() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account3, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_4() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account4, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_5() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account5, gno_account0pw, gno_unlockTime)
~ gno_unlock_account_6() \n\r -- => gno_update_accounts() \n\r -- / *gno_w_unlock(gno_account6, gno_account0pw, gno_unlockTime)
~ gno_unlock_account(gno_ua_accountNumber) \n\r -- => gno_update_accounts() \n\r -- // gno_unlock_account_0() \n\r -- // gno_unlock_account_1() \n\r -- // gno_unlock_account_2() \n\r -- // gno_unlock_account_3() \n\r -- // gno_unlock_account_4() \n\r -- // gno_unlock_account_5() \n\r -- // gno_unlock_account_6()
~ gno_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(fromAccount) \n\r -- / ** gno.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ gno_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(fromAccountNumber) \n\r -- / ** gno.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ gno_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(fromAccount) \n\r -- / ** gno.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ gno_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(fromAccountNumber) \n\r -- / ** gno.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ gno_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(callAccount) \n\r / ** gno.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ gno_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => gno_update_accounts() \n\r -- => gno_unlock_account(callAccount) \n\r -- / ** gno.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ gno_help() <-- You Are Here. ''')