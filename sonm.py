#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global snm_account_0_a
global snm_account_1_a
global snm_account_2_a
global snm_account_3_a
global snm_account_4_a
global snm_account_5_a
global snm_account_6_a
global snm_address
global snm_abi
global snm
global snm_call_0
global snm_call_1
global snm_call_2
global snm_call_3
global snm_call_4
global snm_call_5
global snm_call_6
global snm_call_ab
global snm_accounts
global snm_account_0_pw
global snm_account_1_pw
global snm_account_2_pw
global snm_account_3_pw
global snm_account_4_pw
global snm_account_5_pw
global snm_account_6_pw
global snm_account_0_n
global snm_account_1_n
global snm_account_2_n
global snm_account_3_n
global snm_account_4_n
global snm_account_5_n
global snm_account_6_n
global snm_account1pw
global snm_account2pw
global snm_account3pw
global snm_account4pw
global snm_account5pw
global snm_account6pw
global snm_last_price
global snm_accounts_range
global snm_tokenName
global snm_last_ethereum_price
global snm_unlockTime
global snm_balance
global snm_balanceOf
global snm_unlock
global snm_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
snm_token_d = 1e18
_e_d = 1e18
snm_accounts_range = '[0, 6]'
snm_unlock = web3.personal.unlockAccount
snm_last_ethereum_price = 370.00
snm_last_price = 0.08
snm_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
snm_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
snm_tokenName = 'Sonm Token'
snm_unlockTime = hex(10000) # Must be hex()
snm_account_0_a = snm_accounts[0]
snm_account_1_a = snm_accounts[1]
snm_account_2_a = snm_accounts[2]
snm_account_3_a = snm_accounts[3]
snm_account_4_a = snm_accounts[4]
snm_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
snm_account_6_a = snm_accounts[6]
# Supply Unlock Passwords For Transactions Below
snm_account_0_pw = 'GuildSkrypt2017!@#'
snm_account_1_pw = ''
snm_account_2_pw = 'GuildSkrypt2017!@#'
snm_account_3_pw = ''
snm_account_4_pw = ''
snm_account_5_pw = ''
snm_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
snm_account_0_n = 'Skotys Bittrex Account'
snm_account_1_n = 'Jeffs Account'
snm_account_2_n = 'Skrypts Bittrex Account'
snm_account_3_n = 'Skotys Personal Account'
snm_account_4_n = 'Unknown'
snm_account_5_n = 'Watched \'Bittrex\' Account.'
snm_account_6_n = 'Watched Account (1)'
# Contract Information Below :
snm_address = '0x983F6d60db79ea8cA4eB9968C6aFf8cfA04B3c63'
snm_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":false,"inputs":[{"name":"_for","type":"address"},{"name":"tokenCount","type":"uint256"}],"name":"issueTokens","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
snm = web3.eth.contract(abi=snm_abi, address=snm_address)
snm_balanceOf = snm.call().balanceOf
# End Contract Information
def snm_update_accounts():
 global snm_account0
 global snm_account1
 global snm_account2
 global snm_account3
 global snm_account4
 global snm_account5
 global snm_account6
 global snm_account0_n
 global snm_account1_n
 global snm_account2_n
 global snm_account3_n
 global snm_account4_n
 global snm_account5_n
 global snm_account6_n
 global snm_account0pw
 global snm_account1pw
 global snm_account2pw
 global snm_account3pw
 global snm_account4pw
 global snm_account5pw
 global snm_account6pw
 snm_account0 = snm_account_0_a
 snm_account1 = snm_account_1_a
 snm_account2 = snm_account_2_a
 snm_account3 = snm_account_3_a
 snm_account4 = snm_account_4_a
 snm_account5 = snm_account_5_a
 snm_account6 = snm_account_6_a
 snm_account0_n = snm_account_0_n
 snm_account1_n = snm_account_1_n
 snm_account2_n = snm_account_2_n
 snm_account3_n = snm_account_3_n
 snm_account4_n = snm_account_4_n
 snm_account5_n = snm_account_5_n
 snm_account6_n = snm_account_6_n
 snm_account0pw = snm_account_0_pw
 snm_account1pw = snm_account_1_pw
 snm_account2pw = snm_account_2_pw
 snm_account3pw = snm_account_3_pw
 snm_account4pw = snm_account_4_pw
 snm_account5pw = snm_account_5_pw
 snm_account6pw = snm_account_6_pw
 print(snm_tokenName+' Accounts Updated.')
