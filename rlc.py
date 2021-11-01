#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global rlc_account_0_a
global rlc_account_1_a
global rlc_account_2_a
global rlc_account_3_a
global rlc_account_4_a
global rlc_account_5_a
global rlc_account_6_a
global rlc_address
global rlc_abi
global rlc
global rlc_call_0
global rlc_call_1
global rlc_call_2
global rlc_call_3
global rlc_call_4
global rlc_call_5
global rlc_call_6
global rlc_call_ab
global rlc_accounts
global rlc_account_0_pw
global rlc_account_1_pw
global rlc_account_2_pw
global rlc_account_3_pw
global rlc_account_4_pw
global rlc_account_5_pw
global rlc_account_6_pw
global rlc_account_0_n
global rlc_account_1_n
global rlc_account_2_n
global rlc_account_3_n
global rlc_account_4_n
global rlc_account_5_n
global rlc_account_6_n
global rlc_account1pw
global rlc_account2pw
global rlc_account3pw
global rlc_account4pw
global rlc_account5pw
global rlc_account6pw
global rlc_last_price
global rlc_accounts_range
global rlc_tokenName
global rlc_last_ethereum_price
global rlc_unlockTime
global rlc_balance
global rlc_balanceOf
global rlc_unlock
global rlc_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
rlc_token_d = 1e9
_e_d = 1e18
rlc_accounts_range = '[0, 6]'
rlc_unlock = web3.personal.unlockAccount
rlc_last_ethereum_price = 370.00
rlc_last_price = 0.63
rlc_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
rlc_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
rlc_tokenName = 'RLC Token'
rlc_unlockTime = hex(10000) # Must be hex()
rlc_account_0_a = rlc_accounts[0]
rlc_account_1_a = rlc_accounts[1]
rlc_account_2_a = rlc_accounts[2]
rlc_account_3_a = rlc_accounts[3]
rlc_account_4_a = rlc_accounts[4]
rlc_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
rlc_account_6_a = rlc_accounts[6]
# Supply Unlock Passwords For Transactions Below
rlc_account_0_pw = 'GuildSkrypt2017!@#'
rlc_account_1_pw = ''
rlc_account_2_pw = 'GuildSkrypt2017!@#'
rlc_account_3_pw = ''
rlc_account_4_pw = ''
rlc_account_5_pw = ''
rlc_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
rlc_account_0_n = 'Skotys Bittrex Account'
rlc_account_1_n = 'Jeffs Account'
rlc_account_2_n = 'Skrypts Bittrex Account'
rlc_account_3_n = 'Skotys Personal Account'
rlc_account_4_n = 'Unknown'
rlc_account_5_n = 'Watched \'Bittrex\' Account.'
rlc_account_6_n = 'Watched Account (1)'
# Contract Information Below :
rlc_address = '0x607F4C5BB672230e8672085532f7e901544a7375'
rlc_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"initialSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unlock","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"locked","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
rlc = web3.eth.contract(abi=rlc_abi, address=rlc_address)
rlc_balanceOf = rlc.call().balanceOf
# End Contract Information
def rlc_update_accounts():
 global rlc_account0
 global rlc_account1
 global rlc_account2
 global rlc_account3
 global rlc_account4
 global rlc_account5
 global rlc_account6
 global rlc_account0_n
 global rlc_account1_n
 global rlc_account2_n
 global rlc_account3_n
 global rlc_account4_n
 global rlc_account5_n
 global rlc_account6_n
 global rlc_account0pw
 global rlc_account1pw
 global rlc_account2pw
 global rlc_account3pw
 global rlc_account4pw
 global rlc_account5pw
 global rlc_account6pw
 rlc_account0 = rlc_account_0_a
 rlc_account1 = rlc_account_1_a
 rlc_account2 = rlc_account_2_a
 rlc_account3 = rlc_account_3_a
 rlc_account4 = rlc_account_4_a
 rlc_account5 = rlc_account_5_a
 rlc_account6 = rlc_account_6_a
 rlc_account0_n = rlc_account_0_n
 rlc_account1_n = rlc_account_1_n
 rlc_account2_n = rlc_account_2_n
 rlc_account3_n = rlc_account_3_n
 rlc_account4_n = rlc_account_4_n
 rlc_account5_n = rlc_account_5_n
 rlc_account6_n = rlc_account_6_n
 rlc_account0pw = rlc_account_0_pw
 rlc_account1pw = rlc_account_1_pw
 rlc_account2pw = rlc_account_2_pw
 rlc_account3pw = rlc_account_3_pw
 rlc_account4pw = rlc_account_4_pw
 rlc_account5pw = rlc_account_5_pw
 rlc_account6pw = rlc_account_6_pw
 print(rlc_tokenName+' Accounts Updated.')
