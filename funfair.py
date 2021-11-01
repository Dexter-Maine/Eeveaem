#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global fun_account_0_a
global fun_account_1_a
global fun_account_2_a
global fun_account_3_a
global fun_account_4_a
global fun_account_5_a
global fun_account_6_a
global fun_address
global fun_abi
global fun
global fun_call_0
global fun_call_1
global fun_call_2
global fun_call_3
global fun_call_4
global fun_call_5
global fun_call_6
global fun_call_ab
global fun_accounts
global fun_account_0_pw
global fun_account_1_pw
global fun_account_2_pw
global fun_account_3_pw
global fun_account_4_pw
global fun_account_5_pw
global fun_account_6_pw
global fun_account_0_n
global fun_account_1_n
global fun_account_2_n
global fun_account_3_n
global fun_account_4_n
global fun_account_5_n
global fun_account_6_n
global fun_account1pw
global fun_account2pw
global fun_account3pw
global fun_account4pw
global fun_account5pw
global fun_account6pw
global fun_last_price
global fun_accounts_range
global fun_tokenName
global fun_last_ethereum_price
global fun_unlockTime
global fun_balance
global fun_balanceOf
global fun_unlock
global fun_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
fun_token_d = 1e8
_e_d = 1e18
fun_accounts_range = '[0, 6]'
fun_unlock = web3.personal.unlockAccount
fun_last_ethereum_price = 370.00
fun_last_price = 0.03
fun_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
fun_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
fun_tokenName = 'FunFair Token'
fun_unlockTime = hex(10000) # Must be hex()
fun_account_0_a = fun_accounts[0]
fun_account_1_a = fun_accounts[1]
fun_account_2_a = fun_accounts[2]
fun_account_3_a = fun_accounts[3]
fun_account_4_a = fun_accounts[4]
fun_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
fun_account_6_a = fun_accounts[6]
# Supply Unlock Passwords For Transactions Below
fun_account_0_pw = 'GuildSkrypt2017!@#'
fun_account_1_pw = ''
fun_account_2_pw = 'GuildSkrypt2017!@#'
fun_account_3_pw = ''
fun_account_4_pw = ''
fun_account_5_pw = ''
fun_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
fun_account_0_n = 'Skotys Bittrex Account'
fun_account_1_n = 'Jeffs Account'
fun_account_2_n = 'Skrypts Bittrex Account'
fun_account_3_n = 'Skotys Personal Account'
fun_account_4_n = 'Unknown'
fun_account_5_n = 'Watched \'Bittrex\' Account.'
fun_account_6_n = 'Watched Account (1)'
# Contract Information Below :
fun_address = '0x419D0d8BdD9aF5e606Ae2232ed285Aff190E711b'
fun_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"multilocked","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"bits","type":"uint256[]"}],"name":"multiApprove","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"motd","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_m","type":"string"}],"name":"setMotd","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_to","type":"address"}],"name":"claimTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"a","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"lockMultis","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"controllerApprove","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_c","type":"address"}],"name":"setController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"controllerTransfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"changeOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"bits","type":"uint256[]"}],"name":"multiTransfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"finalized","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"message","type":"string"}],"name":"Motd","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"token","type":"address"},{"indexed":false,"name":"to","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"logTokenTransfer","type":"event"}]
fun = web3.eth.contract(abi=fun_abi, address=fun_address)
fun_balanceOf = fun.call().balanceOf
# End Contract Information
def fun_update_accounts():
 global fun_account0
 global fun_account1
 global fun_account2
 global fun_account3
 global fun_account4
 global fun_account5
 global fun_account6
 global fun_account0_n
 global fun_account1_n
 global fun_account2_n
 global fun_account3_n
 global fun_account4_n
 global fun_account5_n
 global fun_account6_n
 global fun_account0pw
 global fun_account1pw
 global fun_account2pw
 global fun_account3pw
 global fun_account4pw
 global fun_account5pw
 global fun_account6pw
 fun_account0 = fun_account_0_a
 fun_account1 = fun_account_1_a
 fun_account2 = fun_account_2_a
 fun_account3 = fun_account_3_a
 fun_account4 = fun_account_4_a
 fun_account5 = fun_account_5_a
 fun_account6 = fun_account_6_a
 fun_account0_n = fun_account_0_n
 fun_account1_n = fun_account_1_n
 fun_account2_n = fun_account_2_n
 fun_account3_n = fun_account_3_n
 fun_account4_n = fun_account_4_n
 fun_account5_n = fun_account_5_n
 fun_account6_n = fun_account_6_n
 fun_account0pw = fun_account_0_pw
 fun_account1pw = fun_account_1_pw
 fun_account2pw = fun_account_2_pw
 fun_account3pw = fun_account_3_pw
 fun_account4pw = fun_account_4_pw
 fun_account5pw = fun_account_5_pw
 fun_account6pw = fun_account_6_pw
 print(fun_tokenName+' Accounts Updated.')
