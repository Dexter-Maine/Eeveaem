#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global storj_account_0_a
global storj_account_1_a
global storj_account_2_a
global storj_account_3_a
global storj_account_4_a
global storj_account_5_a
global storj_account_6_a
global storj_address
global storj_abi
global storj
global storj_call_0
global storj_call_1
global storj_call_2
global storj_call_3
global storj_call_4
global storj_call_5
global storj_call_6
global storj_call_ab
global storj_accounts
global storj_account_0_pw
global storj_account_1_pw
global storj_account_2_pw
global storj_account_3_pw
global storj_account_4_pw
global storj_account_5_pw
global storj_account_6_pw
global storj_account_0_n
global storj_account_1_n
global storj_account_2_n
global storj_account_3_n
global storj_account_4_n
global storj_account_5_n
global storj_account_6_n
global storj_account1pw
global storj_account2pw
global storj_account3pw
global storj_account4pw
global storj_account5pw
global storj_account6pw
global storj_last_price
global storj_accounts_range
global storj_tokenName
global storj_last_ethereum_price
global storj_unlockTime
global storj_balance
global storj_balanceOf
global storj_unlock
global storj_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
storj_token_d = 1e8
_e_d = 1e18
storj_accounts_range = '[0, 6]'
storj_unlock = web3.personal.unlockAccount
storj_last_ethereum_price = 370.00
storj_last_price = 0.97
storj_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
storj_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
storj_tokenName = 'Storj Token'
storj_unlockTime = hex(10000) # Must be hex()
storj_account_0_a = storj_accounts[0]
storj_account_1_a = storj_accounts[1]
storj_account_2_a = storj_accounts[2]
storj_account_3_a = storj_accounts[3]
storj_account_4_a = storj_accounts[4]
storj_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
storj_account_6_a = storj_accounts[6]
# Supply Unlock Passwords For Transactions Below
storj_account_0_pw = 'GuildSkrypt2017!@#'
storj_account_1_pw = ''
storj_account_2_pw = 'GuildSkrypt2017!@#'
storj_account_3_pw = ''
storj_account_4_pw = ''
storj_account_5_pw = ''
storj_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
storj_account_0_n = 'Skotys Bittrex Account'
storj_account_1_n = 'Jeffs Account'
storj_account_2_n = 'Skrypts Bittrex Account'
storj_account_3_n = 'Skotys Personal Account'
storj_account_4_n = 'Unknown'
storj_account_5_n = 'Watched \'Bittrex\' Account.'
storj_account_6_n = 'Watched Account (1)'
# Contract Information Below :
storj_address = '0xB64ef51C888972c908CFacf59B47C1AfBC0Ab8aC'
storj_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"burnAmount","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"upgrade","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getUpgradeState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"canUpgrade","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalUpgraded","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"agent","type":"address"}],"name":"setUpgradeAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isToken","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"BURN_ADDRESS","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"master","type":"address"}],"name":"setUpgradeMaster","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_owner","type":"address"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_totalSupply","type":"uint256"},{"name":"_decimals","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Upgrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"agent","type":"address"}],"name":"UpgradeAgentSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"burner","type":"address"},{"indexed":false,"name":"burnedAmount","type":"uint256"}],"name":"Burned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
storj = web3.eth.contract(abi=storj_abi, address=storj_address)
storj_balanceOf = storj.call().balanceOf
# End Contract Information
def storj_update_accounts():
 global storj_account0
 global storj_account1
 global storj_account2
 global storj_account3
 global storj_account4
 global storj_account5
 global storj_account6
 global storj_account0_n
 global storj_account1_n
 global storj_account2_n
 global storj_account3_n
 global storj_account4_n
 global storj_account5_n
 global storj_account6_n
 global storj_account0pw
 global storj_account1pw
 global storj_account2pw
 global storj_account3pw
 global storj_account4pw
 global storj_account5pw
 global storj_account6pw
 storj_account0 = storj_account_0_a
 storj_account1 = storj_account_1_a
 storj_account2 = storj_account_2_a
 storj_account3 = storj_account_3_a
 storj_account4 = storj_account_4_a
 storj_account5 = storj_account_5_a
 storj_account6 = storj_account_6_a
 storj_account0_n = storj_account_0_n
 storj_account1_n = storj_account_1_n
 storj_account2_n = storj_account_2_n
 storj_account3_n = storj_account_3_n
 storj_account4_n = storj_account_4_n
 storj_account5_n = storj_account_5_n
 storj_account6_n = storj_account_6_n
 storj_account0pw = storj_account_0_pw
 storj_account1pw = storj_account_1_pw
 storj_account2pw = storj_account_2_pw
 storj_account3pw = storj_account_3_pw
 storj_account4pw = storj_account_4_pw
 storj_account5pw = storj_account_5_pw
 storj_account6pw = storj_account_6_pw
 print(storj_tokenName+' Accounts Updated.')
