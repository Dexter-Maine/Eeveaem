#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global qrl_account_0_a
global qrl_account_1_a
global qrl_account_2_a
global qrl_account_3_a
global qrl_account_4_a
global qrl_account_5_a
global qrl_account_6_a
global qrl_address
global qrl_abi
global qrl
global qrl_call_0
global qrl_call_1
global qrl_call_2
global qrl_call_3
global qrl_call_4
global qrl_call_5
global qrl_call_6
global qrl_call_ab
global qrl_accounts
global qrl_account_0_pw
global qrl_account_1_pw
global qrl_account_2_pw
global qrl_account_3_pw
global qrl_account_4_pw
global qrl_account_5_pw
global qrl_account_6_pw
global qrl_account_0_n
global qrl_account_1_n
global qrl_account_2_n
global qrl_account_3_n
global qrl_account_4_n
global qrl_account_5_n
global qrl_account_6_n
global qrl_account1pw
global qrl_account2pw
global qrl_account3pw
global qrl_account4pw
global qrl_account5pw
global qrl_account6pw
global qrl_last_price
global qrl_accounts_range
global qrl_tokenName
global qrl_last_ethereum_price
global qrl_unlockTime
global qrl_balance
global qrl_balanceOf
global qrl_unlock
global qrl_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
qrl_token_d = 1e8
_e_d = 1e18
qrl_accounts_range = '[0, 6]'
qrl_unlock = web3.personal.unlockAccount
qrl_last_ethereum_price = 370.00
qrl_last_price = 0.70
qrl_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
qrl_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
qrl_tokenName = 'Qrl Token'
qrl_unlockTime = hex(10000) # Must be hex()
qrl_account_0_a = qrl_accounts[0]
qrl_account_1_a = qrl_accounts[1]
qrl_account_2_a = qrl_accounts[2]
qrl_account_3_a = qrl_accounts[3]
qrl_account_4_a = qrl_accounts[4]
qrl_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
qrl_account_6_a = qrl_accounts[6]
# Supply Unlock Passwords For Transactions Below
qrl_account_0_pw = 'GuildSkrypt2017!@#'
qrl_account_1_pw = ''
qrl_account_2_pw = 'GuildSkrypt2017!@#'
qrl_account_3_pw = ''
qrl_account_4_pw = ''
qrl_account_5_pw = ''
qrl_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
qrl_account_0_n = 'Skotys Bittrex Account'
qrl_account_1_n = 'Jeffs Account'
qrl_account_2_n = 'Skrypts Bittrex Account'
qrl_account_3_n = 'Skotys Personal Account'
qrl_account_4_n = 'Unknown'
qrl_account_5_n = 'Watched \'Bittrex\' Account.'
qrl_account_6_n = 'Watched Account (1)'
# Contract Information Below :
qrl_address = '0x697beac28B09E122C4332D163985e8a73121b97F'
qrl_abi = [{"constant":true,"inputs":[],"name":"creator","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"currentState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"supplyOut","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"allSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"close","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"forAddress","type":"address"},{"name":"tokenCount","type":"uint256"}],"name":"issueTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newCreator","type":"address"}],"name":"changeCreator","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"fb","type":"uint256"}],"name":"freeze","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"data","type":"uint256"}],"name":"setAllSupply","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
qrl = web3.eth.contract(abi=qrl_abi, address=qrl_address)
qrl_balanceOf = qrl.call().balanceOf
# End Contract Information
def qrl_update_accounts():
 global qrl_account0
 global qrl_account1
 global qrl_account2
 global qrl_account3
 global qrl_account4
 global qrl_account5
 global qrl_account6
 global qrl_account0_n
 global qrl_account1_n
 global qrl_account2_n
 global qrl_account3_n
 global qrl_account4_n
 global qrl_account5_n
 global qrl_account6_n
 global qrl_account0pw
 global qrl_account1pw
 global qrl_account2pw
 global qrl_account3pw
 global qrl_account4pw
 global qrl_account5pw
 global qrl_account6pw
 qrl_account0 = qrl_account_0_a
 qrl_account1 = qrl_account_1_a
 qrl_account2 = qrl_account_2_a
 qrl_account3 = qrl_account_3_a
 qrl_account4 = qrl_account_4_a
 qrl_account5 = qrl_account_5_a
 qrl_account6 = qrl_account_6_a
 qrl_account0_n = qrl_account_0_n
 qrl_account1_n = qrl_account_1_n
 qrl_account2_n = qrl_account_2_n
 qrl_account3_n = qrl_account_3_n
 qrl_account4_n = qrl_account_4_n
 qrl_account5_n = qrl_account_5_n
 qrl_account6_n = qrl_account_6_n
 qrl_account0pw = qrl_account_0_pw
 qrl_account1pw = qrl_account_1_pw
 qrl_account2pw = qrl_account_2_pw
 qrl_account3pw = qrl_account_3_pw
 qrl_account4pw = qrl_account_4_pw
 qrl_account5pw = qrl_account_5_pw
 qrl_account6pw = qrl_account_6_pw
 print(qrl_tokenName+' Accounts Updated.')