def snm_update_balances():
 global snm_call_0
 global snm_call_1
 global snm_call_2
 global snm_call_3
 global snm_call_4
 global snm_call_5
 global snm_call_6
 global snm_w_call_0
 global snm_w_call_1
 global snm_w_call_2
 global snm_w_call_3
 global snm_w_call_4
 global snm_w_call_5
 global snm_w_call_6
 snm_update_accounts()
 print('Updating '+snm_tokenName+' Balances Please Wait...')
 snm_call_0 = snm_balanceOf(snm_account0)
 snm_call_1 = snm_balanceOf(snm_account1)
 snm_call_2 = snm_balanceOf(snm_account2)
 snm_call_3 = snm_balanceOf(snm_account3)
 snm_call_4 = snm_balanceOf(snm_account4)
 snm_call_5 = snm_balanceOf(snm_account5)
 snm_call_6 = snm_balanceOf(snm_account6)
 snm_w_call_0 = snm_balance(snm_account0)
 snm_w_call_1 = snm_balance(snm_account1)
 snm_w_call_2 = snm_balance(snm_account2)
 snm_w_call_3 = snm_balance(snm_account3)
 snm_w_call_4 = snm_balance(snm_account4)
 snm_w_call_5 = snm_balance(snm_account5)
 snm_w_call_6 = snm_balance(snm_account6)
 print(snm_tokenName+' Balances Updated.')
def snm_list_all_accounts():
 snm_update_accounts()
 print(snm_tokenName+' '+snm_account0_n+': '+snm_account0)
 print(snm_tokenName+' '+snm_account1_n+': '+snm_account1)
 print(snm_tokenName+' '+snm_account2_n+': '+snm_account2)
 print(snm_tokenName+' '+snm_account3_n+': '+snm_account3)
 print(snm_tokenName+' '+snm_account4_n+': '+snm_account4)
 print(snm_tokenName+' '+snm_account5_n+': '+snm_account5)
 print(snm_tokenName+' '+snm_account6_n+': '+snm_account6)

