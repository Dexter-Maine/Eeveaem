#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global ndc_account_0_a
global ndc_account_1_a
global ndc_account_2_a
global ndc_account_3_a
global ndc_account_4_a
global ndc_account_5_a
global ndc_account_6_a
global ndc_address
global ndc_abi
global ndc
global ndc_call_0
global ndc_call_1
global ndc_call_2
global ndc_call_3
global ndc_call_4
global ndc_call_5
global ndc_call_6
global ndc_call_ab
global ndc_accounts
global ndc_account_0_pw
global ndc_account_1_pw
global ndc_account_2_pw
global ndc_account_3_pw
global ndc_account_4_pw
global ndc_account_5_pw
global ndc_account_6_pw
global ndc_account_0_n
global ndc_account_1_n
global ndc_account_2_n
global ndc_account_3_n
global ndc_account_4_n
global ndc_account_5_n
global ndc_account_6_n
global ndc_account1pw
global ndc_account2pw
global ndc_account3pw
global ndc_account4pw
global ndc_account5pw
global ndc_account6pw
global ndc_last_price
global ndc_accounts_range
global ndc_tokenName
global ndc_last_ethereum_price
global ndc_unlockTime
global ndc_balance
global ndc_balanceOf
global ndc_unlock
global ndc_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
ndc_token_d = 1e18
_e_d = 1e18
ndc_accounts_range = '[0, 6]'
ndc_unlock = web3.personal.unlockAccount
ndc_last_ethereum_price = 370.00
ndc_last_price = 0.19
ndc_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
ndc_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
ndc_tokenName = 'NeverDie Token'
ndc_unlockTime = hex(10000) # Must be hex()
ndc_account_0_a = ndc_accounts[0]
ndc_account_1_a = ndc_accounts[1]
ndc_account_2_a = ndc_accounts[2]
ndc_account_3_a = ndc_accounts[3]
ndc_account_4_a = ndc_accounts[4]
ndc_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
ndc_account_6_a = ndc_accounts[6]
# Supply Unlock Passwords For Transactions Below
ndc_account_0_pw = 'GuildSkrypt2017!@#'
ndc_account_1_pw = ''
ndc_account_2_pw = 'GuildSkrypt2017!@#'
ndc_account_3_pw = ''
ndc_account_4_pw = ''
ndc_account_5_pw = ''
ndc_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
ndc_account_0_n = 'Skotys Bittrex Account'
ndc_account_1_n = 'Jeffs Account'
ndc_account_2_n = 'Skrypts Bittrex Account'
ndc_account_3_n = 'Skotys Personal Account'
ndc_account_4_n = 'Unknown'
ndc_account_5_n = 'Watched \'Bittrex\' Account.'
ndc_account_6_n = 'Watched Account (1)'
# Contract Information Below :
ndc_address = '0xA54ddC7B3CcE7FC8b1E3Fa0256D0DB80D2c10970'
ndc_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"inputs":[{"name":"_initialAmount","type":"uint256"},{"name":"_tokenName","type":"string"},{"name":"_decimalUnits","type":"uint8"},{"name":"_tokenSymbol","type":"string"}],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
ndc = web3.eth.contract(abi=ndc_abi, address=ndc_address)
ndc_balanceOf = ndc.call().balanceOf
# End Contract Information
def ndc_update_accounts():
 global ndc_account0
 global ndc_account1
 global ndc_account2
 global ndc_account3
 global ndc_account4
 global ndc_account5
 global ndc_account6
 global ndc_account0_n
 global ndc_account1_n
 global ndc_account2_n
 global ndc_account3_n
 global ndc_account4_n
 global ndc_account5_n
 global ndc_account6_n
 global ndc_account0pw
 global ndc_account1pw
 global ndc_account2pw
 global ndc_account3pw
 global ndc_account4pw
 global ndc_account5pw
 global ndc_account6pw
 ndc_account0 = ndc_account_0_a
 ndc_account1 = ndc_account_1_a
 ndc_account2 = ndc_account_2_a
 ndc_account3 = ndc_account_3_a
 ndc_account4 = ndc_account_4_a
 ndc_account5 = ndc_account_5_a
 ndc_account6 = ndc_account_6_a
 ndc_account0_n = ndc_account_0_n
 ndc_account1_n = ndc_account_1_n
 ndc_account2_n = ndc_account_2_n
 ndc_account3_n = ndc_account_3_n
 ndc_account4_n = ndc_account_4_n
 ndc_account5_n = ndc_account_5_n
 ndc_account6_n = ndc_account_6_n
 ndc_account0pw = ndc_account_0_pw
 ndc_account1pw = ndc_account_1_pw
 ndc_account2pw = ndc_account_2_pw
 ndc_account3pw = ndc_account_3_pw
 ndc_account4pw = ndc_account_4_pw
 ndc_account5pw = ndc_account_5_pw
 ndc_account6pw = ndc_account_6_pw
 print(ndc_tokenName+' Accounts Updated.')