def rlc_update_balances():
 global rlc_call_0
 global rlc_call_1
 global rlc_call_2
 global rlc_call_3
 global rlc_call_4
 global rlc_call_5
 global rlc_call_6
 global rlc_w_call_0
 global rlc_w_call_1
 global rlc_w_call_2
 global rlc_w_call_3
 global rlc_w_call_4
 global rlc_w_call_5
 global rlc_w_call_6
 rlc_update_accounts()
 print('Updating '+rlc_tokenName+' Balances Please Wait...')
 rlc_call_0 = rlc_balanceOf(rlc_account0)
 rlc_call_1 = rlc_balanceOf(rlc_account1)
 rlc_call_2 = rlc_balanceOf(rlc_account2)
 rlc_call_3 = rlc_balanceOf(rlc_account3)
 rlc_call_4 = rlc_balanceOf(rlc_account4)
 rlc_call_5 = rlc_balanceOf(rlc_account5)
 rlc_call_6 = rlc_balanceOf(rlc_account6)
 rlc_w_call_0 = rlc_balance(rlc_account0)
 rlc_w_call_1 = rlc_balance(rlc_account1)
 rlc_w_call_2 = rlc_balance(rlc_account2)
 rlc_w_call_3 = rlc_balance(rlc_account3)
 rlc_w_call_4 = rlc_balance(rlc_account4)
 rlc_w_call_5 = rlc_balance(rlc_account5)
 rlc_w_call_6 = rlc_balance(rlc_account6)
 print(rlc_tokenName+' Balances Updated.')
def rlc_list_all_accounts():
 rlc_update_accounts()
 print(rlc_tokenName+' '+rlc_account0_n+': '+rlc_account0)
 print(rlc_tokenName+' '+rlc_account1_n+': '+rlc_account1)
 print(rlc_tokenName+' '+rlc_account2_n+': '+rlc_account2)
 print(rlc_tokenName+' '+rlc_account3_n+': '+rlc_account3)
 print(rlc_tokenName+' '+rlc_account4_n+': '+rlc_account4)
 print(rlc_tokenName+' '+rlc_account5_n+': '+rlc_account5)
 print(rlc_tokenName+' '+rlc_account6_n+': '+rlc_account6)