def snm_account_balance(accountNumber):
 snm_update_balances()
 snm_ab_account_number = accountNumber
 snm_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if snm_ab_account_number == snm_ab_input[0]:
  print('Calling '+snm_account0_n+' '+snm_tokenName+' Balance: ')
  print(snm_account0_n+': '+snm_tokenName+' Balance: '+str(snm_call_0 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_0 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[1]:
  print('Calling '+snm_account1_n+' '+snm_tokenName+' Balance: ')
  print(snm_account1_n+': '+snm_tokenName+' Balance: '+str(snm_call_1 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_1 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[2]:
  print('Calling '+snm_account2_n+' '+snm_tokenName+' Balance: ')
  print(snm_account2_n+': '+snm_tokenName+' Balance: '+str(snm_call_2 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_2 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[3]:
  print('Calling '+snm_account3_n+' '+snm_tokenName+' Balance: ')
  print(snm_account3_n+': '+snm_tokenName+' Balance: '+str(snm_call_3 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_3 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[4]:
  print('Calling '+snm_account4_n+' '+snm_tokenName+' Balance: ')
  print(snm_account4_n+': '+snm_tokenName+' Balance: '+str(snm_call_4 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_4 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[5]:
  print('Calling '+snm_account5_n+' '+snm_tokenName+' Balance: ')
  print(snm_account5_n+': '+snm_tokenName+' Balance: '+str(snm_call_5 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_5 / snm_token_d * snm_last_price))
 if snm_ab_account_number == snm_ab_input[6]:
  print('Calling '+snm_account6_n+' '+snm_tokenName+' Balance: ')
  print(snm_account6_n+': '+snm_tokenName+' Balance: '+str(snm_call_6 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_6 / snm_token_d * snm_last_price))
 if snm_ab_account_number not in snm_ab_input:
  print('Must Integer Within Range '+snm_accounts_range+'.')

def snm_list_all_account_balances():
 snm_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+snm_tokenName+' Balance: ')
 print(snm_account0_n+': '+snm_tokenName+' Balance: '+str(snm_call_0 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_0 / snm_token_d * snm_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(snm_account0_n+': Ethereum Balance '+str(snm_w_call_0 / _e_d)+' $'+str(snm_w_call_0 / _e_d * snm_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+snm_tokenName+' Balance: ')
 print(snm_account1_n+': '+snm_tokenName+' Balance: '+str(snm_call_1 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_1 / snm_token_d * snm_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(snm_account1_n+': Ethereum Balance '+str(snm_w_call_1 / _e_d)+' $'+str(snm_w_call_1 / _e_d * snm_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+snm_tokenName+' Balance: ')
 print(snm_account2_n+': '+snm_tokenName+' Balance: '+str(snm_call_2 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_2 / snm_token_d * snm_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(snm_account2_n+': Ethereum Balance '+str(snm_w_call_2 / _e_d)+' $'+str(snm_w_call_2 / _e_d * snm_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+snm_tokenName+' Balance: ')
 print(snm_account3_n+': '+snm_tokenName+' Balance: '+str(snm_call_3 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_3 / snm_token_d * snm_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(snm_account3_n+': Ethereum Balance '+str(snm_w_call_3 / _e_d)+' $'+str(snm_w_call_3 / _e_d * snm_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+snm_tokenName+' Balance: ')
 print(snm_account4_n+': '+snm_tokenName+' Balance: '+str(snm_call_4 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_4 / snm_token_d * snm_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(snm_account4_n+': Ethereum Balance '+str(snm_w_call_4 / _e_d)+' $'+str(snm_w_call_4 / _e_d * snm_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+snm_tokenName+' Balance: ')
 print(snm_account5_n+': '+snm_tokenName+' Balance: '+str(snm_call_5 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_5 / snm_token_d * snm_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(snm_account5_n+': Ethereum Balance '+str(snm_w_call_5 / _e_d)+' $'+str(snm_w_call_5 /_e_d * snm_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+snm_tokenName+' Balance: ')
 print(snm_account6_n+': '+snm_tokenName+' Balance: '+str(snm_call_6 / snm_token_d)+' Usd/'+snm_tokenName+' Balance: $'+str(snm_call_6 / snm_token_d * snm_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(snm_account6_n+': Ethereum Balance '+str(snm_w_call_6 / _e_d)+' $'+str(snm_w_call_6 / _e_d * snm_last_ethereum_price))
def snm_unlock_all_accounts():
  snm_unlock_account_0()
  snm_unlock_account_1()
  snm_unlock_account_2()
  snm_unlock_account_3()
  snm_unlock_account_4()
  snm_unlock_account_5()
  snm_unlock_account_6()


def snm_unlock_account_0():
  global snm_account0pw
  global snm_account0
  global snm_account0_n
  snm_update_accounts()
  snm_u_a_0 = snm_w_unlock(snm_account0, snm_account0pw, snm_unlockTime)
  if snm_u_a_0 == False:
    if snm_account0pw == '':
     snm_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account0_n+' Passphrase Denied: '+snm_account0pw_r)
    elif snm_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snm_account0_n+' Passphrase Denied: '+snm_account0pw)
  if snm_u_a_0 == True:
   print(snm_account0_n+' Unlocked')

def snm_unlock_account_1():
  global snm_account1pw
  global snm_account1
  global snm_account1_n
  snm_update_accounts()
  snm_u_a_1 = snm_unlock(snm_account1, snm_account1pw, snm_unlockTime)
  if snm_u_a_1 == False:
    if snm_account1pw == '':
     snm_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account1_n+' Passphrase Denied: '+snm_account1pw_r)
    elif snm_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snm_account1_n+' Passphrase Denied: '+snm_account1pw)
  if snm_u_a_1 == True:
   print(snm_account1_n+' Unlocked')

def snm_unlock_account_2():
  global snm_account2pw
  global snm_account2
  global snm_account2_n
  snm_update_accounts()
  snm_u_a_2 = snm_unlock(snm_account2, snm_account2pw, snm_unlockTime)
  if snm_u_a_2 == False:
    if snm_account2pw == '':
     snm_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account2_n+' Passphrase Denied: '+snm_account2pw_r)
    elif snm_account2pw != '':
     print('Unlock Failure With Account '+snm_account2_n+' Passphrase Denied: '+snm_account2pw)
  if snm_u_a_2 == True:
   print(snm_account2_n+' Unlocked')

def snm_unlock_account_3():
  global snm_account3pw
  global snm_account3
  global snm_account3_n
  snm_update_accounts()
  snm_u_a_3 = snm_unlock(snm_account3, snm_account3pw, snm_unlockTime)
  if snm_u_a_3 == False:
    if snm_account3pw == '':
     snm_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account3_n+' Passphrase Denied: '+snm_account3pw_r)
    elif snm_account3pw != '':
     print('Unlock Failure With Account '+snm_account3_n+' Passphrase Denied: '+snm_account3pw)
  if snm_u_a_3 == True:
   print(snm_account3_n+' Unlocked')

def snm_unlock_account_4():
  global snm_account4pw
  global snm_account4
  global snm_account4_n
  snm_update_accounts()
  snm_u_a_4 = snm_unlock(snm_account4, snm_account4pw, snm_unlockTime)
  if snm_u_a_4 == False:
    if snm_account4pw == '':
     snm_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account4_n+' Passphrase Denied: '+snm_account4pw_r)
    elif snm_account4pw != '':
     print('Unlock Failure With Account '+snm_account4_n+' Passphrase Denied: '+snm_account4pw)
  if snm_u_a_4 == True:
   print(snm_account4_n+' Unlocked')

def snm_unlock_account_5():
  global snm_account5pw
  global snm_account5
  global snm_account5_n
  snm_update_accounts()
  snm_u_a_5 = snm_unlock(snm_account5, snm_account5pw, snm_unlockTime)
  if snm_u_a_5 == False:
    if snm_account5pw == '':
     snm_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account5_n+' Passphrase Denied: '+snm_account5pw_r)
    elif snm_account5pw != '':
     print('Unlock Failure With Account '+snm_account5_n+' Passphrase Denied: '+snm_account5pw)
  if snm_u_a_5 == True:
   print(snm_account5_n+' Unlocked')

def snm_unlock_account_6():
  global snm_account6pw
  global snm_account6
  global snm_account6_n
  snm_update_accounts()
  snm_u_a_6 = snm_unlock(snm_account6, snm_account6pw, snm_unlockTime)
  if snm_u_a_6 == False:
    if snm_account6pw == '':
     snm_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snm_account6_n+' Passphrase Denied: '+snm_account6pw_r)
    elif snm_account6pw != '':
     print('Unlock Failure With Account '+snm_account6_n+' Passphrase Denied: '+snm_account6pw)
  if snm_u_a_6 == True:
   print(snm_account6_n+' Unlocked')

def snm_unlock_account(snm_ua_accountNumber):
 snm_update_accounts()
 snm_ua_account_number = snm_ua_accountNumber
 snm_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if snm_ua_account_number == snm_ua_input[0]:
  snm_unlock_account_0()
 if snm_ua_account_number == snm_ua_input[1]:
  snm_unlock_account_1()
 if snm_ua_account_number == snm_ua_input[2]:
  snm_unlock_account_2()
 if snm_ua_account_number == snm_ua_input[3]:
  snm_unlock_account_3()
 if snm_ua_account_number == snm_ua_input[4]:
  snm_unlock_account_4()
 if snm_ua_account_number == snm_ua_input[5]:
  snm_unlock_account_5()
 if snm_ua_account_number == snm_ua_input[6]:
  snm_unlock_account_6()
 if snm_ua_account_number not in snm_ua_input:
  print('Must Integer Within Range '+snm_accounts_range+'.')
 

def snm_approve_between_accounts(fromAccount, toAccount, msgValue):
  snm_update_accounts()
  snm_a_0 = snm.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(snm_a_0)

def snm_approve(fromAccountNumber, toAddress, msgValue):
  snm_update_accounts()
  snm_unlock_account(fromAccountNumber)
  snm_a_1 = snm.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(snm_a_1)

def snm_transfer_between_accounts(fromAccount, toAccount, msgValue):
  snm_update_accounts()
  snm_unlock_account(fromAccount)
  snm_t_0 = snm.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(snm_t_0)

def snm_transfer(fromAccountNumber, toAddress, msgValue):
  snm_update_accounts()
  snm_unlock_account(fromAccountNumber)
  snm_t_1 = snm.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(snm_t_1)

def snm_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  snm_update_accounts()
  snm_unlock_account(callAccount)
  snm_tf_0 = snm.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(snm_tf_0)

def snm_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  snm_update_accounts()
  snm_unlock_account(callAccount)
  snm_tf_1 = snm.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(snm_tf_1)
  


def snm_help():
  print('Following Functions For '+snm_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * snm_unlock => web3.personal.unlockAccount
/ * snm_accounts => web3.personal.listAccounts
/ * snm_balance = web3.eth.getBalance
** snm => web3.eth.contract(abi=snm_abi, address=snm_address)
** / * snm_balanceOf => snm.call().balanceOf

~ Function Listing Below:
~ snm_update_accounts()
~ snm_update_balances() \n\r -- => snm_update_accounts()
~ snm_list_all_accounts() \n\r -- => snm_update_accounts()
~ snm_account_balance(accountNumber) \n\r -- => snm_update_balances() 
~ snm_list_all_account_balances() \n\r -- => snm_update_balances()
~ snm_unlock_all_accounts() \n\r -- => snm_unlock_account_0() \n\r -- => snm_unlock_account_1() \n\r -- => snm_unlock_account_2() \n\r -- => snm_unlock_account_3() \n\r -- => snm_unlock_account_4() \n\r -- => snm_unlock_account_5() \n\r -- => snm_unlock_account_6() 
~ snm_unlock_account_0() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account0, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_1() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account1, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_2() \n\r -- => snm_update_accounts() \n\r --/ *snm_w_unlock(snm_account2, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_3() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account3, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_4() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account4, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_5() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account5, snm_account0pw, snm_unlockTime)
~ snm_unlock_account_6() \n\r -- => snm_update_accounts() \n\r -- / *snm_w_unlock(snm_account6, snm_account0pw, snm_unlockTime)
~ snm_unlock_account(snm_ua_accountNumber) \n\r -- => snm_update_accounts() \n\r -- // snm_unlock_account_0() \n\r -- // snm_unlock_account_1() \n\r -- // snm_unlock_account_2() \n\r -- // snm_unlock_account_3() \n\r -- // snm_unlock_account_4() \n\r -- // snm_unlock_account_5() \n\r -- // snm_unlock_account_6()
~ snm_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(fromAccount) \n\r -- / ** snm.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snm_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(fromAccountNumber) \n\r -- / ** snm.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snm_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(fromAccount) \n\r -- / ** snm.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ snm_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(fromAccountNumber) \n\r -- / ** snm.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snm_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(callAccount) \n\r / ** snm.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snm_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snm_update_accounts() \n\r -- => snm_unlock_account(callAccount) \n\r -- / ** snm.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ snm_help() <-- You Are Here. ''')