def storj_update_balances():
 global storj_call_0
 global storj_call_1
 global storj_call_2
 global storj_call_3
 global storj_call_4
 global storj_call_5
 global storj_call_6
 global storj_w_call_0
 global storj_w_call_1
 global storj_w_call_2
 global storj_w_call_3
 global storj_w_call_4
 global storj_w_call_5
 global storj_w_call_6
 storj_update_accounts()
 print('Updating '+storj_tokenName+' Balances Please Wait...')
 storj_call_0 = storj_balanceOf(storj_account0)
 storj_call_1 = storj_balanceOf(storj_account1)
 storj_call_2 = storj_balanceOf(storj_account2)
 storj_call_3 = storj_balanceOf(storj_account3)
 storj_call_4 = storj_balanceOf(storj_account4)
 storj_call_5 = storj_balanceOf(storj_account5)
 storj_call_6 = storj_balanceOf(storj_account6)
 storj_w_call_0 = storj_balance(storj_account0)
 storj_w_call_1 = storj_balance(storj_account1)
 storj_w_call_2 = storj_balance(storj_account2)
 storj_w_call_3 = storj_balance(storj_account3)
 storj_w_call_4 = storj_balance(storj_account4)
 storj_w_call_5 = storj_balance(storj_account5)
 storj_w_call_6 = storj_balance(storj_account6)
 print(storj_tokenName+' Balances Updated.')
def storj_list_all_accounts():
 storj_update_accounts()
 print(storj_tokenName+' '+storj_account0_n+': '+storj_account0)
 print(storj_tokenName+' '+storj_account1_n+': '+storj_account1)
 print(storj_tokenName+' '+storj_account2_n+': '+storj_account2)
 print(storj_tokenName+' '+storj_account3_n+': '+storj_account3)
 print(storj_tokenName+' '+storj_account4_n+': '+storj_account4)
 print(storj_tokenName+' '+storj_account5_n+': '+storj_account5)
 print(storj_tokenName+' '+storj_account6_n+': '+storj_account6)

