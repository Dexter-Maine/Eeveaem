#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global swt_account_0_a
global swt_account_1_a
global swt_account_2_a
global swt_account_3_a
global swt_account_4_a
global swt_account_5_a
global swt_account_6_a
global swt_address
global swt_abi
global swt
global swt_call_0
global swt_call_1
global swt_call_2
global swt_call_3
global swt_call_4
global swt_call_5
global swt_call_6
global swt_call_ab
global swt_accounts
global swt_account_0_pw
global swt_account_1_pw
global swt_account_2_pw
global swt_account_3_pw
global swt_account_4_pw
global swt_account_5_pw
global swt_account_6_pw
global swt_account_0_n
global swt_account_1_n
global swt_account_2_n
global swt_account_3_n
global swt_account_4_n
global swt_account_5_n
global swt_account_6_n
global swt_account1pw
global swt_account2pw
global swt_account3pw
global swt_account4pw
global swt_account5pw
global swt_account6pw
global swt_last_price
global swt_accounts_range
global swt_tokenName
global swt_last_ethereum_price
global swt_unlockTime
global swt_balance
global swt_balanceOf
global swt_unlock
global swt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
swt_token_d = 1e18
_e_d = 1e18
swt_accounts_range = '[0, 6]'
swt_unlock = web3.personal.unlockAccount
swt_last_ethereum_price = 370.00
swt_last_price = 2.02
swt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
swt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
swt_tokenName = 'SwarmCity Token'
swt_unlockTime = hex(10000) # Must be hex()
swt_account_0_a = swt_accounts[0]
swt_account_1_a = swt_accounts[1]
swt_account_2_a = swt_accounts[2]
swt_account_3_a = swt_accounts[3]
swt_account_4_a = swt_accounts[4]
swt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
swt_account_6_a = swt_accounts[6]
# Supply Unlock Passwords For Transactions Below
swt_account_0_pw = 'GuildSkrypt2017!@#'
swt_account_1_pw = ''
swt_account_2_pw = 'GuildSkrypt2017!@#'
swt_account_3_pw = ''
swt_account_4_pw = ''
swt_account_5_pw = ''
swt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
swt_account_0_n = 'Skotys Bittrex Account'
swt_account_1_n = 'Jeffs Account'
swt_account_2_n = 'Skrypts Bittrex Account'
swt_account_3_n = 'Skotys Personal Account'
swt_account_4_n = 'Unknown'
swt_account_5_n = 'Watched \'Bittrex\' Account.'
swt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
swt_address = '0xB9e7F8568e08d5659f5D29C4997173d84CdF2607'
swt_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creationBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_blockNumber","type":"uint256"}],"name":"balanceOfAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_cloneTokenName","type":"string"},{"name":"_cloneDecimalUnits","type":"uint8"},{"name":"_cloneTokenSymbol","type":"string"},{"name":"_snapshotBlock","type":"uint256"},{"name":"_transfersEnabled","type":"bool"}],"name":"createCloneToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"generateTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_blockNumber","type":"uint256"}],"name":"totalSupplyAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentSnapShotBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroyTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_transfersEnabled","type":"bool"}],"name":"enableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[{"name":"_tokenFactory","type":"address"},{"name":"_parentToken","type":"address"},{"name":"_parentSnapShotBlock","type":"uint256"},{"name":"_tokenName","type":"string"},{"name":"_decimalUnits","type":"uint8"},{"name":"_tokenSymbol","type":"string"},{"name":"_transfersEnabled","type":"bool"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_cloneToken","type":"address"},{"indexed":false,"name":"_snapshotBlock","type":"uint256"}],"name":"NewCloneToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Approval","type":"event"}]
swt = web3.eth.contract(abi=swt_abi, address=swt_address)
swt_balanceOf = swt.call().balanceOf
# End Contract Information
def swt_update_accounts():
 global swt_account0
 global swt_account1
 global swt_account2
 global swt_account3
 global swt_account4
 global swt_account5
 global swt_account6
 global swt_account0_n
 global swt_account1_n
 global swt_account2_n
 global swt_account3_n
 global swt_account4_n
 global swt_account5_n
 global swt_account6_n
 global swt_account0pw
 global swt_account1pw
 global swt_account2pw
 global swt_account3pw
 global swt_account4pw
 global swt_account5pw
 global swt_account6pw
 swt_account0 = swt_account_0_a
 swt_account1 = swt_account_1_a
 swt_account2 = swt_account_2_a
 swt_account3 = swt_account_3_a
 swt_account4 = swt_account_4_a
 swt_account5 = swt_account_5_a
 swt_account6 = swt_account_6_a
 swt_account0_n = swt_account_0_n
 swt_account1_n = swt_account_1_n
 swt_account2_n = swt_account_2_n
 swt_account3_n = swt_account_3_n
 swt_account4_n = swt_account_4_n
 swt_account5_n = swt_account_5_n
 swt_account6_n = swt_account_6_n
 swt_account0pw = swt_account_0_pw
 swt_account1pw = swt_account_1_pw
 swt_account2pw = swt_account_2_pw
 swt_account3pw = swt_account_3_pw
 swt_account4pw = swt_account_4_pw
 swt_account5pw = swt_account_5_pw
 swt_account6pw = swt_account_6_pw
 print(swt_tokenName+' Accounts Updated.')
