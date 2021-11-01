#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global gnt_account_0_a
global gnt_account_1_a
global gnt_account_2_a
global gnt_account_3_a
global gnt_account_4_a
global gnt_account_5_a
global gnt_account_6_a
global gnt_address
global gnt_abi
global gnt
global gnt_call_0
global gnt_call_1
global gnt_call_2
global gnt_call_3
global gnt_call_4
global gnt_call_5
global gnt_call_6
global gnt_call_ab
global gnt_accounts
global gnt_account_0_pw
global gnt_account_1_pw
global gnt_account_2_pw
global gnt_account_3_pw
global gnt_account_4_pw
global gnt_account_5_pw
global gnt_account_6_pw
global gnt_account_0_n
global gnt_account_1_n
global gnt_account_2_n
global gnt_account_3_n
global gnt_account_4_n
global gnt_account_5_n
global gnt_account_6_n
global gnt_account1pw
global gnt_account2pw
global gnt_account3pw
global gnt_account4pw
global gnt_account5pw
global gnt_account6pw
global gnt_last_price
global gnt_accounts_range
global gnt_tokenName
global gnt_last_ethereum_price
global gnt_unlockTime
global gnt_balance
global gnt_balanceOf
global gnt_unlock
global gnt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
gnt_token_d = 1e18
_e_d = 1e18
gnt_accounts_range = '[0, 6]'
gnt_unlock = web3.personal.unlockAccount
gnt_last_ethereum_price = 370.00
gnt_last_price = 0.32
gnt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
gnt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
gnt_tokenName = 'Golem Token'
gnt_unlockTime = hex(10000) # Must be hex()
gnt_account_0_a = gnt_accounts[0]
gnt_account_1_a = gnt_accounts[1]
gnt_account_2_a = gnt_accounts[2]
gnt_account_3_a = gnt_accounts[3]
gnt_account_4_a = gnt_accounts[4]
gnt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
gnt_account_6_a = gnt_accounts[6]
# Supply Unlock Passwords For Transactions Below
gnt_account_0_pw = 'GuildSkrypt2017!@#'
gnt_account_1_pw = ''
gnt_account_2_pw = 'GuildSkrypt2017!@#'
gnt_account_3_pw = ''
gnt_account_4_pw = ''
gnt_account_5_pw = ''
gnt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
gnt_account_0_n = 'Skotys Bittrex Account'
gnt_account_1_n = 'Jeffs Account'
gnt_account_2_n = 'Skrypts Bittrex Account'
gnt_account_3_n = 'Skotys Personal Account'
gnt_account_4_n = 'Unknown'
gnt_account_5_n = 'Watched \'Bittrex\' Account.'
gnt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
gnt_address = '0xa74476443119A942dE498590Fe1f2454d7D4aC0d'
gnt_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"golemFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_master","type":"address"}],"name":"setMigrationMaster","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"migrate","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"migrationMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationCap","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_agent","type":"address"}],"name":"setMigrationAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"migrationAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingEndBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalMigrated","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationMin","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"funding","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingStartBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"create","outputs":[],"payable":true,"type":"function"},{"inputs":[{"name":"_golemFactory","type":"address"},{"name":"_migrationMaster","type":"address"},{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingEndBlock","type":"uint256"}],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Migrate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Refund","type":"event"}]
gnt = web3.eth.contract(abi=gnt_abi, address=gnt_address)
gnt_balanceOf = gnt.call().balanceOf
# End Contract Information
def gnt_update_accounts():
 global gnt_account0
 global gnt_account1
 global gnt_account2
 global gnt_account3
 global gnt_account4
 global gnt_account5
 global gnt_account6
 global gnt_account0_n
 global gnt_account1_n
 global gnt_account2_n
 global gnt_account3_n
 global gnt_account4_n
 global gnt_account5_n
 global gnt_account6_n
 global gnt_account0pw
 global gnt_account1pw
 global gnt_account2pw
 global gnt_account3pw
 global gnt_account4pw
 global gnt_account5pw
 global gnt_account6pw
 gnt_account0 = gnt_account_0_a
 gnt_account1 = gnt_account_1_a
 gnt_account2 = gnt_account_2_a
 gnt_account3 = gnt_account_3_a
 gnt_account4 = gnt_account_4_a
 gnt_account5 = gnt_account_5_a
 gnt_account6 = gnt_account_6_a
 gnt_account0_n = gnt_account_0_n
 gnt_account1_n = gnt_account_1_n
 gnt_account2_n = gnt_account_2_n
 gnt_account3_n = gnt_account_3_n
 gnt_account4_n = gnt_account_4_n
 gnt_account5_n = gnt_account_5_n
 gnt_account6_n = gnt_account_6_n
 gnt_account0pw = gnt_account_0_pw
 gnt_account1pw = gnt_account_1_pw
 gnt_account2pw = gnt_account_2_pw
 gnt_account3pw = gnt_account_3_pw
 gnt_account4pw = gnt_account_4_pw
 gnt_account5pw = gnt_account_5_pw
 gnt_account6pw = gnt_account_6_pw
 print(gnt_tokenName+' Accounts Updated.')
