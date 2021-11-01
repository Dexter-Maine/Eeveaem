#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global snc_account_0_a
global snc_account_1_a
global snc_account_2_a
global snc_account_3_a
global snc_account_4_a
global snc_account_5_a
global snc_account_6_a
global snc_address
global snc_abi
global snc
global snc_call_0
global snc_call_1
global snc_call_2
global snc_call_3
global snc_call_4
global snc_call_5
global snc_call_6
global snc_call_ab
global snc_accounts
global snc_account_0_pw
global snc_account_1_pw
global snc_account_2_pw
global snc_account_3_pw
global snc_account_4_pw
global snc_account_5_pw
global snc_account_6_pw
global snc_account_0_n
global snc_account_1_n
global snc_account_2_n
global snc_account_3_n
global snc_account_4_n
global snc_account_5_n
global snc_account_6_n
global snc_account1pw
global snc_account2pw
global snc_account3pw
global snc_account4pw
global snc_account5pw
global snc_account6pw
global snc_last_price
global snc_accounts_range
global snc_tokenName
global snc_last_ethereum_price
global snc_unlockTime
global snc_balance
global snc_balanceOf
global snc_unlock
global snc_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
snc_token_d = 1e18
_e_d = 1e18
snc_accounts_range = '[0, 6]'
snc_unlock = web3.personal.unlockAccount
snc_last_ethereum_price = 370.00
snc_last_price = 0.05
snc_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
snc_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
snc_tokenName = 'SunContract Token'
snc_unlockTime = hex(10000) # Must be hex()
snc_account_0_a = snc_accounts[0]
snc_account_1_a = snc_accounts[1]
snc_account_2_a = snc_accounts[2]
snc_account_3_a = snc_accounts[3]
snc_account_4_a = snc_accounts[4]
snc_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
snc_account_6_a = snc_accounts[6]
# Supply Unlock Passwords For Transactions Below
snc_account_0_pw = 'GuildSkrypt2017!@#'
snc_account_1_pw = ''
snc_account_2_pw = 'GuildSkrypt2017!@#'
snc_account_3_pw = ''
snc_account_4_pw = ''
snc_account_5_pw = ''
snc_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
snc_account_0_n = 'Skotys Bittrex Account'
snc_account_1_n = 'Jeffs Account'
snc_account_2_n = 'Skrypts Bittrex Account'
snc_account_3_n = 'Skotys Personal Account'
snc_account_4_n = 'Unknown'
snc_account_5_n = 'Watched \'Bittrex\' Account.'
snc_account_6_n = 'Watched Account (1)'
# Contract Information Below :
snc_address = '0xF4134146AF2d511Dd5EA8cDB1C4AC88C57D60404'
snc_abi = [{"constant":true,"inputs":[{"name":"_querryAddress","type":"address"}],"name":"isRestrictedAddress","outputs":[{"name":"answer","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint256"}],"name":"burnTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFrozenUntilBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"icoContractAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_frozenUntilBlock","type":"uint256"},{"name":"_reason","type":"string"}],"name":"freezeTransfersUntil","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mintTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_icoAddress","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_frozenUntilBlock","type":"uint256"},{"indexed":false,"name":"_reason","type":"string"}],"name":"TokenFrozen","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
snc = web3.eth.contract(abi=snc_abi, address=snc_address)
snc_balanceOf = snc.call().balanceOf
# End Contract Information
def snc_update_accounts():
 global snc_account0
 global snc_account1
 global snc_account2
 global snc_account3
 global snc_account4
 global snc_account5
 global snc_account6
 global snc_account0_n
 global snc_account1_n
 global snc_account2_n
 global snc_account3_n
 global snc_account4_n
 global snc_account5_n
 global snc_account6_n
 global snc_account0pw
 global snc_account1pw
 global snc_account2pw
 global snc_account3pw
 global snc_account4pw
 global snc_account5pw
 global snc_account6pw
 snc_account0 = snc_account_0_a
 snc_account1 = snc_account_1_a
 snc_account2 = snc_account_2_a
 snc_account3 = snc_account_3_a
 snc_account4 = snc_account_4_a
 snc_account5 = snc_account_5_a
 snc_account6 = snc_account_6_a
 snc_account0_n = snc_account_0_n
 snc_account1_n = snc_account_1_n
 snc_account2_n = snc_account_2_n
 snc_account3_n = snc_account_3_n
 snc_account4_n = snc_account_4_n
 snc_account5_n = snc_account_5_n
 snc_account6_n = snc_account_6_n
 snc_account0pw = snc_account_0_pw
 snc_account1pw = snc_account_1_pw
 snc_account2pw = snc_account_2_pw
 snc_account3pw = snc_account_3_pw
 snc_account4pw = snc_account_4_pw
 snc_account5pw = snc_account_5_pw
 snc_account6pw = snc_account_6_pw
 print(snc_tokenName+' Accounts Updated.')
def snc_update_balances():
 global snc_call_0
 global snc_call_1
 global snc_call_2
 global snc_call_3
 global snc_call_4
 global snc_call_5
 global snc_call_6
 global snc_w_call_0
 global snc_w_call_1
 global snc_w_call_2
 global snc_w_call_3
 global snc_w_call_4
 global snc_w_call_5
 global snc_w_call_6
 snc_update_accounts()
 print('Updating '+snc_tokenName+' Balances Please Wait...')
 snc_call_0 = snc_balanceOf(snc_account0)
 snc_call_1 = snc_balanceOf(snc_account1)
 snc_call_2 = snc_balanceOf(snc_account2)
 snc_call_3 = snc_balanceOf(snc_account3)
 snc_call_4 = snc_balanceOf(snc_account4)
 snc_call_5 = snc_balanceOf(snc_account5)
 snc_call_6 = snc_balanceOf(snc_account6)
 snc_w_call_0 = snc_balance(snc_account0)
 snc_w_call_1 = snc_balance(snc_account1)
 snc_w_call_2 = snc_balance(snc_account2)
 snc_w_call_3 = snc_balance(snc_account3)
 snc_w_call_4 = snc_balance(snc_account4)
 snc_w_call_5 = snc_balance(snc_account5)
 snc_w_call_6 = snc_balance(snc_account6)
 print(snc_tokenName+' Balances Updated.')
def snc_list_all_accounts():
 snc_update_accounts()
 print(snc_tokenName+' '+snc_account0_n+': '+snc_account0)
 print(snc_tokenName+' '+snc_account1_n+': '+snc_account1)
 print(snc_tokenName+' '+snc_account2_n+': '+snc_account2)
 print(snc_tokenName+' '+snc_account3_n+': '+snc_account3)
 print(snc_tokenName+' '+snc_account4_n+': '+snc_account4)
 print(snc_tokenName+' '+snc_account5_n+': '+snc_account5)
 print(snc_tokenName+' '+snc_account6_n+': '+snc_account6)

def snc_account_balance(accountNumber):
 snc_update_balances()
 snc_ab_account_number = accountNumber
 snc_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if snc_ab_account_number == snc_ab_input[0]:
  print('Calling '+snc_account0_n+' '+snc_tokenName+' Balance: ')
  print(snc_account0_n+': '+snc_tokenName+' Balance: '+str(snc_call_0 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_0 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[1]:
  print('Calling '+snc_account1_n+' '+snc_tokenName+' Balance: ')
  print(snc_account1_n+': '+snc_tokenName+' Balance: '+str(snc_call_1 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_1 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[2]:
  print('Calling '+snc_account2_n+' '+snc_tokenName+' Balance: ')
  print(snc_account2_n+': '+snc_tokenName+' Balance: '+str(snc_call_2 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_2 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[3]:
  print('Calling '+snc_account3_n+' '+snc_tokenName+' Balance: ')
  print(snc_account3_n+': '+snc_tokenName+' Balance: '+str(snc_call_3 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_3 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[4]:
  print('Calling '+snc_account4_n+' '+snc_tokenName+' Balance: ')
  print(snc_account4_n+': '+snc_tokenName+' Balance: '+str(snc_call_4 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_4 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[5]:
  print('Calling '+snc_account5_n+' '+snc_tokenName+' Balance: ')
  print(snc_account5_n+': '+snc_tokenName+' Balance: '+str(snc_call_5 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_5 / snc_token_d * snc_last_price))
 if snc_ab_account_number == snc_ab_input[6]:
  print('Calling '+snc_account6_n+' '+snc_tokenName+' Balance: ')
  print(snc_account6_n+': '+snc_tokenName+' Balance: '+str(snc_call_6 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_6 / snc_token_d * snc_last_price))
 if snc_ab_account_number not in snc_ab_input:
  print('Must Integer Within Range '+snc_accounts_range+'.')

def snc_list_all_account_balances():
 snc_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+snc_tokenName+' Balance: ')
 print(snc_account0_n+': '+snc_tokenName+' Balance: '+str(snc_call_0 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_0 / snc_token_d * snc_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(snc_account0_n+': Ethereum Balance '+str(snc_w_call_0 / _e_d)+' $'+str(snc_w_call_0 / _e_d * snc_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+snc_tokenName+' Balance: ')
 print(snc_account1_n+': '+snc_tokenName+' Balance: '+str(snc_call_1 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_1 / snc_token_d * snc_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(snc_account1_n+': Ethereum Balance '+str(snc_w_call_1 / _e_d)+' $'+str(snc_w_call_1 / _e_d * snc_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+snc_tokenName+' Balance: ')
 print(snc_account2_n+': '+snc_tokenName+' Balance: '+str(snc_call_2 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_2 / snc_token_d * snc_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(snc_account2_n+': Ethereum Balance '+str(snc_w_call_2 / _e_d)+' $'+str(snc_w_call_2 / _e_d * snc_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+snc_tokenName+' Balance: ')
 print(snc_account3_n+': '+snc_tokenName+' Balance: '+str(snc_call_3 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_3 / snc_token_d * snc_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(snc_account3_n+': Ethereum Balance '+str(snc_w_call_3 / _e_d)+' $'+str(snc_w_call_3 / _e_d * snc_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+snc_tokenName+' Balance: ')
 print(snc_account4_n+': '+snc_tokenName+' Balance: '+str(snc_call_4 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_4 / snc_token_d * snc_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(snc_account4_n+': Ethereum Balance '+str(snc_w_call_4 / _e_d)+' $'+str(snc_w_call_4 / _e_d * snc_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+snc_tokenName+' Balance: ')
 print(snc_account5_n+': '+snc_tokenName+' Balance: '+str(snc_call_5 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_5 / snc_token_d * snc_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(snc_account5_n+': Ethereum Balance '+str(snc_w_call_5 / _e_d)+' $'+str(snc_w_call_5 /_e_d * snc_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+snc_tokenName+' Balance: ')
 print(snc_account6_n+': '+snc_tokenName+' Balance: '+str(snc_call_6 / snc_token_d)+' Usd/'+snc_tokenName+' Balance: $'+str(snc_call_6 / snc_token_d * snc_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(snc_account6_n+': Ethereum Balance '+str(snc_w_call_6 / _e_d)+' $'+str(snc_w_call_6 / _e_d * snc_last_ethereum_price))
def snc_unlock_all_accounts():
  snc_unlock_account_0()
  snc_unlock_account_1()
  snc_unlock_account_2()
  snc_unlock_account_3()
  snc_unlock_account_4()
  snc_unlock_account_5()
  snc_unlock_account_6()


def snc_unlock_account_0():
  global snc_account0pw
  global snc_account0
  global snc_account0_n
  snc_update_accounts()
  snc_u_a_0 = snc_w_unlock(snc_account0, snc_account0pw, snc_unlockTime)
  if snc_u_a_0 == False:
    if snc_account0pw == '':
     snc_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account0_n+' Passphrase Denied: '+snc_account0pw_r)
    elif snc_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snc_account0_n+' Passphrase Denied: '+snc_account0pw)
  if snc_u_a_0 == True:
   print(snc_account0_n+' Unlocked')

def snc_unlock_account_1():
  global snc_account1pw
  global snc_account1
  global snc_account1_n
  snc_update_accounts()
  snc_u_a_1 = snc_unlock(snc_account1, snc_account1pw, snc_unlockTime)
  if snc_u_a_1 == False:
    if snc_account1pw == '':
     snc_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account1_n+' Passphrase Denied: '+snc_account1pw_r)
    elif snc_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snc_account1_n+' Passphrase Denied: '+snc_account1pw)
  if snc_u_a_1 == True:
   print(snc_account1_n+' Unlocked')

def snc_unlock_account_2():
  global snc_account2pw
  global snc_account2
  global snc_account2_n
  snc_update_accounts()
  snc_u_a_2 = snc_unlock(snc_account2, snc_account2pw, snc_unlockTime)
  if snc_u_a_2 == False:
    if snc_account2pw == '':
     snc_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account2_n+' Passphrase Denied: '+snc_account2pw_r)
    elif snc_account2pw != '':
     print('Unlock Failure With Account '+snc_account2_n+' Passphrase Denied: '+snc_account2pw)
  if snc_u_a_2 == True:
   print(snc_account2_n+' Unlocked')

def snc_unlock_account_3():
  global snc_account3pw
  global snc_account3
  global snc_account3_n
  snc_update_accounts()
  snc_u_a_3 = snc_unlock(snc_account3, snc_account3pw, snc_unlockTime)
  if snc_u_a_3 == False:
    if snc_account3pw == '':
     snc_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account3_n+' Passphrase Denied: '+snc_account3pw_r)
    elif snc_account3pw != '':
     print('Unlock Failure With Account '+snc_account3_n+' Passphrase Denied: '+snc_account3pw)
  if snc_u_a_3 == True:
   print(snc_account3_n+' Unlocked')

def snc_unlock_account_4():
  global snc_account4pw
  global snc_account4
  global snc_account4_n
  snc_update_accounts()
  snc_u_a_4 = snc_unlock(snc_account4, snc_account4pw, snc_unlockTime)
  if snc_u_a_4 == False:
    if snc_account4pw == '':
     snc_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account4_n+' Passphrase Denied: '+snc_account4pw_r)
    elif snc_account4pw != '':
     print('Unlock Failure With Account '+snc_account4_n+' Passphrase Denied: '+snc_account4pw)
  if snc_u_a_4 == True:
   print(snc_account4_n+' Unlocked')

def snc_unlock_account_5():
  global snc_account5pw
  global snc_account5
  global snc_account5_n
  snc_update_accounts()
  snc_u_a_5 = snc_unlock(snc_account5, snc_account5pw, snc_unlockTime)
  if snc_u_a_5 == False:
    if snc_account5pw == '':
     snc_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account5_n+' Passphrase Denied: '+snc_account5pw_r)
    elif snc_account5pw != '':
     print('Unlock Failure With Account '+snc_account5_n+' Passphrase Denied: '+snc_account5pw)
  if snc_u_a_5 == True:
   print(snc_account5_n+' Unlocked')

def snc_unlock_account_6():
  global snc_account6pw
  global snc_account6
  global snc_account6_n
  snc_update_accounts()
  snc_u_a_6 = snc_unlock(snc_account6, snc_account6pw, snc_unlockTime)
  if snc_u_a_6 == False:
    if snc_account6pw == '':
     snc_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snc_account6_n+' Passphrase Denied: '+snc_account6pw_r)
    elif snc_account6pw != '':
     print('Unlock Failure With Account '+snc_account6_n+' Passphrase Denied: '+snc_account6pw)
  if snc_u_a_6 == True:
   print(snc_account6_n+' Unlocked')

def snc_unlock_account(snc_ua_accountNumber):
 snc_update_accounts()
 snc_ua_account_number = snc_ua_accountNumber
 snc_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if snc_ua_account_number == snc_ua_input[0]:
  snc_unlock_account_0()
 if snc_ua_account_number == snc_ua_input[1]:
  snc_unlock_account_1()
 if snc_ua_account_number == snc_ua_input[2]:
  snc_unlock_account_2()
 if snc_ua_account_number == snc_ua_input[3]:
  snc_unlock_account_3()
 if snc_ua_account_number == snc_ua_input[4]:
  snc_unlock_account_4()
 if snc_ua_account_number == snc_ua_input[5]:
  snc_unlock_account_5()
 if snc_ua_account_number == snc_ua_input[6]:
  snc_unlock_account_6()
 if snc_ua_account_number not in snc_ua_input:
  print('Must Integer Within Range '+snc_accounts_range+'.')
 

def snc_approve_between_accounts(fromAccount, toAccount, msgValue):
  snc_update_accounts()
  snc_a_0 = snc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(snc_a_0)

def snc_approve(fromAccountNumber, toAddress, msgValue):
  snc_update_accounts()
  snc_unlock_account(fromAccountNumber)
  snc_a_1 = snc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(snc_a_1)

def snc_transfer_between_accounts(fromAccount, toAccount, msgValue):
  snc_update_accounts()
  snc_unlock_account(fromAccount)
  snc_t_0 = snc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(snc_t_0)

def snc_transfer(fromAccountNumber, toAddress, msgValue):
  snc_update_accounts()
  snc_unlock_account(fromAccountNumber)
  snc_t_1 = snc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(snc_t_1)

def snc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  snc_update_accounts()
  snc_unlock_account(callAccount)
  snc_tf_0 = snc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(snc_tf_0)

def snc_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  snc_update_accounts()
  snc_unlock_account(callAccount)
  snc_tf_1 = snc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(snc_tf_1)
  


def snc_help():
  print('Following Functions For '+snc_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * snc_unlock => web3.personal.unlockAccount
/ * snc_accounts => web3.personal.listAccounts
/ * snc_balance = web3.eth.getBalance
** snc => web3.eth.contract(abi=snc_abi, address=snc_address)
** / * snc_balanceOf => snc.call().balanceOf

~ Function Listing Below:
~ snc_update_accounts()
~ snc_update_balances() \n\r -- => snc_update_accounts()
~ snc_list_all_accounts() \n\r -- => snc_update_accounts()
~ snc_account_balance(accountNumber) \n\r -- => snc_update_balances() 
~ snc_list_all_account_balances() \n\r -- => snc_update_balances()
~ snc_unlock_all_accounts() \n\r -- => snc_unlock_account_0() \n\r -- => snc_unlock_account_1() \n\r -- => snc_unlock_account_2() \n\r -- => snc_unlock_account_3() \n\r -- => snc_unlock_account_4() \n\r -- => snc_unlock_account_5() \n\r -- => snc_unlock_account_6() 
~ snc_unlock_account_0() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account0, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_1() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account1, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_2() \n\r -- => snc_update_accounts() \n\r --/ *snc_w_unlock(snc_account2, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_3() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account3, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_4() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account4, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_5() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account5, snc_account0pw, snc_unlockTime)
~ snc_unlock_account_6() \n\r -- => snc_update_accounts() \n\r -- / *snc_w_unlock(snc_account6, snc_account0pw, snc_unlockTime)
~ snc_unlock_account(snc_ua_accountNumber) \n\r -- => snc_update_accounts() \n\r -- // snc_unlock_account_0() \n\r -- // snc_unlock_account_1() \n\r -- // snc_unlock_account_2() \n\r -- // snc_unlock_account_3() \n\r -- // snc_unlock_account_4() \n\r -- // snc_unlock_account_5() \n\r -- // snc_unlock_account_6()
~ snc_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(fromAccount) \n\r -- / ** snc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snc_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(fromAccountNumber) \n\r -- / ** snc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snc_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(fromAccount) \n\r -- / ** snc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ snc_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(fromAccountNumber) \n\r -- / ** snc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(callAccount) \n\r / ** snc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snc_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snc_update_accounts() \n\r -- => snc_unlock_account(callAccount) \n\r -- / ** snc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ snc_help() <-- You Are Here. ''')