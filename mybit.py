#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global myb_account_0_a
global myb_account_1_a
global myb_account_2_a
global myb_account_3_a
global myb_account_4_a
global myb_account_5_a
global myb_account_6_a
global myb_address
global myb_abi
global myb
global myb_call_0
global myb_call_1
global myb_call_2
global myb_call_3
global myb_call_4
global myb_call_5
global myb_call_6
global myb_call_ab
global myb_accounts
global myb_account_0_pw
global myb_account_1_pw
global myb_account_2_pw
global myb_account_3_pw
global myb_account_4_pw
global myb_account_5_pw
global myb_account_6_pw
global myb_account_0_n
global myb_account_1_n
global myb_account_2_n
global myb_account_3_n
global myb_account_4_n
global myb_account_5_n
global myb_account_6_n
global myb_account1pw
global myb_account2pw
global myb_account3pw
global myb_account4pw
global myb_account5pw
global myb_account6pw
global myb_last_price
global myb_accounts_range
global myb_tokenName
global myb_last_ethereum_price
global myb_unlockTime
global myb_balance
global myb_balanceOf
global myb_unlock
global myb_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
myb_token_d = 1e8
_e_d = 1e18
myb_accounts_range = '[0, 6]'
myb_unlock = web3.personal.unlockAccount
myb_last_ethereum_price = 370.00
myb_last_price = 3.06
myb_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
myb_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
myb_tokenName = 'MyBit Token'
myb_unlockTime = hex(10000) # Must be hex()
myb_account_0_a = myb_accounts[0]
myb_account_1_a = myb_accounts[1]
myb_account_2_a = myb_accounts[2]
myb_account_3_a = myb_accounts[3]
myb_account_4_a = myb_accounts[4]
myb_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
myb_account_6_a = myb_accounts[6]
# Supply Unlock Passwords For Transactions Below
myb_account_0_pw = 'GuildSkrypt2017!@#'
myb_account_1_pw = ''
myb_account_2_pw = 'GuildSkrypt2017!@#'
myb_account_3_pw = ''
myb_account_4_pw = ''
myb_account_5_pw = ''
myb_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
myb_account_0_n = 'Skotys Bittrex Account'
myb_account_1_n = 'Jeffs Account'
myb_account_2_n = 'Skrypts Bittrex Account'
myb_account_3_n = 'Skotys Personal Account'
myb_account_4_n = 'Unknown'
myb_account_5_n = 'Watched \'Bittrex\' Account.'
myb_account_6_n = 'Watched Account (1)'
# Contract Information Below :
myb_address = '0x94298F1e0Ab2DFaD6eEFfB1426846a3c29D98090'
myb_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"target","type":"address"},{"name":"mintedAmount","type":"uint256"}],"name":"mintToken","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"changeOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"decimalUnits","type":"uint8"},{"name":"tokenSymbol","type":"string"}],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
myb = web3.eth.contract(abi=myb_abi, address=myb_address)
myb_balanceOf = myb.call().balanceOf
# End Contract Information
def myb_update_accounts():
 global myb_account0
 global myb_account1
 global myb_account2
 global myb_account3
 global myb_account4
 global myb_account5
 global myb_account6
 global myb_account0_n
 global myb_account1_n
 global myb_account2_n
 global myb_account3_n
 global myb_account4_n
 global myb_account5_n
 global myb_account6_n
 global myb_account0pw
 global myb_account1pw
 global myb_account2pw
 global myb_account3pw
 global myb_account4pw
 global myb_account5pw
 global myb_account6pw
 myb_account0 = myb_account_0_a
 myb_account1 = myb_account_1_a
 myb_account2 = myb_account_2_a
 myb_account3 = myb_account_3_a
 myb_account4 = myb_account_4_a
 myb_account5 = myb_account_5_a
 myb_account6 = myb_account_6_a
 myb_account0_n = myb_account_0_n
 myb_account1_n = myb_account_1_n
 myb_account2_n = myb_account_2_n
 myb_account3_n = myb_account_3_n
 myb_account4_n = myb_account_4_n
 myb_account5_n = myb_account_5_n
 myb_account6_n = myb_account_6_n
 myb_account0pw = myb_account_0_pw
 myb_account1pw = myb_account_1_pw
 myb_account2pw = myb_account_2_pw
 myb_account3pw = myb_account_3_pw
 myb_account4pw = myb_account_4_pw
 myb_account5pw = myb_account_5_pw
 myb_account6pw = myb_account_6_pw
 print(myb_tokenName+' Accounts Updated.')
