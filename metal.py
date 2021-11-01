#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global mtl_account_0_a
global mtl_account_1_a
global mtl_account_2_a
global mtl_account_3_a
global mtl_account_4_a
global mtl_account_5_a
global mtl_account_6_a
global mtl_address
global mtl_abi
global mtl
global mtl_call_0
global mtl_call_1
global mtl_call_2
global mtl_call_3
global mtl_call_4
global mtl_call_5
global mtl_call_6
global mtl_call_ab
global mtl_accounts
global mtl_account_0_pw
global mtl_account_1_pw
global mtl_account_2_pw
global mtl_account_3_pw
global mtl_account_4_pw
global mtl_account_5_pw
global mtl_account_6_pw
global mtl_account_0_n
global mtl_account_1_n
global mtl_account_2_n
global mtl_account_3_n
global mtl_account_4_n
global mtl_account_5_n
global mtl_account_6_n
global mtl_account1pw
global mtl_account2pw
global mtl_account3pw
global mtl_account4pw
global mtl_account5pw
global mtl_account6pw
global mtl_last_price
global mtl_accounts_range
global mtl_tokenName
global mtl_last_ethereum_price
global mtl_unlockTime
global mtl_balance
global mtl_balanceOf
global mtl_unlock
global mtl_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
mtl_token_d = 1e8
_e_d = 1e18
mtl_accounts_range = '[0, 6]'
mtl_unlock = web3.personal.unlockAccount
mtl_last_ethereum_price = 370.00
mtl_last_price = 9.30
mtl_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
mtl_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
mtl_tokenName = 'Metal Token'
mtl_unlockTime = hex(10000) # Must be hex()
mtl_account_0_a = mtl_accounts[0]
mtl_account_1_a = mtl_accounts[1]
mtl_account_2_a = mtl_accounts[2]
mtl_account_3_a = mtl_accounts[3]
mtl_account_4_a = mtl_accounts[4]
mtl_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
mtl_account_6_a = mtl_accounts[6]
# Supply Unlock Passwords For Transactions Below
mtl_account_0_pw = 'GuildSkrypt2017!@#'
mtl_account_1_pw = ''
mtl_account_2_pw = 'GuildSkrypt2017!@#'
mtl_account_3_pw = ''
mtl_account_4_pw = ''
mtl_account_5_pw = ''
mtl_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
mtl_account_0_n = 'Skotys Bittrex Account'
mtl_account_1_n = 'Jeffs Account'
mtl_account_2_n = 'Skrypts Bittrex Account'
mtl_account_3_n = 'Skotys Personal Account'
mtl_account_4_n = 'Unknown'
mtl_account_5_n = 'Watched \'Bittrex\' Account.'
mtl_account_6_n = 'Watched Account (1)'
# Contract Information Below :
mtl_address = '0xF433089366899D83a9f26A773D59ec7eCF30355e'
mtl_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"INITIAL_SUPPLY","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
mtl = web3.eth.contract(abi=mtl_abi, address=mtl_address)
mtl_balanceOf = mtl.call().balanceOf
# End Contract Information
def mtl_update_accounts():
 global mtl_account0
 global mtl_account1
 global mtl_account2
 global mtl_account3
 global mtl_account4
 global mtl_account5
 global mtl_account6
 global mtl_account0_n
 global mtl_account1_n
 global mtl_account2_n
 global mtl_account3_n
 global mtl_account4_n
 global mtl_account5_n
 global mtl_account6_n
 global mtl_account0pw
 global mtl_account1pw
 global mtl_account2pw
 global mtl_account3pw
 global mtl_account4pw
 global mtl_account5pw
 global mtl_account6pw
 mtl_account0 = mtl_account_0_a
 mtl_account1 = mtl_account_1_a
 mtl_account2 = mtl_account_2_a
 mtl_account3 = mtl_account_3_a
 mtl_account4 = mtl_account_4_a
 mtl_account5 = mtl_account_5_a
 mtl_account6 = mtl_account_6_a
 mtl_account0_n = mtl_account_0_n
 mtl_account1_n = mtl_account_1_n
 mtl_account2_n = mtl_account_2_n
 mtl_account3_n = mtl_account_3_n
 mtl_account4_n = mtl_account_4_n
 mtl_account5_n = mtl_account_5_n
 mtl_account6_n = mtl_account_6_n
 mtl_account0pw = mtl_account_0_pw
 mtl_account1pw = mtl_account_1_pw
 mtl_account2pw = mtl_account_2_pw
 mtl_account3pw = mtl_account_3_pw
 mtl_account4pw = mtl_account_4_pw
 mtl_account5pw = mtl_account_5_pw
 mtl_account6pw = mtl_account_6_pw
 print(mtl_tokenName+' Accounts Updated.')