def rlc_account_balance(accountNumber):
 rlc_update_balances()
 rlc_ab_account_number = accountNumber
 rlc_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if rlc_ab_account_number == rlc_ab_input[0]:
  print('Calling '+rlc_account0_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account0_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_0 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_0 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[1]:
  print('Calling '+rlc_account1_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account1_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_1 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_1 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[2]:
  print('Calling '+rlc_account2_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account2_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_2 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_2 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[3]:
  print('Calling '+rlc_account3_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account3_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_3 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_3 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[4]:
  print('Calling '+rlc_account4_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account4_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_4 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_4 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[5]:
  print('Calling '+rlc_account5_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account5_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_5 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_5 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number == rlc_ab_input[6]:
  print('Calling '+rlc_account6_n+' '+rlc_tokenName+' Balance: ')
  print(rlc_account6_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_6 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_6 / rlc_token_d * rlc_last_price))
 if rlc_ab_account_number not in rlc_ab_input:
  print('Must Integer Within Range '+rlc_accounts_range+'.')

def rlc_list_all_account_balances():
 rlc_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+rlc_tokenName+' Balance: ')
 print(rlc_account0_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_0 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_0 / rlc_token_d * rlc_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(rlc_account0_n+': Ethereum Balance '+str(rlc_w_call_0 / _e_d)+' $'+str(rlc_w_call_0 / _e_d * rlc_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+rlc_tokenName+' Balance: ')
 print(rlc_account1_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_1 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_1 / rlc_token_d * rlc_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(rlc_account1_n+': Ethereum Balance '+str(rlc_w_call_1 / _e_d)+' $'+str(rlc_w_call_1 / _e_d * rlc_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+rlc_tokenName+' Balance: ')
 print(rlc_account2_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_2 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_2 / rlc_token_d * rlc_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(rlc_account2_n+': Ethereum Balance '+str(rlc_w_call_2 / _e_d)+' $'+str(rlc_w_call_2 / _e_d * rlc_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+rlc_tokenName+' Balance: ')
 print(rlc_account3_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_3 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_3 / rlc_token_d * rlc_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(rlc_account3_n+': Ethereum Balance '+str(rlc_w_call_3 / _e_d)+' $'+str(rlc_w_call_3 / _e_d * rlc_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+rlc_tokenName+' Balance: ')
 print(rlc_account4_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_4 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_4 / rlc_token_d * rlc_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(rlc_account4_n+': Ethereum Balance '+str(rlc_w_call_4 / _e_d)+' $'+str(rlc_w_call_4 / _e_d * rlc_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+rlc_tokenName+' Balance: ')
 print(rlc_account5_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_5 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_5 / rlc_token_d * rlc_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(rlc_account5_n+': Ethereum Balance '+str(rlc_w_call_5 / _e_d)+' $'+str(rlc_w_call_5 /_e_d * rlc_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+rlc_tokenName+' Balance: ')
 print(rlc_account6_n+': '+rlc_tokenName+' Balance: '+str(rlc_call_6 / rlc_token_d)+' Usd/'+rlc_tokenName+' Balance: $'+str(rlc_call_6 / rlc_token_d * rlc_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(rlc_account6_n+': Ethereum Balance '+str(rlc_w_call_6 / _e_d)+' $'+str(rlc_w_call_6 / _e_d * rlc_last_ethereum_price))
def rlc_unlock_all_accounts():
  rlc_unlock_account_0()
  rlc_unlock_account_1()
  rlc_unlock_account_2()
  rlc_unlock_account_3()
  rlc_unlock_account_4()
  rlc_unlock_account_5()
  rlc_unlock_account_6()


def rlc_unlock_account_0():
  global rlc_account0pw
  global rlc_account0
  global rlc_account0_n
  rlc_update_accounts()
  rlc_u_a_0 = rlc_w_unlock(rlc_account0, rlc_account0pw, rlc_unlockTime)
  if rlc_u_a_0 == False:
    if rlc_account0pw == '':
     rlc_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account0_n+' Passphrase Denied: '+rlc_account0pw_r)
    elif rlc_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rlc_account0_n+' Passphrase Denied: '+rlc_account0pw)
  if rlc_u_a_0 == True:
   print(rlc_account0_n+' Unlocked')

def rlc_unlock_account_1():
  global rlc_account1pw
  global rlc_account1
  global rlc_account1_n
  rlc_update_accounts()
  rlc_u_a_1 = rlc_unlock(rlc_account1, rlc_account1pw, rlc_unlockTime)
  if rlc_u_a_1 == False:
    if rlc_account1pw == '':
     rlc_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account1_n+' Passphrase Denied: '+rlc_account1pw_r)
    elif rlc_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rlc_account1_n+' Passphrase Denied: '+rlc_account1pw)
  if rlc_u_a_1 == True:
   print(rlc_account1_n+' Unlocked')

def rlc_unlock_account_2():
  global rlc_account2pw
  global rlc_account2
  global rlc_account2_n
  rlc_update_accounts()
  rlc_u_a_2 = rlc_unlock(rlc_account2, rlc_account2pw, rlc_unlockTime)
  if rlc_u_a_2 == False:
    if rlc_account2pw == '':
     rlc_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account2_n+' Passphrase Denied: '+rlc_account2pw_r)
    elif rlc_account2pw != '':
     print('Unlock Failure With Account '+rlc_account2_n+' Passphrase Denied: '+rlc_account2pw)
  if rlc_u_a_2 == True:
   print(rlc_account2_n+' Unlocked')

def rlc_unlock_account_3():
  global rlc_account3pw
  global rlc_account3
  global rlc_account3_n
  rlc_update_accounts()
  rlc_u_a_3 = rlc_unlock(rlc_account3, rlc_account3pw, rlc_unlockTime)
  if rlc_u_a_3 == False:
    if rlc_account3pw == '':
     rlc_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account3_n+' Passphrase Denied: '+rlc_account3pw_r)
    elif rlc_account3pw != '':
     print('Unlock Failure With Account '+rlc_account3_n+' Passphrase Denied: '+rlc_account3pw)
  if rlc_u_a_3 == True:
   print(rlc_account3_n+' Unlocked')

def rlc_unlock_account_4():
  global rlc_account4pw
  global rlc_account4
  global rlc_account4_n
  rlc_update_accounts()
  rlc_u_a_4 = rlc_unlock(rlc_account4, rlc_account4pw, rlc_unlockTime)
  if rlc_u_a_4 == False:
    if rlc_account4pw == '':
     rlc_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account4_n+' Passphrase Denied: '+rlc_account4pw_r)
    elif rlc_account4pw != '':
     print('Unlock Failure With Account '+rlc_account4_n+' Passphrase Denied: '+rlc_account4pw)
  if rlc_u_a_4 == True:
   print(rlc_account4_n+' Unlocked')

def rlc_unlock_account_5():
  global rlc_account5pw
  global rlc_account5
  global rlc_account5_n
  rlc_update_accounts()
  rlc_u_a_5 = rlc_unlock(rlc_account5, rlc_account5pw, rlc_unlockTime)
  if rlc_u_a_5 == False:
    if rlc_account5pw == '':
     rlc_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account5_n+' Passphrase Denied: '+rlc_account5pw_r)
    elif rlc_account5pw != '':
     print('Unlock Failure With Account '+rlc_account5_n+' Passphrase Denied: '+rlc_account5pw)
  if rlc_u_a_5 == True:
   print(rlc_account5_n+' Unlocked')

def rlc_unlock_account_6():
  global rlc_account6pw
  global rlc_account6
  global rlc_account6_n
  rlc_update_accounts()
  rlc_u_a_6 = rlc_unlock(rlc_account6, rlc_account6pw, rlc_unlockTime)
  if rlc_u_a_6 == False:
    if rlc_account6pw == '':
     rlc_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlc_account6_n+' Passphrase Denied: '+rlc_account6pw_r)
    elif rlc_account6pw != '':
     print('Unlock Failure With Account '+rlc_account6_n+' Passphrase Denied: '+rlc_account6pw)
  if rlc_u_a_6 == True:
   print(rlc_account6_n+' Unlocked')

def rlc_unlock_account(rlc_ua_accountNumber):
 rlc_update_accounts()
 rlc_ua_account_number = rlc_ua_accountNumber
 rlc_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if rlc_ua_account_number == rlc_ua_input[0]:
  rlc_unlock_account_0()
 if rlc_ua_account_number == rlc_ua_input[1]:
  rlc_unlock_account_1()
 if rlc_ua_account_number == rlc_ua_input[2]:
  rlc_unlock_account_2()
 if rlc_ua_account_number == rlc_ua_input[3]:
  rlc_unlock_account_3()
 if rlc_ua_account_number == rlc_ua_input[4]:
  rlc_unlock_account_4()
 if rlc_ua_account_number == rlc_ua_input[5]:
  rlc_unlock_account_5()
 if rlc_ua_account_number == rlc_ua_input[6]:
  rlc_unlock_account_6()
 if rlc_ua_account_number not in rlc_ua_input:
  print('Must Integer Within Range '+rlc_accounts_range+'.')
 

def rlc_approve_between_accounts(fromAccount, toAccount, msgValue):
  rlc_update_accounts()
  rlc_a_0 = rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(rlc_a_0)

def rlc_approve(fromAccountNumber, toAddress, msgValue):
  rlc_update_accounts()
  rlc_unlock_account(fromAccountNumber)
  rlc_a_1 = rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(rlc_a_1)

def rlc_transfer_between_accounts(fromAccount, toAccount, msgValue):
  rlc_update_accounts()
  rlc_unlock_account(fromAccount)
  rlc_t_0 = rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(rlc_t_0)

def rlc_transfer(fromAccountNumber, toAddress, msgValue):
  rlc_update_accounts()
  rlc_unlock_account(fromAccountNumber)
  rlc_t_1 = rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(rlc_t_1)

def rlc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  rlc_update_accounts()
  rlc_unlock_account(callAccount)
  rlc_tf_0 = rlc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(rlc_tf_0)

def rlc_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  rlc_update_accounts()
  rlc_unlock_account(callAccount)
  rlc_tf_1 = rlc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(rlc_tf_1)
  


def rlc_help():
  print('Following Functions For '+rlc_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * rlc_unlock => web3.personal.unlockAccount
/ * rlc_accounts => web3.personal.listAccounts
/ * rlc_balance = web3.eth.getBalance
** rlc => web3.eth.contract(abi=rlc_abi, address=rlc_address)
** / * rlc_balanceOf => rlc.call().balanceOf

~ Function Listing Below:
~ rlc_update_accounts()
~ rlc_update_balances() \n\r -- => rlc_update_accounts()
~ rlc_list_all_accounts() \n\r -- => rlc_update_accounts()
~ rlc_account_balance(accountNumber) \n\r -- => rlc_update_balances() 
~ rlc_list_all_account_balances() \n\r -- => rlc_update_balances()
~ rlc_unlock_all_accounts() \n\r -- => rlc_unlock_account_0() \n\r -- => rlc_unlock_account_1() \n\r -- => rlc_unlock_account_2() \n\r -- => rlc_unlock_account_3() \n\r -- => rlc_unlock_account_4() \n\r -- => rlc_unlock_account_5() \n\r -- => rlc_unlock_account_6() 
~ rlc_unlock_account_0() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account0, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_1() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account1, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_2() \n\r -- => rlc_update_accounts() \n\r --/ *rlc_w_unlock(rlc_account2, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_3() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account3, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_4() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account4, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_5() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account5, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account_6() \n\r -- => rlc_update_accounts() \n\r -- / *rlc_w_unlock(rlc_account6, rlc_account0pw, rlc_unlockTime)
~ rlc_unlock_account(rlc_ua_accountNumber) \n\r -- => rlc_update_accounts() \n\r -- // rlc_unlock_account_0() \n\r -- // rlc_unlock_account_1() \n\r -- // rlc_unlock_account_2() \n\r -- // rlc_unlock_account_3() \n\r -- // rlc_unlock_account_4() \n\r -- // rlc_unlock_account_5() \n\r -- // rlc_unlock_account_6()
~ rlc_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(fromAccount) \n\r -- / ** rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rlc_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(fromAccountNumber) \n\r -- / ** rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rlc_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(fromAccount) \n\r -- / ** rlc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ rlc_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(fromAccountNumber) \n\r -- / ** rlc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rlc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(callAccount) \n\r / ** rlc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rlc_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rlc_update_accounts() \n\r -- => rlc_unlock_account(callAccount) \n\r -- / ** rlc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ rlc_help() <-- You Are Here. ''')