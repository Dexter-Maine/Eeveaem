#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global dgd_account_0_a
global dgd_account_1_a
global dgd_account_2_a
global dgd_account_3_a
global dgd_account_4_a
global dgd_account_5_a
global dgd_account_6_a
global dgd_address
global dgd_abi
global dgd
global dgd_call_0
global dgd_call_1
global dgd_call_2
global dgd_call_3
global dgd_call_4
global dgd_call_5
global dgd_call_6
global dgd_call_ab
global dgd_accounts
global dgd_account_0_pw
global dgd_account_1_pw
global dgd_account_2_pw
global dgd_account_3_pw
global dgd_account_4_pw
global dgd_account_5_pw
global dgd_account_6_pw
global dgd_account_0_n
global dgd_account_1_n
global dgd_account_2_n
global dgd_account_3_n
global dgd_account_4_n
global dgd_account_5_n
global dgd_account_6_n
global dgd_account1pw
global dgd_account2pw
global dgd_account3pw
global dgd_account4pw
global dgd_account5pw
global dgd_account6pw
global dgd_last_price
global dgd_accounts_range
global dgd_tokenName
global dgd_last_ethereum_price
global dgd_unlockTime
global dgd_balance
global dgd_balanceOf
global dgd_unlock
global dgd_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
dgd_token_d = 1e9
_e_d = 1e18
dgd_accounts_range = '[0, 6]'
dgd_unlock = web3.personal.unlockAccount
dgd_last_ethereum_price = 370.00
dgd_last_price = 99.24
dgd_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
dgd_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
dgd_tokenName = 'DGD Token'
dgd_unlockTime = hex(10000) # Must be hex()
dgd_account_0_a = dgd_accounts[0]
dgd_account_1_a = dgd_accounts[1]
dgd_account_2_a = dgd_accounts[2]
dgd_account_3_a = dgd_accounts[3]
dgd_account_4_a = dgd_accounts[4]
dgd_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
dgd_account_6_a = dgd_accounts[6]
# Supply Unlock Passwords For Transactions Below
dgd_account_0_pw = 'GuildSkrypt2017!@#'
dgd_account_1_pw = ''
dgd_account_2_pw = 'GuildSkrypt2017!@#'
dgd_account_3_pw = ''
dgd_account_4_pw = ''
dgd_account_5_pw = ''
dgd_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
dgd_account_0_n = 'Skotys Bittrex Account'
dgd_account_1_n = 'Jeffs Account'
dgd_account_2_n = 'Skrypts Bittrex Account'
dgd_account_3_n = 'Skotys Personal Account'
dgd_account_4_n = 'Unknown'
dgd_account_5_n = 'Watched \'Bittrex\' Account.'
dgd_account_6_n = 'Watched Account (1)'
# Contract Information Below :
dgd_address = '0xE0B7927c4aF23765Cb51314A0E0521A9645F0E2A'
dgd_abi = [{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"setOwner","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"subtractSafely","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeToAdd","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"addSafely","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"locked","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeToSubtract","outputs":[{"name":"","type":"bool"}],"type":"function"},{"inputs":[],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_recipient","type":"address"},{"indexed":true,"name":"_amount","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
dgd = web3.eth.contract(abi=dgd_abi, address=dgd_address)
dgd_balanceOf = dgd.call().balanceOf
# End Contract Information
def dgd_update_accounts():
 global dgd_account0
 global dgd_account1
 global dgd_account2
 global dgd_account3
 global dgd_account4
 global dgd_account5
 global dgd_account6
 global dgd_account0_n
 global dgd_account1_n
 global dgd_account2_n
 global dgd_account3_n
 global dgd_account4_n
 global dgd_account5_n
 global dgd_account6_n
 global dgd_account0pw
 global dgd_account1pw
 global dgd_account2pw
 global dgd_account3pw
 global dgd_account4pw
 global dgd_account5pw
 global dgd_account6pw
 dgd_account0 = dgd_account_0_a
 dgd_account1 = dgd_account_1_a
 dgd_account2 = dgd_account_2_a
 dgd_account3 = dgd_account_3_a
 dgd_account4 = dgd_account_4_a
 dgd_account5 = dgd_account_5_a
 dgd_account6 = dgd_account_6_a
 dgd_account0_n = dgd_account_0_n
 dgd_account1_n = dgd_account_1_n
 dgd_account2_n = dgd_account_2_n
 dgd_account3_n = dgd_account_3_n
 dgd_account4_n = dgd_account_4_n
 dgd_account5_n = dgd_account_5_n
 dgd_account6_n = dgd_account_6_n
 dgd_account0pw = dgd_account_0_pw
 dgd_account1pw = dgd_account_1_pw
 dgd_account2pw = dgd_account_2_pw
 dgd_account3pw = dgd_account_3_pw
 dgd_account4pw = dgd_account_4_pw
 dgd_account5pw = dgd_account_5_pw
 dgd_account6pw = dgd_account_6_pw
 print(dgd_tokenName+' Accounts Updated.')
def dgd_update_balances():
 global dgd_call_0
 global dgd_call_1
 global dgd_call_2
 global dgd_call_3
 global dgd_call_4
 global dgd_call_5
 global dgd_call_6
 global dgd_w_call_0
 global dgd_w_call_1
 global dgd_w_call_2
 global dgd_w_call_3
 global dgd_w_call_4
 global dgd_w_call_5
 global dgd_w_call_6
 dgd_update_accounts()
 print('Updating '+dgd_tokenName+' Balances Please Wait...')
 dgd_call_0 = dgd_balanceOf(dgd_account0)
 dgd_call_1 = dgd_balanceOf(dgd_account1)
 dgd_call_2 = dgd_balanceOf(dgd_account2)
 dgd_call_3 = dgd_balanceOf(dgd_account3)
 dgd_call_4 = dgd_balanceOf(dgd_account4)
 dgd_call_5 = dgd_balanceOf(dgd_account5)
 dgd_call_6 = dgd_balanceOf(dgd_account6)
 dgd_w_call_0 = dgd_balance(dgd_account0)
 dgd_w_call_1 = dgd_balance(dgd_account1)
 dgd_w_call_2 = dgd_balance(dgd_account2)
 dgd_w_call_3 = dgd_balance(dgd_account3)
 dgd_w_call_4 = dgd_balance(dgd_account4)
 dgd_w_call_5 = dgd_balance(dgd_account5)
 dgd_w_call_6 = dgd_balance(dgd_account6)
 print(dgd_tokenName+' Balances Updated.')
def dgd_list_all_accounts():
 dgd_update_accounts()
 print(dgd_tokenName+' '+dgd_account0_n+': '+dgd_account0)
 print(dgd_tokenName+' '+dgd_account1_n+': '+dgd_account1)
 print(dgd_tokenName+' '+dgd_account2_n+': '+dgd_account2)
 print(dgd_tokenName+' '+dgd_account3_n+': '+dgd_account3)
 print(dgd_tokenName+' '+dgd_account4_n+': '+dgd_account4)
 print(dgd_tokenName+' '+dgd_account5_n+': '+dgd_account5)
 print(dgd_tokenName+' '+dgd_account6_n+': '+dgd_account6)

def dgd_account_balance(accountNumber):
 dgd_update_balances()
 dgd_ab_account_number = accountNumber
 dgd_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if dgd_ab_account_number == dgd_ab_input[0]:
  print('Calling '+dgd_account0_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account0_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_0 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_0 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[1]:
  print('Calling '+dgd_account1_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account1_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_1 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_1 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[2]:
  print('Calling '+dgd_account2_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account2_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_2 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_2 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[3]:
  print('Calling '+dgd_account3_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account3_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_3 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_3 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[4]:
  print('Calling '+dgd_account4_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account4_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_4 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_4 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[5]:
  print('Calling '+dgd_account5_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account5_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_5 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_5 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number == dgd_ab_input[6]:
  print('Calling '+dgd_account6_n+' '+dgd_tokenName+' Balance: ')
  print(dgd_account6_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_6 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_6 / dgd_token_d * dgd_last_price))
 if dgd_ab_account_number not in dgd_ab_input:
  print('Must Integer Within Range '+dgd_accounts_range+'.')

def dgd_list_all_account_balances():
 dgd_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+dgd_tokenName+' Balance: ')
 print(dgd_account0_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_0 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_0 / dgd_token_d * dgd_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(dgd_account0_n+': Ethereum Balance '+str(dgd_w_call_0 / _e_d)+' $'+str(dgd_w_call_0 / _e_d * dgd_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+dgd_tokenName+' Balance: ')
 print(dgd_account1_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_1 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_1 / dgd_token_d * dgd_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(dgd_account1_n+': Ethereum Balance '+str(dgd_w_call_1 / _e_d)+' $'+str(dgd_w_call_1 / _e_d * dgd_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+dgd_tokenName+' Balance: ')
 print(dgd_account2_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_2 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_2 / dgd_token_d * dgd_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(dgd_account2_n+': Ethereum Balance '+str(dgd_w_call_2 / _e_d)+' $'+str(dgd_w_call_2 / _e_d * dgd_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+dgd_tokenName+' Balance: ')
 print(dgd_account3_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_3 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_3 / dgd_token_d * dgd_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(dgd_account3_n+': Ethereum Balance '+str(dgd_w_call_3 / _e_d)+' $'+str(dgd_w_call_3 / _e_d * dgd_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+dgd_tokenName+' Balance: ')
 print(dgd_account4_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_4 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_4 / dgd_token_d * dgd_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(dgd_account4_n+': Ethereum Balance '+str(dgd_w_call_4 / _e_d)+' $'+str(dgd_w_call_4 / _e_d * dgd_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+dgd_tokenName+' Balance: ')
 print(dgd_account5_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_5 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_5 / dgd_token_d * dgd_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(dgd_account5_n+': Ethereum Balance '+str(dgd_w_call_5 / _e_d)+' $'+str(dgd_w_call_5 /_e_d * dgd_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+dgd_tokenName+' Balance: ')
 print(dgd_account6_n+': '+dgd_tokenName+' Balance: '+str(dgd_call_6 / dgd_token_d)+' Usd/'+dgd_tokenName+' Balance: $'+str(dgd_call_6 / dgd_token_d * dgd_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(dgd_account6_n+': Ethereum Balance '+str(dgd_w_call_6 / _e_d)+' $'+str(dgd_w_call_6 / _e_d * dgd_last_ethereum_price))
def dgd_unlock_all_accounts():
  dgd_unlock_account_0()
  dgd_unlock_account_1()
  dgd_unlock_account_2()
  dgd_unlock_account_3()
  dgd_unlock_account_4()
  dgd_unlock_account_5()
  dgd_unlock_account_6()


def dgd_unlock_account_0():
  global dgd_account0pw
  global dgd_account0
  global dgd_account0_n
  dgd_update_accounts()
  dgd_u_a_0 = dgd_w_unlock(dgd_account0, dgd_account0pw, dgd_unlockTime)
  if dgd_u_a_0 == False:
    if dgd_account0pw == '':
     dgd_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account0_n+' Passphrase Denied: '+dgd_account0pw_r)
    elif dgd_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+dgd_account0_n+' Passphrase Denied: '+dgd_account0pw)
  if dgd_u_a_0 == True:
   print(dgd_account0_n+' Unlocked')

def dgd_unlock_account_1():
  global dgd_account1pw
  global dgd_account1
  global dgd_account1_n
  dgd_update_accounts()
  dgd_u_a_1 = dgd_unlock(dgd_account1, dgd_account1pw, dgd_unlockTime)
  if dgd_u_a_1 == False:
    if dgd_account1pw == '':
     dgd_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account1_n+' Passphrase Denied: '+dgd_account1pw_r)
    elif dgd_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+dgd_account1_n+' Passphrase Denied: '+dgd_account1pw)
  if dgd_u_a_1 == True:
   print(dgd_account1_n+' Unlocked')

def dgd_unlock_account_2():
  global dgd_account2pw
  global dgd_account2
  global dgd_account2_n
  dgd_update_accounts()
  dgd_u_a_2 = dgd_unlock(dgd_account2, dgd_account2pw, dgd_unlockTime)
  if dgd_u_a_2 == False:
    if dgd_account2pw == '':
     dgd_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account2_n+' Passphrase Denied: '+dgd_account2pw_r)
    elif dgd_account2pw != '':
     print('Unlock Failure With Account '+dgd_account2_n+' Passphrase Denied: '+dgd_account2pw)
  if dgd_u_a_2 == True:
   print(dgd_account2_n+' Unlocked')

def dgd_unlock_account_3():
  global dgd_account3pw
  global dgd_account3
  global dgd_account3_n
  dgd_update_accounts()
  dgd_u_a_3 = dgd_unlock(dgd_account3, dgd_account3pw, dgd_unlockTime)
  if dgd_u_a_3 == False:
    if dgd_account3pw == '':
     dgd_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account3_n+' Passphrase Denied: '+dgd_account3pw_r)
    elif dgd_account3pw != '':
     print('Unlock Failure With Account '+dgd_account3_n+' Passphrase Denied: '+dgd_account3pw)
  if dgd_u_a_3 == True:
   print(dgd_account3_n+' Unlocked')

def dgd_unlock_account_4():
  global dgd_account4pw
  global dgd_account4
  global dgd_account4_n
  dgd_update_accounts()
  dgd_u_a_4 = dgd_unlock(dgd_account4, dgd_account4pw, dgd_unlockTime)
  if dgd_u_a_4 == False:
    if dgd_account4pw == '':
     dgd_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account4_n+' Passphrase Denied: '+dgd_account4pw_r)
    elif dgd_account4pw != '':
     print('Unlock Failure With Account '+dgd_account4_n+' Passphrase Denied: '+dgd_account4pw)
  if dgd_u_a_4 == True:
   print(dgd_account4_n+' Unlocked')

def dgd_unlock_account_5():
  global dgd_account5pw
  global dgd_account5
  global dgd_account5_n
  dgd_update_accounts()
  dgd_u_a_5 = dgd_unlock(dgd_account5, dgd_account5pw, dgd_unlockTime)
  if dgd_u_a_5 == False:
    if dgd_account5pw == '':
     dgd_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account5_n+' Passphrase Denied: '+dgd_account5pw_r)
    elif dgd_account5pw != '':
     print('Unlock Failure With Account '+dgd_account5_n+' Passphrase Denied: '+dgd_account5pw)
  if dgd_u_a_5 == True:
   print(dgd_account5_n+' Unlocked')

def dgd_unlock_account_6():
  global dgd_account6pw
  global dgd_account6
  global dgd_account6_n
  dgd_update_accounts()
  dgd_u_a_6 = dgd_unlock(dgd_account6, dgd_account6pw, dgd_unlockTime)
  if dgd_u_a_6 == False:
    if dgd_account6pw == '':
     dgd_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dgd_account6_n+' Passphrase Denied: '+dgd_account6pw_r)
    elif dgd_account6pw != '':
     print('Unlock Failure With Account '+dgd_account6_n+' Passphrase Denied: '+dgd_account6pw)
  if dgd_u_a_6 == True:
   print(dgd_account6_n+' Unlocked')

def dgd_unlock_account(dgd_ua_accountNumber):
 dgd_update_accounts()
 dgd_ua_account_number = dgd_ua_accountNumber
 dgd_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if dgd_ua_account_number == dgd_ua_input[0]:
  dgd_unlock_account_0()
 if dgd_ua_account_number == dgd_ua_input[1]:
  dgd_unlock_account_1()
 if dgd_ua_account_number == dgd_ua_input[2]:
  dgd_unlock_account_2()
 if dgd_ua_account_number == dgd_ua_input[3]:
  dgd_unlock_account_3()
 if dgd_ua_account_number == dgd_ua_input[4]:
  dgd_unlock_account_4()
 if dgd_ua_account_number == dgd_ua_input[5]:
  dgd_unlock_account_5()
 if dgd_ua_account_number == dgd_ua_input[6]:
  dgd_unlock_account_6()
 if dgd_ua_account_number not in dgd_ua_input:
  print('Must Integer Within Range '+dgd_accounts_range+'.')
 

def dgd_approve_between_accounts(fromAccount, toAccount, msgValue):
  dgd_update_accounts()
  dgd_a_0 = dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(dgd_a_0)

def dgd_approve(fromAccountNumber, toAddress, msgValue):
  dgd_update_accounts()
  dgd_unlock_account(fromAccountNumber)
  dgd_a_1 = dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(dgd_a_1)

def dgd_transfer_between_accounts(fromAccount, toAccount, msgValue):
  dgd_update_accounts()
  dgd_unlock_account(fromAccount)
  dgd_t_0 = dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(dgd_t_0)

def dgd_transfer(fromAccountNumber, toAddress, msgValue):
  dgd_update_accounts()
  dgd_unlock_account(fromAccountNumber)
  dgd_t_1 = dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(dgd_t_1)

def dgd_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  dgd_update_accounts()
  dgd_unlock_account(callAccount)
  dgd_tf_0 = dgd.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(dgd_tf_0)

def dgd_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  dgd_update_accounts()
  dgd_unlock_account(callAccount)
  dgd_tf_1 = dgd.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(dgd_tf_1)
  


def dgd_help():
  print('Following Functions For '+dgd_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * dgd_unlock => web3.personal.unlockAccount
/ * dgd_accounts => web3.personal.listAccounts
/ * dgd_balance = web3.eth.getBalance
** dgd => web3.eth.contract(abi=dgd_abi, address=dgd_address)
** / * dgd_balanceOf => dgd.call().balanceOf

~ Function Listing Below:
~ dgd_update_accounts()
~ dgd_update_balances() \n\r -- => dgd_update_accounts()
~ dgd_list_all_accounts() \n\r -- => dgd_update_accounts()
~ dgd_account_balance(accountNumber) \n\r -- => dgd_update_balances() 
~ dgd_list_all_account_balances() \n\r -- => dgd_update_balances()
~ dgd_unlock_all_accounts() \n\r -- => dgd_unlock_account_0() \n\r -- => dgd_unlock_account_1() \n\r -- => dgd_unlock_account_2() \n\r -- => dgd_unlock_account_3() \n\r -- => dgd_unlock_account_4() \n\r -- => dgd_unlock_account_5() \n\r -- => dgd_unlock_account_6() 
~ dgd_unlock_account_0() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account0, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_1() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account1, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_2() \n\r -- => dgd_update_accounts() \n\r --/ *dgd_w_unlock(dgd_account2, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_3() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account3, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_4() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account4, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_5() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account5, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account_6() \n\r -- => dgd_update_accounts() \n\r -- / *dgd_w_unlock(dgd_account6, dgd_account0pw, dgd_unlockTime)
~ dgd_unlock_account(dgd_ua_accountNumber) \n\r -- => dgd_update_accounts() \n\r -- // dgd_unlock_account_0() \n\r -- // dgd_unlock_account_1() \n\r -- // dgd_unlock_account_2() \n\r -- // dgd_unlock_account_3() \n\r -- // dgd_unlock_account_4() \n\r -- // dgd_unlock_account_5() \n\r -- // dgd_unlock_account_6()
~ dgd_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(fromAccount) \n\r -- / ** dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ dgd_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(fromAccountNumber) \n\r -- / ** dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ dgd_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(fromAccount) \n\r -- / ** dgd.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ dgd_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(fromAccountNumber) \n\r -- / ** dgd.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ dgd_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(callAccount) \n\r / ** dgd.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ dgd_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => dgd_update_accounts() \n\r -- => dgd_unlock_account(callAccount) \n\r -- / ** dgd.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ dgd_help() <-- You Are Here. ''')