def mtl_update_balances():
 global mtl_call_0
 global mtl_call_1
 global mtl_call_2
 global mtl_call_3
 global mtl_call_4
 global mtl_call_5
 global mtl_call_6
 global mtl_w_call_0
 global mtl_w_call_1
 global mtl_w_call_2
 global mtl_w_call_3
 global mtl_w_call_4
 global mtl_w_call_5
 global mtl_w_call_6
 mtl_update_accounts()
 print('Updating '+mtl_tokenName+' Balances Please Wait...')
 mtl_call_0 = mtl_balanceOf(mtl_account0)
 mtl_call_1 = mtl_balanceOf(mtl_account1)
 mtl_call_2 = mtl_balanceOf(mtl_account2)
 mtl_call_3 = mtl_balanceOf(mtl_account3)
 mtl_call_4 = mtl_balanceOf(mtl_account4)
 mtl_call_5 = mtl_balanceOf(mtl_account5)
 mtl_call_6 = mtl_balanceOf(mtl_account6)
 mtl_w_call_0 = mtl_balance(mtl_account0)
 mtl_w_call_1 = mtl_balance(mtl_account1)
 mtl_w_call_2 = mtl_balance(mtl_account2)
 mtl_w_call_3 = mtl_balance(mtl_account3)
 mtl_w_call_4 = mtl_balance(mtl_account4)
 mtl_w_call_5 = mtl_balance(mtl_account5)
 mtl_w_call_6 = mtl_balance(mtl_account6)
 print(mtl_tokenName+' Balances Updated.')
def mtl_list_all_accounts():
 mtl_update_accounts()
 print(mtl_tokenName+' '+mtl_account0_n+': '+mtl_account0)
 print(mtl_tokenName+' '+mtl_account1_n+': '+mtl_account1)
 print(mtl_tokenName+' '+mtl_account2_n+': '+mtl_account2)
 print(mtl_tokenName+' '+mtl_account3_n+': '+mtl_account3)
 print(mtl_tokenName+' '+mtl_account4_n+': '+mtl_account4)
 print(mtl_tokenName+' '+mtl_account5_n+': '+mtl_account5)
 print(mtl_tokenName+' '+mtl_account6_n+': '+mtl_account6)