def qrl_update_balances():
 global qrl_call_0
 global qrl_call_1
 global qrl_call_2
 global qrl_call_3
 global qrl_call_4
 global qrl_call_5
 global qrl_call_6
 global qrl_w_call_0
 global qrl_w_call_1
 global qrl_w_call_2
 global qrl_w_call_3
 global qrl_w_call_4
 global qrl_w_call_5
 global qrl_w_call_6
 qrl_update_accounts()
 print('Updating '+qrl_tokenName+' Balances Please Wait...')
 qrl_call_0 = qrl_balanceOf(qrl_account0)
 qrl_call_1 = qrl_balanceOf(qrl_account1)
 qrl_call_2 = qrl_balanceOf(qrl_account2)
 qrl_call_3 = qrl_balanceOf(qrl_account3)
 qrl_call_4 = qrl_balanceOf(qrl_account4)
 qrl_call_5 = qrl_balanceOf(qrl_account5)
 qrl_call_6 = qrl_balanceOf(qrl_account6)
 qrl_w_call_0 = qrl_balance(qrl_account0)
 qrl_w_call_1 = qrl_balance(qrl_account1)
 qrl_w_call_2 = qrl_balance(qrl_account2)
 qrl_w_call_3 = qrl_balance(qrl_account3)
 qrl_w_call_4 = qrl_balance(qrl_account4)
 qrl_w_call_5 = qrl_balance(qrl_account5)
 qrl_w_call_6 = qrl_balance(qrl_account6)
 print(qrl_tokenName+' Balances Updated.')
def qrl_list_all_accounts():
 qrl_update_accounts()
 print(qrl_tokenName+' '+qrl_account0_n+': '+qrl_account0)
 print(qrl_tokenName+' '+qrl_account1_n+': '+qrl_account1)
 print(qrl_tokenName+' '+qrl_account2_n+': '+qrl_account2)
 print(qrl_tokenName+' '+qrl_account3_n+': '+qrl_account3)
 print(qrl_tokenName+' '+qrl_account4_n+': '+qrl_account4)
 print(qrl_tokenName+' '+qrl_account5_n+': '+qrl_account5)
 print(qrl_tokenName+' '+qrl_account6_n+': '+qrl_account6)

