#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global nxc_account_0_a
global nxc_account_1_a
global nxc_account_2_a
global nxc_account_3_a
global nxc_account_4_a
global nxc_account_5_a
global nxc_account_6_a
global nxc_address
global nxc_abi
global nxc
global nxc_call_0
global nxc_call_1
global nxc_call_2
global nxc_call_3
global nxc_call_4
global nxc_call_5
global nxc_call_6
global nxc_call_ab
global nxc_accounts
global nxc_account_0_pw
global nxc_account_1_pw
global nxc_account_2_pw
global nxc_account_3_pw
global nxc_account_4_pw
global nxc_account_5_pw
global nxc_account_6_pw
global nxc_account_0_n
global nxc_account_1_n
global nxc_account_2_n
global nxc_account_3_n
global nxc_account_4_n
global nxc_account_5_n
global nxc_account_6_n
global nxc_account1pw
global nxc_account2pw
global nxc_account3pw
global nxc_account4pw
global nxc_account5pw
global nxc_account6pw
global nxc_last_price
global nxc_accounts_range
global nxc_tokenName
global nxc_last_ethereum_price
global nxc_unlockTime
global nxc_balance
global nxc_balanceOf
global nxc_unlock
global nxc_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
nxc_token_d = 1e3
_e_d = 1e18
nxc_accounts_range = '[0, 6]'
nxc_unlock = web3.personal.unlockAccount
nxc_last_ethereum_price = 370.00
nxc_last_price = 0.30
nxc_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
nxc_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
nxc_tokenName = 'Nexium Token'
nxc_unlockTime = hex(10000) # Must be hex()
nxc_account_0_a = nxc_accounts[0]
nxc_account_1_a = nxc_accounts[1]
nxc_account_2_a = nxc_accounts[2]
nxc_account_3_a = nxc_accounts[3]
nxc_account_4_a = nxc_accounts[4]
nxc_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
nxc_account_6_a = nxc_accounts[6]
# Supply Unlock Passwords For Transactions Below
nxc_account_0_pw = 'GuildSkrypt2017!@#'
nxc_account_1_pw = ''
nxc_account_2_pw = 'GuildSkrypt2017!@#'
nxc_account_3_pw = ''
nxc_account_4_pw = ''
nxc_account_5_pw = ''
nxc_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
nxc_account_0_n = 'Skotys Bittrex Account'
nxc_account_1_n = 'Jeffs Account'
nxc_account_2_n = 'Skrypts Bittrex Account'
nxc_account_3_n = 'Skotys Personal Account'
nxc_account_4_n = 'Unknown'
nxc_account_5_n = 'Watched \'Bittrex\' Account.'
nxc_account_6_n = 'Watched Account (1)'
# Contract Information Below :
nxc_address = '0x45e42D659D9f9466cD5DF622506033145a9b89Bc'
nxc_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":true,"inputs":[],"name":"initialSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"burnAddress","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
nxc = web3.eth.contract(abi=nxc_abi, address=nxc_address)
nxc_balanceOf = nxc.call().balanceOf
# End Contract Information
def nxc_update_accounts():
 global nxc_account0
 global nxc_account1
 global nxc_account2
 global nxc_account3
 global nxc_account4
 global nxc_account5
 global nxc_account6
 global nxc_account0_n
 global nxc_account1_n
 global nxc_account2_n
 global nxc_account3_n
 global nxc_account4_n
 global nxc_account5_n
 global nxc_account6_n
 global nxc_account0pw
 global nxc_account1pw
 global nxc_account2pw
 global nxc_account3pw
 global nxc_account4pw
 global nxc_account5pw
 global nxc_account6pw
 nxc_account0 = nxc_account_0_a
 nxc_account1 = nxc_account_1_a
 nxc_account2 = nxc_account_2_a
 nxc_account3 = nxc_account_3_a
 nxc_account4 = nxc_account_4_a
 nxc_account5 = nxc_account_5_a
 nxc_account6 = nxc_account_6_a
 nxc_account0_n = nxc_account_0_n
 nxc_account1_n = nxc_account_1_n
 nxc_account2_n = nxc_account_2_n
 nxc_account3_n = nxc_account_3_n
 nxc_account4_n = nxc_account_4_n
 nxc_account5_n = nxc_account_5_n
 nxc_account6_n = nxc_account_6_n
 nxc_account0pw = nxc_account_0_pw
 nxc_account1pw = nxc_account_1_pw
 nxc_account2pw = nxc_account_2_pw
 nxc_account3pw = nxc_account_3_pw
 nxc_account4pw = nxc_account_4_pw
 nxc_account5pw = nxc_account_5_pw
 nxc_account6pw = nxc_account_6_pw
 print(nxc_tokenName+' Accounts Updated.')
