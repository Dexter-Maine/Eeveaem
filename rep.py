#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global rep_account_0_a
global rep_account_1_a
global rep_account_2_a
global rep_account_3_a
global rep_account_4_a
global rep_account_5_a
global rep_account_6_a
global rep_address
global rep_abi
global rep
global rep_call_0
global rep_call_1
global rep_call_2
global rep_call_3
global rep_call_4
global rep_call_5
global rep_call_6
global rep_call_ab
global rep_accounts
global rep_account_0_pw
global rep_account_1_pw
global rep_account_2_pw
global rep_account_3_pw
global rep_account_4_pw
global rep_account_5_pw
global rep_account_6_pw
global rep_account_0_n
global rep_account_1_n
global rep_account_2_n
global rep_account_3_n
global rep_account_4_n
global rep_account_5_n
global rep_account_6_n
global rep_account1pw
global rep_account2pw
global rep_account3pw
global rep_account4pw
global rep_account5pw
global rep_account6pw
global rep_last_price
global rep_accounts_range
global rep_tokenName
global rep_last_ethereum_price
global rep_unlockTime
global rep_balance
global rep_balanceOf
global rep_unlock
global rep_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
rep_token_d = 1e18
_e_d = 1e18
rep_accounts_range = '[0, 6]'
rep_unlock = web3.personal.unlockAccount
rep_last_ethereum_price = 370.00
rep_last_price = 26.41
rep_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
rep_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
rep_tokenName = 'REP Token'
rep_unlockTime = hex(10000) # Must be hex()
rep_account_0_a = rep_accounts[0]
rep_account_1_a = rep_accounts[1]
rep_account_2_a = rep_accounts[2]
rep_account_3_a = rep_accounts[3]
rep_account_4_a = rep_accounts[4]
rep_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
rep_account_6_a = rep_accounts[6]
# Supply Unlock Passwords For Transactions Below
rep_account_0_pw = 'GuildSkrypt2017!@#'
rep_account_1_pw = ''
rep_account_2_pw = 'GuildSkrypt2017!@#'
rep_account_3_pw = ''
rep_account_4_pw = ''
rep_account_5_pw = ''
rep_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
rep_account_0_n = 'Skotys Bittrex Account'
rep_account_1_n = 'Jeffs Account'
rep_account_2_n = 'Skrypts Bittrex Account'
rep_account_3_n = 'Skotys Personal Account'
rep_account_4_n = 'Unknown'
rep_account_5_n = 'Watched \'Bittrex\' Account.'
rep_account_6_n = 'Watched Account (1)'
# Contract Information Below :
rep_address = '0xE94327D07Fc17907b4DB788E5aDf2ed424adDff6'
rep_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"initialized","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holder","type":"address"}],"name":"migrateBalance","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"targetSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holders","type":"address[]"}],"name":"migrateBalances","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"legacyRepContract","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_legacyRepContract","type":"address"},{"name":"_amountUsedToFreeze","type":"uint256"},{"name":"_accountToSendFrozenRepTo","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"holder","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"Migrated","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
rep = web3.eth.contract(abi=rep_abi, address=rep_address)
rep_balanceOf = rep.call().balanceOf
# End Contract Information
def rep_update_accounts():
 global rep_account0
 global rep_account1
 global rep_account2
 global rep_account3
 global rep_account4
 global rep_account5
 global rep_account6
 global rep_account0_n
 global rep_account1_n
 global rep_account2_n
 global rep_account3_n
 global rep_account4_n
 global rep_account5_n
 global rep_account6_n
 global rep_account0pw
 global rep_account1pw
 global rep_account2pw
 global rep_account3pw
 global rep_account4pw
 global rep_account5pw
 global rep_account6pw
 rep_account0 = rep_account_0_a
 rep_account1 = rep_account_1_a
 rep_account2 = rep_account_2_a
 rep_account3 = rep_account_3_a
 rep_account4 = rep_account_4_a
 rep_account5 = rep_account_5_a
 rep_account6 = rep_account_6_a
 rep_account0_n = rep_account_0_n
 rep_account1_n = rep_account_1_n
 rep_account2_n = rep_account_2_n
 rep_account3_n = rep_account_3_n
 rep_account4_n = rep_account_4_n
 rep_account5_n = rep_account_5_n
 rep_account6_n = rep_account_6_n
 rep_account0pw = rep_account_0_pw
 rep_account1pw = rep_account_1_pw
 rep_account2pw = rep_account_2_pw
 rep_account3pw = rep_account_3_pw
 rep_account4pw = rep_account_4_pw
 rep_account5pw = rep_account_5_pw
 rep_account6pw = rep_account_6_pw
 print(rep_tokenName+' Accounts Updated.')
def rep_update_balances():
 global rep_call_0
 global rep_call_1
 global rep_call_2
 global rep_call_3
 global rep_call_4
 global rep_call_5
 global rep_call_6
 global rep_w_call_0
 global rep_w_call_1
 global rep_w_call_2
 global rep_w_call_3
 global rep_w_call_4
 global rep_w_call_5
 global rep_w_call_6
 rep_update_accounts()
 print('Updating '+rep_tokenName+' Balances Please Wait...')
 rep_call_0 = rep_balanceOf(rep_account0)
 rep_call_1 = rep_balanceOf(rep_account1)
 rep_call_2 = rep_balanceOf(rep_account2)
 rep_call_3 = rep_balanceOf(rep_account3)
 rep_call_4 = rep_balanceOf(rep_account4)
 rep_call_5 = rep_balanceOf(rep_account5)
 rep_call_6 = rep_balanceOf(rep_account6)
 rep_w_call_0 = rep_balance(rep_account0)
 rep_w_call_1 = rep_balance(rep_account1)
 rep_w_call_2 = rep_balance(rep_account2)
 rep_w_call_3 = rep_balance(rep_account3)
 rep_w_call_4 = rep_balance(rep_account4)
 rep_w_call_5 = rep_balance(rep_account5)
 rep_w_call_6 = rep_balance(rep_account6)
 print(rep_tokenName+' Balances Updated.')
def rep_list_all_accounts():
 rep_update_accounts()
 print(rep_tokenName+' '+rep_account0_n+': '+rep_account0)
 print(rep_tokenName+' '+rep_account1_n+': '+rep_account1)
 print(rep_tokenName+' '+rep_account2_n+': '+rep_account2)
 print(rep_tokenName+' '+rep_account3_n+': '+rep_account3)
 print(rep_tokenName+' '+rep_account4_n+': '+rep_account4)
 print(rep_tokenName+' '+rep_account5_n+': '+rep_account5)
 print(rep_tokenName+' '+rep_account6_n+': '+rep_account6)

def rep_account_balance(accountNumber):
 rep_update_balances()
 rep_ab_account_number = accountNumber
 rep_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if rep_ab_account_number == rep_ab_input[0]:
  print('Calling '+rep_account0_n+' '+rep_tokenName+' Balance: ')
  print(rep_account0_n+': '+rep_tokenName+' Balance: '+str(rep_call_0 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_0 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[1]:
  print('Calling '+rep_account1_n+' '+rep_tokenName+' Balance: ')
  print(rep_account1_n+': '+rep_tokenName+' Balance: '+str(rep_call_1 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_1 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[2]:
  print('Calling '+rep_account2_n+' '+rep_tokenName+' Balance: ')
  print(rep_account2_n+': '+rep_tokenName+' Balance: '+str(rep_call_2 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_2 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[3]:
  print('Calling '+rep_account3_n+' '+rep_tokenName+' Balance: ')
  print(rep_account3_n+': '+rep_tokenName+' Balance: '+str(rep_call_3 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_3 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[4]:
  print('Calling '+rep_account4_n+' '+rep_tokenName+' Balance: ')
  print(rep_account4_n+': '+rep_tokenName+' Balance: '+str(rep_call_4 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_4 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[5]:
  print('Calling '+rep_account5_n+' '+rep_tokenName+' Balance: ')
  print(rep_account5_n+': '+rep_tokenName+' Balance: '+str(rep_call_5 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_5 / rep_token_d * rep_last_price))
 if rep_ab_account_number == rep_ab_input[6]:
  print('Calling '+rep_account6_n+' '+rep_tokenName+' Balance: ')
  print(rep_account6_n+': '+rep_tokenName+' Balance: '+str(rep_call_6 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_6 / rep_token_d * rep_last_price))
 if rep_ab_account_number not in rep_ab_input:
  print('Must Integer Within Range '+rep_accounts_range+'.')

def rep_list_all_account_balances():
 rep_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+rep_tokenName+' Balance: ')
 print(rep_account0_n+': '+rep_tokenName+' Balance: '+str(rep_call_0 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_0 / rep_token_d * rep_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(rep_account0_n+': Ethereum Balance '+str(rep_w_call_0 / _e_d)+' $'+str(rep_w_call_0 / _e_d * rep_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+rep_tokenName+' Balance: ')
 print(rep_account1_n+': '+rep_tokenName+' Balance: '+str(rep_call_1 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_1 / rep_token_d * rep_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(rep_account1_n+': Ethereum Balance '+str(rep_w_call_1 / _e_d)+' $'+str(rep_w_call_1 / _e_d * rep_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+rep_tokenName+' Balance: ')
 print(rep_account2_n+': '+rep_tokenName+' Balance: '+str(rep_call_2 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_2 / rep_token_d * rep_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(rep_account2_n+': Ethereum Balance '+str(rep_w_call_2 / _e_d)+' $'+str(rep_w_call_2 / _e_d * rep_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+rep_tokenName+' Balance: ')
 print(rep_account3_n+': '+rep_tokenName+' Balance: '+str(rep_call_3 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_3 / rep_token_d * rep_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(rep_account3_n+': Ethereum Balance '+str(rep_w_call_3 / _e_d)+' $'+str(rep_w_call_3 / _e_d * rep_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+rep_tokenName+' Balance: ')
 print(rep_account4_n+': '+rep_tokenName+' Balance: '+str(rep_call_4 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_4 / rep_token_d * rep_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(rep_account4_n+': Ethereum Balance '+str(rep_w_call_4 / _e_d)+' $'+str(rep_w_call_4 / _e_d * rep_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+rep_tokenName+' Balance: ')
 print(rep_account5_n+': '+rep_tokenName+' Balance: '+str(rep_call_5 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_5 / rep_token_d * rep_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(rep_account5_n+': Ethereum Balance '+str(rep_w_call_5 / _e_d)+' $'+str(rep_w_call_5 /_e_d * rep_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+rep_tokenName+' Balance: ')
 print(rep_account6_n+': '+rep_tokenName+' Balance: '+str(rep_call_6 / rep_token_d)+' Usd/'+rep_tokenName+' Balance: $'+str(rep_call_6 / rep_token_d * rep_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(rep_account6_n+': Ethereum Balance '+str(rep_w_call_6 / _e_d)+' $'+str(rep_w_call_6 / _e_d * rep_last_ethereum_price))
def rep_unlock_all_accounts():
  rep_unlock_account_0()
  rep_unlock_account_1()
  rep_unlock_account_2()
  rep_unlock_account_3()
  rep_unlock_account_4()
  rep_unlock_account_5()
  rep_unlock_account_6()


def rep_unlock_account_0():
  global rep_account0pw
  global rep_account0
  global rep_account0_n
  rep_update_accounts()
  rep_u_a_0 = rep_w_unlock(rep_account0, rep_account0pw, rep_unlockTime)
  if rep_u_a_0 == False:
    if rep_account0pw == '':
     rep_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account0_n+' Passphrase Denied: '+rep_account0pw_r)
    elif rep_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rep_account0_n+' Passphrase Denied: '+rep_account0pw)
  if rep_u_a_0 == True:
   print(rep_account0_n+' Unlocked')

def rep_unlock_account_1():
  global rep_account1pw
  global rep_account1
  global rep_account1_n
  rep_update_accounts()
  rep_u_a_1 = rep_unlock(rep_account1, rep_account1pw, rep_unlockTime)
  if rep_u_a_1 == False:
    if rep_account1pw == '':
     rep_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account1_n+' Passphrase Denied: '+rep_account1pw_r)
    elif rep_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rep_account1_n+' Passphrase Denied: '+rep_account1pw)
  if rep_u_a_1 == True:
   print(rep_account1_n+' Unlocked')

def rep_unlock_account_2():
  global rep_account2pw
  global rep_account2
  global rep_account2_n
  rep_update_accounts()
  rep_u_a_2 = rep_unlock(rep_account2, rep_account2pw, rep_unlockTime)
  if rep_u_a_2 == False:
    if rep_account2pw == '':
     rep_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account2_n+' Passphrase Denied: '+rep_account2pw_r)
    elif rep_account2pw != '':
     print('Unlock Failure With Account '+rep_account2_n+' Passphrase Denied: '+rep_account2pw)
  if rep_u_a_2 == True:
   print(rep_account2_n+' Unlocked')

def rep_unlock_account_3():
  global rep_account3pw
  global rep_account3
  global rep_account3_n
  rep_update_accounts()
  rep_u_a_3 = rep_unlock(rep_account3, rep_account3pw, rep_unlockTime)
  if rep_u_a_3 == False:
    if rep_account3pw == '':
     rep_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account3_n+' Passphrase Denied: '+rep_account3pw_r)
    elif rep_account3pw != '':
     print('Unlock Failure With Account '+rep_account3_n+' Passphrase Denied: '+rep_account3pw)
  if rep_u_a_3 == True:
   print(rep_account3_n+' Unlocked')

def rep_unlock_account_4():
  global rep_account4pw
  global rep_account4
  global rep_account4_n
  rep_update_accounts()
  rep_u_a_4 = rep_unlock(rep_account4, rep_account4pw, rep_unlockTime)
  if rep_u_a_4 == False:
    if rep_account4pw == '':
     rep_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account4_n+' Passphrase Denied: '+rep_account4pw_r)
    elif rep_account4pw != '':
     print('Unlock Failure With Account '+rep_account4_n+' Passphrase Denied: '+rep_account4pw)
  if rep_u_a_4 == True:
   print(rep_account4_n+' Unlocked')

def rep_unlock_account_5():
  global rep_account5pw
  global rep_account5
  global rep_account5_n
  rep_update_accounts()
  rep_u_a_5 = rep_unlock(rep_account5, rep_account5pw, rep_unlockTime)
  if rep_u_a_5 == False:
    if rep_account5pw == '':
     rep_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account5_n+' Passphrase Denied: '+rep_account5pw_r)
    elif rep_account5pw != '':
     print('Unlock Failure With Account '+rep_account5_n+' Passphrase Denied: '+rep_account5pw)
  if rep_u_a_5 == True:
   print(rep_account5_n+' Unlocked')

def rep_unlock_account_6():
  global rep_account6pw
  global rep_account6
  global rep_account6_n
  rep_update_accounts()
  rep_u_a_6 = rep_unlock(rep_account6, rep_account6pw, rep_unlockTime)
  if rep_u_a_6 == False:
    if rep_account6pw == '':
     rep_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rep_account6_n+' Passphrase Denied: '+rep_account6pw_r)
    elif rep_account6pw != '':
     print('Unlock Failure With Account '+rep_account6_n+' Passphrase Denied: '+rep_account6pw)
  if rep_u_a_6 == True:
   print(rep_account6_n+' Unlocked')

def rep_unlock_account(rep_ua_accountNumber):
 rep_update_accounts()
 rep_ua_account_number = rep_ua_accountNumber
 rep_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if rep_ua_account_number == rep_ua_input[0]:
  rep_unlock_account_0()
 if rep_ua_account_number == rep_ua_input[1]:
  rep_unlock_account_1()
 if rep_ua_account_number == rep_ua_input[2]:
  rep_unlock_account_2()
 if rep_ua_account_number == rep_ua_input[3]:
  rep_unlock_account_3()
 if rep_ua_account_number == rep_ua_input[4]:
  rep_unlock_account_4()
 if rep_ua_account_number == rep_ua_input[5]:
  rep_unlock_account_5()
 if rep_ua_account_number == rep_ua_input[6]:
  rep_unlock_account_6()
 if rep_ua_account_number not in rep_ua_input:
  print('Must Integer Within Range '+rep_accounts_range+'.')
 

def rep_approve_between_accounts(fromAccount, toAccount, msgValue):
  rep_update_accounts()
  rep_a_0 = rep.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(rep_a_0)

def rep_approve(fromAccountNumber, toAddress, msgValue):
  rep_update_accounts()
  rep_unlock_account(fromAccountNumber)
  rep_a_1 = rep.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(rep_a_1)

def rep_transfer_between_accounts(fromAccount, toAccount, msgValue):
  rep_update_accounts()
  rep_unlock_account(fromAccount)
  rep_t_0 = rep.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(rep_t_0)

def rep_transfer(fromAccountNumber, toAddress, msgValue):
  rep_update_accounts()
  rep_unlock_account(fromAccountNumber)
  rep_t_1 = rep.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(rep_t_1)

def rep_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  rep_update_accounts()
  rep_unlock_account(callAccount)
  rep_tf_0 = rep.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(rep_tf_0)

def rep_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  rep_update_accounts()
  rep_unlock_account(callAccount)
  rep_tf_1 = rep.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(rep_tf_1)
  


def rep_help():
  print('Following Functions For '+rep_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * rep_unlock => web3.personal.unlockAccount
/ * rep_accounts => web3.personal.listAccounts
/ * rep_balance = web3.eth.getBalance
** rep => web3.eth.contract(abi=rep_abi, address=rep_address)
** / * rep_balanceOf => rep.call().balanceOf

~ Function Listing Below:
~ rep_update_accounts()
~ rep_update_balances() \n\r -- => rep_update_accounts()
~ rep_list_all_accounts() \n\r -- => rep_update_accounts()
~ rep_account_balance(accountNumber) \n\r -- => rep_update_balances() 
~ rep_list_all_account_balances() \n\r -- => rep_update_balances()
~ rep_unlock_all_accounts() \n\r -- => rep_unlock_account_0() \n\r -- => rep_unlock_account_1() \n\r -- => rep_unlock_account_2() \n\r -- => rep_unlock_account_3() \n\r -- => rep_unlock_account_4() \n\r -- => rep_unlock_account_5() \n\r -- => rep_unlock_account_6() 
~ rep_unlock_account_0() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account0, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_1() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account1, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_2() \n\r -- => rep_update_accounts() \n\r --/ *rep_w_unlock(rep_account2, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_3() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account3, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_4() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account4, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_5() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account5, rep_account0pw, rep_unlockTime)
~ rep_unlock_account_6() \n\r -- => rep_update_accounts() \n\r -- / *rep_w_unlock(rep_account6, rep_account0pw, rep_unlockTime)
~ rep_unlock_account(rep_ua_accountNumber) \n\r -- => rep_update_accounts() \n\r -- // rep_unlock_account_0() \n\r -- // rep_unlock_account_1() \n\r -- // rep_unlock_account_2() \n\r -- // rep_unlock_account_3() \n\r -- // rep_unlock_account_4() \n\r -- // rep_unlock_account_5() \n\r -- // rep_unlock_account_6()
~ rep_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(fromAccount) \n\r -- / ** rep.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rep_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(fromAccountNumber) \n\r -- / ** rep.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rep_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(fromAccount) \n\r -- / ** rep.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ rep_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(fromAccountNumber) \n\r -- / ** rep.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rep_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(callAccount) \n\r / ** rep.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rep_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rep_update_accounts() \n\r -- => rep_unlock_account(callAccount) \n\r -- / ** rep.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ rep_help() <-- You Are Here. ''')