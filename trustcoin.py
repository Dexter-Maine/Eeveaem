#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global trst_account_0_a
global trst_account_1_a
global trst_account_2_a
global trst_account_3_a
global trst_account_4_a
global trst_account_5_a
global trst_account_6_a
global trst_address
global trst_abi
global trst
global trst_call_0
global trst_call_1
global trst_call_2
global trst_call_3
global trst_call_4
global trst_call_5
global trst_call_6
global trst_call_ab
global trst_accounts
global trst_account_0_pw
global trst_account_1_pw
global trst_account_2_pw
global trst_account_3_pw
global trst_account_4_pw
global trst_account_5_pw
global trst_account_6_pw
global trst_account_0_n
global trst_account_1_n
global trst_account_2_n
global trst_account_3_n
global trst_account_4_n
global trst_account_5_n
global trst_account_6_n
global trst_account1pw
global trst_account2pw
global trst_account3pw
global trst_account4pw
global trst_account5pw
global trst_account6pw
global trst_last_price
global trst_accounts_range
global trst_tokenName
global trst_last_ethereum_price
global trst_unlocktrst
global trst_balance
global trst_balanceOf
global trst_unlock
global trst_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
trst_token_d = 1e6
_e_d = 1e18
trst_accounts_range = '[0, 6]'
trst_unlock = web3.personal.unlockAccount
trst_last_ethereum_price = 370.00
trst_last_price = 0.27
trst_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
trst_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
trst_tokenName = 'TrustCoin Token'
trst_unlocktrst = hex(10000) # Must be hex()
trst_account_0_a = trst_accounts[0]
trst_account_1_a = trst_accounts[1]
trst_account_2_a = trst_accounts[2]
trst_account_3_a = trst_accounts[3]
trst_account_4_a = trst_accounts[4]
trst_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
trst_account_6_a = trst_accounts[6]
# Supply Unlock Passwords For Transactions Below
trst_account_0_pw = 'GuildSkrypt2017!@#'
trst_account_1_pw = ''
trst_account_2_pw = 'GuildSkrypt2017!@#'
trst_account_3_pw = ''
trst_account_4_pw = ''
trst_account_5_pw = ''
trst_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
trst_account_0_n = 'Skotys Bittrex Account'
trst_account_1_n = 'Jeffs Account'
trst_account_2_n = 'Skrypts Bittrex Account'
trst_account_3_n = 'Skotys Personal Account'
trst_account_4_n = 'Unknown'
trst_account_5_n = 'Watched \'Bittrex\' Account.'
trst_account_6_n = 'Watched Account (1)'
# Contract Information Below :
trst_address = '0xCb94be6f13A1182E4A4B6140cb7bf2025d28e41B'
trst_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"migrationInfo","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newMigrationInfoSetter","type":"address"}],"name":"changeMigrationInfoSetter","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"migrationInfoSetter","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_currentValue","type":"uint256"},{"name":"_newValue","type":"uint256"}],"name":"compareAndApprove","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_migrationInfo","type":"string"}],"name":"setMigrationInfo","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"_migrationInfoSetter","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newMigrationInfo","type":"string"}],"name":"MigrationInfoSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
trst = web3.eth.contract(abi=trst_abi, address=trst_address)
trst_balanceOf = trst.call().balanceOf
# End Contract Information
def trst_update_accounts():
 global trst_account0
 global trst_account1
 global trst_account2
 global trst_account3
 global trst_account4
 global trst_account5
 global trst_account6
 global trst_account0_n
 global trst_account1_n
 global trst_account2_n
 global trst_account3_n
 global trst_account4_n
 global trst_account5_n
 global trst_account6_n
 global trst_account0pw
 global trst_account1pw
 global trst_account2pw
 global trst_account3pw
 global trst_account4pw
 global trst_account5pw
 global trst_account6pw
 trst_account0 = trst_account_0_a
 trst_account1 = trst_account_1_a
 trst_account2 = trst_account_2_a
 trst_account3 = trst_account_3_a
 trst_account4 = trst_account_4_a
 trst_account5 = trst_account_5_a
 trst_account6 = trst_account_6_a
 trst_account0_n = trst_account_0_n
 trst_account1_n = trst_account_1_n
 trst_account2_n = trst_account_2_n
 trst_account3_n = trst_account_3_n
 trst_account4_n = trst_account_4_n
 trst_account5_n = trst_account_5_n
 trst_account6_n = trst_account_6_n
 trst_account0pw = trst_account_0_pw
 trst_account1pw = trst_account_1_pw
 trst_account2pw = trst_account_2_pw
 trst_account3pw = trst_account_3_pw
 trst_account4pw = trst_account_4_pw
 trst_account5pw = trst_account_5_pw
 trst_account6pw = trst_account_6_pw
 print(trst_tokenName+' Accounts Updated.')