def nxc_update_balances():
 global nxc_call_0
 global nxc_call_1
 global nxc_call_2
 global nxc_call_3
 global nxc_call_4
 global nxc_call_5
 global nxc_call_6
 global nxc_w_call_0
 global nxc_w_call_1
 global nxc_w_call_2
 global nxc_w_call_3
 global nxc_w_call_4
 global nxc_w_call_5
 global nxc_w_call_6
 nxc_update_accounts()
 print('Updating '+nxc_tokenName+' Balances Please Wait...')
 nxc_call_0 = nxc_balanceOf(nxc_account0)
 nxc_call_1 = nxc_balanceOf(nxc_account1)
 nxc_call_2 = nxc_balanceOf(nxc_account2)
 nxc_call_3 = nxc_balanceOf(nxc_account3)
 nxc_call_4 = nxc_balanceOf(nxc_account4)
 nxc_call_5 = nxc_balanceOf(nxc_account5)
 nxc_call_6 = nxc_balanceOf(nxc_account6)
 nxc_w_call_0 = nxc_balance(nxc_account0)
 nxc_w_call_1 = nxc_balance(nxc_account1)
 nxc_w_call_2 = nxc_balance(nxc_account2)
 nxc_w_call_3 = nxc_balance(nxc_account3)
 nxc_w_call_4 = nxc_balance(nxc_account4)
 nxc_w_call_5 = nxc_balance(nxc_account5)
 nxc_w_call_6 = nxc_balance(nxc_account6)
 print(nxc_tokenName+' Balances Updated.')
def nxc_list_all_accounts():
 nxc_update_accounts()
 print(nxc_tokenName+' '+nxc_account0_n+': '+nxc_account0)
 print(nxc_tokenName+' '+nxc_account1_n+': '+nxc_account1)
 print(nxc_tokenName+' '+nxc_account2_n+': '+nxc_account2)
 print(nxc_tokenName+' '+nxc_account3_n+': '+nxc_account3)
 print(nxc_tokenName+' '+nxc_account4_n+': '+nxc_account4)
 print(nxc_tokenName+' '+nxc_account5_n+': '+nxc_account5)
 print(nxc_tokenName+' '+nxc_account6_n+': '+nxc_account6)