def swt_update_balances():
 global swt_call_0
 global swt_call_1
 global swt_call_2
 global swt_call_3
 global swt_call_4
 global swt_call_5
 global swt_call_6
 global swt_w_call_0
 global swt_w_call_1
 global swt_w_call_2
 global swt_w_call_3
 global swt_w_call_4
 global swt_w_call_5
 global swt_w_call_6
 swt_update_accounts()
 print('Updating '+swt_tokenName+' Balances Please Wait...')
 swt_call_0 = swt_balanceOf(swt_account0)
 swt_call_1 = swt_balanceOf(swt_account1)
 swt_call_2 = swt_balanceOf(swt_account2)
 swt_call_3 = swt_balanceOf(swt_account3)
 swt_call_4 = swt_balanceOf(swt_account4)
 swt_call_5 = swt_balanceOf(swt_account5)
 swt_call_6 = swt_balanceOf(swt_account6)
 swt_w_call_0 = swt_balance(swt_account0)
 swt_w_call_1 = swt_balance(swt_account1)
 swt_w_call_2 = swt_balance(swt_account2)
 swt_w_call_3 = swt_balance(swt_account3)
 swt_w_call_4 = swt_balance(swt_account4)
 swt_w_call_5 = swt_balance(swt_account5)
 swt_w_call_6 = swt_balance(swt_account6)
 print(swt_tokenName+' Balances Updated.')
def swt_list_all_accounts():
 swt_update_accounts()
 print(swt_tokenName+' '+swt_account0_n+': '+swt_account0)
 print(swt_tokenName+' '+swt_account1_n+': '+swt_account1)
 print(swt_tokenName+' '+swt_account2_n+': '+swt_account2)
 print(swt_tokenName+' '+swt_account3_n+': '+swt_account3)
 print(swt_tokenName+' '+swt_account4_n+': '+swt_account4)
 print(swt_tokenName+' '+swt_account5_n+': '+swt_account5)
 print(swt_tokenName+' '+swt_account6_n+': '+swt_account6)