def fun_update_balances():
 global fun_call_0
 global fun_call_1
 global fun_call_2
 global fun_call_3
 global fun_call_4
 global fun_call_5
 global fun_call_6
 global fun_w_call_0
 global fun_w_call_1
 global fun_w_call_2
 global fun_w_call_3
 global fun_w_call_4
 global fun_w_call_5
 global fun_w_call_6
 fun_update_accounts()
 print('Updating '+fun_tokenName+' Balances Please Wait...')
 fun_call_0 = fun_balanceOf(fun_account0)
 fun_call_1 = fun_balanceOf(fun_account1)
 fun_call_2 = fun_balanceOf(fun_account2)
 fun_call_3 = fun_balanceOf(fun_account3)
 fun_call_4 = fun_balanceOf(fun_account4)
 fun_call_5 = fun_balanceOf(fun_account5)
 fun_call_6 = fun_balanceOf(fun_account6)
 fun_w_call_0 = fun_balance(fun_account0)
 fun_w_call_1 = fun_balance(fun_account1)
 fun_w_call_2 = fun_balance(fun_account2)
 fun_w_call_3 = fun_balance(fun_account3)
 fun_w_call_4 = fun_balance(fun_account4)
 fun_w_call_5 = fun_balance(fun_account5)
 fun_w_call_6 = fun_balance(fun_account6)
 print(fun_tokenName+' Balances Updated.')
def fun_list_all_accounts():
 fun_update_accounts()
 print(fun_tokenName+' '+fun_account0_n+': '+fun_account0)
 print(fun_tokenName+' '+fun_account1_n+': '+fun_account1)
 print(fun_tokenName+' '+fun_account2_n+': '+fun_account2)
 print(fun_tokenName+' '+fun_account3_n+': '+fun_account3)
 print(fun_tokenName+' '+fun_account4_n+': '+fun_account4)
 print(fun_tokenName+' '+fun_account5_n+': '+fun_account5)
 print(fun_tokenName+' '+fun_account6_n+': '+fun_account6)