def nxc_account_balance(accountNumber):
 nxc_update_balances()
 nxc_ab_account_number = accountNumber
 nxc_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if nxc_ab_account_number == nxc_ab_input[0]:
  print('Calling '+nxc_account0_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account0_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_0 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_0 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[1]:
  print('Calling '+nxc_account1_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account1_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_1 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_1 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[2]:
  print('Calling '+nxc_account2_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account2_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_2 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_2 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[3]:
  print('Calling '+nxc_account3_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account3_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_3 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_3 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[4]:
  print('Calling '+nxc_account4_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account4_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_4 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_4 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[5]:
  print('Calling '+nxc_account5_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account5_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_5 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_5 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number == nxc_ab_input[6]:
  print('Calling '+nxc_account6_n+' '+nxc_tokenName+' Balance: ')
  print(nxc_account6_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_6 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_6 / nxc_token_d * nxc_last_price))
 if nxc_ab_account_number not in nxc_ab_input:
  print('Must Integer Within Range '+nxc_accounts_range+'.')

def nxc_list_all_account_balances():
 nxc_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+nxc_tokenName+' Balance: ')
 print(nxc_account0_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_0 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_0 / nxc_token_d * nxc_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(nxc_account0_n+': Ethereum Balance '+str(nxc_w_call_0 / _e_d)+' $'+str(nxc_w_call_0 / _e_d * nxc_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+nxc_tokenName+' Balance: ')
 print(nxc_account1_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_1 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_1 / nxc_token_d * nxc_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(nxc_account1_n+': Ethereum Balance '+str(nxc_w_call_1 / _e_d)+' $'+str(nxc_w_call_1 / _e_d * nxc_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+nxc_tokenName+' Balance: ')
 print(nxc_account2_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_2 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_2 / nxc_token_d * nxc_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(nxc_account2_n+': Ethereum Balance '+str(nxc_w_call_2 / _e_d)+' $'+str(nxc_w_call_2 / _e_d * nxc_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+nxc_tokenName+' Balance: ')
 print(nxc_account3_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_3 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_3 / nxc_token_d * nxc_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(nxc_account3_n+': Ethereum Balance '+str(nxc_w_call_3 / _e_d)+' $'+str(nxc_w_call_3 / _e_d * nxc_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+nxc_tokenName+' Balance: ')
 print(nxc_account4_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_4 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_4 / nxc_token_d * nxc_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(nxc_account4_n+': Ethereum Balance '+str(nxc_w_call_4 / _e_d)+' $'+str(nxc_w_call_4 / _e_d * nxc_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+nxc_tokenName+' Balance: ')
 print(nxc_account5_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_5 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_5 / nxc_token_d * nxc_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(nxc_account5_n+': Ethereum Balance '+str(nxc_w_call_5 / _e_d)+' $'+str(nxc_w_call_5 /_e_d * nxc_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+nxc_tokenName+' Balance: ')
 print(nxc_account6_n+': '+nxc_tokenName+' Balance: '+str(nxc_call_6 / nxc_token_d)+' Usd/'+nxc_tokenName+' Balance: $'+str(nxc_call_6 / nxc_token_d * nxc_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(nxc_account6_n+': Ethereum Balance '+str(nxc_w_call_6 / _e_d)+' $'+str(nxc_w_call_6 / _e_d * nxc_last_ethereum_price))
def nxc_unlock_all_accounts():
  nxc_unlock_account_0()
  nxc_unlock_account_1()
  nxc_unlock_account_2()
  nxc_unlock_account_3()
  nxc_unlock_account_4()
  nxc_unlock_account_5()
  nxc_unlock_account_6()


def nxc_unlock_account_0():
  global nxc_account0pw
  global nxc_account0
  global nxc_account0_n
  nxc_update_accounts()
  nxc_u_a_0 = nxc_w_unlock(nxc_account0, nxc_account0pw, nxc_unlockTime)
  if nxc_u_a_0 == False:
    if nxc_account0pw == '':
     nxc_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account0_n+' Passphrase Denied: '+nxc_account0pw_r)
    elif nxc_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+nxc_account0_n+' Passphrase Denied: '+nxc_account0pw)
  if nxc_u_a_0 == True:
   print(nxc_account0_n+' Unlocked')

def nxc_unlock_account_1():
  global nxc_account1pw
  global nxc_account1
  global nxc_account1_n
  nxc_update_accounts()
  nxc_u_a_1 = nxc_unlock(nxc_account1, nxc_account1pw, nxc_unlockTime)
  if nxc_u_a_1 == False:
    if nxc_account1pw == '':
     nxc_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account1_n+' Passphrase Denied: '+nxc_account1pw_r)
    elif nxc_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+nxc_account1_n+' Passphrase Denied: '+nxc_account1pw)
  if nxc_u_a_1 == True:
   print(nxc_account1_n+' Unlocked')

def nxc_unlock_account_2():
  global nxc_account2pw
  global nxc_account2
  global nxc_account2_n
  nxc_update_accounts()
  nxc_u_a_2 = nxc_unlock(nxc_account2, nxc_account2pw, nxc_unlockTime)
  if nxc_u_a_2 == False:
    if nxc_account2pw == '':
     nxc_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account2_n+' Passphrase Denied: '+nxc_account2pw_r)
    elif nxc_account2pw != '':
     print('Unlock Failure With Account '+nxc_account2_n+' Passphrase Denied: '+nxc_account2pw)
  if nxc_u_a_2 == True:
   print(nxc_account2_n+' Unlocked')

def nxc_unlock_account_3():
  global nxc_account3pw
  global nxc_account3
  global nxc_account3_n
  nxc_update_accounts()
  nxc_u_a_3 = nxc_unlock(nxc_account3, nxc_account3pw, nxc_unlockTime)
  if nxc_u_a_3 == False:
    if nxc_account3pw == '':
     nxc_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account3_n+' Passphrase Denied: '+nxc_account3pw_r)
    elif nxc_account3pw != '':
     print('Unlock Failure With Account '+nxc_account3_n+' Passphrase Denied: '+nxc_account3pw)
  if nxc_u_a_3 == True:
   print(nxc_account3_n+' Unlocked')

def nxc_unlock_account_4():
  global nxc_account4pw
  global nxc_account4
  global nxc_account4_n
  nxc_update_accounts()
  nxc_u_a_4 = nxc_unlock(nxc_account4, nxc_account4pw, nxc_unlockTime)
  if nxc_u_a_4 == False:
    if nxc_account4pw == '':
     nxc_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account4_n+' Passphrase Denied: '+nxc_account4pw_r)
    elif nxc_account4pw != '':
     print('Unlock Failure With Account '+nxc_account4_n+' Passphrase Denied: '+nxc_account4pw)
  if nxc_u_a_4 == True:
   print(nxc_account4_n+' Unlocked')

def nxc_unlock_account_5():
  global nxc_account5pw
  global nxc_account5
  global nxc_account5_n
  nxc_update_accounts()
  nxc_u_a_5 = nxc_unlock(nxc_account5, nxc_account5pw, nxc_unlockTime)
  if nxc_u_a_5 == False:
    if nxc_account5pw == '':
     nxc_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account5_n+' Passphrase Denied: '+nxc_account5pw_r)
    elif nxc_account5pw != '':
     print('Unlock Failure With Account '+nxc_account5_n+' Passphrase Denied: '+nxc_account5pw)
  if nxc_u_a_5 == True:
   print(nxc_account5_n+' Unlocked')

def nxc_unlock_account_6():
  global nxc_account6pw
  global nxc_account6
  global nxc_account6_n
  nxc_update_accounts()
  nxc_u_a_6 = nxc_unlock(nxc_account6, nxc_account6pw, nxc_unlockTime)
  if nxc_u_a_6 == False:
    if nxc_account6pw == '':
     nxc_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nxc_account6_n+' Passphrase Denied: '+nxc_account6pw_r)
    elif nxc_account6pw != '':
     print('Unlock Failure With Account '+nxc_account6_n+' Passphrase Denied: '+nxc_account6pw)
  if nxc_u_a_6 == True:
   print(nxc_account6_n+' Unlocked')

def nxc_unlock_account(nxc_ua_accountNumber):
 nxc_update_accounts()
 nxc_ua_account_number = nxc_ua_accountNumber
 nxc_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if nxc_ua_account_number == nxc_ua_input[0]:
  nxc_unlock_account_0()
 if nxc_ua_account_number == nxc_ua_input[1]:
  nxc_unlock_account_1()
 if nxc_ua_account_number == nxc_ua_input[2]:
  nxc_unlock_account_2()
 if nxc_ua_account_number == nxc_ua_input[3]:
  nxc_unlock_account_3()
 if nxc_ua_account_number == nxc_ua_input[4]:
  nxc_unlock_account_4()
 if nxc_ua_account_number == nxc_ua_input[5]:
  nxc_unlock_account_5()
 if nxc_ua_account_number == nxc_ua_input[6]:
  nxc_unlock_account_6()
 if nxc_ua_account_number not in nxc_ua_input:
  print('Must Integer Within Range '+nxc_accounts_range+'.')
 

def nxc_approve_between_accounts(fromAccount, toAccount, msgValue):
  nxc_update_accounts()
  nxc_a_0 = nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(nxc_a_0)

def nxc_approve(fromAccountNumber, toAddress, msgValue):
  nxc_update_accounts()
  nxc_unlock_account(fromAccountNumber)
  nxc_a_1 = nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(nxc_a_1)

def nxc_transfer_between_accounts(fromAccount, toAccount, msgValue):
  nxc_update_accounts()
  nxc_unlock_account(fromAccount)
  nxc_t_0 = nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(nxc_t_0)

def nxc_transfer(fromAccountNumber, toAddress, msgValue):
  nxc_update_accounts()
  nxc_unlock_account(fromAccountNumber)
  nxc_t_1 = nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(nxc_t_1)

def nxc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  nxc_update_accounts()
  nxc_unlock_account(callAccount)
  nxc_tf_0 = nxc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(nxc_tf_0)

def nxc_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  nxc_update_accounts()
  nxc_unlock_account(callAccount)
  nxc_tf_1 = nxc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(nxc_tf_1)
  


def nxc_help():
  print('Following Functions For '+nxc_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * nxc_unlock => web3.personal.unlockAccount
/ * nxc_accounts => web3.personal.listAccounts
/ * nxc_balance = web3.eth.getBalance
** nxc => web3.eth.contract(abi=nxc_abi, address=nxc_address)
** / * nxc_balanceOf => nxc.call().balanceOf

~ Function Listing Below:
~ nxc_update_accounts()
~ nxc_update_balances() \n\r -- => nxc_update_accounts()
~ nxc_list_all_accounts() \n\r -- => nxc_update_accounts()
~ nxc_account_balance(accountNumber) \n\r -- => nxc_update_balances() 
~ nxc_list_all_account_balances() \n\r -- => nxc_update_balances()
~ nxc_unlock_all_accounts() \n\r -- => nxc_unlock_account_0() \n\r -- => nxc_unlock_account_1() \n\r -- => nxc_unlock_account_2() \n\r -- => nxc_unlock_account_3() \n\r -- => nxc_unlock_account_4() \n\r -- => nxc_unlock_account_5() \n\r -- => nxc_unlock_account_6() 
~ nxc_unlock_account_0() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account0, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_1() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account1, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_2() \n\r -- => nxc_update_accounts() \n\r --/ *nxc_w_unlock(nxc_account2, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_3() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account3, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_4() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account4, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_5() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account5, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account_6() \n\r -- => nxc_update_accounts() \n\r -- / *nxc_w_unlock(nxc_account6, nxc_account0pw, nxc_unlockTime)
~ nxc_unlock_account(nxc_ua_accountNumber) \n\r -- => nxc_update_accounts() \n\r -- // nxc_unlock_account_0() \n\r -- // nxc_unlock_account_1() \n\r -- // nxc_unlock_account_2() \n\r -- // nxc_unlock_account_3() \n\r -- // nxc_unlock_account_4() \n\r -- // nxc_unlock_account_5() \n\r -- // nxc_unlock_account_6()
~ nxc_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(fromAccount) \n\r -- / ** nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ nxc_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(fromAccountNumber) \n\r -- / ** nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ nxc_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(fromAccount) \n\r -- / ** nxc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ nxc_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(fromAccountNumber) \n\r -- / ** nxc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ nxc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(callAccount) \n\r / ** nxc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ nxc_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => nxc_update_accounts() \n\r -- => nxc_unlock_account(callAccount) \n\r -- / ** nxc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ nxc_help() <-- You Are Here. ''')