#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global edg_account_0_a
global edg_account_1_a
global edg_account_2_a
global edg_account_3_a
global edg_account_4_a
global edg_account_5_a
global edg_account_6_a
global edg_address
global edg_abi
global edg
global edg_call_0
global edg_call_1
global edg_call_2
global edg_call_3
global edg_call_4
global edg_call_5
global edg_call_6
global edg_call_ab
global edg_accounts
global edg_account_0_pw
global edg_account_1_pw
global edg_account_2_pw
global edg_account_3_pw
global edg_account_4_pw
global edg_account_5_pw
global edg_account_6_pw
global edg_account_0_n
global edg_account_1_n
global edg_account_2_n
global edg_account_3_n
global edg_account_4_n
global edg_account_5_n
global edg_account_6_n
global edg_account1pw
global edg_account2pw
global edg_account3pw
global edg_account4pw
global edg_account5pw
global edg_account6pw
global edg_last_price
global edg_accounts_range
global edg_tokenName
global edg_last_ethereum_price
global edg_unlockTime
global edg_balance
global edg_balanceOf
global edg_unlock
global edg_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
edg_token_d = 1e0
_e_d = 1e18
edg_accounts_range = '[0, 6]'
edg_unlock = web3.personal.unlockAccount
edg_last_ethereum_price = 370.00
edg_last_price = 0.72
edg_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
edg_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
edg_tokenName = 'Edgeless Token'
edg_unlockTime = hex(10000) # Must be hex()
edg_account_0_a = edg_accounts[0]
edg_account_1_a = edg_accounts[1]
edg_account_2_a = edg_accounts[2]
edg_account_3_a = edg_accounts[3]
edg_account_4_a = edg_accounts[4]
edg_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
edg_account_6_a = edg_accounts[6]
# Supply Unlock Passwords For Transactions Below
edg_account_0_pw = 'GuildSkrypt2017!@#'
edg_account_1_pw = ''
edg_account_2_pw = 'GuildSkrypt2017!@#'
edg_account_3_pw = ''
edg_account_4_pw = ''
edg_account_5_pw = ''
edg_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
edg_account_0_n = 'Skotys Bittrex Account'
edg_account_1_n = 'Jeffs Account'
edg_account_2_n = 'Skrypts Bittrex Account'
edg_account_3_n = 'Skotys Personal Account'
edg_account_4_n = 'Unknown'
edg_account_5_n = 'Watched \'Bittrex\' Account.'
edg_account_6_n = 'Watched Account (1)'
# Contract Information Below :
edg_address = '0x08711D3B02C8758F2FB3ab4e80228418a7F8e39c'
edg_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"burn","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"startTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Burned","type":"event"}]
edg = web3.eth.contract(abi=edg_abi, address=edg_address)
edg_balanceOf = edg.call().balanceOf
# End Contract Information
def edg_update_accounts():
 global edg_account0
 global edg_account1
 global edg_account2
 global edg_account3
 global edg_account4
 global edg_account5
 global edg_account6
 global edg_account0_n
 global edg_account1_n
 global edg_account2_n
 global edg_account3_n
 global edg_account4_n
 global edg_account5_n
 global edg_account6_n
 global edg_account0pw
 global edg_account1pw
 global edg_account2pw
 global edg_account3pw
 global edg_account4pw
 global edg_account5pw
 global edg_account6pw
 edg_account0 = edg_account_0_a
 edg_account1 = edg_account_1_a
 edg_account2 = edg_account_2_a
 edg_account3 = edg_account_3_a
 edg_account4 = edg_account_4_a
 edg_account5 = edg_account_5_a
 edg_account6 = edg_account_6_a
 edg_account0_n = edg_account_0_n
 edg_account1_n = edg_account_1_n
 edg_account2_n = edg_account_2_n
 edg_account3_n = edg_account_3_n
 edg_account4_n = edg_account_4_n
 edg_account5_n = edg_account_5_n
 edg_account6_n = edg_account_6_n
 edg_account0pw = edg_account_0_pw
 edg_account1pw = edg_account_1_pw
 edg_account2pw = edg_account_2_pw
 edg_account3pw = edg_account_3_pw
 edg_account4pw = edg_account_4_pw
 edg_account5pw = edg_account_5_pw
 edg_account6pw = edg_account_6_pw
 print(edg_tokenName+' Accounts Updated.')