def myb_update_balances():
 global myb_call_0
 global myb_call_1
 global myb_call_2
 global myb_call_3
 global myb_call_4
 global myb_call_5
 global myb_call_6
 global myb_w_call_0
 global myb_w_call_1
 global myb_w_call_2
 global myb_w_call_3
 global myb_w_call_4
 global myb_w_call_5
 global myb_w_call_6
 myb_update_accounts()
 print('Updating '+myb_tokenName+' Balances Please Wait...')
 myb_call_0 = myb_balanceOf(myb_account0)
 myb_call_1 = myb_balanceOf(myb_account1)
 myb_call_2 = myb_balanceOf(myb_account2)
 myb_call_3 = myb_balanceOf(myb_account3)
 myb_call_4 = myb_balanceOf(myb_account4)
 myb_call_5 = myb_balanceOf(myb_account5)
 myb_call_6 = myb_balanceOf(myb_account6)
 myb_w_call_0 = myb_balance(myb_account0)
 myb_w_call_1 = myb_balance(myb_account1)
 myb_w_call_2 = myb_balance(myb_account2)
 myb_w_call_3 = myb_balance(myb_account3)
 myb_w_call_4 = myb_balance(myb_account4)
 myb_w_call_5 = myb_balance(myb_account5)
 myb_w_call_6 = myb_balance(myb_account6)
 print(myb_tokenName+' Balances Updated.')
def myb_list_all_accounts():
 myb_update_accounts()
 print(myb_tokenName+' '+myb_account0_n+': '+myb_account0)
 print(myb_tokenName+' '+myb_account1_n+': '+myb_account1)
 print(myb_tokenName+' '+myb_account2_n+': '+myb_account2)
 print(myb_tokenName+' '+myb_account3_n+': '+myb_account3)
 print(myb_tokenName+' '+myb_account4_n+': '+myb_account4)
 print(myb_tokenName+' '+myb_account5_n+': '+myb_account5)
 print(myb_tokenName+' '+myb_account6_n+': '+myb_account6)

