#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global omg_account_0_a
global omg_account_1_a
global omg_account_2_a
global omg_account_3_a
global omg_account_4_a
global omg_account_5_a
global omg_account_6_a
global omg_address
global omg_abi
global omg
global omg_call_0
global omg_call_1
global omg_call_2
global omg_call_3
global omg_call_4
global omg_call_5
global omg_call_6
global omg_call_ab
global omg_accounts
global omg_account_0_pw
global omg_account_1_pw
global omg_account_2_pw
global omg_account_3_pw
global omg_account_4_pw
global omg_account_5_pw
global omg_account_6_pw
global omg_account_0_n
global omg_account_1_n
global omg_account_2_n
global omg_account_3_n
global omg_account_4_n
global omg_account_5_n
global omg_account_6_n
global omg_account1pw
global omg_account2pw
global omg_account3pw
global omg_account4pw
global omg_account5pw
global omg_account6pw
global omg_last_price
global omg_accounts_range
global omg_tokenName
global omg_last_ethereum_price
global omg_unlockTime
global omg_balance
global omg_balanceOf
global omg_unlock
global omg_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
omg_token_d = 1e18
_e_d = 1e18
omg_accounts_range = '[0, 6]'
omg_unlock = web3.personal.unlockAccount
omg_last_ethereum_price = 370.00
omg_last_price = 11.32
omg_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
omg_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
omg_tokenName = 'OmiseGo Token'
omg_unlockTime = hex(10000) # Must be hex()
omg_account_0_a = omg_accounts[0]
omg_account_1_a = omg_accounts[1]
omg_account_2_a = omg_accounts[2]
omg_account_3_a = omg_accounts[3]
omg_account_4_a = omg_accounts[4]
omg_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
omg_account_6_a = omg_accounts[6]
# Supply Unlock Passwords For Transactions Below
omg_account_0_pw = 'GuildSkrypt2017!@#'
omg_account_1_pw = ''
omg_account_2_pw = 'GuildSkrypt2017!@#'
omg_account_3_pw = ''
omg_account_4_pw = ''
omg_account_5_pw = ''
omg_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
omg_account_0_n = 'Skotys Bittrex Account'
omg_account_1_n = 'Jeffs Account'
omg_account_2_n = 'Skrypts Bittrex Account'
omg_account_3_n = 'Skotys Personal Account'
omg_account_4_n = 'Unknown'
omg_account_5_n = 'Watched \'Bittrex\' Account.'
omg_account_6_n = 'Watched Account (1)'
# Contract Information Below :
omg_address = '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07'
omg_abi = [{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
omg = web3.eth.contract(abi=omg_abi, address=omg_address)
omg_balanceOf = omg.call().balanceOf
# End Contract Information
def omg_update_accounts():
 global omg_account0
 global omg_account1
 global omg_account2
 global omg_account3
 global omg_account4
 global omg_account5
 global omg_account6
 global omg_account0_n
 global omg_account1_n
 global omg_account2_n
 global omg_account3_n
 global omg_account4_n
 global omg_account5_n
 global omg_account6_n
 global omg_account0pw
 global omg_account1pw
 global omg_account2pw
 global omg_account3pw
 global omg_account4pw
 global omg_account5pw
 global omg_account6pw
 omg_account0 = omg_account_0_a
 omg_account1 = omg_account_1_a
 omg_account2 = omg_account_2_a
 omg_account3 = omg_account_3_a
 omg_account4 = omg_account_4_a
 omg_account5 = omg_account_5_a
 omg_account6 = omg_account_6_a
 omg_account0_n = omg_account_0_n
 omg_account1_n = omg_account_1_n
 omg_account2_n = omg_account_2_n
 omg_account3_n = omg_account_3_n
 omg_account4_n = omg_account_4_n
 omg_account5_n = omg_account_5_n
 omg_account6_n = omg_account_6_n
 omg_account0pw = omg_account_0_pw
 omg_account1pw = omg_account_1_pw
 omg_account2pw = omg_account_2_pw
 omg_account3pw = omg_account_3_pw
 omg_account4pw = omg_account_4_pw
 omg_account5pw = omg_account_5_pw
 omg_account6pw = omg_account_6_pw
 print(omg_tokenName+' Accounts Updated.')
def omg_update_balances():
 global omg_call_0
 global omg_call_1
 global omg_call_2
 global omg_call_3
 global omg_call_4
 global omg_call_5
 global omg_call_6
 global omg_w_call_0
 global omg_w_call_1
 global omg_w_call_2
 global omg_w_call_3
 global omg_w_call_4
 global omg_w_call_5
 global omg_w_call_6
 omg_update_accounts()
 print('Updating '+omg_tokenName+' Balances Please Wait...')
 omg_call_0 = omg_balanceOf(omg_account0)
 omg_call_1 = omg_balanceOf(omg_account1)
 omg_call_2 = omg_balanceOf(omg_account2)
 omg_call_3 = omg_balanceOf(omg_account3)
 omg_call_4 = omg_balanceOf(omg_account4)
 omg_call_5 = omg_balanceOf(omg_account5)
 omg_call_6 = omg_balanceOf(omg_account6)
 omg_w_call_0 = omg_balance(omg_account0)
 omg_w_call_1 = omg_balance(omg_account1)
 omg_w_call_2 = omg_balance(omg_account2)
 omg_w_call_3 = omg_balance(omg_account3)
 omg_w_call_4 = omg_balance(omg_account4)
 omg_w_call_5 = omg_balance(omg_account5)
 omg_w_call_6 = omg_balance(omg_account6)
 print(omg_tokenName+' Balances Updated.')
def omg_list_all_accounts():
 omg_update_accounts()
 print(omg_tokenName+' '+omg_account0_n+': '+omg_account0)
 print(omg_tokenName+' '+omg_account1_n+': '+omg_account1)
 print(omg_tokenName+' '+omg_account2_n+': '+omg_account2)
 print(omg_tokenName+' '+omg_account3_n+': '+omg_account3)
 print(omg_tokenName+' '+omg_account4_n+': '+omg_account4)
 print(omg_tokenName+' '+omg_account5_n+': '+omg_account5)
 print(omg_tokenName+' '+omg_account6_n+': '+omg_account6)

def omg_account_balance(accountNumber):
 omg_update_balances()
 omg_ab_account_number = accountNumber
 omg_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if omg_ab_account_number == omg_ab_input[0]:
  print('Calling '+omg_account0_n+' '+omg_tokenName+' Balance: ')
  print(omg_account0_n+': '+omg_tokenName+' Balance: '+str(omg_call_0 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_0 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[1]:
  print('Calling '+omg_account1_n+' '+omg_tokenName+' Balance: ')
  print(omg_account1_n+': '+omg_tokenName+' Balance: '+str(omg_call_1 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_1 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[2]:
  print('Calling '+omg_account2_n+' '+omg_tokenName+' Balance: ')
  print(omg_account2_n+': '+omg_tokenName+' Balance: '+str(omg_call_2 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_2 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[3]:
  print('Calling '+omg_account3_n+' '+omg_tokenName+' Balance: ')
  print(omg_account3_n+': '+omg_tokenName+' Balance: '+str(omg_call_3 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_3 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[4]:
  print('Calling '+omg_account4_n+' '+omg_tokenName+' Balance: ')
  print(omg_account4_n+': '+omg_tokenName+' Balance: '+str(omg_call_4 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_4 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[5]:
  print('Calling '+omg_account5_n+' '+omg_tokenName+' Balance: ')
  print(omg_account5_n+': '+omg_tokenName+' Balance: '+str(omg_call_5 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_5 / omg_token_d * omg_last_price))
 if omg_ab_account_number == omg_ab_input[6]:
  print('Calling '+omg_account6_n+' '+omg_tokenName+' Balance: ')
  print(omg_account6_n+': '+omg_tokenName+' Balance: '+str(omg_call_6 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_6 / omg_token_d * omg_last_price))
 if omg_ab_account_number not in omg_ab_input:
  print('Must Integer Within Range '+omg_accounts_range+'.')

def omg_list_all_account_balances():
 omg_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+omg_tokenName+' Balance: ')
 print(omg_account0_n+': '+omg_tokenName+' Balance: '+str(omg_call_0 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_0 / omg_token_d * omg_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(omg_account0_n+': Ethereum Balance '+str(omg_w_call_0 / _e_d)+' $'+str(omg_w_call_0 / _e_d * omg_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+omg_tokenName+' Balance: ')
 print(omg_account1_n+': '+omg_tokenName+' Balance: '+str(omg_call_1 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_1 / omg_token_d * omg_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(omg_account1_n+': Ethereum Balance '+str(omg_w_call_1 / _e_d)+' $'+str(omg_w_call_1 / _e_d * omg_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+omg_tokenName+' Balance: ')
 print(omg_account2_n+': '+omg_tokenName+' Balance: '+str(omg_call_2 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_2 / omg_token_d * omg_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(omg_account2_n+': Ethereum Balance '+str(omg_w_call_2 / _e_d)+' $'+str(omg_w_call_2 / _e_d * omg_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+omg_tokenName+' Balance: ')
 print(omg_account3_n+': '+omg_tokenName+' Balance: '+str(omg_call_3 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_3 / omg_token_d * omg_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(omg_account3_n+': Ethereum Balance '+str(omg_w_call_3 / _e_d)+' $'+str(omg_w_call_3 / _e_d * omg_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+omg_tokenName+' Balance: ')
 print(omg_account4_n+': '+omg_tokenName+' Balance: '+str(omg_call_4 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_4 / omg_token_d * omg_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(omg_account4_n+': Ethereum Balance '+str(omg_w_call_4 / _e_d)+' $'+str(omg_w_call_4 / _e_d * omg_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+omg_tokenName+' Balance: ')
 print(omg_account5_n+': '+omg_tokenName+' Balance: '+str(omg_call_5 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_5 / omg_token_d * omg_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(omg_account5_n+': Ethereum Balance '+str(omg_w_call_5 / _e_d)+' $'+str(omg_w_call_5 /_e_d * omg_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+omg_tokenName+' Balance: ')
 print(omg_account6_n+': '+omg_tokenName+' Balance: '+str(omg_call_6 / omg_token_d)+' Usd/'+omg_tokenName+' Balance: $'+str(omg_call_6 / omg_token_d * omg_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(omg_account6_n+': Ethereum Balance '+str(omg_w_call_6 / _e_d)+' $'+str(omg_w_call_6 / _e_d * omg_last_ethereum_price))
def omg_unlock_all_accounts():
  omg_unlock_account_0()
  omg_unlock_account_1()
  omg_unlock_account_2()
  omg_unlock_account_3()
  omg_unlock_account_4()
  omg_unlock_account_5()
  omg_unlock_account_6()


def omg_unlock_account_0():
  global omg_account0pw
  global omg_account0
  global omg_account0_n
  omg_update_accounts()
  omg_u_a_0 = omg_w_unlock(omg_account0, omg_account0pw, omg_unlockTime)
  if omg_u_a_0 == False:
    if omg_account0pw == '':
     omg_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account0_n+' Passphrase Denied: '+omg_account0pw_r)
    elif omg_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+omg_account0_n+' Passphrase Denied: '+omg_account0pw)
  if omg_u_a_0 == True:
   print(omg_account0_n+' Unlocked')

def omg_unlock_account_1():
  global omg_account1pw
  global omg_account1
  global omg_account1_n
  omg_update_accounts()
  omg_u_a_1 = omg_unlock(omg_account1, omg_account1pw, omg_unlockTime)
  if omg_u_a_1 == False:
    if omg_account1pw == '':
     omg_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account1_n+' Passphrase Denied: '+omg_account1pw_r)
    elif omg_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+omg_account1_n+' Passphrase Denied: '+omg_account1pw)
  if omg_u_a_1 == True:
   print(omg_account1_n+' Unlocked')

def omg_unlock_account_2():
  global omg_account2pw
  global omg_account2
  global omg_account2_n
  omg_update_accounts()
  omg_u_a_2 = omg_unlock(omg_account2, omg_account2pw, omg_unlockTime)
  if omg_u_a_2 == False:
    if omg_account2pw == '':
     omg_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account2_n+' Passphrase Denied: '+omg_account2pw_r)
    elif omg_account2pw != '':
     print('Unlock Failure With Account '+omg_account2_n+' Passphrase Denied: '+omg_account2pw)
  if omg_u_a_2 == True:
   print(omg_account2_n+' Unlocked')

def omg_unlock_account_3():
  global omg_account3pw
  global omg_account3
  global omg_account3_n
  omg_update_accounts()
  omg_u_a_3 = omg_unlock(omg_account3, omg_account3pw, omg_unlockTime)
  if omg_u_a_3 == False:
    if omg_account3pw == '':
     omg_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account3_n+' Passphrase Denied: '+omg_account3pw_r)
    elif omg_account3pw != '':
     print('Unlock Failure With Account '+omg_account3_n+' Passphrase Denied: '+omg_account3pw)
  if omg_u_a_3 == True:
   print(omg_account3_n+' Unlocked')

def omg_unlock_account_4():
  global omg_account4pw
  global omg_account4
  global omg_account4_n
  omg_update_accounts()
  omg_u_a_4 = omg_unlock(omg_account4, omg_account4pw, omg_unlockTime)
  if omg_u_a_4 == False:
    if omg_account4pw == '':
     omg_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account4_n+' Passphrase Denied: '+omg_account4pw_r)
    elif omg_account4pw != '':
     print('Unlock Failure With Account '+omg_account4_n+' Passphrase Denied: '+omg_account4pw)
  if omg_u_a_4 == True:
   print(omg_account4_n+' Unlocked')

def omg_unlock_account_5():
  global omg_account5pw
  global omg_account5
  global omg_account5_n
  omg_update_accounts()
  omg_u_a_5 = omg_unlock(omg_account5, omg_account5pw, omg_unlockTime)
  if omg_u_a_5 == False:
    if omg_account5pw == '':
     omg_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account5_n+' Passphrase Denied: '+omg_account5pw_r)
    elif omg_account5pw != '':
     print('Unlock Failure With Account '+omg_account5_n+' Passphrase Denied: '+omg_account5pw)
  if omg_u_a_5 == True:
   print(omg_account5_n+' Unlocked')

def omg_unlock_account_6():
  global omg_account6pw
  global omg_account6
  global omg_account6_n
  omg_update_accounts()
  omg_u_a_6 = omg_unlock(omg_account6, omg_account6pw, omg_unlockTime)
  if omg_u_a_6 == False:
    if omg_account6pw == '':
     omg_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+omg_account6_n+' Passphrase Denied: '+omg_account6pw_r)
    elif omg_account6pw != '':
     print('Unlock Failure With Account '+omg_account6_n+' Passphrase Denied: '+omg_account6pw)
  if omg_u_a_6 == True:
   print(omg_account6_n+' Unlocked')

def omg_unlock_account(omg_ua_accountNumber):
 omg_update_accounts()
 omg_ua_account_number = omg_ua_accountNumber
 omg_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if omg_ua_account_number == omg_ua_input[0]:
  omg_unlock_account_0()
 if omg_ua_account_number == omg_ua_input[1]:
  omg_unlock_account_1()
 if omg_ua_account_number == omg_ua_input[2]:
  omg_unlock_account_2()
 if omg_ua_account_number == omg_ua_input[3]:
  omg_unlock_account_3()
 if omg_ua_account_number == omg_ua_input[4]:
  omg_unlock_account_4()
 if omg_ua_account_number == omg_ua_input[5]:
  omg_unlock_account_5()
 if omg_ua_account_number == omg_ua_input[6]:
  omg_unlock_account_6()
 if omg_ua_account_number not in omg_ua_input:
  print('Must Integer Within Range '+omg_accounts_range+'.')
 

def omg_approve_between_accounts(fromAccount, toAccount, msgValue):
  omg_update_accounts()
  omg_a_0 = omg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(omg_a_0)

def omg_approve(fromAccountNumber, toAddress, msgValue):
  omg_update_accounts()
  omg_unlock_account(fromAccountNumber)
  omg_a_1 = omg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(omg_a_1)

def omg_transfer_between_accounts(fromAccount, toAccount, msgValue):
  omg_update_accounts()
  omg_unlock_account(fromAccount)
  omg_t_0 = omg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(omg_t_0)

def omg_transfer(fromAccountNumber, toAddress, msgValue):
  omg_update_accounts()
  omg_unlock_account(fromAccountNumber)
  omg_t_1 = omg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(omg_t_1)

def omg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  omg_update_accounts()
  omg_unlock_account(callAccount)
  omg_tf_0 = omg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(omg_tf_0)

def omg_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  omg_update_accounts()
  omg_unlock_account(callAccount)
  omg_tf_1 = omg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(omg_tf_1)
  


def omg_help():
  print('Following Functions For '+omg_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * omg_unlock => web3.personal.unlockAccount
/ * omg_accounts => web3.personal.listAccounts
/ * omg_balance = web3.eth.getBalance
** omg => web3.eth.contract(abi=omg_abi, address=omg_address)
** / * omg_balanceOf => omg.call().balanceOf

~ Function Listing Below:
~ omg_update_accounts()
~ omg_update_balances() \n\r -- => omg_update_accounts()
~ omg_list_all_accounts() \n\r -- => omg_update_accounts()
~ omg_account_balance(accountNumber) \n\r -- => omg_update_balances() 
~ omg_list_all_account_balances() \n\r -- => omg_update_balances()
~ omg_unlock_all_accounts() \n\r -- => omg_unlock_account_0() \n\r -- => omg_unlock_account_1() \n\r -- => omg_unlock_account_2() \n\r -- => omg_unlock_account_3() \n\r -- => omg_unlock_account_4() \n\r -- => omg_unlock_account_5() \n\r -- => omg_unlock_account_6() 
~ omg_unlock_account_0() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account0, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_1() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account1, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_2() \n\r -- => omg_update_accounts() \n\r --/ *omg_w_unlock(omg_account2, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_3() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account3, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_4() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account4, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_5() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account5, omg_account0pw, omg_unlockTime)
~ omg_unlock_account_6() \n\r -- => omg_update_accounts() \n\r -- / *omg_w_unlock(omg_account6, omg_account0pw, omg_unlockTime)
~ omg_unlock_account(omg_ua_accountNumber) \n\r -- => omg_update_accounts() \n\r -- // omg_unlock_account_0() \n\r -- // omg_unlock_account_1() \n\r -- // omg_unlock_account_2() \n\r -- // omg_unlock_account_3() \n\r -- // omg_unlock_account_4() \n\r -- // omg_unlock_account_5() \n\r -- // omg_unlock_account_6()
~ omg_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(fromAccount) \n\r -- / ** omg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ omg_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(fromAccountNumber) \n\r -- / ** omg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ omg_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(fromAccount) \n\r -- / ** omg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ omg_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(fromAccountNumber) \n\r -- / ** omg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ omg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(callAccount) \n\r / ** omg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ omg_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => omg_update_accounts() \n\r -- => omg_unlock_account(callAccount) \n\r -- / ** omg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ omg_help() <-- You Are Here. ''')