def edg_update_balances():
 global edg_call_0
 global edg_call_1
 global edg_call_2
 global edg_call_3
 global edg_call_4
 global edg_call_5
 global edg_call_6
 global edg_w_call_0
 global edg_w_call_1
 global edg_w_call_2
 global edg_w_call_3
 global edg_w_call_4
 global edg_w_call_5
 global edg_w_call_6
 edg_update_accounts()
 print('Updating '+edg_tokenName+' Balances Please Wait...')
 edg_call_0 = edg_balanceOf(edg_account0)
 edg_call_1 = edg_balanceOf(edg_account1)
 edg_call_2 = edg_balanceOf(edg_account2)
 edg_call_3 = edg_balanceOf(edg_account3)
 edg_call_4 = edg_balanceOf(edg_account4)
 edg_call_5 = edg_balanceOf(edg_account5)
 edg_call_6 = edg_balanceOf(edg_account6)
 edg_w_call_0 = edg_balance(edg_account0)
 edg_w_call_1 = edg_balance(edg_account1)
 edg_w_call_2 = edg_balance(edg_account2)
 edg_w_call_3 = edg_balance(edg_account3)
 edg_w_call_4 = edg_balance(edg_account4)
 edg_w_call_5 = edg_balance(edg_account5)
 edg_w_call_6 = edg_balance(edg_account6)
 print(edg_tokenName+' Balances Updated.')
def edg_list_all_accounts():
 edg_update_accounts()
 print(edg_tokenName+' '+edg_account0_n+': '+edg_account0)
 print(edg_tokenName+' '+edg_account1_n+': '+edg_account1)
 print(edg_tokenName+' '+edg_account2_n+': '+edg_account2)
 print(edg_tokenName+' '+edg_account3_n+': '+edg_account3)
 print(edg_tokenName+' '+edg_account4_n+': '+edg_account4)
 print(edg_tokenName+' '+edg_account5_n+': '+edg_account5)
 print(edg_tokenName+' '+edg_account6_n+': '+edg_account6)