def ndc_update_balances():
 global ndc_call_0
 global ndc_call_1
 global ndc_call_2
 global ndc_call_3
 global ndc_call_4
 global ndc_call_5
 global ndc_call_6
 global ndc_w_call_0
 global ndc_w_call_1
 global ndc_w_call_2
 global ndc_w_call_3
 global ndc_w_call_4
 global ndc_w_call_5
 global ndc_w_call_6
 ndc_update_accounts()
 print('Updating '+ndc_tokenName+' Balances Please Wait...')
 ndc_call_0 = ndc_balanceOf(ndc_account0)
 ndc_call_1 = ndc_balanceOf(ndc_account1)
 ndc_call_2 = ndc_balanceOf(ndc_account2)
 ndc_call_3 = ndc_balanceOf(ndc_account3)
 ndc_call_4 = ndc_balanceOf(ndc_account4)
 ndc_call_5 = ndc_balanceOf(ndc_account5)
 ndc_call_6 = ndc_balanceOf(ndc_account6)
 ndc_w_call_0 = ndc_balance(ndc_account0)
 ndc_w_call_1 = ndc_balance(ndc_account1)
 ndc_w_call_2 = ndc_balance(ndc_account2)
 ndc_w_call_3 = ndc_balance(ndc_account3)
 ndc_w_call_4 = ndc_balance(ndc_account4)
 ndc_w_call_5 = ndc_balance(ndc_account5)
 ndc_w_call_6 = ndc_balance(ndc_account6)
 print(ndc_tokenName+' Balances Updated.')
def ndc_list_all_accounts():
 ndc_update_accounts()
 print(ndc_tokenName+' '+ndc_account0_n+': '+ndc_account0)
 print(ndc_tokenName+' '+ndc_account1_n+': '+ndc_account1)
 print(ndc_tokenName+' '+ndc_account2_n+': '+ndc_account2)
 print(ndc_tokenName+' '+ndc_account3_n+': '+ndc_account3)
 print(ndc_tokenName+' '+ndc_account4_n+': '+ndc_account4)
 print(ndc_tokenName+' '+ndc_account5_n+': '+ndc_account5)
 print(ndc_tokenName+' '+ndc_account6_n+': '+ndc_account6)

