#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global qtum_account_0_a
global qtum_account_1_a
global qtum_account_2_a
global qtum_account_3_a
global qtum_account_4_a
global qtum_account_5_a
global qtum_account_6_a
global qtum_address
global qtum_abi
global qtum
global qtum_call_0
global qtum_call_1
global qtum_call_2
global qtum_call_3
global qtum_call_4
global qtum_call_5
global qtum_call_6
global qtum_call_ab
global qtum_accounts
global qtum_account_0_pw
global qtum_account_1_pw
global qtum_account_2_pw
global qtum_account_3_pw
global qtum_account_4_pw
global qtum_account_5_pw
global qtum_account_6_pw
global qtum_account_0_n
global qtum_account_1_n
global qtum_account_2_n
global qtum_account_3_n
global qtum_account_4_n
global qtum_account_5_n
global qtum_account_6_n
global qtum_account1pw
global qtum_account2pw
global qtum_account3pw
global qtum_account4pw
global qtum_account5pw
global qtum_account6pw
global qtum_last_price
global qtum_accounts_range
global qtum_tokenName
global qtum_last_ethereum_price
global qtum_unlockTime
global qtum_balance
global qtum_balanceOf
global qtum_unlock
global qtum_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
qtum_token_d = 1e18
_e_d = 1e18
qtum_accounts_range = '[0, 6]'
qtum_unlock = web3.personal.unlockAccount
qtum_last_ethereum_price = 370.00
qtum_last_price = 16.90
qtum_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
qtum_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
qtum_tokenName = 'Qtum Token'
qtum_unlockTime = hex(10000) # Must be hex()
qtum_account_0_a = qtum_accounts[0]
qtum_account_1_a = qtum_accounts[1]
qtum_account_2_a = qtum_accounts[2]
qtum_account_3_a = qtum_accounts[3]
qtum_account_4_a = qtum_accounts[4]
qtum_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
qtum_account_6_a = qtum_accounts[6]
# Supply Unlock Passwords For Transactions Below
qtum_account_0_pw = 'GuildSkrypt2017!@#'
qtum_account_1_pw = ''
qtum_account_2_pw = 'GuildSkrypt2017!@#'
qtum_account_3_pw = ''
qtum_account_4_pw = ''
qtum_account_5_pw = ''
qtum_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
qtum_account_0_n = 'Skotys Bittrex Account'
qtum_account_1_n = 'Jeffs Account'
qtum_account_2_n = 'Skrypts Bittrex Account'
qtum_account_3_n = 'Skotys Personal Account'
qtum_account_4_n = 'Unknown'
qtum_account_5_n = 'Watched \'Bittrex\' Account.'
qtum_account_6_n = 'Watched Account (1)'
# Contract Information Below :
qtum_address = '0x9a642d6b3368ddc662CA244bAdf32cDA716005BC'
qtum_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"_initialAmount","type":"uint256"},{"name":"_tokenName","type":"string"},{"name":"_decimalUnits","type":"uint8"},{"name":"_tokenSymbol","type":"string"}],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
qtum = web3.eth.contract(abi=qtum_abi, address=qtum_address)
qtum_balanceOf = qtum.call().balanceOf
# End Contract Information
def qtum_update_accounts():
 global qtum_account0
 global qtum_account1
 global qtum_account2
 global qtum_account3
 global qtum_account4
 global qtum_account5
 global qtum_account6
 global qtum_account0_n
 global qtum_account1_n
 global qtum_account2_n
 global qtum_account3_n
 global qtum_account4_n
 global qtum_account5_n
 global qtum_account6_n
 global qtum_account0pw
 global qtum_account1pw
 global qtum_account2pw
 global qtum_account3pw
 global qtum_account4pw
 global qtum_account5pw
 global qtum_account6pw
 qtum_account0 = qtum_account_0_a
 qtum_account1 = qtum_account_1_a
 qtum_account2 = qtum_account_2_a
 qtum_account3 = qtum_account_3_a
 qtum_account4 = qtum_account_4_a
 qtum_account5 = qtum_account_5_a
 qtum_account6 = qtum_account_6_a
 qtum_account0_n = qtum_account_0_n
 qtum_account1_n = qtum_account_1_n
 qtum_account2_n = qtum_account_2_n
 qtum_account3_n = qtum_account_3_n
 qtum_account4_n = qtum_account_4_n
 qtum_account5_n = qtum_account_5_n
 qtum_account6_n = qtum_account_6_n
 qtum_account0pw = qtum_account_0_pw
 qtum_account1pw = qtum_account_1_pw
 qtum_account2pw = qtum_account_2_pw
 qtum_account3pw = qtum_account_3_pw
 qtum_account4pw = qtum_account_4_pw
 qtum_account5pw = qtum_account_5_pw
 qtum_account6pw = qtum_account_6_pw
 print(qtum_tokenName+' Accounts Updated.')