def edg_account_balance(accountNumber):
 edg_update_balances()
 edg_ab_account_number = accountNumber
 edg_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if edg_ab_account_number == edg_ab_input[0]:
  print('Calling '+edg_account0_n+' '+edg_tokenName+' Balance: ')
  print(edg_account0_n+': '+edg_tokenName+' Balance: '+str(edg_call_0 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_0 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[1]:
  print('Calling '+edg_account1_n+' '+edg_tokenName+' Balance: ')
  print(edg_account1_n+': '+edg_tokenName+' Balance: '+str(edg_call_1 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_1 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[2]:
  print('Calling '+edg_account2_n+' '+edg_tokenName+' Balance: ')
  print(edg_account2_n+': '+edg_tokenName+' Balance: '+str(edg_call_2 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_2 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[3]:
  print('Calling '+edg_account3_n+' '+edg_tokenName+' Balance: ')
  print(edg_account3_n+': '+edg_tokenName+' Balance: '+str(edg_call_3 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_3 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[4]:
  print('Calling '+edg_account4_n+' '+edg_tokenName+' Balance: ')
  print(edg_account4_n+': '+edg_tokenName+' Balance: '+str(edg_call_4 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_4 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[5]:
  print('Calling '+edg_account5_n+' '+edg_tokenName+' Balance: ')
  print(edg_account5_n+': '+edg_tokenName+' Balance: '+str(edg_call_5 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_5 / edg_token_d * edg_last_price))
 if edg_ab_account_number == edg_ab_input[6]:
  print('Calling '+edg_account6_n+' '+edg_tokenName+' Balance: ')
  print(edg_account6_n+': '+edg_tokenName+' Balance: '+str(edg_call_6 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_6 / edg_token_d * edg_last_price))
 if edg_ab_account_number not in edg_ab_input:
  print('Must Integer Within Range '+edg_accounts_range+'.')

def edg_list_all_account_balances():
 edg_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+edg_tokenName+' Balance: ')
 print(edg_account0_n+': '+edg_tokenName+' Balance: '+str(edg_call_0 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_0 / edg_token_d * edg_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(edg_account0_n+': Ethereum Balance '+str(edg_w_call_0 / _e_d)+' $'+str(edg_w_call_0 / _e_d * edg_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+edg_tokenName+' Balance: ')
 print(edg_account1_n+': '+edg_tokenName+' Balance: '+str(edg_call_1 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_1 / edg_token_d * edg_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(edg_account1_n+': Ethereum Balance '+str(edg_w_call_1 / _e_d)+' $'+str(edg_w_call_1 / _e_d * edg_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+edg_tokenName+' Balance: ')
 print(edg_account2_n+': '+edg_tokenName+' Balance: '+str(edg_call_2 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_2 / edg_token_d * edg_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(edg_account2_n+': Ethereum Balance '+str(edg_w_call_2 / _e_d)+' $'+str(edg_w_call_2 / _e_d * edg_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+edg_tokenName+' Balance: ')
 print(edg_account3_n+': '+edg_tokenName+' Balance: '+str(edg_call_3 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_3 / edg_token_d * edg_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(edg_account3_n+': Ethereum Balance '+str(edg_w_call_3 / _e_d)+' $'+str(edg_w_call_3 / _e_d * edg_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+edg_tokenName+' Balance: ')
 print(edg_account4_n+': '+edg_tokenName+' Balance: '+str(edg_call_4 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_4 / edg_token_d * edg_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(edg_account4_n+': Ethereum Balance '+str(edg_w_call_4 / _e_d)+' $'+str(edg_w_call_4 / _e_d * edg_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+edg_tokenName+' Balance: ')
 print(edg_account5_n+': '+edg_tokenName+' Balance: '+str(edg_call_5 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_5 / edg_token_d * edg_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(edg_account5_n+': Ethereum Balance '+str(edg_w_call_5 / _e_d)+' $'+str(edg_w_call_5 /_e_d * edg_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+edg_tokenName+' Balance: ')
 print(edg_account6_n+': '+edg_tokenName+' Balance: '+str(edg_call_6 / edg_token_d)+' Usd/'+edg_tokenName+' Balance: $'+str(edg_call_6 / edg_token_d * edg_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(edg_account6_n+': Ethereum Balance '+str(edg_w_call_6 / _e_d)+' $'+str(edg_w_call_6 / _e_d * edg_last_ethereum_price))
def edg_unlock_all_accounts():
  edg_unlock_account_0()
  edg_unlock_account_1()
  edg_unlock_account_2()
  edg_unlock_account_3()
  edg_unlock_account_4()
  edg_unlock_account_5()
  edg_unlock_account_6()


def edg_unlock_account_0():
  global edg_account0pw
  global edg_account0
  global edg_account0_n
  edg_update_accounts()
  edg_u_a_0 = edg_w_unlock(edg_account0, edg_account0pw, edg_unlockTime)
  if edg_u_a_0 == False:
    if edg_account0pw == '':
     edg_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account0_n+' Passphrase Denied: '+edg_account0pw_r)
    elif edg_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+edg_account0_n+' Passphrase Denied: '+edg_account0pw)
  if edg_u_a_0 == True:
   print(edg_account0_n+' Unlocked')

def edg_unlock_account_1():
  global edg_account1pw
  global edg_account1
  global edg_account1_n
  edg_update_accounts()
  edg_u_a_1 = edg_unlock(edg_account1, edg_account1pw, edg_unlockTime)
  if edg_u_a_1 == False:
    if edg_account1pw == '':
     edg_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account1_n+' Passphrase Denied: '+edg_account1pw_r)
    elif edg_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+edg_account1_n+' Passphrase Denied: '+edg_account1pw)
  if edg_u_a_1 == True:
   print(edg_account1_n+' Unlocked')

def edg_unlock_account_2():
  global edg_account2pw
  global edg_account2
  global edg_account2_n
  edg_update_accounts()
  edg_u_a_2 = edg_unlock(edg_account2, edg_account2pw, edg_unlockTime)
  if edg_u_a_2 == False:
    if edg_account2pw == '':
     edg_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account2_n+' Passphrase Denied: '+edg_account2pw_r)
    elif edg_account2pw != '':
     print('Unlock Failure With Account '+edg_account2_n+' Passphrase Denied: '+edg_account2pw)
  if edg_u_a_2 == True:
   print(edg_account2_n+' Unlocked')

def edg_unlock_account_3():
  global edg_account3pw
  global edg_account3
  global edg_account3_n
  edg_update_accounts()
  edg_u_a_3 = edg_unlock(edg_account3, edg_account3pw, edg_unlockTime)
  if edg_u_a_3 == False:
    if edg_account3pw == '':
     edg_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account3_n+' Passphrase Denied: '+edg_account3pw_r)
    elif edg_account3pw != '':
     print('Unlock Failure With Account '+edg_account3_n+' Passphrase Denied: '+edg_account3pw)
  if edg_u_a_3 == True:
   print(edg_account3_n+' Unlocked')

def edg_unlock_account_4():
  global edg_account4pw
  global edg_account4
  global edg_account4_n
  edg_update_accounts()
  edg_u_a_4 = edg_unlock(edg_account4, edg_account4pw, edg_unlockTime)
  if edg_u_a_4 == False:
    if edg_account4pw == '':
     edg_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account4_n+' Passphrase Denied: '+edg_account4pw_r)
    elif edg_account4pw != '':
     print('Unlock Failure With Account '+edg_account4_n+' Passphrase Denied: '+edg_account4pw)
  if edg_u_a_4 == True:
   print(edg_account4_n+' Unlocked')

def edg_unlock_account_5():
  global edg_account5pw
  global edg_account5
  global edg_account5_n
  edg_update_accounts()
  edg_u_a_5 = edg_unlock(edg_account5, edg_account5pw, edg_unlockTime)
  if edg_u_a_5 == False:
    if edg_account5pw == '':
     edg_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account5_n+' Passphrase Denied: '+edg_account5pw_r)
    elif edg_account5pw != '':
     print('Unlock Failure With Account '+edg_account5_n+' Passphrase Denied: '+edg_account5pw)
  if edg_u_a_5 == True:
   print(edg_account5_n+' Unlocked')

def edg_unlock_account_6():
  global edg_account6pw
  global edg_account6
  global edg_account6_n
  edg_update_accounts()
  edg_u_a_6 = edg_unlock(edg_account6, edg_account6pw, edg_unlockTime)
  if edg_u_a_6 == False:
    if edg_account6pw == '':
     edg_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+edg_account6_n+' Passphrase Denied: '+edg_account6pw_r)
    elif edg_account6pw != '':
     print('Unlock Failure With Account '+edg_account6_n+' Passphrase Denied: '+edg_account6pw)
  if edg_u_a_6 == True:
   print(edg_account6_n+' Unlocked')

def edg_unlock_account(edg_ua_accountNumber):
 edg_update_accounts()
 edg_ua_account_number = edg_ua_accountNumber
 edg_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if edg_ua_account_number == edg_ua_input[0]:
  edg_unlock_account_0()
 if edg_ua_account_number == edg_ua_input[1]:
  edg_unlock_account_1()
 if edg_ua_account_number == edg_ua_input[2]:
  edg_unlock_account_2()
 if edg_ua_account_number == edg_ua_input[3]:
  edg_unlock_account_3()
 if edg_ua_account_number == edg_ua_input[4]:
  edg_unlock_account_4()
 if edg_ua_account_number == edg_ua_input[5]:
  edg_unlock_account_5()
 if edg_ua_account_number == edg_ua_input[6]:
  edg_unlock_account_6()
 if edg_ua_account_number not in edg_ua_input:
  print('Must Integer Within Range '+edg_accounts_range+'.')
 

def edg_approve_between_accounts(fromAccount, toAccount, msgValue):
  edg_update_accounts()
  edg_a_0 = edg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(edg_a_0)

def edg_approve(fromAccountNumber, toAddress, msgValue):
  edg_update_accounts()
  edg_unlock_account(fromAccountNumber)
  edg_a_1 = edg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(edg_a_1)

def edg_transfer_between_accounts(fromAccount, toAccount, msgValue):
  edg_update_accounts()
  edg_unlock_account(fromAccount)
  edg_t_0 = edg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(edg_t_0)

def edg_transfer(fromAccountNumber, toAddress, msgValue):
  edg_update_accounts()
  edg_unlock_account(fromAccountNumber)
  edg_t_1 = edg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(edg_t_1)

def edg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  edg_update_accounts()
  edg_unlock_account(callAccount)
  edg_tf_0 = edg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(edg_tf_0)

def edg_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  edg_update_accounts()
  edg_unlock_account(callAccount)
  edg_tf_1 = edg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(edg_tf_1)
  


def edg_help():
  print('Following Functions For '+edg_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * edg_unlock => web3.personal.unlockAccount
/ * edg_accounts => web3.personal.listAccounts
/ * edg_balance = web3.eth.getBalance
** edg => web3.eth.contract(abi=edg_abi, address=edg_address)
** / * edg_balanceOf => edg.call().balanceOf

~ Function Listing Below:
~ edg_update_accounts()
~ edg_update_balances() \n\r -- => edg_update_accounts()
~ edg_list_all_accounts() \n\r -- => edg_update_accounts()
~ edg_account_balance(accountNumber) \n\r -- => edg_update_balances() 
~ edg_list_all_account_balances() \n\r -- => edg_update_balances()
~ edg_unlock_all_accounts() \n\r -- => edg_unlock_account_0() \n\r -- => edg_unlock_account_1() \n\r -- => edg_unlock_account_2() \n\r -- => edg_unlock_account_3() \n\r -- => edg_unlock_account_4() \n\r -- => edg_unlock_account_5() \n\r -- => edg_unlock_account_6() 
~ edg_unlock_account_0() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account0, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_1() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account1, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_2() \n\r -- => edg_update_accounts() \n\r --/ *edg_w_unlock(edg_account2, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_3() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account3, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_4() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account4, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_5() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account5, edg_account0pw, edg_unlockTime)
~ edg_unlock_account_6() \n\r -- => edg_update_accounts() \n\r -- / *edg_w_unlock(edg_account6, edg_account0pw, edg_unlockTime)
~ edg_unlock_account(edg_ua_accountNumber) \n\r -- => edg_update_accounts() \n\r -- // edg_unlock_account_0() \n\r -- // edg_unlock_account_1() \n\r -- // edg_unlock_account_2() \n\r -- // edg_unlock_account_3() \n\r -- // edg_unlock_account_4() \n\r -- // edg_unlock_account_5() \n\r -- // edg_unlock_account_6()
~ edg_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(fromAccount) \n\r -- / ** edg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ edg_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(fromAccountNumber) \n\r -- / ** edg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ edg_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(fromAccount) \n\r -- / ** edg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ edg_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(fromAccountNumber) \n\r -- / ** edg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ edg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(callAccount) \n\r / ** edg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ edg_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => edg_update_accounts() \n\r -- => edg_unlock_account(callAccount) \n\r -- / ** edg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ edg_help() <-- You Are Here. ''')