def ndc_account_balance(accountNumber):
 ndc_update_balances()
 ndc_ab_account_number = accountNumber
 ndc_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if ndc_ab_account_number == ndc_ab_input[0]:
  print('Calling '+ndc_account0_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account0_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_0 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_0 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[1]:
  print('Calling '+ndc_account1_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account1_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_1 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_1 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[2]:
  print('Calling '+ndc_account2_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account2_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_2 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_2 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[3]:
  print('Calling '+ndc_account3_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account3_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_3 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_3 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[4]:
  print('Calling '+ndc_account4_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account4_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_4 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_4 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[5]:
  print('Calling '+ndc_account5_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account5_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_5 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_5 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number == ndc_ab_input[6]:
  print('Calling '+ndc_account6_n+' '+ndc_tokenName+' Balance: ')
  print(ndc_account6_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_6 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_6 / ndc_token_d * ndc_last_price))
 if ndc_ab_account_number not in ndc_ab_input:
  print('Must Integer Within Range '+ndc_accounts_range+'.')

def ndc_list_all_account_balances():
 ndc_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+ndc_tokenName+' Balance: ')
 print(ndc_account0_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_0 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_0 / ndc_token_d * ndc_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(ndc_account0_n+': Ethereum Balance '+str(ndc_w_call_0 / _e_d)+' $'+str(ndc_w_call_0 / _e_d * ndc_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+ndc_tokenName+' Balance: ')
 print(ndc_account1_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_1 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_1 / ndc_token_d * ndc_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(ndc_account1_n+': Ethereum Balance '+str(ndc_w_call_1 / _e_d)+' $'+str(ndc_w_call_1 / _e_d * ndc_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+ndc_tokenName+' Balance: ')
 print(ndc_account2_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_2 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_2 / ndc_token_d * ndc_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(ndc_account2_n+': Ethereum Balance '+str(ndc_w_call_2 / _e_d)+' $'+str(ndc_w_call_2 / _e_d * ndc_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+ndc_tokenName+' Balance: ')
 print(ndc_account3_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_3 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_3 / ndc_token_d * ndc_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(ndc_account3_n+': Ethereum Balance '+str(ndc_w_call_3 / _e_d)+' $'+str(ndc_w_call_3 / _e_d * ndc_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+ndc_tokenName+' Balance: ')
 print(ndc_account4_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_4 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_4 / ndc_token_d * ndc_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(ndc_account4_n+': Ethereum Balance '+str(ndc_w_call_4 / _e_d)+' $'+str(ndc_w_call_4 / _e_d * ndc_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+ndc_tokenName+' Balance: ')
 print(ndc_account5_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_5 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_5 / ndc_token_d * ndc_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(ndc_account5_n+': Ethereum Balance '+str(ndc_w_call_5 / _e_d)+' $'+str(ndc_w_call_5 /_e_d * ndc_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+ndc_tokenName+' Balance: ')
 print(ndc_account6_n+': '+ndc_tokenName+' Balance: '+str(ndc_call_6 / ndc_token_d)+' Usd/'+ndc_tokenName+' Balance: $'+str(ndc_call_6 / ndc_token_d * ndc_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(ndc_account6_n+': Ethereum Balance '+str(ndc_w_call_6 / _e_d)+' $'+str(ndc_w_call_6 / _e_d * ndc_last_ethereum_price))
def ndc_unlock_all_accounts():
  ndc_unlock_account_0()
  ndc_unlock_account_1()
  ndc_unlock_account_2()
  ndc_unlock_account_3()
  ndc_unlock_account_4()
  ndc_unlock_account_5()
  ndc_unlock_account_6()


def ndc_unlock_account_0():
  global ndc_account0pw
  global ndc_account0
  global ndc_account0_n
  ndc_update_accounts()
  ndc_u_a_0 = ndc_w_unlock(ndc_account0, ndc_account0pw, ndc_unlockTime)
  if ndc_u_a_0 == False:
    if ndc_account0pw == '':
     ndc_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account0_n+' Passphrase Denied: '+ndc_account0pw_r)
    elif ndc_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ndc_account0_n+' Passphrase Denied: '+ndc_account0pw)
  if ndc_u_a_0 == True:
   print(ndc_account0_n+' Unlocked')

def ndc_unlock_account_1():
  global ndc_account1pw
  global ndc_account1
  global ndc_account1_n
  ndc_update_accounts()
  ndc_u_a_1 = ndc_unlock(ndc_account1, ndc_account1pw, ndc_unlockTime)
  if ndc_u_a_1 == False:
    if ndc_account1pw == '':
     ndc_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account1_n+' Passphrase Denied: '+ndc_account1pw_r)
    elif ndc_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ndc_account1_n+' Passphrase Denied: '+ndc_account1pw)
  if ndc_u_a_1 == True:
   print(ndc_account1_n+' Unlocked')

def ndc_unlock_account_2():
  global ndc_account2pw
  global ndc_account2
  global ndc_account2_n
  ndc_update_accounts()
  ndc_u_a_2 = ndc_unlock(ndc_account2, ndc_account2pw, ndc_unlockTime)
  if ndc_u_a_2 == False:
    if ndc_account2pw == '':
     ndc_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account2_n+' Passphrase Denied: '+ndc_account2pw_r)
    elif ndc_account2pw != '':
     print('Unlock Failure With Account '+ndc_account2_n+' Passphrase Denied: '+ndc_account2pw)
  if ndc_u_a_2 == True:
   print(ndc_account2_n+' Unlocked')

def ndc_unlock_account_3():
  global ndc_account3pw
  global ndc_account3
  global ndc_account3_n
  ndc_update_accounts()
  ndc_u_a_3 = ndc_unlock(ndc_account3, ndc_account3pw, ndc_unlockTime)
  if ndc_u_a_3 == False:
    if ndc_account3pw == '':
     ndc_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account3_n+' Passphrase Denied: '+ndc_account3pw_r)
    elif ndc_account3pw != '':
     print('Unlock Failure With Account '+ndc_account3_n+' Passphrase Denied: '+ndc_account3pw)
  if ndc_u_a_3 == True:
   print(ndc_account3_n+' Unlocked')

def ndc_unlock_account_4():
  global ndc_account4pw
  global ndc_account4
  global ndc_account4_n
  ndc_update_accounts()
  ndc_u_a_4 = ndc_unlock(ndc_account4, ndc_account4pw, ndc_unlockTime)
  if ndc_u_a_4 == False:
    if ndc_account4pw == '':
     ndc_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account4_n+' Passphrase Denied: '+ndc_account4pw_r)
    elif ndc_account4pw != '':
     print('Unlock Failure With Account '+ndc_account4_n+' Passphrase Denied: '+ndc_account4pw)
  if ndc_u_a_4 == True:
   print(ndc_account4_n+' Unlocked')

def ndc_unlock_account_5():
  global ndc_account5pw
  global ndc_account5
  global ndc_account5_n
  ndc_update_accounts()
  ndc_u_a_5 = ndc_unlock(ndc_account5, ndc_account5pw, ndc_unlockTime)
  if ndc_u_a_5 == False:
    if ndc_account5pw == '':
     ndc_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account5_n+' Passphrase Denied: '+ndc_account5pw_r)
    elif ndc_account5pw != '':
     print('Unlock Failure With Account '+ndc_account5_n+' Passphrase Denied: '+ndc_account5pw)
  if ndc_u_a_5 == True:
   print(ndc_account5_n+' Unlocked')

def ndc_unlock_account_6():
  global ndc_account6pw
  global ndc_account6
  global ndc_account6_n
  ndc_update_accounts()
  ndc_u_a_6 = ndc_unlock(ndc_account6, ndc_account6pw, ndc_unlockTime)
  if ndc_u_a_6 == False:
    if ndc_account6pw == '':
     ndc_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ndc_account6_n+' Passphrase Denied: '+ndc_account6pw_r)
    elif ndc_account6pw != '':
     print('Unlock Failure With Account '+ndc_account6_n+' Passphrase Denied: '+ndc_account6pw)
  if ndc_u_a_6 == True:
   print(ndc_account6_n+' Unlocked')

def ndc_unlock_account(ndc_ua_accountNumber):
 ndc_update_accounts()
 ndc_ua_account_number = ndc_ua_accountNumber
 ndc_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if ndc_ua_account_number == ndc_ua_input[0]:
  ndc_unlock_account_0()
 if ndc_ua_account_number == ndc_ua_input[1]:
  ndc_unlock_account_1()
 if ndc_ua_account_number == ndc_ua_input[2]:
  ndc_unlock_account_2()
 if ndc_ua_account_number == ndc_ua_input[3]:
  ndc_unlock_account_3()
 if ndc_ua_account_number == ndc_ua_input[4]:
  ndc_unlock_account_4()
 if ndc_ua_account_number == ndc_ua_input[5]:
  ndc_unlock_account_5()
 if ndc_ua_account_number == ndc_ua_input[6]:
  ndc_unlock_account_6()
 if ndc_ua_account_number not in ndc_ua_input:
  print('Must Integer Within Range '+ndc_accounts_range+'.')
 

def ndc_approve_between_accounts(fromAccount, toAccount, msgValue):
  ndc_update_accounts()
  ndc_a_0 = ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(ndc_a_0)

def ndc_approve(fromAccountNumber, toAddress, msgValue):
  ndc_update_accounts()
  ndc_unlock_account(fromAccountNumber)
  ndc_a_1 = ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(ndc_a_1)

def ndc_transfer_between_accounts(fromAccount, toAccount, msgValue):
  ndc_update_accounts()
  ndc_unlock_account(fromAccount)
  ndc_t_0 = ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(ndc_t_0)

def ndc_transfer(fromAccountNumber, toAddress, msgValue):
  ndc_update_accounts()
  ndc_unlock_account(fromAccountNumber)
  ndc_t_1 = ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(ndc_t_1)

def ndc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  ndc_update_accounts()
  ndc_unlock_account(callAccount)
  ndc_tf_0 = ndc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(ndc_tf_0)

def ndc_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  ndc_update_accounts()
  ndc_unlock_account(callAccount)
  ndc_tf_1 = ndc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(ndc_tf_1)
  


def ndc_help():
  print('Following Functions For '+ndc_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * ndc_unlock => web3.personal.unlockAccount
/ * ndc_accounts => web3.personal.listAccounts
/ * ndc_balance = web3.eth.getBalance
** ndc => web3.eth.contract(abi=ndc_abi, address=ndc_address)
** / * ndc_balanceOf => ndc.call().balanceOf

~ Function Listing Below:
~ ndc_update_accounts()
~ ndc_update_balances() \n\r -- => ndc_update_accounts()
~ ndc_list_all_accounts() \n\r -- => ndc_update_accounts()
~ ndc_account_balance(accountNumber) \n\r -- => ndc_update_balances() 
~ ndc_list_all_account_balances() \n\r -- => ndc_update_balances()
~ ndc_unlock_all_accounts() \n\r -- => ndc_unlock_account_0() \n\r -- => ndc_unlock_account_1() \n\r -- => ndc_unlock_account_2() \n\r -- => ndc_unlock_account_3() \n\r -- => ndc_unlock_account_4() \n\r -- => ndc_unlock_account_5() \n\r -- => ndc_unlock_account_6() 
~ ndc_unlock_account_0() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account0, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_1() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account1, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_2() \n\r -- => ndc_update_accounts() \n\r --/ *ndc_w_unlock(ndc_account2, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_3() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account3, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_4() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account4, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_5() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account5, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account_6() \n\r -- => ndc_update_accounts() \n\r -- / *ndc_w_unlock(ndc_account6, ndc_account0pw, ndc_unlockTime)
~ ndc_unlock_account(ndc_ua_accountNumber) \n\r -- => ndc_update_accounts() \n\r -- // ndc_unlock_account_0() \n\r -- // ndc_unlock_account_1() \n\r -- // ndc_unlock_account_2() \n\r -- // ndc_unlock_account_3() \n\r -- // ndc_unlock_account_4() \n\r -- // ndc_unlock_account_5() \n\r -- // ndc_unlock_account_6()
~ ndc_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(fromAccount) \n\r -- / ** ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ndc_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(fromAccountNumber) \n\r -- / ** ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ndc_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(fromAccount) \n\r -- / ** ndc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ ndc_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(fromAccountNumber) \n\r -- / ** ndc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ndc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(callAccount) \n\r / ** ndc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ndc_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ndc_update_accounts() \n\r -- => ndc_unlock_account(callAccount) \n\r -- / ** ndc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ ndc_help() <-- You Are Here. ''')