def gnt_update_balances():
 global gnt_call_0
 global gnt_call_1
 global gnt_call_2
 global gnt_call_3
 global gnt_call_4
 global gnt_call_5
 global gnt_call_6
 global gnt_w_call_0
 global gnt_w_call_1
 global gnt_w_call_2
 global gnt_w_call_3
 global gnt_w_call_4
 global gnt_w_call_5
 global gnt_w_call_6
 gnt_update_accounts()
 print('Updating '+gnt_tokenName+' Balances Please Wait...')
 gnt_call_0 = gnt_balanceOf(gnt_account0)
 gnt_call_1 = gnt_balanceOf(gnt_account1)
 gnt_call_2 = gnt_balanceOf(gnt_account2)
 gnt_call_3 = gnt_balanceOf(gnt_account3)
 gnt_call_4 = gnt_balanceOf(gnt_account4)
 gnt_call_5 = gnt_balanceOf(gnt_account5)
 gnt_call_6 = gnt_balanceOf(gnt_account6)
 gnt_w_call_0 = gnt_balance(gnt_account0)
 gnt_w_call_1 = gnt_balance(gnt_account1)
 gnt_w_call_2 = gnt_balance(gnt_account2)
 gnt_w_call_3 = gnt_balance(gnt_account3)
 gnt_w_call_4 = gnt_balance(gnt_account4)
 gnt_w_call_5 = gnt_balance(gnt_account5)
 gnt_w_call_6 = gnt_balance(gnt_account6)
 print(gnt_tokenName+' Balances Updated.')
def gnt_list_all_accounts():
 gnt_update_accounts()
 print(gnt_tokenName+' '+gnt_account0_n+': '+gnt_account0)
 print(gnt_tokenName+' '+gnt_account1_n+': '+gnt_account1)
 print(gnt_tokenName+' '+gnt_account2_n+': '+gnt_account2)
 print(gnt_tokenName+' '+gnt_account3_n+': '+gnt_account3)
 print(gnt_tokenName+' '+gnt_account4_n+': '+gnt_account4)
 print(gnt_tokenName+' '+gnt_account5_n+': '+gnt_account5)
 print(gnt_tokenName+' '+gnt_account6_n+': '+gnt_account6)