def qtum_update_balances():
 global qtum_call_0
 global qtum_call_1
 global qtum_call_2
 global qtum_call_3
 global qtum_call_4
 global qtum_call_5
 global qtum_call_6
 global qtum_w_call_0
 global qtum_w_call_1
 global qtum_w_call_2
 global qtum_w_call_3
 global qtum_w_call_4
 global qtum_w_call_5
 global qtum_w_call_6
 qtum_update_accounts()
 print('Updating '+qtum_tokenName+' Balances Please Wait...')
 qtum_call_0 = qtum_balanceOf(qtum_account0)
 qtum_call_1 = qtum_balanceOf(qtum_account1)
 qtum_call_2 = qtum_balanceOf(qtum_account2)
 qtum_call_3 = qtum_balanceOf(qtum_account3)
 qtum_call_4 = qtum_balanceOf(qtum_account4)
 qtum_call_5 = qtum_balanceOf(qtum_account5)
 qtum_call_6 = qtum_balanceOf(qtum_account6)
 qtum_w_call_0 = qtum_balance(qtum_account0)
 qtum_w_call_1 = qtum_balance(qtum_account1)
 qtum_w_call_2 = qtum_balance(qtum_account2)
 qtum_w_call_3 = qtum_balance(qtum_account3)
 qtum_w_call_4 = qtum_balance(qtum_account4)
 qtum_w_call_5 = qtum_balance(qtum_account5)
 qtum_w_call_6 = qtum_balance(qtum_account6)
 print(qtum_tokenName+' Balances Updated.')
def qtum_list_all_accounts():
 qtum_update_accounts()
 print(qtum_tokenName+' '+qtum_account0_n+': '+qtum_account0)
 print(qtum_tokenName+' '+qtum_account1_n+': '+qtum_account1)
 print(qtum_tokenName+' '+qtum_account2_n+': '+qtum_account2)
 print(qtum_tokenName+' '+qtum_account3_n+': '+qtum_account3)
 print(qtum_tokenName+' '+qtum_account4_n+': '+qtum_account4)
 print(qtum_tokenName+' '+qtum_account5_n+': '+qtum_account5)
 print(qtum_tokenName+' '+qtum_account6_n+': '+qtum_account6)