def trst_update_balances():
 global trst_call_0
 global trst_call_1
 global trst_call_2
 global trst_call_3
 global trst_call_4
 global trst_call_5
 global trst_call_6
 global trst_w_call_0
 global trst_w_call_1
 global trst_w_call_2
 global trst_w_call_3
 global trst_w_call_4
 global trst_w_call_5
 global trst_w_call_6
 trst_update_accounts()
 print('Updating '+trst_tokenName+' Balances Please Wait...')
 trst_call_0 = trst_balanceOf(trst_account0)
 trst_call_1 = trst_balanceOf(trst_account1)
 trst_call_2 = trst_balanceOf(trst_account2)
 trst_call_3 = trst_balanceOf(trst_account3)
 trst_call_4 = trst_balanceOf(trst_account4)
 trst_call_5 = trst_balanceOf(trst_account5)
 trst_call_6 = trst_balanceOf(trst_account6)
 trst_w_call_0 = trst_balance(trst_account0)
 trst_w_call_1 = trst_balance(trst_account1)
 trst_w_call_2 = trst_balance(trst_account2)
 trst_w_call_3 = trst_balance(trst_account3)
 trst_w_call_4 = trst_balance(trst_account4)
 trst_w_call_5 = trst_balance(trst_account5)
 trst_w_call_6 = trst_balance(trst_account6)
 print(trst_tokenName+' Balances Updated.')
def trst_list_all_accounts():
 trst_update_accounts()
 print(trst_tokenName+' '+trst_account0_n+': '+trst_account0)
 print(trst_tokenName+' '+trst_account1_n+': '+trst_account1)
 print(trst_tokenName+' '+trst_account2_n+': '+trst_account2)
 print(trst_tokenName+' '+trst_account3_n+': '+trst_account3)
 print(trst_tokenName+' '+trst_account4_n+': '+trst_account4)
 print(trst_tokenName+' '+trst_account5_n+': '+trst_account5)
 print(trst_tokenName+' '+trst_account6_n+': '+trst_account6)