def gnt_account_balance(accountNumber):
 gnt_update_balances()
 gnt_ab_account_number = accountNumber
 gnt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if gnt_ab_account_number == gnt_ab_input[0]:
  print('Calling '+gnt_account0_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account0_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_0 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_0 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[1]:
  print('Calling '+gnt_account1_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account1_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_1 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_1 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[2]:
  print('Calling '+gnt_account2_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account2_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_2 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_2 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[3]:
  print('Calling '+gnt_account3_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account3_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_3 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_3 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[4]:
  print('Calling '+gnt_account4_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account4_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_4 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_4 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[5]:
  print('Calling '+gnt_account5_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account5_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_5 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_5 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number == gnt_ab_input[6]:
  print('Calling '+gnt_account6_n+' '+gnt_tokenName+' Balance: ')
  print(gnt_account6_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_6 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_6 / gnt_token_d * gnt_last_price))
 if gnt_ab_account_number not in gnt_ab_input:
  print('Must Integer Within Range '+gnt_accounts_range+'.')

def gnt_list_all_account_balances():
 gnt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+gnt_tokenName+' Balance: ')
 print(gnt_account0_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_0 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_0 / gnt_token_d * gnt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(gnt_account0_n+': Ethereum Balance '+str(gnt_w_call_0 / _e_d)+' $'+str(gnt_w_call_0 / _e_d * gnt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+gnt_tokenName+' Balance: ')
 print(gnt_account1_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_1 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_1 / gnt_token_d * gnt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(gnt_account1_n+': Ethereum Balance '+str(gnt_w_call_1 / _e_d)+' $'+str(gnt_w_call_1 / _e_d * gnt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+gnt_tokenName+' Balance: ')
 print(gnt_account2_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_2 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_2 / gnt_token_d * gnt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(gnt_account2_n+': Ethereum Balance '+str(gnt_w_call_2 / _e_d)+' $'+str(gnt_w_call_2 / _e_d * gnt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+gnt_tokenName+' Balance: ')
 print(gnt_account3_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_3 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_3 / gnt_token_d * gnt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(gnt_account3_n+': Ethereum Balance '+str(gnt_w_call_3 / _e_d)+' $'+str(gnt_w_call_3 / _e_d * gnt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+gnt_tokenName+' Balance: ')
 print(gnt_account4_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_4 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_4 / gnt_token_d * gnt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(gnt_account4_n+': Ethereum Balance '+str(gnt_w_call_4 / _e_d)+' $'+str(gnt_w_call_4 / _e_d * gnt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+gnt_tokenName+' Balance: ')
 print(gnt_account5_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_5 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_5 / gnt_token_d * gnt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(gnt_account5_n+': Ethereum Balance '+str(gnt_w_call_5 / _e_d)+' $'+str(gnt_w_call_5 /_e_d * gnt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+gnt_tokenName+' Balance: ')
 print(gnt_account6_n+': '+gnt_tokenName+' Balance: '+str(gnt_call_6 / gnt_token_d)+' Usd/'+gnt_tokenName+' Balance: $'+str(gnt_call_6 / gnt_token_d * gnt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(gnt_account6_n+': Ethereum Balance '+str(gnt_w_call_6 / _e_d)+' $'+str(gnt_w_call_6 / _e_d * gnt_last_ethereum_price))
def gnt_unlock_all_accounts():
  gnt_unlock_account_0()
  gnt_unlock_account_1()
  gnt_unlock_account_2()
  gnt_unlock_account_3()
  gnt_unlock_account_4()
  gnt_unlock_account_5()
  gnt_unlock_account_6()


def gnt_unlock_account_0():
  global gnt_account0pw
  global gnt_account0
  global gnt_account0_n
  gnt_update_accounts()
  gnt_u_a_0 = gnt_w_unlock(gnt_account0, gnt_account0pw, gnt_unlockTime)
  if gnt_u_a_0 == False:
    if gnt_account0pw == '':
     gnt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account0_n+' Passphrase Denied: '+gnt_account0pw_r)
    elif gnt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+gnt_account0_n+' Passphrase Denied: '+gnt_account0pw)
  if gnt_u_a_0 == True:
   print(gnt_account0_n+' Unlocked')

def gnt_unlock_account_1():
  global gnt_account1pw
  global gnt_account1
  global gnt_account1_n
  gnt_update_accounts()
  gnt_u_a_1 = gnt_unlock(gnt_account1, gnt_account1pw, gnt_unlockTime)
  if gnt_u_a_1 == False:
    if gnt_account1pw == '':
     gnt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account1_n+' Passphrase Denied: '+gnt_account1pw_r)
    elif gnt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+gnt_account1_n+' Passphrase Denied: '+gnt_account1pw)
  if gnt_u_a_1 == True:
   print(gnt_account1_n+' Unlocked')

def gnt_unlock_account_2():
  global gnt_account2pw
  global gnt_account2
  global gnt_account2_n
  gnt_update_accounts()
  gnt_u_a_2 = gnt_unlock(gnt_account2, gnt_account2pw, gnt_unlockTime)
  if gnt_u_a_2 == False:
    if gnt_account2pw == '':
     gnt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account2_n+' Passphrase Denied: '+gnt_account2pw_r)
    elif gnt_account2pw != '':
     print('Unlock Failure With Account '+gnt_account2_n+' Passphrase Denied: '+gnt_account2pw)
  if gnt_u_a_2 == True:
   print(gnt_account2_n+' Unlocked')

def gnt_unlock_account_3():
  global gnt_account3pw
  global gnt_account3
  global gnt_account3_n
  gnt_update_accounts()
  gnt_u_a_3 = gnt_unlock(gnt_account3, gnt_account3pw, gnt_unlockTime)
  if gnt_u_a_3 == False:
    if gnt_account3pw == '':
     gnt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account3_n+' Passphrase Denied: '+gnt_account3pw_r)
    elif gnt_account3pw != '':
     print('Unlock Failure With Account '+gnt_account3_n+' Passphrase Denied: '+gnt_account3pw)
  if gnt_u_a_3 == True:
   print(gnt_account3_n+' Unlocked')

def gnt_unlock_account_4():
  global gnt_account4pw
  global gnt_account4
  global gnt_account4_n
  gnt_update_accounts()
  gnt_u_a_4 = gnt_unlock(gnt_account4, gnt_account4pw, gnt_unlockTime)
  if gnt_u_a_4 == False:
    if gnt_account4pw == '':
     gnt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account4_n+' Passphrase Denied: '+gnt_account4pw_r)
    elif gnt_account4pw != '':
     print('Unlock Failure With Account '+gnt_account4_n+' Passphrase Denied: '+gnt_account4pw)
  if gnt_u_a_4 == True:
   print(gnt_account4_n+' Unlocked')

def gnt_unlock_account_5():
  global gnt_account5pw
  global gnt_account5
  global gnt_account5_n
  gnt_update_accounts()
  gnt_u_a_5 = gnt_unlock(gnt_account5, gnt_account5pw, gnt_unlockTime)
  if gnt_u_a_5 == False:
    if gnt_account5pw == '':
     gnt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account5_n+' Passphrase Denied: '+gnt_account5pw_r)
    elif gnt_account5pw != '':
     print('Unlock Failure With Account '+gnt_account5_n+' Passphrase Denied: '+gnt_account5pw)
  if gnt_u_a_5 == True:
   print(gnt_account5_n+' Unlocked')

def gnt_unlock_account_6():
  global gnt_account6pw
  global gnt_account6
  global gnt_account6_n
  gnt_update_accounts()
  gnt_u_a_6 = gnt_unlock(gnt_account6, gnt_account6pw, gnt_unlockTime)
  if gnt_u_a_6 == False:
    if gnt_account6pw == '':
     gnt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+gnt_account6_n+' Passphrase Denied: '+gnt_account6pw_r)
    elif gnt_account6pw != '':
     print('Unlock Failure With Account '+gnt_account6_n+' Passphrase Denied: '+gnt_account6pw)
  if gnt_u_a_6 == True:
   print(gnt_account6_n+' Unlocked')

def gnt_unlock_account(gnt_ua_accountNumber):
 gnt_update_accounts()
 gnt_ua_account_number = gnt_ua_accountNumber
 gnt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if gnt_ua_account_number == gnt_ua_input[0]:
  gnt_unlock_account_0()
 if gnt_ua_account_number == gnt_ua_input[1]:
  gnt_unlock_account_1()
 if gnt_ua_account_number == gnt_ua_input[2]:
  gnt_unlock_account_2()
 if gnt_ua_account_number == gnt_ua_input[3]:
  gnt_unlock_account_3()
 if gnt_ua_account_number == gnt_ua_input[4]:
  gnt_unlock_account_4()
 if gnt_ua_account_number == gnt_ua_input[5]:
  gnt_unlock_account_5()
 if gnt_ua_account_number == gnt_ua_input[6]:
  gnt_unlock_account_6()
 if gnt_ua_account_number not in gnt_ua_input:
  print('Must Integer Within Range '+gnt_accounts_range+'.')
 

def gnt_approve_between_accounts(fromAccount, toAccount, msgValue):
  gnt_update_accounts()
  gnt_a_0 = gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(gnt_a_0)

def gnt_approve(fromAccountNumber, toAddress, msgValue):
  gnt_update_accounts()
  gnt_unlock_account(fromAccountNumber)
  gnt_a_1 = gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(gnt_a_1)

def gnt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  gnt_update_accounts()
  gnt_unlock_account(fromAccount)
  gnt_t_0 = gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(gnt_t_0)

def gnt_transfer(fromAccountNumber, toAddress, msgValue):
  gnt_update_accounts()
  gnt_unlock_account(fromAccountNumber)
  gnt_t_1 = gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(gnt_t_1)

def gnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  gnt_update_accounts()
  gnt_unlock_account(callAccount)
  gnt_tf_0 = gnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(gnt_tf_0)

def gnt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  gnt_update_accounts()
  gnt_unlock_account(callAccount)
  gnt_tf_1 = gnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(gnt_tf_1)
  


def gnt_help():
  print('Following Functions For '+gnt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * gnt_unlock => web3.personal.unlockAccount
/ * gnt_accounts => web3.personal.listAccounts
/ * gnt_balance = web3.eth.getBalance
** gnt => web3.eth.contract(abi=gnt_abi, address=gnt_address)
** / * gnt_balanceOf => gnt.call().balanceOf

~ Function Listing Below:
~ gnt_update_accounts()
~ gnt_update_balances() \n\r -- => gnt_update_accounts()
~ gnt_list_all_accounts() \n\r -- => gnt_update_accounts()
~ gnt_account_balance(accountNumber) \n\r -- => gnt_update_balances() 
~ gnt_list_all_account_balances() \n\r -- => gnt_update_balances()
~ gnt_unlock_all_accounts() \n\r -- => gnt_unlock_account_0() \n\r -- => gnt_unlock_account_1() \n\r -- => gnt_unlock_account_2() \n\r -- => gnt_unlock_account_3() \n\r -- => gnt_unlock_account_4() \n\r -- => gnt_unlock_account_5() \n\r -- => gnt_unlock_account_6() 
~ gnt_unlock_account_0() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account0, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_1() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account1, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_2() \n\r -- => gnt_update_accounts() \n\r --/ *gnt_w_unlock(gnt_account2, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_3() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account3, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_4() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account4, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_5() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account5, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account_6() \n\r -- => gnt_update_accounts() \n\r -- / *gnt_w_unlock(gnt_account6, gnt_account0pw, gnt_unlockTime)
~ gnt_unlock_account(gnt_ua_accountNumber) \n\r -- => gnt_update_accounts() \n\r -- // gnt_unlock_account_0() \n\r -- // gnt_unlock_account_1() \n\r -- // gnt_unlock_account_2() \n\r -- // gnt_unlock_account_3() \n\r -- // gnt_unlock_account_4() \n\r -- // gnt_unlock_account_5() \n\r -- // gnt_unlock_account_6()
~ gnt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(fromAccount) \n\r -- / ** gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ gnt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(fromAccountNumber) \n\r -- / ** gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ gnt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(fromAccount) \n\r -- / ** gnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ gnt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(fromAccountNumber) \n\r -- / ** gnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ gnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(callAccount) \n\r / ** gnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ gnt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => gnt_update_accounts() \n\r -- => gnt_unlock_account(callAccount) \n\r -- / ** gnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ gnt_help() <-- You Are Here. ''')