#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global bat_account_0_a
global bat_account_1_a
global bat_account_2_a
global bat_account_3_a
global bat_account_4_a
global bat_account_5_a
global bat_account_6_a
global bat_address
global bat_abi
global bat
global bat_call_0
global bat_call_1
global bat_call_2
global bat_call_3
global bat_call_4
global bat_call_5
global bat_call_6
global bat_call_ab
global bat_accounts
global bat_account_0_pw
global bat_account_1_pw
global bat_account_2_pw
global bat_account_3_pw
global bat_account_4_pw
global bat_account_5_pw
global bat_account_6_pw
global bat_account_0_n
global bat_account_1_n
global bat_account_2_n
global bat_account_3_n
global bat_account_4_n
global bat_account_5_n
global bat_account_6_n
global bat_account1pw
global bat_account2pw
global bat_account3pw
global bat_account4pw
global bat_account5pw
global bat_account6pw
global bat_last_price
global bat_accounts_range
global bat_tokenName
global bat_last_ethereum_price
global bat_unlockTime
global bat_balance
global bat_balanceOf
global bat_unlock
global bat_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
bat_token_d = 1e18
_e_d = 1e18
bat_accounts_range = '[0, 6]'
bat_unlock = web3.personal.unlockAccount
bat_last_ethereum_price = 370.00
bat_last_price = 0.23
bat_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
bat_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
bat_tokenName = 'Basic Attention Token'
bat_unlockTime = hex(10000) # Must be hex()
bat_account_0_a = bat_accounts[0]
bat_account_1_a = bat_accounts[1]
bat_account_2_a = bat_accounts[2]
bat_account_3_a = bat_accounts[3]
bat_account_4_a = bat_accounts[4]
bat_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
bat_account_6_a = bat_accounts[6]
# Supply Unlock Passwords For Transactions Below
bat_account_0_pw = 'GuildSkrypt2017!@#'
bat_account_1_pw = ''
bat_account_2_pw = 'GuildSkrypt2017!@#'
bat_account_3_pw = ''
bat_account_4_pw = ''
bat_account_5_pw = ''
bat_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
bat_account_0_n = 'Skotys Bittrex Account'
bat_account_1_n = 'Jeffs Account'
bat_account_2_n = 'Skrypts Bittrex Account'
bat_account_3_n = 'Skotys Personal Account'
bat_account_4_n = 'Unknown'
bat_account_5_n = 'Watched \'Bittrex\' Account.'
bat_account_6_n = 'Watched Account (1)'
# Contract Information Below :
bat_address = '0x0D8775F648430679A709E98d2b0Cb6250d2887EF'
bat_abi = [{"constant":true,"inputs":[],"name":"batFundDeposit","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"batFund","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenExchangeRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationCap","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isFinalized","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingEndBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ethFundDeposit","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"createTokens","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationMin","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingStartBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"_ethFundDeposit","type":"address"},{"name":"_batFundDeposit","type":"address"},{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingEndBlock","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"LogRefund","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"CreateBAT","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
bat = web3.eth.contract(abi=bat_abi, address=bat_address)
bat_balanceOf = bat.call().balanceOf
# End Contract Information
def bat_update_accounts():
 global bat_account0
 global bat_account1
 global bat_account2
 global bat_account3
 global bat_account4
 global bat_account5
 global bat_account6
 global bat_account0_n
 global bat_account1_n
 global bat_account2_n
 global bat_account3_n
 global bat_account4_n
 global bat_account5_n
 global bat_account6_n
 global bat_account0pw
 global bat_account1pw
 global bat_account2pw
 global bat_account3pw
 global bat_account4pw
 global bat_account5pw
 global bat_account6pw
 bat_account0 = bat_account_0_a
 bat_account1 = bat_account_1_a
 bat_account2 = bat_account_2_a
 bat_account3 = bat_account_3_a
 bat_account4 = bat_account_4_a
 bat_account5 = bat_account_5_a
 bat_account6 = bat_account_6_a
 bat_account0_n = bat_account_0_n
 bat_account1_n = bat_account_1_n
 bat_account2_n = bat_account_2_n
 bat_account3_n = bat_account_3_n
 bat_account4_n = bat_account_4_n
 bat_account5_n = bat_account_5_n
 bat_account6_n = bat_account_6_n
 bat_account0pw = bat_account_0_pw
 bat_account1pw = bat_account_1_pw
 bat_account2pw = bat_account_2_pw
 bat_account3pw = bat_account_3_pw
 bat_account4pw = bat_account_4_pw
 bat_account5pw = bat_account_5_pw
 bat_account6pw = bat_account_6_pw
 print(bat_tokenName+' Accounts Updated.')
def bat_update_balances():
 global bat_call_0
 global bat_call_1
 global bat_call_2
 global bat_call_3
 global bat_call_4
 global bat_call_5
 global bat_call_6
 global bat_w_call_0
 global bat_w_call_1
 global bat_w_call_2
 global bat_w_call_3
 global bat_w_call_4
 global bat_w_call_5
 global bat_w_call_6
 bat_update_accounts()
 print('Updating '+bat_tokenName+' Balances Please Wait...')
 bat_call_0 = bat_balanceOf(bat_account0)
 bat_call_1 = bat_balanceOf(bat_account1)
 bat_call_2 = bat_balanceOf(bat_account2)
 bat_call_3 = bat_balanceOf(bat_account3)
 bat_call_4 = bat_balanceOf(bat_account4)
 bat_call_5 = bat_balanceOf(bat_account5)
 bat_call_6 = bat_balanceOf(bat_account6)
 bat_w_call_0 = bat_balance(bat_account0)
 bat_w_call_1 = bat_balance(bat_account1)
 bat_w_call_2 = bat_balance(bat_account2)
 bat_w_call_3 = bat_balance(bat_account3)
 bat_w_call_4 = bat_balance(bat_account4)
 bat_w_call_5 = bat_balance(bat_account5)
 bat_w_call_6 = bat_balance(bat_account6)
 print(bat_tokenName+' Balances Updated.')
def bat_list_all_accounts():
 bat_update_accounts()
 print(bat_tokenName+' '+bat_account0_n+': '+bat_account0)
 print(bat_tokenName+' '+bat_account1_n+': '+bat_account1)
 print(bat_tokenName+' '+bat_account2_n+': '+bat_account2)
 print(bat_tokenName+' '+bat_account3_n+': '+bat_account3)
 print(bat_tokenName+' '+bat_account4_n+': '+bat_account4)
 print(bat_tokenName+' '+bat_account5_n+': '+bat_account5)
 print(bat_tokenName+' '+bat_account6_n+': '+bat_account6)

def bat_account_balance(accountNumber):
 bat_update_balances()
 bat_ab_account_number = accountNumber
 bat_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if bat_ab_account_number == bat_ab_input[0]:
  print('Calling '+bat_account0_n+' '+bat_tokenName+' Balance: ')
  print(bat_account0_n+': '+bat_tokenName+' Balance: '+str(bat_call_0 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_0 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[1]:
  print('Calling '+bat_account1_n+' '+bat_tokenName+' Balance: ')
  print(bat_account1_n+': '+bat_tokenName+' Balance: '+str(bat_call_1 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_1 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[2]:
  print('Calling '+bat_account2_n+' '+bat_tokenName+' Balance: ')
  print(bat_account2_n+': '+bat_tokenName+' Balance: '+str(bat_call_2 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_2 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[3]:
  print('Calling '+bat_account3_n+' '+bat_tokenName+' Balance: ')
  print(bat_account3_n+': '+bat_tokenName+' Balance: '+str(bat_call_3 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_3 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[4]:
  print('Calling '+bat_account4_n+' '+bat_tokenName+' Balance: ')
  print(bat_account4_n+': '+bat_tokenName+' Balance: '+str(bat_call_4 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_4 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[5]:
  print('Calling '+bat_account5_n+' '+bat_tokenName+' Balance: ')
  print(bat_account5_n+': '+bat_tokenName+' Balance: '+str(bat_call_5 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_5 / bat_token_d * bat_last_price))
 if bat_ab_account_number == bat_ab_input[6]:
  print('Calling '+bat_account6_n+' '+bat_tokenName+' Balance: ')
  print(bat_account6_n+': '+bat_tokenName+' Balance: '+str(bat_call_6 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_6 / bat_token_d * bat_last_price))
 if bat_ab_account_number not in bat_ab_input:
  print('Must Integer Within Range '+bat_accounts_range+'.')

def bat_list_all_account_balances():
 bat_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+bat_tokenName+' Balance: ')
 print(bat_account0_n+': '+bat_tokenName+' Balance: '+str(bat_call_0 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_0 / bat_token_d * bat_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(bat_account0_n+': Ethereum Balance '+str(bat_w_call_0 / _e_d)+' $'+str(bat_w_call_0 / _e_d * bat_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+bat_tokenName+' Balance: ')
 print(bat_account1_n+': '+bat_tokenName+' Balance: '+str(bat_call_1 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_1 / bat_token_d * bat_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(bat_account1_n+': Ethereum Balance '+str(bat_w_call_1 / _e_d)+' $'+str(bat_w_call_1 / _e_d * bat_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+bat_tokenName+' Balance: ')
 print(bat_account2_n+': '+bat_tokenName+' Balance: '+str(bat_call_2 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_2 / bat_token_d * bat_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(bat_account2_n+': Ethereum Balance '+str(bat_w_call_2 / _e_d)+' $'+str(bat_w_call_2 / _e_d * bat_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+bat_tokenName+' Balance: ')
 print(bat_account3_n+': '+bat_tokenName+' Balance: '+str(bat_call_3 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_3 / bat_token_d * bat_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(bat_account3_n+': Ethereum Balance '+str(bat_w_call_3 / _e_d)+' $'+str(bat_w_call_3 / _e_d * bat_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+bat_tokenName+' Balance: ')
 print(bat_account4_n+': '+bat_tokenName+' Balance: '+str(bat_call_4 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_4 / bat_token_d * bat_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(bat_account4_n+': Ethereum Balance '+str(bat_w_call_4 / _e_d)+' $'+str(bat_w_call_4 / _e_d * bat_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+bat_tokenName+' Balance: ')
 print(bat_account5_n+': '+bat_tokenName+' Balance: '+str(bat_call_5 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_5 / bat_token_d * bat_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(bat_account5_n+': Ethereum Balance '+str(bat_w_call_5 / _e_d)+' $'+str(bat_w_call_5 /_e_d * bat_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+bat_tokenName+' Balance: ')
 print(bat_account6_n+': '+bat_tokenName+' Balance: '+str(bat_call_6 / bat_token_d)+' Usd/'+bat_tokenName+' Balance: $'+str(bat_call_6 / bat_token_d * bat_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(bat_account6_n+': Ethereum Balance '+str(bat_w_call_6 / _e_d)+' $'+str(bat_w_call_6 / _e_d * bat_last_ethereum_price))
def bat_unlock_all_accounts():
  bat_unlock_account_0()
  bat_unlock_account_1()
  bat_unlock_account_2()
  bat_unlock_account_3()
  bat_unlock_account_4()
  bat_unlock_account_5()
  bat_unlock_account_6()


def bat_unlock_account_0():
  global bat_account0pw
  global bat_account0
  global bat_account0_n
  bat_update_accounts()
  bat_u_a_0 = bat_w_unlock(bat_account0, bat_account0pw, bat_unlockTime)
  if bat_u_a_0 == False:
    if bat_account0pw == '':
     bat_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account0_n+' Passphrase Denied: '+bat_account0pw_r)
    elif bat_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bat_account0_n+' Passphrase Denied: '+bat_account0pw)
  if bat_u_a_0 == True:
   print(bat_account0_n+' Unlocked')

def bat_unlock_account_1():
  global bat_account1pw
  global bat_account1
  global bat_account1_n
  bat_update_accounts()
  bat_u_a_1 = bat_unlock(bat_account1, bat_account1pw, bat_unlockTime)
  if bat_u_a_1 == False:
    if bat_account1pw == '':
     bat_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account1_n+' Passphrase Denied: '+bat_account1pw_r)
    elif bat_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bat_account1_n+' Passphrase Denied: '+bat_account1pw)
  if bat_u_a_1 == True:
   print(bat_account1_n+' Unlocked')

def bat_unlock_account_2():
  global bat_account2pw
  global bat_account2
  global bat_account2_n
  bat_update_accounts()
  bat_u_a_2 = bat_unlock(bat_account2, bat_account2pw, bat_unlockTime)
  if bat_u_a_2 == False:
    if bat_account2pw == '':
     bat_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account2_n+' Passphrase Denied: '+bat_account2pw_r)
    elif bat_account2pw != '':
     print('Unlock Failure With Account '+bat_account2_n+' Passphrase Denied: '+bat_account2pw)
  if bat_u_a_2 == True:
   print(bat_account2_n+' Unlocked')

def bat_unlock_account_3():
  global bat_account3pw
  global bat_account3
  global bat_account3_n
  bat_update_accounts()
  bat_u_a_3 = bat_unlock(bat_account3, bat_account3pw, bat_unlockTime)
  if bat_u_a_3 == False:
    if bat_account3pw == '':
     bat_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account3_n+' Passphrase Denied: '+bat_account3pw_r)
    elif bat_account3pw != '':
     print('Unlock Failure With Account '+bat_account3_n+' Passphrase Denied: '+bat_account3pw)
  if bat_u_a_3 == True:
   print(bat_account3_n+' Unlocked')

def bat_unlock_account_4():
  global bat_account4pw
  global bat_account4
  global bat_account4_n
  bat_update_accounts()
  bat_u_a_4 = bat_unlock(bat_account4, bat_account4pw, bat_unlockTime)
  if bat_u_a_4 == False:
    if bat_account4pw == '':
     bat_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account4_n+' Passphrase Denied: '+bat_account4pw_r)
    elif bat_account4pw != '':
     print('Unlock Failure With Account '+bat_account4_n+' Passphrase Denied: '+bat_account4pw)
  if bat_u_a_4 == True:
   print(bat_account4_n+' Unlocked')

def bat_unlock_account_5():
  global bat_account5pw
  global bat_account5
  global bat_account5_n
  bat_update_accounts()
  bat_u_a_5 = bat_unlock(bat_account5, bat_account5pw, bat_unlockTime)
  if bat_u_a_5 == False:
    if bat_account5pw == '':
     bat_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account5_n+' Passphrase Denied: '+bat_account5pw_r)
    elif bat_account5pw != '':
     print('Unlock Failure With Account '+bat_account5_n+' Passphrase Denied: '+bat_account5pw)
  if bat_u_a_5 == True:
   print(bat_account5_n+' Unlocked')

def bat_unlock_account_6():
  global bat_account6pw
  global bat_account6
  global bat_account6_n
  bat_update_accounts()
  bat_u_a_6 = bat_unlock(bat_account6, bat_account6pw, bat_unlockTime)
  if bat_u_a_6 == False:
    if bat_account6pw == '':
     bat_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bat_account6_n+' Passphrase Denied: '+bat_account6pw_r)
    elif bat_account6pw != '':
     print('Unlock Failure With Account '+bat_account6_n+' Passphrase Denied: '+bat_account6pw)
  if bat_u_a_6 == True:
   print(bat_account6_n+' Unlocked')

def bat_unlock_account(bat_ua_accountNumber):
 bat_update_accounts()
 bat_ua_account_number = bat_ua_accountNumber
 bat_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if bat_ua_account_number == bat_ua_input[0]:
  bat_unlock_account_0()
 if bat_ua_account_number == bat_ua_input[1]:
  bat_unlock_account_1()
 if bat_ua_account_number == bat_ua_input[2]:
  bat_unlock_account_2()
 if bat_ua_account_number == bat_ua_input[3]:
  bat_unlock_account_3()
 if bat_ua_account_number == bat_ua_input[4]:
  bat_unlock_account_4()
 if bat_ua_account_number == bat_ua_input[5]:
  bat_unlock_account_5()
 if bat_ua_account_number == bat_ua_input[6]:
  bat_unlock_account_6()
 if bat_ua_account_number not in bat_ua_input:
  print('Must Integer Within Range '+bat_accounts_range+'.')
 

def bat_approve_between_accounts(fromAccount, toAccount, msgValue):
  bat_update_accounts()
  bat_a_0 = bat.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(bat_a_0)

def bat_approve(fromAccountNumber, toAddress, msgValue):
  bat_update_accounts()
  bat_unlock_account(fromAccountNumber)
  bat_a_1 = bat.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(bat_a_1)

def bat_transfer_between_accounts(fromAccount, toAccount, msgValue):
  bat_update_accounts()
  bat_unlock_account(fromAccount)
  bat_t_0 = bat.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(bat_t_0)

def bat_transfer(fromAccountNumber, toAddress, msgValue):
  bat_update_accounts()
  bat_unlock_account(fromAccountNumber)
  bat_t_1 = bat.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(bat_t_1)

def bat_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  bat_update_accounts()
  bat_unlock_account(callAccount)
  bat_tf_0 = bat.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(bat_tf_0)

def bat_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  bat_update_accounts()
  bat_unlock_account(callAccount)
  bat_tf_1 = bat.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(bat_tf_1)
  


def bat_help():
  print('Following Functions For '+bat_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * bat_unlock => web3.personal.unlockAccount
/ * bat_accounts => web3.personal.listAccounts
/ * bat_balance = web3.eth.getBalance
** bat => web3.eth.contract(abi=bat_abi, address=bat_address)
** / * bat_balanceOf => bat.call().balanceOf

~ Function Listing Below:
~ bat_update_accounts()
~ bat_update_balances() \n\r -- => bat_update_accounts()
~ bat_list_all_accounts() \n\r -- => bat_update_accounts()
~ bat_account_balance(accountNumber) \n\r -- => bat_update_balances() 
~ bat_list_all_account_balances() \n\r -- => bat_update_balances()
~ bat_unlock_all_accounts() \n\r -- => bat_unlock_account_0() \n\r -- => bat_unlock_account_1() \n\r -- => bat_unlock_account_2() \n\r -- => bat_unlock_account_3() \n\r -- => bat_unlock_account_4() \n\r -- => bat_unlock_account_5() \n\r -- => bat_unlock_account_6() 
~ bat_unlock_account_0() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account0, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_1() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account1, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_2() \n\r -- => bat_update_accounts() \n\r --/ *bat_w_unlock(bat_account2, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_3() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account3, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_4() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account4, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_5() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account5, bat_account0pw, bat_unlockTime)
~ bat_unlock_account_6() \n\r -- => bat_update_accounts() \n\r -- / *bat_w_unlock(bat_account6, bat_account0pw, bat_unlockTime)
~ bat_unlock_account(bat_ua_accountNumber) \n\r -- => bat_update_accounts() \n\r -- // bat_unlock_account_0() \n\r -- // bat_unlock_account_1() \n\r -- // bat_unlock_account_2() \n\r -- // bat_unlock_account_3() \n\r -- // bat_unlock_account_4() \n\r -- // bat_unlock_account_5() \n\r -- // bat_unlock_account_6()
~ bat_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(fromAccount) \n\r -- / ** bat.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bat_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(fromAccountNumber) \n\r -- / ** bat.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bat_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(fromAccount) \n\r -- / ** bat.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ bat_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(fromAccountNumber) \n\r -- / ** bat.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bat_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(callAccount) \n\r / ** bat.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bat_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bat_update_accounts() \n\r -- => bat_unlock_account(callAccount) \n\r -- / ** bat.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ bat_help() <-- You Are Here. ''')