def qtum_account_balance(accountNumber):
 qtum_update_balances()
 qtum_ab_account_number = accountNumber
 qtum_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if qtum_ab_account_number == qtum_ab_input[0]:
  print('Calling '+qtum_account0_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account0_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_0 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_0 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[1]:
  print('Calling '+qtum_account1_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account1_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_1 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_1 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[2]:
  print('Calling '+qtum_account2_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account2_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_2 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_2 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[3]:
  print('Calling '+qtum_account3_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account3_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_3 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_3 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[4]:
  print('Calling '+qtum_account4_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account4_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_4 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_4 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[5]:
  print('Calling '+qtum_account5_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account5_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_5 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_5 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number == qtum_ab_input[6]:
  print('Calling '+qtum_account6_n+' '+qtum_tokenName+' Balance: ')
  print(qtum_account6_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_6 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_6 / qtum_token_d * qtum_last_price))
 if qtum_ab_account_number not in qtum_ab_input:
  print('Must Integer Within Range '+qtum_accounts_range+'.')

def qtum_list_all_account_balances():
 qtum_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+qtum_tokenName+' Balance: ')
 print(qtum_account0_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_0 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_0 / qtum_token_d * qtum_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(qtum_account0_n+': Ethereum Balance '+str(qtum_w_call_0 / _e_d)+' $'+str(qtum_w_call_0 / _e_d * qtum_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+qtum_tokenName+' Balance: ')
 print(qtum_account1_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_1 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_1 / qtum_token_d * qtum_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(qtum_account1_n+': Ethereum Balance '+str(qtum_w_call_1 / _e_d)+' $'+str(qtum_w_call_1 / _e_d * qtum_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+qtum_tokenName+' Balance: ')
 print(qtum_account2_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_2 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_2 / qtum_token_d * qtum_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(qtum_account2_n+': Ethereum Balance '+str(qtum_w_call_2 / _e_d)+' $'+str(qtum_w_call_2 / _e_d * qtum_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+qtum_tokenName+' Balance: ')
 print(qtum_account3_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_3 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_3 / qtum_token_d * qtum_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(qtum_account3_n+': Ethereum Balance '+str(qtum_w_call_3 / _e_d)+' $'+str(qtum_w_call_3 / _e_d * qtum_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+qtum_tokenName+' Balance: ')
 print(qtum_account4_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_4 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_4 / qtum_token_d * qtum_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(qtum_account4_n+': Ethereum Balance '+str(qtum_w_call_4 / _e_d)+' $'+str(qtum_w_call_4 / _e_d * qtum_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+qtum_tokenName+' Balance: ')
 print(qtum_account5_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_5 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_5 / qtum_token_d * qtum_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(qtum_account5_n+': Ethereum Balance '+str(qtum_w_call_5 / _e_d)+' $'+str(qtum_w_call_5 /_e_d * qtum_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+qtum_tokenName+' Balance: ')
 print(qtum_account6_n+': '+qtum_tokenName+' Balance: '+str(qtum_call_6 / qtum_token_d)+' Usd/'+qtum_tokenName+' Balance: $'+str(qtum_call_6 / qtum_token_d * qtum_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(qtum_account6_n+': Ethereum Balance '+str(qtum_w_call_6 / _e_d)+' $'+str(qtum_w_call_6 / _e_d * qtum_last_ethereum_price))
def qtum_unlock_all_accounts():
  qtum_unlock_account_0()
  qtum_unlock_account_1()
  qtum_unlock_account_2()
  qtum_unlock_account_3()
  qtum_unlock_account_4()
  qtum_unlock_account_5()
  qtum_unlock_account_6()


def qtum_unlock_account_0():
  global qtum_account0pw
  global qtum_account0
  global qtum_account0_n
  qtum_update_accounts()
  qtum_u_a_0 = qtum_w_unlock(qtum_account0, qtum_account0pw, qtum_unlockTime)
  if qtum_u_a_0 == False:
    if qtum_account0pw == '':
     qtum_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account0_n+' Passphrase Denied: '+qtum_account0pw_r)
    elif qtum_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+qtum_account0_n+' Passphrase Denied: '+qtum_account0pw)
  if qtum_u_a_0 == True:
   print(qtum_account0_n+' Unlocked')

def qtum_unlock_account_1():
  global qtum_account1pw
  global qtum_account1
  global qtum_account1_n
  qtum_update_accounts()
  qtum_u_a_1 = qtum_unlock(qtum_account1, qtum_account1pw, qtum_unlockTime)
  if qtum_u_a_1 == False:
    if qtum_account1pw == '':
     qtum_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account1_n+' Passphrase Denied: '+qtum_account1pw_r)
    elif qtum_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+qtum_account1_n+' Passphrase Denied: '+qtum_account1pw)
  if qtum_u_a_1 == True:
   print(qtum_account1_n+' Unlocked')

def qtum_unlock_account_2():
  global qtum_account2pw
  global qtum_account2
  global qtum_account2_n
  qtum_update_accounts()
  qtum_u_a_2 = qtum_unlock(qtum_account2, qtum_account2pw, qtum_unlockTime)
  if qtum_u_a_2 == False:
    if qtum_account2pw == '':
     qtum_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account2_n+' Passphrase Denied: '+qtum_account2pw_r)
    elif qtum_account2pw != '':
     print('Unlock Failure With Account '+qtum_account2_n+' Passphrase Denied: '+qtum_account2pw)
  if qtum_u_a_2 == True:
   print(qtum_account2_n+' Unlocked')

def qtum_unlock_account_3():
  global qtum_account3pw
  global qtum_account3
  global qtum_account3_n
  qtum_update_accounts()
  qtum_u_a_3 = qtum_unlock(qtum_account3, qtum_account3pw, qtum_unlockTime)
  if qtum_u_a_3 == False:
    if qtum_account3pw == '':
     qtum_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account3_n+' Passphrase Denied: '+qtum_account3pw_r)
    elif qtum_account3pw != '':
     print('Unlock Failure With Account '+qtum_account3_n+' Passphrase Denied: '+qtum_account3pw)
  if qtum_u_a_3 == True:
   print(qtum_account3_n+' Unlocked')

def qtum_unlock_account_4():
  global qtum_account4pw
  global qtum_account4
  global qtum_account4_n
  qtum_update_accounts()
  qtum_u_a_4 = qtum_unlock(qtum_account4, qtum_account4pw, qtum_unlockTime)
  if qtum_u_a_4 == False:
    if qtum_account4pw == '':
     qtum_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account4_n+' Passphrase Denied: '+qtum_account4pw_r)
    elif qtum_account4pw != '':
     print('Unlock Failure With Account '+qtum_account4_n+' Passphrase Denied: '+qtum_account4pw)
  if qtum_u_a_4 == True:
   print(qtum_account4_n+' Unlocked')

def qtum_unlock_account_5():
  global qtum_account5pw
  global qtum_account5
  global qtum_account5_n
  qtum_update_accounts()
  qtum_u_a_5 = qtum_unlock(qtum_account5, qtum_account5pw, qtum_unlockTime)
  if qtum_u_a_5 == False:
    if qtum_account5pw == '':
     qtum_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account5_n+' Passphrase Denied: '+qtum_account5pw_r)
    elif qtum_account5pw != '':
     print('Unlock Failure With Account '+qtum_account5_n+' Passphrase Denied: '+qtum_account5pw)
  if qtum_u_a_5 == True:
   print(qtum_account5_n+' Unlocked')

def qtum_unlock_account_6():
  global qtum_account6pw
  global qtum_account6
  global qtum_account6_n
  qtum_update_accounts()
  qtum_u_a_6 = qtum_unlock(qtum_account6, qtum_account6pw, qtum_unlockTime)
  if qtum_u_a_6 == False:
    if qtum_account6pw == '':
     qtum_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qtum_account6_n+' Passphrase Denied: '+qtum_account6pw_r)
    elif qtum_account6pw != '':
     print('Unlock Failure With Account '+qtum_account6_n+' Passphrase Denied: '+qtum_account6pw)
  if qtum_u_a_6 == True:
   print(qtum_account6_n+' Unlocked')

def qtum_unlock_account(qtum_ua_accountNumber):
 qtum_update_accounts()
 qtum_ua_account_number = qtum_ua_accountNumber
 qtum_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if qtum_ua_account_number == qtum_ua_input[0]:
  qtum_unlock_account_0()
 if qtum_ua_account_number == qtum_ua_input[1]:
  qtum_unlock_account_1()
 if qtum_ua_account_number == qtum_ua_input[2]:
  qtum_unlock_account_2()
 if qtum_ua_account_number == qtum_ua_input[3]:
  qtum_unlock_account_3()
 if qtum_ua_account_number == qtum_ua_input[4]:
  qtum_unlock_account_4()
 if qtum_ua_account_number == qtum_ua_input[5]:
  qtum_unlock_account_5()
 if qtum_ua_account_number == qtum_ua_input[6]:
  qtum_unlock_account_6()
 if qtum_ua_account_number not in qtum_ua_input:
  print('Must Integer Within Range '+qtum_accounts_range+'.')
 

def qtum_approve_between_accounts(fromAccount, toAccount, msgValue):
  qtum_update_accounts()
  qtum_a_0 = qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(qtum_a_0)

def qtum_approve(fromAccountNumber, toAddress, msgValue):
  qtum_update_accounts()
  qtum_unlock_account(fromAccountNumber)
  qtum_a_1 = qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(qtum_a_1)

def qtum_transfer_between_accounts(fromAccount, toAccount, msgValue):
  qtum_update_accounts()
  qtum_unlock_account(fromAccount)
  qtum_t_0 = qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(qtum_t_0)

def qtum_transfer(fromAccountNumber, toAddress, msgValue):
  qtum_update_accounts()
  qtum_unlock_account(fromAccountNumber)
  qtum_t_1 = qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(qtum_t_1)

def qtum_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  qtum_update_accounts()
  qtum_unlock_account(callAccount)
  qtum_tf_0 = qtum.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(qtum_tf_0)

def qtum_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  qtum_update_accounts()
  qtum_unlock_account(callAccount)
  qtum_tf_1 = qtum.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(qtum_tf_1)
  


def qtum_help():
  print('Following Functions For '+qtum_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * qtum_unlock => web3.personal.unlockAccount
/ * qtum_accounts => web3.personal.listAccounts
/ * qtum_balance = web3.eth.getBalance
** qtum => web3.eth.contract(abi=qtum_abi, address=qtum_address)
** / * qtum_balanceOf => qtum.call().balanceOf

~ Function Listing Below:
~ qtum_update_accounts()
~ qtum_update_balances() \n\r -- => qtum_update_accounts()
~ qtum_list_all_accounts() \n\r -- => qtum_update_accounts()
~ qtum_account_balance(accountNumber) \n\r -- => qtum_update_balances() 
~ qtum_list_all_account_balances() \n\r -- => qtum_update_balances()
~ qtum_unlock_all_accounts() \n\r -- => qtum_unlock_account_0() \n\r -- => qtum_unlock_account_1() \n\r -- => qtum_unlock_account_2() \n\r -- => qtum_unlock_account_3() \n\r -- => qtum_unlock_account_4() \n\r -- => qtum_unlock_account_5() \n\r -- => qtum_unlock_account_6() 
~ qtum_unlock_account_0() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account0, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_1() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account1, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_2() \n\r -- => qtum_update_accounts() \n\r --/ *qtum_w_unlock(qtum_account2, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_3() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account3, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_4() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account4, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_5() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account5, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account_6() \n\r -- => qtum_update_accounts() \n\r -- / *qtum_w_unlock(qtum_account6, qtum_account0pw, qtum_unlockTime)
~ qtum_unlock_account(qtum_ua_accountNumber) \n\r -- => qtum_update_accounts() \n\r -- // qtum_unlock_account_0() \n\r -- // qtum_unlock_account_1() \n\r -- // qtum_unlock_account_2() \n\r -- // qtum_unlock_account_3() \n\r -- // qtum_unlock_account_4() \n\r -- // qtum_unlock_account_5() \n\r -- // qtum_unlock_account_6()
~ qtum_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(fromAccount) \n\r -- / ** qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ qtum_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(fromAccountNumber) \n\r -- / ** qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ qtum_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(fromAccount) \n\r -- / ** qtum.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ qtum_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(fromAccountNumber) \n\r -- / ** qtum.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ qtum_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(callAccount) \n\r / ** qtum.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ qtum_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => qtum_update_accounts() \n\r -- => qtum_unlock_account(callAccount) \n\r -- / ** qtum.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ qtum_help() <-- You Are Here. ''')