def qrl_account_balance(accountNumber):
 qrl_update_balances()
 qrl_ab_account_number = accountNumber
 qrl_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if qrl_ab_account_number == qrl_ab_input[0]:
  print('Calling '+qrl_account0_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account0_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_0 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_0 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[1]:
  print('Calling '+qrl_account1_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account1_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_1 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_1 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[2]:
  print('Calling '+qrl_account2_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account2_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_2 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_2 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[3]:
  print('Calling '+qrl_account3_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account3_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_3 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_3 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[4]:
  print('Calling '+qrl_account4_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account4_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_4 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_4 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[5]:
  print('Calling '+qrl_account5_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account5_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_5 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_5 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number == qrl_ab_input[6]:
  print('Calling '+qrl_account6_n+' '+qrl_tokenName+' Balance: ')
  print(qrl_account6_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_6 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_6 / qrl_token_d * qrl_last_price))
 if qrl_ab_account_number not in qrl_ab_input:
  print('Must Integer Within Range '+qrl_accounts_range+'.')

def qrl_list_all_account_balances():
 qrl_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+qrl_tokenName+' Balance: ')
 print(qrl_account0_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_0 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_0 / qrl_token_d * qrl_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(qrl_account0_n+': Ethereum Balance '+str(qrl_w_call_0 / _e_d)+' $'+str(qrl_w_call_0 / _e_d * qrl_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+qrl_tokenName+' Balance: ')
 print(qrl_account1_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_1 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_1 / qrl_token_d * qrl_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(qrl_account1_n+': Ethereum Balance '+str(qrl_w_call_1 / _e_d)+' $'+str(qrl_w_call_1 / _e_d * qrl_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+qrl_tokenName+' Balance: ')
 print(qrl_account2_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_2 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_2 / qrl_token_d * qrl_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(qrl_account2_n+': Ethereum Balance '+str(qrl_w_call_2 / _e_d)+' $'+str(qrl_w_call_2 / _e_d * qrl_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+qrl_tokenName+' Balance: ')
 print(qrl_account3_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_3 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_3 / qrl_token_d * qrl_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(qrl_account3_n+': Ethereum Balance '+str(qrl_w_call_3 / _e_d)+' $'+str(qrl_w_call_3 / _e_d * qrl_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+qrl_tokenName+' Balance: ')
 print(qrl_account4_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_4 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_4 / qrl_token_d * qrl_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(qrl_account4_n+': Ethereum Balance '+str(qrl_w_call_4 / _e_d)+' $'+str(qrl_w_call_4 / _e_d * qrl_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+qrl_tokenName+' Balance: ')
 print(qrl_account5_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_5 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_5 / qrl_token_d * qrl_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(qrl_account5_n+': Ethereum Balance '+str(qrl_w_call_5 / _e_d)+' $'+str(qrl_w_call_5 /_e_d * qrl_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+qrl_tokenName+' Balance: ')
 print(qrl_account6_n+': '+qrl_tokenName+' Balance: '+str(qrl_call_6 / qrl_token_d)+' Usd/'+qrl_tokenName+' Balance: $'+str(qrl_call_6 / qrl_token_d * qrl_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(qrl_account6_n+': Ethereum Balance '+str(qrl_w_call_6 / _e_d)+' $'+str(qrl_w_call_6 / _e_d * qrl_last_ethereum_price))
def qrl_unlock_all_accounts():
  qrl_unlock_account_0()
  qrl_unlock_account_1()
  qrl_unlock_account_2()
  qrl_unlock_account_3()
  qrl_unlock_account_4()
  qrl_unlock_account_5()
  qrl_unlock_account_6()


def qrl_unlock_account_0():
  global qrl_account0pw
  global qrl_account0
  global qrl_account0_n
  qrl_update_accounts()
  qrl_u_a_0 = qrl_w_unlock(qrl_account0, qrl_account0pw, qrl_unlockTime)
  if qrl_u_a_0 == False:
    if qrl_account0pw == '':
     qrl_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account0_n+' Passphrase Denied: '+qrl_account0pw_r)
    elif qrl_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+qrl_account0_n+' Passphrase Denied: '+qrl_account0pw)
  if qrl_u_a_0 == True:
   print(qrl_account0_n+' Unlocked')

def qrl_unlock_account_1():
  global qrl_account1pw
  global qrl_account1
  global qrl_account1_n
  qrl_update_accounts()
  qrl_u_a_1 = qrl_unlock(qrl_account1, qrl_account1pw, qrl_unlockTime)
  if qrl_u_a_1 == False:
    if qrl_account1pw == '':
     qrl_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account1_n+' Passphrase Denied: '+qrl_account1pw_r)
    elif qrl_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+qrl_account1_n+' Passphrase Denied: '+qrl_account1pw)
  if qrl_u_a_1 == True:
   print(qrl_account1_n+' Unlocked')

def qrl_unlock_account_2():
  global qrl_account2pw
  global qrl_account2
  global qrl_account2_n
  qrl_update_accounts()
  qrl_u_a_2 = qrl_unlock(qrl_account2, qrl_account2pw, qrl_unlockTime)
  if qrl_u_a_2 == False:
    if qrl_account2pw == '':
     qrl_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account2_n+' Passphrase Denied: '+qrl_account2pw_r)
    elif qrl_account2pw != '':
     print('Unlock Failure With Account '+qrl_account2_n+' Passphrase Denied: '+qrl_account2pw)
  if qrl_u_a_2 == True:
   print(qrl_account2_n+' Unlocked')

def qrl_unlock_account_3():
  global qrl_account3pw
  global qrl_account3
  global qrl_account3_n
  qrl_update_accounts()
  qrl_u_a_3 = qrl_unlock(qrl_account3, qrl_account3pw, qrl_unlockTime)
  if qrl_u_a_3 == False:
    if qrl_account3pw == '':
     qrl_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account3_n+' Passphrase Denied: '+qrl_account3pw_r)
    elif qrl_account3pw != '':
     print('Unlock Failure With Account '+qrl_account3_n+' Passphrase Denied: '+qrl_account3pw)
  if qrl_u_a_3 == True:
   print(qrl_account3_n+' Unlocked')

def qrl_unlock_account_4():
  global qrl_account4pw
  global qrl_account4
  global qrl_account4_n
  qrl_update_accounts()
  qrl_u_a_4 = qrl_unlock(qrl_account4, qrl_account4pw, qrl_unlockTime)
  if qrl_u_a_4 == False:
    if qrl_account4pw == '':
     qrl_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account4_n+' Passphrase Denied: '+qrl_account4pw_r)
    elif qrl_account4pw != '':
     print('Unlock Failure With Account '+qrl_account4_n+' Passphrase Denied: '+qrl_account4pw)
  if qrl_u_a_4 == True:
   print(qrl_account4_n+' Unlocked')

def qrl_unlock_account_5():
  global qrl_account5pw
  global qrl_account5
  global qrl_account5_n
  qrl_update_accounts()
  qrl_u_a_5 = qrl_unlock(qrl_account5, qrl_account5pw, qrl_unlockTime)
  if qrl_u_a_5 == False:
    if qrl_account5pw == '':
     qrl_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account5_n+' Passphrase Denied: '+qrl_account5pw_r)
    elif qrl_account5pw != '':
     print('Unlock Failure With Account '+qrl_account5_n+' Passphrase Denied: '+qrl_account5pw)
  if qrl_u_a_5 == True:
   print(qrl_account5_n+' Unlocked')

def qrl_unlock_account_6():
  global qrl_account6pw
  global qrl_account6
  global qrl_account6_n
  qrl_update_accounts()
  qrl_u_a_6 = qrl_unlock(qrl_account6, qrl_account6pw, qrl_unlockTime)
  if qrl_u_a_6 == False:
    if qrl_account6pw == '':
     qrl_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+qrl_account6_n+' Passphrase Denied: '+qrl_account6pw_r)
    elif qrl_account6pw != '':
     print('Unlock Failure With Account '+qrl_account6_n+' Passphrase Denied: '+qrl_account6pw)
  if qrl_u_a_6 == True:
   print(qrl_account6_n+' Unlocked')

def qrl_unlock_account(qrl_ua_accountNumber):
 qrl_update_accounts()
 qrl_ua_account_number = qrl_ua_accountNumber
 qrl_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if qrl_ua_account_number == qrl_ua_input[0]:
  qrl_unlock_account_0()
 if qrl_ua_account_number == qrl_ua_input[1]:
  qrl_unlock_account_1()
 if qrl_ua_account_number == qrl_ua_input[2]:
  qrl_unlock_account_2()
 if qrl_ua_account_number == qrl_ua_input[3]:
  qrl_unlock_account_3()
 if qrl_ua_account_number == qrl_ua_input[4]:
  qrl_unlock_account_4()
 if qrl_ua_account_number == qrl_ua_input[5]:
  qrl_unlock_account_5()
 if qrl_ua_account_number == qrl_ua_input[6]:
  qrl_unlock_account_6()
 if qrl_ua_account_number not in qrl_ua_input:
  print('Must Integer Within Range '+qrl_accounts_range+'.')
 

def qrl_approve_between_accounts(fromAccount, toAccount, msgValue):
  qrl_update_accounts()
  qrl_a_0 = qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(qrl_a_0)

def qrl_approve(fromAccountNumber, toAddress, msgValue):
  qrl_update_accounts()
  qrl_unlock_account(fromAccountNumber)
  qrl_a_1 = qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(qrl_a_1)

def qrl_transfer_between_accounts(fromAccount, toAccount, msgValue):
  qrl_update_accounts()
  qrl_unlock_account(fromAccount)
  qrl_t_0 = qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(qrl_t_0)

def qrl_transfer(fromAccountNumber, toAddress, msgValue):
  qrl_update_accounts()
  qrl_unlock_account(fromAccountNumber)
  qrl_t_1 = qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(qrl_t_1)

def qrl_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  qrl_update_accounts()
  qrl_unlock_account(callAccount)
  qrl_tf_0 = qrl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(qrl_tf_0)

def qrl_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  qrl_update_accounts()
  qrl_unlock_account(callAccount)
  qrl_tf_1 = qrl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(qrl_tf_1)
  


def qrl_help():
  print('Following Functions For '+qrl_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * qrl_unlock => web3.personal.unlockAccount
/ * qrl_accounts => web3.personal.listAccounts
/ * qrl_balance = web3.eth.getBalance
** qrl => web3.eth.contract(abi=qrl_abi, address=qrl_address)
** / * qrl_balanceOf => qrl.call().balanceOf

~ Function Listing Below:
~ qrl_update_accounts()
~ qrl_update_balances() \n\r -- => qrl_update_accounts()
~ qrl_list_all_accounts() \n\r -- => qrl_update_accounts()
~ qrl_account_balance(accountNumber) \n\r -- => qrl_update_balances() 
~ qrl_list_all_account_balances() \n\r -- => qrl_update_balances()
~ qrl_unlock_all_accounts() \n\r -- => qrl_unlock_account_0() \n\r -- => qrl_unlock_account_1() \n\r -- => qrl_unlock_account_2() \n\r -- => qrl_unlock_account_3() \n\r -- => qrl_unlock_account_4() \n\r -- => qrl_unlock_account_5() \n\r -- => qrl_unlock_account_6() 
~ qrl_unlock_account_0() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account0, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_1() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account1, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_2() \n\r -- => qrl_update_accounts() \n\r --/ *qrl_w_unlock(qrl_account2, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_3() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account3, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_4() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account4, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_5() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account5, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account_6() \n\r -- => qrl_update_accounts() \n\r -- / *qrl_w_unlock(qrl_account6, qrl_account0pw, qrl_unlockTime)
~ qrl_unlock_account(qrl_ua_accountNumber) \n\r -- => qrl_update_accounts() \n\r -- // qrl_unlock_account_0() \n\r -- // qrl_unlock_account_1() \n\r -- // qrl_unlock_account_2() \n\r -- // qrl_unlock_account_3() \n\r -- // qrl_unlock_account_4() \n\r -- // qrl_unlock_account_5() \n\r -- // qrl_unlock_account_6()
~ qrl_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(fromAccount) \n\r -- / ** qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ qrl_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(fromAccountNumber) \n\r -- / ** qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ qrl_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(fromAccount) \n\r -- / ** qrl.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ qrl_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(fromAccountNumber) \n\r -- / ** qrl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ qrl_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(callAccount) \n\r / ** qrl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ qrl_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => qrl_update_accounts() \n\r -- => qrl_unlock_account(callAccount) \n\r -- / ** qrl.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ qrl_help() <-- You Are Here. ''')