def mtl_account_balance(accountNumber):
 mtl_update_balances()
 mtl_ab_account_number = accountNumber
 mtl_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if mtl_ab_account_number == mtl_ab_input[0]:
  print('Calling '+mtl_account0_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account0_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_0 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_0 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[1]:
  print('Calling '+mtl_account1_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account1_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_1 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_1 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[2]:
  print('Calling '+mtl_account2_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account2_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_2 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_2 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[3]:
  print('Calling '+mtl_account3_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account3_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_3 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_3 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[4]:
  print('Calling '+mtl_account4_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account4_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_4 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_4 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[5]:
  print('Calling '+mtl_account5_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account5_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_5 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_5 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number == mtl_ab_input[6]:
  print('Calling '+mtl_account6_n+' '+mtl_tokenName+' Balance: ')
  print(mtl_account6_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_6 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_6 / mtl_token_d * mtl_last_price))
 if mtl_ab_account_number not in mtl_ab_input:
  print('Must Integer Within Range '+mtl_accounts_range+'.')

def mtl_list_all_account_balances():
 mtl_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+mtl_tokenName+' Balance: ')
 print(mtl_account0_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_0 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_0 / mtl_token_d * mtl_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(mtl_account0_n+': Ethereum Balance '+str(mtl_w_call_0 / _e_d)+' $'+str(mtl_w_call_0 / _e_d * mtl_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+mtl_tokenName+' Balance: ')
 print(mtl_account1_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_1 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_1 / mtl_token_d * mtl_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(mtl_account1_n+': Ethereum Balance '+str(mtl_w_call_1 / _e_d)+' $'+str(mtl_w_call_1 / _e_d * mtl_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+mtl_tokenName+' Balance: ')
 print(mtl_account2_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_2 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_2 / mtl_token_d * mtl_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(mtl_account2_n+': Ethereum Balance '+str(mtl_w_call_2 / _e_d)+' $'+str(mtl_w_call_2 / _e_d * mtl_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+mtl_tokenName+' Balance: ')
 print(mtl_account3_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_3 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_3 / mtl_token_d * mtl_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(mtl_account3_n+': Ethereum Balance '+str(mtl_w_call_3 / _e_d)+' $'+str(mtl_w_call_3 / _e_d * mtl_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+mtl_tokenName+' Balance: ')
 print(mtl_account4_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_4 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_4 / mtl_token_d * mtl_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(mtl_account4_n+': Ethereum Balance '+str(mtl_w_call_4 / _e_d)+' $'+str(mtl_w_call_4 / _e_d * mtl_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+mtl_tokenName+' Balance: ')
 print(mtl_account5_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_5 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_5 / mtl_token_d * mtl_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(mtl_account5_n+': Ethereum Balance '+str(mtl_w_call_5 / _e_d)+' $'+str(mtl_w_call_5 /_e_d * mtl_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+mtl_tokenName+' Balance: ')
 print(mtl_account6_n+': '+mtl_tokenName+' Balance: '+str(mtl_call_6 / mtl_token_d)+' Usd/'+mtl_tokenName+' Balance: $'+str(mtl_call_6 / mtl_token_d * mtl_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(mtl_account6_n+': Ethereum Balance '+str(mtl_w_call_6 / _e_d)+' $'+str(mtl_w_call_6 / _e_d * mtl_last_ethereum_price))
def mtl_unlock_all_accounts():
  mtl_unlock_account_0()
  mtl_unlock_account_1()
  mtl_unlock_account_2()
  mtl_unlock_account_3()
  mtl_unlock_account_4()
  mtl_unlock_account_5()
  mtl_unlock_account_6()


def mtl_unlock_account_0():
  global mtl_account0pw
  global mtl_account0
  global mtl_account0_n
  mtl_update_accounts()
  mtl_u_a_0 = mtl_w_unlock(mtl_account0, mtl_account0pw, mtl_unlockTime)
  if mtl_u_a_0 == False:
    if mtl_account0pw == '':
     mtl_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account0_n+' Passphrase Denied: '+mtl_account0pw_r)
    elif mtl_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mtl_account0_n+' Passphrase Denied: '+mtl_account0pw)
  if mtl_u_a_0 == True:
   print(mtl_account0_n+' Unlocked')

def mtl_unlock_account_1():
  global mtl_account1pw
  global mtl_account1
  global mtl_account1_n
  mtl_update_accounts()
  mtl_u_a_1 = mtl_unlock(mtl_account1, mtl_account1pw, mtl_unlockTime)
  if mtl_u_a_1 == False:
    if mtl_account1pw == '':
     mtl_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account1_n+' Passphrase Denied: '+mtl_account1pw_r)
    elif mtl_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+mtl_account1_n+' Passphrase Denied: '+mtl_account1pw)
  if mtl_u_a_1 == True:
   print(mtl_account1_n+' Unlocked')

def mtl_unlock_account_2():
  global mtl_account2pw
  global mtl_account2
  global mtl_account2_n
  mtl_update_accounts()
  mtl_u_a_2 = mtl_unlock(mtl_account2, mtl_account2pw, mtl_unlockTime)
  if mtl_u_a_2 == False:
    if mtl_account2pw == '':
     mtl_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account2_n+' Passphrase Denied: '+mtl_account2pw_r)
    elif mtl_account2pw != '':
     print('Unlock Failure With Account '+mtl_account2_n+' Passphrase Denied: '+mtl_account2pw)
  if mtl_u_a_2 == True:
   print(mtl_account2_n+' Unlocked')

def mtl_unlock_account_3():
  global mtl_account3pw
  global mtl_account3
  global mtl_account3_n
  mtl_update_accounts()
  mtl_u_a_3 = mtl_unlock(mtl_account3, mtl_account3pw, mtl_unlockTime)
  if mtl_u_a_3 == False:
    if mtl_account3pw == '':
     mtl_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account3_n+' Passphrase Denied: '+mtl_account3pw_r)
    elif mtl_account3pw != '':
     print('Unlock Failure With Account '+mtl_account3_n+' Passphrase Denied: '+mtl_account3pw)
  if mtl_u_a_3 == True:
   print(mtl_account3_n+' Unlocked')

def mtl_unlock_account_4():
  global mtl_account4pw
  global mtl_account4
  global mtl_account4_n
  mtl_update_accounts()
  mtl_u_a_4 = mtl_unlock(mtl_account4, mtl_account4pw, mtl_unlockTime)
  if mtl_u_a_4 == False:
    if mtl_account4pw == '':
     mtl_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account4_n+' Passphrase Denied: '+mtl_account4pw_r)
    elif mtl_account4pw != '':
     print('Unlock Failure With Account '+mtl_account4_n+' Passphrase Denied: '+mtl_account4pw)
  if mtl_u_a_4 == True:
   print(mtl_account4_n+' Unlocked')

def mtl_unlock_account_5():
  global mtl_account5pw
  global mtl_account5
  global mtl_account5_n
  mtl_update_accounts()
  mtl_u_a_5 = mtl_unlock(mtl_account5, mtl_account5pw, mtl_unlockTime)
  if mtl_u_a_5 == False:
    if mtl_account5pw == '':
     mtl_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account5_n+' Passphrase Denied: '+mtl_account5pw_r)
    elif mtl_account5pw != '':
     print('Unlock Failure With Account '+mtl_account5_n+' Passphrase Denied: '+mtl_account5pw)
  if mtl_u_a_5 == True:
   print(mtl_account5_n+' Unlocked')

def mtl_unlock_account_6():
  global mtl_account6pw
  global mtl_account6
  global mtl_account6_n
  mtl_update_accounts()
  mtl_u_a_6 = mtl_unlock(mtl_account6, mtl_account6pw, mtl_unlockTime)
  if mtl_u_a_6 == False:
    if mtl_account6pw == '':
     mtl_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+mtl_account6_n+' Passphrase Denied: '+mtl_account6pw_r)
    elif mtl_account6pw != '':
     print('Unlock Failure With Account '+mtl_account6_n+' Passphrase Denied: '+mtl_account6pw)
  if mtl_u_a_6 == True:
   print(mtl_account6_n+' Unlocked')

def mtl_unlock_account(mtl_ua_accountNumber):
 mtl_update_accounts()
 mtl_ua_account_number = mtl_ua_accountNumber
 mtl_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if mtl_ua_account_number == mtl_ua_input[0]:
  mtl_unlock_account_0()
 if mtl_ua_account_number == mtl_ua_input[1]:
  mtl_unlock_account_1()
 if mtl_ua_account_number == mtl_ua_input[2]:
  mtl_unlock_account_2()
 if mtl_ua_account_number == mtl_ua_input[3]:
  mtl_unlock_account_3()
 if mtl_ua_account_number == mtl_ua_input[4]:
  mtl_unlock_account_4()
 if mtl_ua_account_number == mtl_ua_input[5]:
  mtl_unlock_account_5()
 if mtl_ua_account_number == mtl_ua_input[6]:
  mtl_unlock_account_6()
 if mtl_ua_account_number not in mtl_ua_input:
  print('Must Integer Within Range '+mtl_accounts_range+'.')
 

def mtl_approve_between_accounts(fromAccount, toAccount, msgValue):
  mtl_update_accounts()
  mtl_a_0 = mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(mtl_a_0)

def mtl_approve(fromAccountNumber, toAddress, msgValue):
  mtl_update_accounts()
  mtl_unlock_account(fromAccountNumber)
  mtl_a_1 = mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(mtl_a_1)

def mtl_transfer_between_accounts(fromAccount, toAccount, msgValue):
  mtl_update_accounts()
  mtl_unlock_account(fromAccount)
  mtl_t_0 = mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(mtl_t_0)

def mtl_transfer(fromAccountNumber, toAddress, msgValue):
  mtl_update_accounts()
  mtl_unlock_account(fromAccountNumber)
  mtl_t_1 = mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(mtl_t_1)

def mtl_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  mtl_update_accounts()
  mtl_unlock_account(callAccount)
  mtl_tf_0 = mtl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(mtl_tf_0)

def mtl_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  mtl_update_accounts()
  mtl_unlock_account(callAccount)
  mtl_tf_1 = mtl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(mtl_tf_1)
  


def mtl_help():
  print('Following Functions For '+mtl_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * mtl_unlock => web3.personal.unlockAccount
/ * mtl_accounts => web3.personal.listAccounts
/ * mtl_balance = web3.eth.getBalance
** mtl => web3.eth.contract(abi=mtl_abi, address=mtl_address)
** / * mtl_balanceOf => mtl.call().balanceOf

~ Function Listing Below:
~ mtl_update_accounts()
~ mtl_update_balances() \n\r -- => mtl_update_accounts()
~ mtl_list_all_accounts() \n\r -- => mtl_update_accounts()
~ mtl_account_balance(accountNumber) \n\r -- => mtl_update_balances() 
~ mtl_list_all_account_balances() \n\r -- => mtl_update_balances()
~ mtl_unlock_all_accounts() \n\r -- => mtl_unlock_account_0() \n\r -- => mtl_unlock_account_1() \n\r -- => mtl_unlock_account_2() \n\r -- => mtl_unlock_account_3() \n\r -- => mtl_unlock_account_4() \n\r -- => mtl_unlock_account_5() \n\r -- => mtl_unlock_account_6() 
~ mtl_unlock_account_0() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account0, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_1() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account1, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_2() \n\r -- => mtl_update_accounts() \n\r --/ *mtl_w_unlock(mtl_account2, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_3() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account3, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_4() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account4, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_5() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account5, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account_6() \n\r -- => mtl_update_accounts() \n\r -- / *mtl_w_unlock(mtl_account6, mtl_account0pw, mtl_unlockTime)
~ mtl_unlock_account(mtl_ua_accountNumber) \n\r -- => mtl_update_accounts() \n\r -- // mtl_unlock_account_0() \n\r -- // mtl_unlock_account_1() \n\r -- // mtl_unlock_account_2() \n\r -- // mtl_unlock_account_3() \n\r -- // mtl_unlock_account_4() \n\r -- // mtl_unlock_account_5() \n\r -- // mtl_unlock_account_6()
~ mtl_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(fromAccount) \n\r -- / ** mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mtl_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(fromAccountNumber) \n\r -- / ** mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ mtl_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(fromAccount) \n\r -- / ** mtl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ mtl_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(fromAccountNumber) \n\r -- / ** mtl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mtl_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(callAccount) \n\r / ** mtl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ mtl_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => mtl_update_accounts() \n\r -- => mtl_unlock_account(callAccount) \n\r -- / ** mtl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ mtl_help() <-- You Are Here. ''')