def swt_account_balance(accountNumber):
 swt_update_balances()
 swt_ab_account_number = accountNumber
 swt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if swt_ab_account_number == swt_ab_input[0]:
  print('Calling '+swt_account0_n+' '+swt_tokenName+' Balance: ')
  print(swt_account0_n+': '+swt_tokenName+' Balance: '+str(swt_call_0 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_0 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[1]:
  print('Calling '+swt_account1_n+' '+swt_tokenName+' Balance: ')
  print(swt_account1_n+': '+swt_tokenName+' Balance: '+str(swt_call_1 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_1 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[2]:
  print('Calling '+swt_account2_n+' '+swt_tokenName+' Balance: ')
  print(swt_account2_n+': '+swt_tokenName+' Balance: '+str(swt_call_2 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_2 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[3]:
  print('Calling '+swt_account3_n+' '+swt_tokenName+' Balance: ')
  print(swt_account3_n+': '+swt_tokenName+' Balance: '+str(swt_call_3 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_3 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[4]:
  print('Calling '+swt_account4_n+' '+swt_tokenName+' Balance: ')
  print(swt_account4_n+': '+swt_tokenName+' Balance: '+str(swt_call_4 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_4 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[5]:
  print('Calling '+swt_account5_n+' '+swt_tokenName+' Balance: ')
  print(swt_account5_n+': '+swt_tokenName+' Balance: '+str(swt_call_5 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_5 / swt_token_d * swt_last_price))
 if swt_ab_account_number == swt_ab_input[6]:
  print('Calling '+swt_account6_n+' '+swt_tokenName+' Balance: ')
  print(swt_account6_n+': '+swt_tokenName+' Balance: '+str(swt_call_6 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_6 / swt_token_d * swt_last_price))
 if swt_ab_account_number not in swt_ab_input:
  print('Must Integer Within Range '+swt_accounts_range+'.')

def swt_list_all_account_balances():
 swt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+swt_tokenName+' Balance: ')
 print(swt_account0_n+': '+swt_tokenName+' Balance: '+str(swt_call_0 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_0 / swt_token_d * swt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(swt_account0_n+': Ethereum Balance '+str(swt_w_call_0 / _e_d)+' $'+str(swt_w_call_0 / _e_d * swt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+swt_tokenName+' Balance: ')
 print(swt_account1_n+': '+swt_tokenName+' Balance: '+str(swt_call_1 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_1 / swt_token_d * swt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(swt_account1_n+': Ethereum Balance '+str(swt_w_call_1 / _e_d)+' $'+str(swt_w_call_1 / _e_d * swt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+swt_tokenName+' Balance: ')
 print(swt_account2_n+': '+swt_tokenName+' Balance: '+str(swt_call_2 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_2 / swt_token_d * swt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(swt_account2_n+': Ethereum Balance '+str(swt_w_call_2 / _e_d)+' $'+str(swt_w_call_2 / _e_d * swt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+swt_tokenName+' Balance: ')
 print(swt_account3_n+': '+swt_tokenName+' Balance: '+str(swt_call_3 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_3 / swt_token_d * swt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(swt_account3_n+': Ethereum Balance '+str(swt_w_call_3 / _e_d)+' $'+str(swt_w_call_3 / _e_d * swt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+swt_tokenName+' Balance: ')
 print(swt_account4_n+': '+swt_tokenName+' Balance: '+str(swt_call_4 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_4 / swt_token_d * swt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(swt_account4_n+': Ethereum Balance '+str(swt_w_call_4 / _e_d)+' $'+str(swt_w_call_4 / _e_d * swt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+swt_tokenName+' Balance: ')
 print(swt_account5_n+': '+swt_tokenName+' Balance: '+str(swt_call_5 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_5 / swt_token_d * swt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(swt_account5_n+': Ethereum Balance '+str(swt_w_call_5 / _e_d)+' $'+str(swt_w_call_5 /_e_d * swt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+swt_tokenName+' Balance: ')
 print(swt_account6_n+': '+swt_tokenName+' Balance: '+str(swt_call_6 / swt_token_d)+' Usd/'+swt_tokenName+' Balance: $'+str(swt_call_6 / swt_token_d * swt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(swt_account6_n+': Ethereum Balance '+str(swt_w_call_6 / _e_d)+' $'+str(swt_w_call_6 / _e_d * swt_last_ethereum_price))
def swt_unlock_all_accounts():
  swt_unlock_account_0()
  swt_unlock_account_1()
  swt_unlock_account_2()
  swt_unlock_account_3()
  swt_unlock_account_4()
  swt_unlock_account_5()
  swt_unlock_account_6()


def swt_unlock_account_0():
  global swt_account0pw
  global swt_account0
  global swt_account0_n
  swt_update_accounts()
  swt_u_a_0 = swt_w_unlock(swt_account0, swt_account0pw, swt_unlockTime)
  if swt_u_a_0 == False:
    if swt_account0pw == '':
     swt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account0_n+' Passphrase Denied: '+swt_account0pw_r)
    elif swt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+swt_account0_n+' Passphrase Denied: '+swt_account0pw)
  if swt_u_a_0 == True:
   print(swt_account0_n+' Unlocked')

def swt_unlock_account_1():
  global swt_account1pw
  global swt_account1
  global swt_account1_n
  swt_update_accounts()
  swt_u_a_1 = swt_unlock(swt_account1, swt_account1pw, swt_unlockTime)
  if swt_u_a_1 == False:
    if swt_account1pw == '':
     swt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account1_n+' Passphrase Denied: '+swt_account1pw_r)
    elif swt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+swt_account1_n+' Passphrase Denied: '+swt_account1pw)
  if swt_u_a_1 == True:
   print(swt_account1_n+' Unlocked')

def swt_unlock_account_2():
  global swt_account2pw
  global swt_account2
  global swt_account2_n
  swt_update_accounts()
  swt_u_a_2 = swt_unlock(swt_account2, swt_account2pw, swt_unlockTime)
  if swt_u_a_2 == False:
    if swt_account2pw == '':
     swt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account2_n+' Passphrase Denied: '+swt_account2pw_r)
    elif swt_account2pw != '':
     print('Unlock Failure With Account '+swt_account2_n+' Passphrase Denied: '+swt_account2pw)
  if swt_u_a_2 == True:
   print(swt_account2_n+' Unlocked')

def swt_unlock_account_3():
  global swt_account3pw
  global swt_account3
  global swt_account3_n
  swt_update_accounts()
  swt_u_a_3 = swt_unlock(swt_account3, swt_account3pw, swt_unlockTime)
  if swt_u_a_3 == False:
    if swt_account3pw == '':
     swt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account3_n+' Passphrase Denied: '+swt_account3pw_r)
    elif swt_account3pw != '':
     print('Unlock Failure With Account '+swt_account3_n+' Passphrase Denied: '+swt_account3pw)
  if swt_u_a_3 == True:
   print(swt_account3_n+' Unlocked')

def swt_unlock_account_4():
  global swt_account4pw
  global swt_account4
  global swt_account4_n
  swt_update_accounts()
  swt_u_a_4 = swt_unlock(swt_account4, swt_account4pw, swt_unlockTime)
  if swt_u_a_4 == False:
    if swt_account4pw == '':
     swt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account4_n+' Passphrase Denied: '+swt_account4pw_r)
    elif swt_account4pw != '':
     print('Unlock Failure With Account '+swt_account4_n+' Passphrase Denied: '+swt_account4pw)
  if swt_u_a_4 == True:
   print(swt_account4_n+' Unlocked')

def swt_unlock_account_5():
  global swt_account5pw
  global swt_account5
  global swt_account5_n
  swt_update_accounts()
  swt_u_a_5 = swt_unlock(swt_account5, swt_account5pw, swt_unlockTime)
  if swt_u_a_5 == False:
    if swt_account5pw == '':
     swt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account5_n+' Passphrase Denied: '+swt_account5pw_r)
    elif swt_account5pw != '':
     print('Unlock Failure With Account '+swt_account5_n+' Passphrase Denied: '+swt_account5pw)
  if swt_u_a_5 == True:
   print(swt_account5_n+' Unlocked')

def swt_unlock_account_6():
  global swt_account6pw
  global swt_account6
  global swt_account6_n
  swt_update_accounts()
  swt_u_a_6 = swt_unlock(swt_account6, swt_account6pw, swt_unlockTime)
  if swt_u_a_6 == False:
    if swt_account6pw == '':
     swt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+swt_account6_n+' Passphrase Denied: '+swt_account6pw_r)
    elif swt_account6pw != '':
     print('Unlock Failure With Account '+swt_account6_n+' Passphrase Denied: '+swt_account6pw)
  if swt_u_a_6 == True:
   print(swt_account6_n+' Unlocked')

def swt_unlock_account(swt_ua_accountNumber):
 swt_update_accounts()
 swt_ua_account_number = swt_ua_accountNumber
 swt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if swt_ua_account_number == swt_ua_input[0]:
  swt_unlock_account_0()
 if swt_ua_account_number == swt_ua_input[1]:
  swt_unlock_account_1()
 if swt_ua_account_number == swt_ua_input[2]:
  swt_unlock_account_2()
 if swt_ua_account_number == swt_ua_input[3]:
  swt_unlock_account_3()
 if swt_ua_account_number == swt_ua_input[4]:
  swt_unlock_account_4()
 if swt_ua_account_number == swt_ua_input[5]:
  swt_unlock_account_5()
 if swt_ua_account_number == swt_ua_input[6]:
  swt_unlock_account_6()
 if swt_ua_account_number not in swt_ua_input:
  print('Must Integer Within Range '+swt_accounts_range+'.')
 

def swt_approve_between_accounts(fromAccount, toAccount, msgValue):
  swt_update_accounts()
  swt_a_0 = swt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(swt_a_0)

def swt_approve(fromAccountNumber, toAddress, msgValue):
  swt_update_accounts()
  swt_unlock_account(fromAccountNumber)
  swt_a_1 = swt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(swt_a_1)

def swt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  swt_update_accounts()
  swt_unlock_account(fromAccount)
  swt_t_0 = swt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(swt_t_0)

def swt_transfer(fromAccountNumber, toAddress, msgValue):
  swt_update_accounts()
  swt_unlock_account(fromAccountNumber)
  swt_t_1 = swt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(swt_t_1)

def swt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  swt_update_accounts()
  swt_unlock_account(callAccount)
  swt_tf_0 = swt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(swt_tf_0)

def swt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  swt_update_accounts()
  swt_unlock_account(callAccount)
  swt_tf_1 = swt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(swt_tf_1)
  


def swt_help():
  print('Following Functions For '+swt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * swt_unlock => web3.personal.unlockAccount
/ * swt_accounts => web3.personal.listAccounts
/ * swt_balance = web3.eth.getBalance
** swt => web3.eth.contract(abi=swt_abi, address=swt_address)
** / * swt_balanceOf => swt.call().balanceOf

~ Function Listing Below:
~ swt_update_accounts()
~ swt_update_balances() \n\r -- => swt_update_accounts()
~ swt_list_all_accounts() \n\r -- => swt_update_accounts()
~ swt_account_balance(accountNumber) \n\r -- => swt_update_balances() 
~ swt_list_all_account_balances() \n\r -- => swt_update_balances()
~ swt_unlock_all_accounts() \n\r -- => swt_unlock_account_0() \n\r -- => swt_unlock_account_1() \n\r -- => swt_unlock_account_2() \n\r -- => swt_unlock_account_3() \n\r -- => swt_unlock_account_4() \n\r -- => swt_unlock_account_5() \n\r -- => swt_unlock_account_6() 
~ swt_unlock_account_0() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account0, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_1() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account1, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_2() \n\r -- => swt_update_accounts() \n\r --/ *swt_w_unlock(swt_account2, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_3() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account3, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_4() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account4, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_5() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account5, swt_account0pw, swt_unlockTime)
~ swt_unlock_account_6() \n\r -- => swt_update_accounts() \n\r -- / *swt_w_unlock(swt_account6, swt_account0pw, swt_unlockTime)
~ swt_unlock_account(swt_ua_accountNumber) \n\r -- => swt_update_accounts() \n\r -- // swt_unlock_account_0() \n\r -- // swt_unlock_account_1() \n\r -- // swt_unlock_account_2() \n\r -- // swt_unlock_account_3() \n\r -- // swt_unlock_account_4() \n\r -- // swt_unlock_account_5() \n\r -- // swt_unlock_account_6()
~ swt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(fromAccount) \n\r -- / ** swt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ swt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(fromAccountNumber) \n\r -- / ** swt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ swt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(fromAccount) \n\r -- / ** swt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ swt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(fromAccountNumber) \n\r -- / ** swt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ swt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(callAccount) \n\r / ** swt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ swt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => swt_update_accounts() \n\r -- => swt_unlock_account(callAccount) \n\r -- / ** swt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ swt_help() <-- You Are Here. ''')