def myb_account_balance(accountNumber):
 myb_update_balances()
 myb_ab_account_number = accountNumber
 myb_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if myb_ab_account_number == myb_ab_input[0]:
  print('Calling '+myb_account0_n+' '+myb_tokenName+' Balance: ')
  print(myb_account0_n+': '+myb_tokenName+' Balance: '+str(myb_call_0 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_0 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[1]:
  print('Calling '+myb_account1_n+' '+myb_tokenName+' Balance: ')
  print(myb_account1_n+': '+myb_tokenName+' Balance: '+str(myb_call_1 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_1 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[2]:
  print('Calling '+myb_account2_n+' '+myb_tokenName+' Balance: ')
  print(myb_account2_n+': '+myb_tokenName+' Balance: '+str(myb_call_2 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_2 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[3]:
  print('Calling '+myb_account3_n+' '+myb_tokenName+' Balance: ')
  print(myb_account3_n+': '+myb_tokenName+' Balance: '+str(myb_call_3 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_3 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[4]:
  print('Calling '+myb_account4_n+' '+myb_tokenName+' Balance: ')
  print(myb_account4_n+': '+myb_tokenName+' Balance: '+str(myb_call_4 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_4 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[5]:
  print('Calling '+myb_account5_n+' '+myb_tokenName+' Balance: ')
  print(myb_account5_n+': '+myb_tokenName+' Balance: '+str(myb_call_5 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_5 / myb_token_d * myb_last_price))
 if myb_ab_account_number == myb_ab_input[6]:
  print('Calling '+myb_account6_n+' '+myb_tokenName+' Balance: ')
  print(myb_account6_n+': '+myb_tokenName+' Balance: '+str(myb_call_6 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_6 / myb_token_d * myb_last_price))
 if myb_ab_account_number not in myb_ab_input:
  print('Must Integer Within Range '+myb_accounts_range+'.')

def myb_list_all_account_balances():
 myb_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+myb_tokenName+' Balance: ')
 print(myb_account0_n+': '+myb_tokenName+' Balance: '+str(myb_call_0 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_0 / myb_token_d * myb_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(myb_account0_n+': Ethereum Balance '+str(myb_w_call_0 / _e_d)+' $'+str(myb_w_call_0 / _e_d * myb_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+myb_tokenName+' Balance: ')
 print(myb_account1_n+': '+myb_tokenName+' Balance: '+str(myb_call_1 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_1 / myb_token_d * myb_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(myb_account1_n+': Ethereum Balance '+str(myb_w_call_1 / _e_d)+' $'+str(myb_w_call_1 / _e_d * myb_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+myb_tokenName+' Balance: ')
 print(myb_account2_n+': '+myb_tokenName+' Balance: '+str(myb_call_2 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_2 / myb_token_d * myb_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(myb_account2_n+': Ethereum Balance '+str(myb_w_call_2 / _e_d)+' $'+str(myb_w_call_2 / _e_d * myb_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+myb_tokenName+' Balance: ')
 print(myb_account3_n+': '+myb_tokenName+' Balance: '+str(myb_call_3 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_3 / myb_token_d * myb_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(myb_account3_n+': Ethereum Balance '+str(myb_w_call_3 / _e_d)+' $'+str(myb_w_call_3 / _e_d * myb_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+myb_tokenName+' Balance: ')
 print(myb_account4_n+': '+myb_tokenName+' Balance: '+str(myb_call_4 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_4 / myb_token_d * myb_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(myb_account4_n+': Ethereum Balance '+str(myb_w_call_4 / _e_d)+' $'+str(myb_w_call_4 / _e_d * myb_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+myb_tokenName+' Balance: ')
 print(myb_account5_n+': '+myb_tokenName+' Balance: '+str(myb_call_5 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_5 / myb_token_d * myb_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(myb_account5_n+': Ethereum Balance '+str(myb_w_call_5 / _e_d)+' $'+str(myb_w_call_5 /_e_d * myb_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+myb_tokenName+' Balance: ')
 print(myb_account6_n+': '+myb_tokenName+' Balance: '+str(myb_call_6 / myb_token_d)+' Usd/'+myb_tokenName+' Balance: $'+str(myb_call_6 / myb_token_d * myb_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(myb_account6_n+': Ethereum Balance '+str(myb_w_call_6 / _e_d)+' $'+str(myb_w_call_6 / _e_d * myb_last_ethereum_price))
def myb_unlock_all_accounts():
  myb_unlock_account_0()
  myb_unlock_account_1()
  myb_unlock_account_2()
  myb_unlock_account_3()
  myb_unlock_account_4()
  myb_unlock_account_5()
  myb_unlock_account_6()


def myb_unlock_account_0():
  global myb_account0pw
  global myb_account0
  global myb_account0_n
  myb_update_accounts()
  myb_u_a_0 = myb_w_unlock(myb_account0, myb_account0pw, myb_unlockTime)
  if myb_u_a_0 == False:
    if myb_account0pw == '':
     myb_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account0_n+' Passphrase Denied: '+myb_account0pw_r)
    elif myb_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+myb_account0_n+' Passphrase Denied: '+myb_account0pw)
  if myb_u_a_0 == True:
   print(myb_account0_n+' Unlocked')

def myb_unlock_account_1():
  global myb_account1pw
  global myb_account1
  global myb_account1_n
  myb_update_accounts()
  myb_u_a_1 = myb_unlock(myb_account1, myb_account1pw, myb_unlockTime)
  if myb_u_a_1 == False:
    if myb_account1pw == '':
     myb_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account1_n+' Passphrase Denied: '+myb_account1pw_r)
    elif myb_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+myb_account1_n+' Passphrase Denied: '+myb_account1pw)
  if myb_u_a_1 == True:
   print(myb_account1_n+' Unlocked')

def myb_unlock_account_2():
  global myb_account2pw
  global myb_account2
  global myb_account2_n
  myb_update_accounts()
  myb_u_a_2 = myb_unlock(myb_account2, myb_account2pw, myb_unlockTime)
  if myb_u_a_2 == False:
    if myb_account2pw == '':
     myb_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account2_n+' Passphrase Denied: '+myb_account2pw_r)
    elif myb_account2pw != '':
     print('Unlock Failure With Account '+myb_account2_n+' Passphrase Denied: '+myb_account2pw)
  if myb_u_a_2 == True:
   print(myb_account2_n+' Unlocked')

def myb_unlock_account_3():
  global myb_account3pw
  global myb_account3
  global myb_account3_n
  myb_update_accounts()
  myb_u_a_3 = myb_unlock(myb_account3, myb_account3pw, myb_unlockTime)
  if myb_u_a_3 == False:
    if myb_account3pw == '':
     myb_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account3_n+' Passphrase Denied: '+myb_account3pw_r)
    elif myb_account3pw != '':
     print('Unlock Failure With Account '+myb_account3_n+' Passphrase Denied: '+myb_account3pw)
  if myb_u_a_3 == True:
   print(myb_account3_n+' Unlocked')

def myb_unlock_account_4():
  global myb_account4pw
  global myb_account4
  global myb_account4_n
  myb_update_accounts()
  myb_u_a_4 = myb_unlock(myb_account4, myb_account4pw, myb_unlockTime)
  if myb_u_a_4 == False:
    if myb_account4pw == '':
     myb_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account4_n+' Passphrase Denied: '+myb_account4pw_r)
    elif myb_account4pw != '':
     print('Unlock Failure With Account '+myb_account4_n+' Passphrase Denied: '+myb_account4pw)
  if myb_u_a_4 == True:
   print(myb_account4_n+' Unlocked')

def myb_unlock_account_5():
  global myb_account5pw
  global myb_account5
  global myb_account5_n
  myb_update_accounts()
  myb_u_a_5 = myb_unlock(myb_account5, myb_account5pw, myb_unlockTime)
  if myb_u_a_5 == False:
    if myb_account5pw == '':
     myb_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account5_n+' Passphrase Denied: '+myb_account5pw_r)
    elif myb_account5pw != '':
     print('Unlock Failure With Account '+myb_account5_n+' Passphrase Denied: '+myb_account5pw)
  if myb_u_a_5 == True:
   print(myb_account5_n+' Unlocked')

def myb_unlock_account_6():
  global myb_account6pw
  global myb_account6
  global myb_account6_n
  myb_update_accounts()
  myb_u_a_6 = myb_unlock(myb_account6, myb_account6pw, myb_unlockTime)
  if myb_u_a_6 == False:
    if myb_account6pw == '':
     myb_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myb_account6_n+' Passphrase Denied: '+myb_account6pw_r)
    elif myb_account6pw != '':
     print('Unlock Failure With Account '+myb_account6_n+' Passphrase Denied: '+myb_account6pw)
  if myb_u_a_6 == True:
   print(myb_account6_n+' Unlocked')

def myb_unlock_account(myb_ua_accountNumber):
 myb_update_accounts()
 myb_ua_account_number = myb_ua_accountNumber
 myb_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if myb_ua_account_number == myb_ua_input[0]:
  myb_unlock_account_0()
 if myb_ua_account_number == myb_ua_input[1]:
  myb_unlock_account_1()
 if myb_ua_account_number == myb_ua_input[2]:
  myb_unlock_account_2()
 if myb_ua_account_number == myb_ua_input[3]:
  myb_unlock_account_3()
 if myb_ua_account_number == myb_ua_input[4]:
  myb_unlock_account_4()
 if myb_ua_account_number == myb_ua_input[5]:
  myb_unlock_account_5()
 if myb_ua_account_number == myb_ua_input[6]:
  myb_unlock_account_6()
 if myb_ua_account_number not in myb_ua_input:
  print('Must Integer Within Range '+myb_accounts_range+'.')
 

def myb_approve_between_accounts(fromAccount, toAccount, msgValue):
  myb_update_accounts()
  myb_a_0 = myb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(myb_a_0)

def myb_approve(fromAccountNumber, toAddress, msgValue):
  myb_update_accounts()
  myb_unlock_account(fromAccountNumber)
  myb_a_1 = myb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(myb_a_1)

def myb_transfer_between_accounts(fromAccount, toAccount, msgValue):
  myb_update_accounts()
  myb_unlock_account(fromAccount)
  myb_t_0 = myb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(myb_t_0)

def myb_transfer(fromAccountNumber, toAddress, msgValue):
  myb_update_accounts()
  myb_unlock_account(fromAccountNumber)
  myb_t_1 = myb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(myb_t_1)

def myb_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  myb_update_accounts()
  myb_unlock_account(callAccount)
  myb_tf_0 = myb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(myb_tf_0)

def myb_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  myb_update_accounts()
  myb_unlock_account(callAccount)
  myb_tf_1 = myb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(myb_tf_1)
  


def myb_help():
  print('Following Functions For '+myb_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * myb_unlock => web3.personal.unlockAccount
/ * myb_accounts => web3.personal.listAccounts
/ * myb_balance = web3.eth.getBalance
** myb => web3.eth.contract(abi=myb_abi, address=myb_address)
** / * myb_balanceOf => myb.call().balanceOf

~ Function Listing Below:
~ myb_update_accounts()
~ myb_update_balances() \n\r -- => myb_update_accounts()
~ myb_list_all_accounts() \n\r -- => myb_update_accounts()
~ myb_account_balance(accountNumber) \n\r -- => myb_update_balances() 
~ myb_list_all_account_balances() \n\r -- => myb_update_balances()
~ myb_unlock_all_accounts() \n\r -- => myb_unlock_account_0() \n\r -- => myb_unlock_account_1() \n\r -- => myb_unlock_account_2() \n\r -- => myb_unlock_account_3() \n\r -- => myb_unlock_account_4() \n\r -- => myb_unlock_account_5() \n\r -- => myb_unlock_account_6() 
~ myb_unlock_account_0() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account0, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_1() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account1, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_2() \n\r -- => myb_update_accounts() \n\r --/ *myb_w_unlock(myb_account2, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_3() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account3, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_4() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account4, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_5() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account5, myb_account0pw, myb_unlockTime)
~ myb_unlock_account_6() \n\r -- => myb_update_accounts() \n\r -- / *myb_w_unlock(myb_account6, myb_account0pw, myb_unlockTime)
~ myb_unlock_account(myb_ua_accountNumber) \n\r -- => myb_update_accounts() \n\r -- // myb_unlock_account_0() \n\r -- // myb_unlock_account_1() \n\r -- // myb_unlock_account_2() \n\r -- // myb_unlock_account_3() \n\r -- // myb_unlock_account_4() \n\r -- // myb_unlock_account_5() \n\r -- // myb_unlock_account_6()
~ myb_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(fromAccount) \n\r -- / ** myb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ myb_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(fromAccountNumber) \n\r -- / ** myb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ myb_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(fromAccount) \n\r -- / ** myb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ myb_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(fromAccountNumber) \n\r -- / ** myb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ myb_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(callAccount) \n\r / ** myb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ myb_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => myb_update_accounts() \n\r -- => myb_unlock_account(callAccount) \n\r -- / ** myb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ myb_help() <-- You Are Here. ''')