def trst_account_balance(accountNumber):
 trst_update_balances()
 trst_ab_account_number = accountNumber
 trst_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if trst_ab_account_number == trst_ab_input[0]:
  print('Calling '+trst_account0_n+' '+trst_tokenName+' Balance: ')
  print(trst_account0_n+': '+trst_tokenName+' Balance: '+str(trst_call_0 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_0 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[1]:
  print('Calling '+trst_account1_n+' '+trst_tokenName+' Balance: ')
  print(trst_account1_n+': '+trst_tokenName+' Balance: '+str(trst_call_1 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_1 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[2]:
  print('Calling '+trst_account2_n+' '+trst_tokenName+' Balance: ')
  print(trst_account2_n+': '+trst_tokenName+' Balance: '+str(trst_call_2 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_2 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[3]:
  print('Calling '+trst_account3_n+' '+trst_tokenName+' Balance: ')
  print(trst_account3_n+': '+trst_tokenName+' Balance: '+str(trst_call_3 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_3 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[4]:
  print('Calling '+trst_account4_n+' '+trst_tokenName+' Balance: ')
  print(trst_account4_n+': '+trst_tokenName+' Balance: '+str(trst_call_4 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_4 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[5]:
  print('Calling '+trst_account5_n+' '+trst_tokenName+' Balance: ')
  print(trst_account5_n+': '+trst_tokenName+' Balance: '+str(trst_call_5 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_5 / trst_token_d * trst_last_price))
 if trst_ab_account_number == trst_ab_input[6]:
  print('Calling '+trst_account6_n+' '+trst_tokenName+' Balance: ')
  print(trst_account6_n+': '+trst_tokenName+' Balance: '+str(trst_call_6 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_6 / trst_token_d * trst_last_price))
 if trst_ab_account_number not in trst_ab_input:
  print('Must Integer Within Range '+trst_accounts_range+'.')

def trst_list_all_account_balances():
 trst_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+trst_tokenName+' Balance: ')
 print(trst_account0_n+': '+trst_tokenName+' Balance: '+str(trst_call_0 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_0 / trst_token_d * trst_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(trst_account0_n+': Ethereum Balance '+str(trst_w_call_0 / _e_d)+' $'+str(trst_w_call_0 / _e_d * trst_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+trst_tokenName+' Balance: ')
 print(trst_account1_n+': '+trst_tokenName+' Balance: '+str(trst_call_1 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_1 / trst_token_d * trst_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(trst_account1_n+': Ethereum Balance '+str(trst_w_call_1 / _e_d)+' $'+str(trst_w_call_1 / _e_d * trst_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+trst_tokenName+' Balance: ')
 print(trst_account2_n+': '+trst_tokenName+' Balance: '+str(trst_call_2 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_2 / trst_token_d * trst_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(trst_account2_n+': Ethereum Balance '+str(trst_w_call_2 / _e_d)+' $'+str(trst_w_call_2 / _e_d * trst_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+trst_tokenName+' Balance: ')
 print(trst_account3_n+': '+trst_tokenName+' Balance: '+str(trst_call_3 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_3 / trst_token_d * trst_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(trst_account3_n+': Ethereum Balance '+str(trst_w_call_3 / _e_d)+' $'+str(trst_w_call_3 / _e_d * trst_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+trst_tokenName+' Balance: ')
 print(trst_account4_n+': '+trst_tokenName+' Balance: '+str(trst_call_4 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_4 / trst_token_d * trst_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(trst_account4_n+': Ethereum Balance '+str(trst_w_call_4 / _e_d)+' $'+str(trst_w_call_4 / _e_d * trst_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+trst_tokenName+' Balance: ')
 print(trst_account5_n+': '+trst_tokenName+' Balance: '+str(trst_call_5 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_5 / trst_token_d * trst_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(trst_account5_n+': Ethereum Balance '+str(trst_w_call_5 / _e_d)+' $'+str(trst_w_call_5 /_e_d * trst_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+trst_tokenName+' Balance: ')
 print(trst_account6_n+': '+trst_tokenName+' Balance: '+str(trst_call_6 / trst_token_d)+' Usd/'+trst_tokenName+' Balance: $'+str(trst_call_6 / trst_token_d * trst_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(trst_account6_n+': Ethereum Balance '+str(trst_w_call_6 / _e_d)+' $'+str(trst_w_call_6 / _e_d * trst_last_ethereum_price))
def trst_unlock_all_accounts():
  trst_unlock_account_0()
  trst_unlock_account_1()
  trst_unlock_account_2()
  trst_unlock_account_3()
  trst_unlock_account_4()
  trst_unlock_account_5()
  trst_unlock_account_6()


def trst_unlock_account_0():
  global trst_account0pw
  global trst_account0
  global trst_account0_n
  trst_update_accounts()
  trst_u_a_0 = trst_w_unlock(trst_account0, trst_account0pw, trst_unlocktrst)
  if trst_u_a_0 == False:
    if trst_account0pw == '':
     trst_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account0_n+' Passphrase Denied: '+trst_account0pw_r)
    elif trst_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+trst_account0_n+' Passphrase Denied: '+trst_account0pw)
  if trst_u_a_0 == True:
   print(trst_account0_n+' Unlocked')

def trst_unlock_account_1():
  global trst_account1pw
  global trst_account1
  global trst_account1_n
  trst_update_accounts()
  trst_u_a_1 = trst_unlock(trst_account1, trst_account1pw, trst_unlocktrst)
  if trst_u_a_1 == False:
    if trst_account1pw == '':
     trst_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account1_n+' Passphrase Denied: '+trst_account1pw_r)
    elif trst_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+trst_account1_n+' Passphrase Denied: '+trst_account1pw)
  if trst_u_a_1 == True:
   print(trst_account1_n+' Unlocked')

def trst_unlock_account_2():
  global trst_account2pw
  global trst_account2
  global trst_account2_n
  trst_update_accounts()
  trst_u_a_2 = trst_unlock(trst_account2, trst_account2pw, trst_unlocktrst)
  if trst_u_a_2 == False:
    if trst_account2pw == '':
     trst_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account2_n+' Passphrase Denied: '+trst_account2pw_r)
    elif trst_account2pw != '':
     print('Unlock Failure With Account '+trst_account2_n+' Passphrase Denied: '+trst_account2pw)
  if trst_u_a_2 == True:
   print(trst_account2_n+' Unlocked')

def trst_unlock_account_3():
  global trst_account3pw
  global trst_account3
  global trst_account3_n
  trst_update_accounts()
  trst_u_a_3 = trst_unlock(trst_account3, trst_account3pw, trst_unlocktrst)
  if trst_u_a_3 == False:
    if trst_account3pw == '':
     trst_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account3_n+' Passphrase Denied: '+trst_account3pw_r)
    elif trst_account3pw != '':
     print('Unlock Failure With Account '+trst_account3_n+' Passphrase Denied: '+trst_account3pw)
  if trst_u_a_3 == True:
   print(trst_account3_n+' Unlocked')

def trst_unlock_account_4():
  global trst_account4pw
  global trst_account4
  global trst_account4_n
  trst_update_accounts()
  trst_u_a_4 = trst_unlock(trst_account4, trst_account4pw, trst_unlocktrst)
  if trst_u_a_4 == False:
    if trst_account4pw == '':
     trst_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account4_n+' Passphrase Denied: '+trst_account4pw_r)
    elif trst_account4pw != '':
     print('Unlock Failure With Account '+trst_account4_n+' Passphrase Denied: '+trst_account4pw)
  if trst_u_a_4 == True:
   print(trst_account4_n+' Unlocked')

def trst_unlock_account_5():
  global trst_account5pw
  global trst_account5
  global trst_account5_n
  trst_update_accounts()
  trst_u_a_5 = trst_unlock(trst_account5, trst_account5pw, trst_unlocktrst)
  if trst_u_a_5 == False:
    if trst_account5pw == '':
     trst_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account5_n+' Passphrase Denied: '+trst_account5pw_r)
    elif trst_account5pw != '':
     print('Unlock Failure With Account '+trst_account5_n+' Passphrase Denied: '+trst_account5pw)
  if trst_u_a_5 == True:
   print(trst_account5_n+' Unlocked')

def trst_unlock_account_6():
  global trst_account6pw
  global trst_account6
  global trst_account6_n
  trst_update_accounts()
  trst_u_a_6 = trst_unlock(trst_account6, trst_account6pw, trst_unlocktrst)
  if trst_u_a_6 == False:
    if trst_account6pw == '':
     trst_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+trst_account6_n+' Passphrase Denied: '+trst_account6pw_r)
    elif trst_account6pw != '':
     print('Unlock Failure With Account '+trst_account6_n+' Passphrase Denied: '+trst_account6pw)
  if trst_u_a_6 == True:
   print(trst_account6_n+' Unlocked')

def trst_unlock_account(trst_ua_accountNumber):
 trst_update_accounts()
 trst_ua_account_number = trst_ua_accountNumber
 trst_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if trst_ua_account_number == trst_ua_input[0]:
  trst_unlock_account_0()
 if trst_ua_account_number == trst_ua_input[1]:
  trst_unlock_account_1()
 if trst_ua_account_number == trst_ua_input[2]:
  trst_unlock_account_2()
 if trst_ua_account_number == trst_ua_input[3]:
  trst_unlock_account_3()
 if trst_ua_account_number == trst_ua_input[4]:
  trst_unlock_account_4()
 if trst_ua_account_number == trst_ua_input[5]:
  trst_unlock_account_5()
 if trst_ua_account_number == trst_ua_input[6]:
  trst_unlock_account_6()
 if trst_ua_account_number not in trst_ua_input:
  print('Must Integer Within Range '+trst_accounts_range+'.')
 

def trst_approve_between_accounts(fromAccount, toAccount, msgValue):
  trst_update_accounts()
  trst_a_0 = trst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(trst_a_0)

def trst_approve(fromAccountNumber, toAddress, msgValue):
  trst_update_accounts()
  trst_unlock_account(fromAccountNumber)
  trst_a_1 = trst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(trst_a_1)

def trst_transfer_between_accounts(fromAccount, toAccount, msgValue):
  trst_update_accounts()
  trst_unlock_account(fromAccount)
  trst_t_0 = trst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(trst_t_0)

def trst_transfer(fromAccountNumber, toAddress, msgValue):
  trst_update_accounts()
  trst_unlock_account(fromAccountNumber)
  trst_t_1 = trst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(trst_t_1)

def trst_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  trst_update_accounts()
  trst_unlock_account(callAccount)
  trst_tf_0 = trst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(trst_tf_0)

def trst_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  trst_update_accounts()
  trst_unlock_account(callAccount)
  trst_tf_1 = trst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(trst_tf_1)
  


def trst_help():
  print('Following Functions For '+trst_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * trst_unlock => web3.personal.unlockAccount
/ * trst_accounts => web3.personal.listAccounts
/ * trst_balance = web3.eth.getBalance
** trst => web3.eth.contract(abi=trst_abi, address=trst_address)
** / * trst_balanceOf => trst.call().balanceOf

~ Function Listing Below:
~ trst_update_accounts()
~ trst_update_balances() \n\r -- => trst_update_accounts()
~ trst_list_all_accounts() \n\r -- => trst_update_accounts()
~ trst_account_balance(accountNumber) \n\r -- => trst_update_balances() 
~ trst_list_all_account_balances() \n\r -- => trst_update_balances()
~ trst_unlock_all_accounts() \n\r -- => trst_unlock_account_0() \n\r -- => trst_unlock_account_1() \n\r -- => trst_unlock_account_2() \n\r -- => trst_unlock_account_3() \n\r -- => trst_unlock_account_4() \n\r -- => trst_unlock_account_5() \n\r -- => trst_unlock_account_6() 
~ trst_unlock_account_0() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account0, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_1() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account1, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_2() \n\r -- => trst_update_accounts() \n\r --/ *trst_w_unlock(trst_account2, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_3() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account3, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_4() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account4, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_5() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account5, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account_6() \n\r -- => trst_update_accounts() \n\r -- / *trst_w_unlock(trst_account6, trst_account0pw, trst_unlocktrst)
~ trst_unlock_account(trst_ua_accountNumber) \n\r -- => trst_update_accounts() \n\r -- // trst_unlock_account_0() \n\r -- // trst_unlock_account_1() \n\r -- // trst_unlock_account_2() \n\r -- // trst_unlock_account_3() \n\r -- // trst_unlock_account_4() \n\r -- // trst_unlock_account_5() \n\r -- // trst_unlock_account_6()
~ trst_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(fromAccount) \n\r -- / ** trst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ trst_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(fromAccountNumber) \n\r -- / ** trst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ trst_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(fromAccount) \n\r -- / ** trst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ trst_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(fromAccountNumber) \n\r -- / ** trst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ trst_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(callAccount) \n\r / ** trst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ trst_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => trst_update_accounts() \n\r -- => trst_unlock_account(callAccount) \n\r -- / ** trst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ trst_help() <-- You Are Here. ''')