def fun_account_balance(accountNumber):
 fun_update_balances()
 fun_ab_account_number = accountNumber
 fun_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if fun_ab_account_number == fun_ab_input[0]:
  print('Calling '+fun_account0_n+' '+fun_tokenName+' Balance: ')
  print(fun_account0_n+': '+fun_tokenName+' Balance: '+str(fun_call_0 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_0 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[1]:
  print('Calling '+fun_account1_n+' '+fun_tokenName+' Balance: ')
  print(fun_account1_n+': '+fun_tokenName+' Balance: '+str(fun_call_1 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_1 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[2]:
  print('Calling '+fun_account2_n+' '+fun_tokenName+' Balance: ')
  print(fun_account2_n+': '+fun_tokenName+' Balance: '+str(fun_call_2 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_2 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[3]:
  print('Calling '+fun_account3_n+' '+fun_tokenName+' Balance: ')
  print(fun_account3_n+': '+fun_tokenName+' Balance: '+str(fun_call_3 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_3 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[4]:
  print('Calling '+fun_account4_n+' '+fun_tokenName+' Balance: ')
  print(fun_account4_n+': '+fun_tokenName+' Balance: '+str(fun_call_4 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_4 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[5]:
  print('Calling '+fun_account5_n+' '+fun_tokenName+' Balance: ')
  print(fun_account5_n+': '+fun_tokenName+' Balance: '+str(fun_call_5 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_5 / fun_token_d * fun_last_price))
 if fun_ab_account_number == fun_ab_input[6]:
  print('Calling '+fun_account6_n+' '+fun_tokenName+' Balance: ')
  print(fun_account6_n+': '+fun_tokenName+' Balance: '+str(fun_call_6 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_6 / fun_token_d * fun_last_price))
 if fun_ab_account_number not in fun_ab_input:
  print('Must Integer Within Range '+fun_accounts_range+'.')

def fun_list_all_account_balances():
 fun_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+fun_tokenName+' Balance: ')
 print(fun_account0_n+': '+fun_tokenName+' Balance: '+str(fun_call_0 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_0 / fun_token_d * fun_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(fun_account0_n+': Ethereum Balance '+str(fun_w_call_0 / _e_d)+' $'+str(fun_w_call_0 / _e_d * fun_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+fun_tokenName+' Balance: ')
 print(fun_account1_n+': '+fun_tokenName+' Balance: '+str(fun_call_1 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_1 / fun_token_d * fun_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(fun_account1_n+': Ethereum Balance '+str(fun_w_call_1 / _e_d)+' $'+str(fun_w_call_1 / _e_d * fun_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+fun_tokenName+' Balance: ')
 print(fun_account2_n+': '+fun_tokenName+' Balance: '+str(fun_call_2 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_2 / fun_token_d * fun_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(fun_account2_n+': Ethereum Balance '+str(fun_w_call_2 / _e_d)+' $'+str(fun_w_call_2 / _e_d * fun_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+fun_tokenName+' Balance: ')
 print(fun_account3_n+': '+fun_tokenName+' Balance: '+str(fun_call_3 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_3 / fun_token_d * fun_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(fun_account3_n+': Ethereum Balance '+str(fun_w_call_3 / _e_d)+' $'+str(fun_w_call_3 / _e_d * fun_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+fun_tokenName+' Balance: ')
 print(fun_account4_n+': '+fun_tokenName+' Balance: '+str(fun_call_4 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_4 / fun_token_d * fun_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(fun_account4_n+': Ethereum Balance '+str(fun_w_call_4 / _e_d)+' $'+str(fun_w_call_4 / _e_d * fun_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+fun_tokenName+' Balance: ')
 print(fun_account5_n+': '+fun_tokenName+' Balance: '+str(fun_call_5 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_5 / fun_token_d * fun_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(fun_account5_n+': Ethereum Balance '+str(fun_w_call_5 / _e_d)+' $'+str(fun_w_call_5 /_e_d * fun_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+fun_tokenName+' Balance: ')
 print(fun_account6_n+': '+fun_tokenName+' Balance: '+str(fun_call_6 / fun_token_d)+' Usd/'+fun_tokenName+' Balance: $'+str(fun_call_6 / fun_token_d * fun_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(fun_account6_n+': Ethereum Balance '+str(fun_w_call_6 / _e_d)+' $'+str(fun_w_call_6 / _e_d * fun_last_ethereum_price))
def fun_unlock_all_accounts():
  fun_unlock_account_0()
  fun_unlock_account_1()
  fun_unlock_account_2()
  fun_unlock_account_3()
  fun_unlock_account_4()
  fun_unlock_account_5()
  fun_unlock_account_6()


def fun_unlock_account_0():
  global fun_account0pw
  global fun_account0
  global fun_account0_n
  fun_update_accounts()
  fun_u_a_0 = fun_w_unlock(fun_account0, fun_account0pw, fun_unlockTime)
  if fun_u_a_0 == False:
    if fun_account0pw == '':
     fun_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account0_n+' Passphrase Denied: '+fun_account0pw_r)
    elif fun_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+fun_account0_n+' Passphrase Denied: '+fun_account0pw)
  if fun_u_a_0 == True:
   print(fun_account0_n+' Unlocked')

def fun_unlock_account_1():
  global fun_account1pw
  global fun_account1
  global fun_account1_n
  fun_update_accounts()
  fun_u_a_1 = fun_unlock(fun_account1, fun_account1pw, fun_unlockTime)
  if fun_u_a_1 == False:
    if fun_account1pw == '':
     fun_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account1_n+' Passphrase Denied: '+fun_account1pw_r)
    elif fun_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+fun_account1_n+' Passphrase Denied: '+fun_account1pw)
  if fun_u_a_1 == True:
   print(fun_account1_n+' Unlocked')

def fun_unlock_account_2():
  global fun_account2pw
  global fun_account2
  global fun_account2_n
  fun_update_accounts()
  fun_u_a_2 = fun_unlock(fun_account2, fun_account2pw, fun_unlockTime)
  if fun_u_a_2 == False:
    if fun_account2pw == '':
     fun_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account2_n+' Passphrase Denied: '+fun_account2pw_r)
    elif fun_account2pw != '':
     print('Unlock Failure With Account '+fun_account2_n+' Passphrase Denied: '+fun_account2pw)
  if fun_u_a_2 == True:
   print(fun_account2_n+' Unlocked')

def fun_unlock_account_3():
  global fun_account3pw
  global fun_account3
  global fun_account3_n
  fun_update_accounts()
  fun_u_a_3 = fun_unlock(fun_account3, fun_account3pw, fun_unlockTime)
  if fun_u_a_3 == False:
    if fun_account3pw == '':
     fun_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account3_n+' Passphrase Denied: '+fun_account3pw_r)
    elif fun_account3pw != '':
     print('Unlock Failure With Account '+fun_account3_n+' Passphrase Denied: '+fun_account3pw)
  if fun_u_a_3 == True:
   print(fun_account3_n+' Unlocked')

def fun_unlock_account_4():
  global fun_account4pw
  global fun_account4
  global fun_account4_n
  fun_update_accounts()
  fun_u_a_4 = fun_unlock(fun_account4, fun_account4pw, fun_unlockTime)
  if fun_u_a_4 == False:
    if fun_account4pw == '':
     fun_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account4_n+' Passphrase Denied: '+fun_account4pw_r)
    elif fun_account4pw != '':
     print('Unlock Failure With Account '+fun_account4_n+' Passphrase Denied: '+fun_account4pw)
  if fun_u_a_4 == True:
   print(fun_account4_n+' Unlocked')

def fun_unlock_account_5():
  global fun_account5pw
  global fun_account5
  global fun_account5_n
  fun_update_accounts()
  fun_u_a_5 = fun_unlock(fun_account5, fun_account5pw, fun_unlockTime)
  if fun_u_a_5 == False:
    if fun_account5pw == '':
     fun_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account5_n+' Passphrase Denied: '+fun_account5pw_r)
    elif fun_account5pw != '':
     print('Unlock Failure With Account '+fun_account5_n+' Passphrase Denied: '+fun_account5pw)
  if fun_u_a_5 == True:
   print(fun_account5_n+' Unlocked')

def fun_unlock_account_6():
  global fun_account6pw
  global fun_account6
  global fun_account6_n
  fun_update_accounts()
  fun_u_a_6 = fun_unlock(fun_account6, fun_account6pw, fun_unlockTime)
  if fun_u_a_6 == False:
    if fun_account6pw == '':
     fun_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+fun_account6_n+' Passphrase Denied: '+fun_account6pw_r)
    elif fun_account6pw != '':
     print('Unlock Failure With Account '+fun_account6_n+' Passphrase Denied: '+fun_account6pw)
  if fun_u_a_6 == True:
   print(fun_account6_n+' Unlocked')

def fun_unlock_account(fun_ua_accountNumber):
 fun_update_accounts()
 fun_ua_account_number = fun_ua_accountNumber
 fun_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if fun_ua_account_number == fun_ua_input[0]:
  fun_unlock_account_0()
 if fun_ua_account_number == fun_ua_input[1]:
  fun_unlock_account_1()
 if fun_ua_account_number == fun_ua_input[2]:
  fun_unlock_account_2()
 if fun_ua_account_number == fun_ua_input[3]:
  fun_unlock_account_3()
 if fun_ua_account_number == fun_ua_input[4]:
  fun_unlock_account_4()
 if fun_ua_account_number == fun_ua_input[5]:
  fun_unlock_account_5()
 if fun_ua_account_number == fun_ua_input[6]:
  fun_unlock_account_6()
 if fun_ua_account_number not in fun_ua_input:
  print('Must Integer Within Range '+fun_accounts_range+'.')
 

def fun_approve_between_accounts(fromAccount, toAccount, msgValue):
  fun_update_accounts()
  fun_a_0 = fun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(fun_a_0)

def fun_approve(fromAccountNumber, toAddress, msgValue):
  fun_update_accounts()
  fun_unlock_account(fromAccountNumber)
  fun_a_1 = fun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(fun_a_1)

def fun_transfer_between_accounts(fromAccount, toAccount, msgValue):
  fun_update_accounts()
  fun_unlock_account(fromAccount)
  fun_t_0 = fun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(fun_t_0)

def fun_transfer(fromAccountNumber, toAddress, msgValue):
  fun_update_accounts()
  fun_unlock_account(fromAccountNumber)
  fun_t_1 = fun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(fun_t_1)

def fun_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  fun_update_accounts()
  fun_unlock_account(callAccount)
  fun_tf_0 = fun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(fun_tf_0)

def fun_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  fun_update_accounts()
  fun_unlock_account(callAccount)
  fun_tf_1 = fun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(fun_tf_1)
  


def fun_help():
  print('Following Functions For '+fun_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * fun_unlock => web3.personal.unlockAccount
/ * fun_accounts => web3.personal.listAccounts
/ * fun_balance = web3.eth.getBalance
** fun => web3.eth.contract(abi=fun_abi, address=fun_address)
** / * fun_balanceOf => fun.call().balanceOf

~ Function Listing Below:
~ fun_update_accounts()
~ fun_update_balances() \n\r -- => fun_update_accounts()
~ fun_list_all_accounts() \n\r -- => fun_update_accounts()
~ fun_account_balance(accountNumber) \n\r -- => fun_update_balances() 
~ fun_list_all_account_balances() \n\r -- => fun_update_balances()
~ fun_unlock_all_accounts() \n\r -- => fun_unlock_account_0() \n\r -- => fun_unlock_account_1() \n\r -- => fun_unlock_account_2() \n\r -- => fun_unlock_account_3() \n\r -- => fun_unlock_account_4() \n\r -- => fun_unlock_account_5() \n\r -- => fun_unlock_account_6() 
~ fun_unlock_account_0() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account0, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_1() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account1, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_2() \n\r -- => fun_update_accounts() \n\r --/ *fun_w_unlock(fun_account2, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_3() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account3, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_4() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account4, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_5() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account5, fun_account0pw, fun_unlockTime)
~ fun_unlock_account_6() \n\r -- => fun_update_accounts() \n\r -- / *fun_w_unlock(fun_account6, fun_account0pw, fun_unlockTime)
~ fun_unlock_account(fun_ua_accountNumber) \n\r -- => fun_update_accounts() \n\r -- // fun_unlock_account_0() \n\r -- // fun_unlock_account_1() \n\r -- // fun_unlock_account_2() \n\r -- // fun_unlock_account_3() \n\r -- // fun_unlock_account_4() \n\r -- // fun_unlock_account_5() \n\r -- // fun_unlock_account_6()
~ fun_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(fromAccount) \n\r -- / ** fun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ fun_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(fromAccountNumber) \n\r -- / ** fun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ fun_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(fromAccount) \n\r -- / ** fun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ fun_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(fromAccountNumber) \n\r -- / ** fun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ fun_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(callAccount) \n\r / ** fun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ fun_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => fun_update_accounts() \n\r -- => fun_unlock_account(callAccount) \n\r -- / ** fun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ fun_help() <-- You Are Here. ''')