def storj_account_balance(accountNumber):
 storj_update_balances()
 storj_ab_account_number = accountNumber
 storj_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if storj_ab_account_number == storj_ab_input[0]:
  print('Calling '+storj_account0_n+' '+storj_tokenName+' Balance: ')
  print(storj_account0_n+': '+storj_tokenName+' Balance: '+str(storj_call_0 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_0 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[1]:
  print('Calling '+storj_account1_n+' '+storj_tokenName+' Balance: ')
  print(storj_account1_n+': '+storj_tokenName+' Balance: '+str(storj_call_1 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_1 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[2]:
  print('Calling '+storj_account2_n+' '+storj_tokenName+' Balance: ')
  print(storj_account2_n+': '+storj_tokenName+' Balance: '+str(storj_call_2 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_2 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[3]:
  print('Calling '+storj_account3_n+' '+storj_tokenName+' Balance: ')
  print(storj_account3_n+': '+storj_tokenName+' Balance: '+str(storj_call_3 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_3 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[4]:
  print('Calling '+storj_account4_n+' '+storj_tokenName+' Balance: ')
  print(storj_account4_n+': '+storj_tokenName+' Balance: '+str(storj_call_4 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_4 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[5]:
  print('Calling '+storj_account5_n+' '+storj_tokenName+' Balance: ')
  print(storj_account5_n+': '+storj_tokenName+' Balance: '+str(storj_call_5 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_5 / storj_token_d * storj_last_price))
 if storj_ab_account_number == storj_ab_input[6]:
  print('Calling '+storj_account6_n+' '+storj_tokenName+' Balance: ')
  print(storj_account6_n+': '+storj_tokenName+' Balance: '+str(storj_call_6 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_6 / storj_token_d * storj_last_price))
 if storj_ab_account_number not in storj_ab_input:
  print('Must Integer Within Range '+storj_accounts_range+'.')

def storj_list_all_account_balances():
 storj_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+storj_tokenName+' Balance: ')
 print(storj_account0_n+': '+storj_tokenName+' Balance: '+str(storj_call_0 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_0 / storj_token_d * storj_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(storj_account0_n+': Ethereum Balance '+str(storj_w_call_0 / _e_d)+' $'+str(storj_w_call_0 / _e_d * storj_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+storj_tokenName+' Balance: ')
 print(storj_account1_n+': '+storj_tokenName+' Balance: '+str(storj_call_1 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_1 / storj_token_d * storj_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(storj_account1_n+': Ethereum Balance '+str(storj_w_call_1 / _e_d)+' $'+str(storj_w_call_1 / _e_d * storj_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+storj_tokenName+' Balance: ')
 print(storj_account2_n+': '+storj_tokenName+' Balance: '+str(storj_call_2 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_2 / storj_token_d * storj_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(storj_account2_n+': Ethereum Balance '+str(storj_w_call_2 / _e_d)+' $'+str(storj_w_call_2 / _e_d * storj_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+storj_tokenName+' Balance: ')
 print(storj_account3_n+': '+storj_tokenName+' Balance: '+str(storj_call_3 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_3 / storj_token_d * storj_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(storj_account3_n+': Ethereum Balance '+str(storj_w_call_3 / _e_d)+' $'+str(storj_w_call_3 / _e_d * storj_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+storj_tokenName+' Balance: ')
 print(storj_account4_n+': '+storj_tokenName+' Balance: '+str(storj_call_4 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_4 / storj_token_d * storj_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(storj_account4_n+': Ethereum Balance '+str(storj_w_call_4 / _e_d)+' $'+str(storj_w_call_4 / _e_d * storj_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+storj_tokenName+' Balance: ')
 print(storj_account5_n+': '+storj_tokenName+' Balance: '+str(storj_call_5 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_5 / storj_token_d * storj_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(storj_account5_n+': Ethereum Balance '+str(storj_w_call_5 / _e_d)+' $'+str(storj_w_call_5 /_e_d * storj_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+storj_tokenName+' Balance: ')
 print(storj_account6_n+': '+storj_tokenName+' Balance: '+str(storj_call_6 / storj_token_d)+' Usd/'+storj_tokenName+' Balance: $'+str(storj_call_6 / storj_token_d * storj_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(storj_account6_n+': Ethereum Balance '+str(storj_w_call_6 / _e_d)+' $'+str(storj_w_call_6 / _e_d * storj_last_ethereum_price))
def storj_unlock_all_accounts():
  storj_unlock_account_0()
  storj_unlock_account_1()
  storj_unlock_account_2()
  storj_unlock_account_3()
  storj_unlock_account_4()
  storj_unlock_account_5()
  storj_unlock_account_6()


def storj_unlock_account_0():
  global storj_account0pw
  global storj_account0
  global storj_account0_n
  storj_update_accounts()
  storj_u_a_0 = storj_w_unlock(storj_account0, storj_account0pw, storj_unlockTime)
  if storj_u_a_0 == False:
    if storj_account0pw == '':
     storj_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account0_n+' Passphrase Denied: '+storj_account0pw_r)
    elif storj_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+storj_account0_n+' Passphrase Denied: '+storj_account0pw)
  if storj_u_a_0 == True:
   print(storj_account0_n+' Unlocked')

def storj_unlock_account_1():
  global storj_account1pw
  global storj_account1
  global storj_account1_n
  storj_update_accounts()
  storj_u_a_1 = storj_unlock(storj_account1, storj_account1pw, storj_unlockTime)
  if storj_u_a_1 == False:
    if storj_account1pw == '':
     storj_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account1_n+' Passphrase Denied: '+storj_account1pw_r)
    elif storj_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+storj_account1_n+' Passphrase Denied: '+storj_account1pw)
  if storj_u_a_1 == True:
   print(storj_account1_n+' Unlocked')

def storj_unlock_account_2():
  global storj_account2pw
  global storj_account2
  global storj_account2_n
  storj_update_accounts()
  storj_u_a_2 = storj_unlock(storj_account2, storj_account2pw, storj_unlockTime)
  if storj_u_a_2 == False:
    if storj_account2pw == '':
     storj_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account2_n+' Passphrase Denied: '+storj_account2pw_r)
    elif storj_account2pw != '':
     print('Unlock Failure With Account '+storj_account2_n+' Passphrase Denied: '+storj_account2pw)
  if storj_u_a_2 == True:
   print(storj_account2_n+' Unlocked')

def storj_unlock_account_3():
  global storj_account3pw
  global storj_account3
  global storj_account3_n
  storj_update_accounts()
  storj_u_a_3 = storj_unlock(storj_account3, storj_account3pw, storj_unlockTime)
  if storj_u_a_3 == False:
    if storj_account3pw == '':
     storj_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account3_n+' Passphrase Denied: '+storj_account3pw_r)
    elif storj_account3pw != '':
     print('Unlock Failure With Account '+storj_account3_n+' Passphrase Denied: '+storj_account3pw)
  if storj_u_a_3 == True:
   print(storj_account3_n+' Unlocked')

def storj_unlock_account_4():
  global storj_account4pw
  global storj_account4
  global storj_account4_n
  storj_update_accounts()
  storj_u_a_4 = storj_unlock(storj_account4, storj_account4pw, storj_unlockTime)
  if storj_u_a_4 == False:
    if storj_account4pw == '':
     storj_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account4_n+' Passphrase Denied: '+storj_account4pw_r)
    elif storj_account4pw != '':
     print('Unlock Failure With Account '+storj_account4_n+' Passphrase Denied: '+storj_account4pw)
  if storj_u_a_4 == True:
   print(storj_account4_n+' Unlocked')

def storj_unlock_account_5():
  global storj_account5pw
  global storj_account5
  global storj_account5_n
  storj_update_accounts()
  storj_u_a_5 = storj_unlock(storj_account5, storj_account5pw, storj_unlockTime)
  if storj_u_a_5 == False:
    if storj_account5pw == '':
     storj_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account5_n+' Passphrase Denied: '+storj_account5pw_r)
    elif storj_account5pw != '':
     print('Unlock Failure With Account '+storj_account5_n+' Passphrase Denied: '+storj_account5pw)
  if storj_u_a_5 == True:
   print(storj_account5_n+' Unlocked')

def storj_unlock_account_6():
  global storj_account6pw
  global storj_account6
  global storj_account6_n
  storj_update_accounts()
  storj_u_a_6 = storj_unlock(storj_account6, storj_account6pw, storj_unlockTime)
  if storj_u_a_6 == False:
    if storj_account6pw == '':
     storj_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+storj_account6_n+' Passphrase Denied: '+storj_account6pw_r)
    elif storj_account6pw != '':
     print('Unlock Failure With Account '+storj_account6_n+' Passphrase Denied: '+storj_account6pw)
  if storj_u_a_6 == True:
   print(storj_account6_n+' Unlocked')

def storj_unlock_account(storj_ua_accountNumber):
 storj_update_accounts()
 storj_ua_account_number = storj_ua_accountNumber
 storj_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if storj_ua_account_number == storj_ua_input[0]:
  storj_unlock_account_0()
 if storj_ua_account_number == storj_ua_input[1]:
  storj_unlock_account_1()
 if storj_ua_account_number == storj_ua_input[2]:
  storj_unlock_account_2()
 if storj_ua_account_number == storj_ua_input[3]:
  storj_unlock_account_3()
 if storj_ua_account_number == storj_ua_input[4]:
  storj_unlock_account_4()
 if storj_ua_account_number == storj_ua_input[5]:
  storj_unlock_account_5()
 if storj_ua_account_number == storj_ua_input[6]:
  storj_unlock_account_6()
 if storj_ua_account_number not in storj_ua_input:
  print('Must Integer Within Range '+storj_accounts_range+'.')
 

def storj_approve_between_accounts(fromAccount, toAccount, msgValue):
  storj_update_accounts()
  storj_a_0 = storj.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(storj_a_0)

def storj_approve(fromAccountNumber, toAddress, msgValue):
  storj_update_accounts()
  storj_unlock_account(fromAccountNumber)
  storj_a_1 = storj.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(storj_a_1)

def storj_transfer_between_accounts(fromAccount, toAccount, msgValue):
  storj_update_accounts()
  storj_unlock_account(fromAccount)
  storj_t_0 = storj.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(storj_t_0)

def storj_transfer(fromAccountNumber, toAddress, msgValue):
  storj_update_accounts()
  storj_unlock_account(fromAccountNumber)
  storj_t_1 = storj.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(storj_t_1)

def storj_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  storj_update_accounts()
  storj_unlock_account(callAccount)
  storj_tf_0 = storj.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(storj_tf_0)

def storj_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  storj_update_accounts()
  storj_unlock_account(callAccount)
  storj_tf_1 = storj.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(storj_tf_1)
  


def storj_help():
  print('Following Functions For '+storj_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * storj_unlock => web3.personal.unlockAccount
/ * storj_accounts => web3.personal.listAccounts
/ * storj_balance = web3.eth.getBalance
** storj => web3.eth.contract(abi=storj_abi, address=storj_address)
** / * storj_balanceOf => storj.call().balanceOf

~ Function Listing Below:
~ storj_update_accounts()
~ storj_update_balances() \n\r -- => storj_update_accounts()
~ storj_list_all_accounts() \n\r -- => storj_update_accounts()
~ storj_account_balance(accountNumber) \n\r -- => storj_update_balances() 
~ storj_list_all_account_balances() \n\r -- => storj_update_balances()
~ storj_unlock_all_accounts() \n\r -- => storj_unlock_account_0() \n\r -- => storj_unlock_account_1() \n\r -- => storj_unlock_account_2() \n\r -- => storj_unlock_account_3() \n\r -- => storj_unlock_account_4() \n\r -- => storj_unlock_account_5() \n\r -- => storj_unlock_account_6() 
~ storj_unlock_account_0() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account0, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_1() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account1, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_2() \n\r -- => storj_update_accounts() \n\r --/ *storj_w_unlock(storj_account2, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_3() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account3, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_4() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account4, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_5() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account5, storj_account0pw, storj_unlockTime)
~ storj_unlock_account_6() \n\r -- => storj_update_accounts() \n\r -- / *storj_w_unlock(storj_account6, storj_account0pw, storj_unlockTime)
~ storj_unlock_account(storj_ua_accountNumber) \n\r -- => storj_update_accounts() \n\r -- // storj_unlock_account_0() \n\r -- // storj_unlock_account_1() \n\r -- // storj_unlock_account_2() \n\r -- // storj_unlock_account_3() \n\r -- // storj_unlock_account_4() \n\r -- // storj_unlock_account_5() \n\r -- // storj_unlock_account_6()
~ storj_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(fromAccount) \n\r -- / ** storj.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ storj_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(fromAccountNumber) \n\r -- / ** storj.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ storj_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(fromAccount) \n\r -- / ** storj.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ storj_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(fromAccountNumber) \n\r -- / ** storj.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ storj_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(callAccount) \n\r / ** storj.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ storj_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => storj_update_accounts() \n\r -- => storj_unlock_account(callAccount) \n\r -- / ** storj.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ storj_help() <-- You Are Here. ''')