#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global pay_account_0_a
global pay_account_1_a
global pay_account_2_a
global pay_account_3_a
global pay_account_4_a
global pay_account_5_a
global pay_account_6_a
global pay_address
global pay_abi
global pay
global pay_call_0
global pay_call_1
global pay_call_2
global pay_call_3
global pay_call_4
global pay_call_5
global pay_call_6
global pay_call_ab
global pay_accounts
global pay_account_0_pw
global pay_account_1_pw
global pay_account_2_pw
global pay_account_3_pw
global pay_account_4_pw
global pay_account_5_pw
global pay_account_6_pw
global pay_account_0_n
global pay_account_1_n
global pay_account_2_n
global pay_account_3_n
global pay_account_4_n
global pay_account_5_n
global pay_account_6_n
global pay_account1pw
global pay_account2pw
global pay_account3pw
global pay_account4pw
global pay_account5pw
global pay_account6pw
global pay_last_price
global pay_accounts_range
global pay_tokenName
global pay_last_ethereum_price
global pay_unlockTime
global pay_balance
global pay_balanceOf
global pay_unlock
global pay_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
pay_token_d = 1e18
_e_d = 1e18
pay_accounts_range = '[0, 6]'
pay_unlock = web3.personal.unlockAccount
pay_last_ethereum_price = 370.00
pay_last_price = 4.18
pay_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
pay_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
pay_tokenName = 'TenXpay Token'
pay_unlockTime = hex(10000) # Must be hex()
pay_account_0_a = pay_accounts[0]
pay_account_1_a = pay_accounts[1]
pay_account_2_a = pay_accounts[2]
pay_account_3_a = pay_accounts[3]
pay_account_4_a = pay_accounts[4]
pay_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
pay_account_6_a = pay_accounts[6]
# Supply Unlock Passwords For Transactions Below
pay_account_0_pw = 'GuildSkrypt2017!@#'
pay_account_1_pw = ''
pay_account_2_pw = 'GuildSkrypt2017!@#'
pay_account_3_pw = ''
pay_account_4_pw = ''
pay_account_5_pw = ''
pay_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
pay_account_0_n = 'Skotys Bittrex Account'
pay_account_1_n = 'Jeffs Account'
pay_account_2_n = 'Skrypts Bittrex Account'
pay_account_3_n = 'Skotys Personal Account'
pay_account_4_n = 'Unknown'
pay_account_5_n = 'Watched \'Bittrex\' Account.'
pay_account_6_n = 'Watched Account (1)'
# Contract Information Below :
pay_address = '0xB97048628DB6B661D4C2aA833e95Dbe1A905B280'
pay_abi = [{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"startTrading","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tradingStarted","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
pay = web3.eth.contract(abi=pay_abi, address=pay_address)
pay_balanceOf = pay.call().balanceOf
# End Contract Information
def pay_update_accounts():
 global pay_account0
 global pay_account1
 global pay_account2
 global pay_account3
 global pay_account4
 global pay_account5
 global pay_account6
 global pay_account0_n
 global pay_account1_n
 global pay_account2_n
 global pay_account3_n
 global pay_account4_n
 global pay_account5_n
 global pay_account6_n
 global pay_account0pw
 global pay_account1pw
 global pay_account2pw
 global pay_account3pw
 global pay_account4pw
 global pay_account5pw
 global pay_account6pw
 pay_account0 = pay_account_0_a
 pay_account1 = pay_account_1_a
 pay_account2 = pay_account_2_a
 pay_account3 = pay_account_3_a
 pay_account4 = pay_account_4_a
 pay_account5 = pay_account_5_a
 pay_account6 = pay_account_6_a
 pay_account0_n = pay_account_0_n
 pay_account1_n = pay_account_1_n
 pay_account2_n = pay_account_2_n
 pay_account3_n = pay_account_3_n
 pay_account4_n = pay_account_4_n
 pay_account5_n = pay_account_5_n
 pay_account6_n = pay_account_6_n
 pay_account0pw = pay_account_0_pw
 pay_account1pw = pay_account_1_pw
 pay_account2pw = pay_account_2_pw
 pay_account3pw = pay_account_3_pw
 pay_account4pw = pay_account_4_pw
 pay_account5pw = pay_account_5_pw
 pay_account6pw = pay_account_6_pw
 print(pay_tokenName+' Accounts Updated.')
def pay_update_balances():
 global pay_call_0
 global pay_call_1
 global pay_call_2
 global pay_call_3
 global pay_call_4
 global pay_call_5
 global pay_call_6
 global pay_w_call_0
 global pay_w_call_1
 global pay_w_call_2
 global pay_w_call_3
 global pay_w_call_4
 global pay_w_call_5
 global pay_w_call_6
 pay_update_accounts()
 print('Updating '+pay_tokenName+' Balances Please Wait...')
 pay_call_0 = pay_balanceOf(pay_account0)
 pay_call_1 = pay_balanceOf(pay_account1)
 pay_call_2 = pay_balanceOf(pay_account2)
 pay_call_3 = pay_balanceOf(pay_account3)
 pay_call_4 = pay_balanceOf(pay_account4)
 pay_call_5 = pay_balanceOf(pay_account5)
 pay_call_6 = pay_balanceOf(pay_account6)
 pay_w_call_0 = pay_balance(pay_account0)
 pay_w_call_1 = pay_balance(pay_account1)
 pay_w_call_2 = pay_balance(pay_account2)
 pay_w_call_3 = pay_balance(pay_account3)
 pay_w_call_4 = pay_balance(pay_account4)
 pay_w_call_5 = pay_balance(pay_account5)
 pay_w_call_6 = pay_balance(pay_account6)
 print(pay_tokenName+' Balances Updated.')
def pay_list_all_accounts():
 pay_update_accounts()
 print(pay_tokenName+' '+pay_account0_n+': '+pay_account0)
 print(pay_tokenName+' '+pay_account1_n+': '+pay_account1)
 print(pay_tokenName+' '+pay_account2_n+': '+pay_account2)
 print(pay_tokenName+' '+pay_account3_n+': '+pay_account3)
 print(pay_tokenName+' '+pay_account4_n+': '+pay_account4)
 print(pay_tokenName+' '+pay_account5_n+': '+pay_account5)
 print(pay_tokenName+' '+pay_account6_n+': '+pay_account6)

def pay_account_balance(accountNumber):
 pay_update_balances()
 pay_ab_account_number = accountNumber
 pay_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if pay_ab_account_number == pay_ab_input[0]:
  print('Calling '+pay_account0_n+' '+pay_tokenName+' Balance: ')
  print(pay_account0_n+': '+pay_tokenName+' Balance: '+str(pay_call_0 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_0 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[1]:
  print('Calling '+pay_account1_n+' '+pay_tokenName+' Balance: ')
  print(pay_account1_n+': '+pay_tokenName+' Balance: '+str(pay_call_1 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_1 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[2]:
  print('Calling '+pay_account2_n+' '+pay_tokenName+' Balance: ')
  print(pay_account2_n+': '+pay_tokenName+' Balance: '+str(pay_call_2 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_2 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[3]:
  print('Calling '+pay_account3_n+' '+pay_tokenName+' Balance: ')
  print(pay_account3_n+': '+pay_tokenName+' Balance: '+str(pay_call_3 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_3 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[4]:
  print('Calling '+pay_account4_n+' '+pay_tokenName+' Balance: ')
  print(pay_account4_n+': '+pay_tokenName+' Balance: '+str(pay_call_4 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_4 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[5]:
  print('Calling '+pay_account5_n+' '+pay_tokenName+' Balance: ')
  print(pay_account5_n+': '+pay_tokenName+' Balance: '+str(pay_call_5 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_5 / pay_token_d * pay_last_price))
 if pay_ab_account_number == pay_ab_input[6]:
  print('Calling '+pay_account6_n+' '+pay_tokenName+' Balance: ')
  print(pay_account6_n+': '+pay_tokenName+' Balance: '+str(pay_call_6 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_6 / pay_token_d * pay_last_price))
 if pay_ab_account_number not in pay_ab_input:
  print('Must Integer Within Range '+pay_accounts_range+'.')

def pay_list_all_account_balances():
 pay_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+pay_tokenName+' Balance: ')
 print(pay_account0_n+': '+pay_tokenName+' Balance: '+str(pay_call_0 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_0 / pay_token_d * pay_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(pay_account0_n+': Ethereum Balance '+str(pay_w_call_0 / _e_d)+' $'+str(pay_w_call_0 / _e_d * pay_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+pay_tokenName+' Balance: ')
 print(pay_account1_n+': '+pay_tokenName+' Balance: '+str(pay_call_1 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_1 / pay_token_d * pay_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(pay_account1_n+': Ethereum Balance '+str(pay_w_call_1 / _e_d)+' $'+str(pay_w_call_1 / _e_d * pay_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+pay_tokenName+' Balance: ')
 print(pay_account2_n+': '+pay_tokenName+' Balance: '+str(pay_call_2 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_2 / pay_token_d * pay_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(pay_account2_n+': Ethereum Balance '+str(pay_w_call_2 / _e_d)+' $'+str(pay_w_call_2 / _e_d * pay_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+pay_tokenName+' Balance: ')
 print(pay_account3_n+': '+pay_tokenName+' Balance: '+str(pay_call_3 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_3 / pay_token_d * pay_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(pay_account3_n+': Ethereum Balance '+str(pay_w_call_3 / _e_d)+' $'+str(pay_w_call_3 / _e_d * pay_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+pay_tokenName+' Balance: ')
 print(pay_account4_n+': '+pay_tokenName+' Balance: '+str(pay_call_4 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_4 / pay_token_d * pay_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(pay_account4_n+': Ethereum Balance '+str(pay_w_call_4 / _e_d)+' $'+str(pay_w_call_4 / _e_d * pay_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+pay_tokenName+' Balance: ')
 print(pay_account5_n+': '+pay_tokenName+' Balance: '+str(pay_call_5 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_5 / pay_token_d * pay_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(pay_account5_n+': Ethereum Balance '+str(pay_w_call_5 / _e_d)+' $'+str(pay_w_call_5 /_e_d * pay_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+pay_tokenName+' Balance: ')
 print(pay_account6_n+': '+pay_tokenName+' Balance: '+str(pay_call_6 / pay_token_d)+' Usd/'+pay_tokenName+' Balance: $'+str(pay_call_6 / pay_token_d * pay_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(pay_account6_n+': Ethereum Balance '+str(pay_w_call_6 / _e_d)+' $'+str(pay_w_call_6 / _e_d * pay_last_ethereum_price))
def pay_unlock_all_accounts():
  pay_unlock_account_0()
  pay_unlock_account_1()
  pay_unlock_account_2()
  pay_unlock_account_3()
  pay_unlock_account_4()
  pay_unlock_account_5()
  pay_unlock_account_6()


def pay_unlock_account_0():
  global pay_account0pw
  global pay_account0
  global pay_account0_n
  pay_update_accounts()
  pay_u_a_0 = pay_w_unlock(pay_account0, pay_account0pw, pay_unlockTime)
  if pay_u_a_0 == False:
    if pay_account0pw == '':
     pay_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account0_n+' Passphrase Denied: '+pay_account0pw_r)
    elif pay_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+pay_account0_n+' Passphrase Denied: '+pay_account0pw)
  if pay_u_a_0 == True:
   print(pay_account0_n+' Unlocked')

def pay_unlock_account_1():
  global pay_account1pw
  global pay_account1
  global pay_account1_n
  pay_update_accounts()
  pay_u_a_1 = pay_unlock(pay_account1, pay_account1pw, pay_unlockTime)
  if pay_u_a_1 == False:
    if pay_account1pw == '':
     pay_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account1_n+' Passphrase Denied: '+pay_account1pw_r)
    elif pay_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+pay_account1_n+' Passphrase Denied: '+pay_account1pw)
  if pay_u_a_1 == True:
   print(pay_account1_n+' Unlocked')

def pay_unlock_account_2():
  global pay_account2pw
  global pay_account2
  global pay_account2_n
  pay_update_accounts()
  pay_u_a_2 = pay_unlock(pay_account2, pay_account2pw, pay_unlockTime)
  if pay_u_a_2 == False:
    if pay_account2pw == '':
     pay_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account2_n+' Passphrase Denied: '+pay_account2pw_r)
    elif pay_account2pw != '':
     print('Unlock Failure With Account '+pay_account2_n+' Passphrase Denied: '+pay_account2pw)
  if pay_u_a_2 == True:
   print(pay_account2_n+' Unlocked')

def pay_unlock_account_3():
  global pay_account3pw
  global pay_account3
  global pay_account3_n
  pay_update_accounts()
  pay_u_a_3 = pay_unlock(pay_account3, pay_account3pw, pay_unlockTime)
  if pay_u_a_3 == False:
    if pay_account3pw == '':
     pay_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account3_n+' Passphrase Denied: '+pay_account3pw_r)
    elif pay_account3pw != '':
     print('Unlock Failure With Account '+pay_account3_n+' Passphrase Denied: '+pay_account3pw)
  if pay_u_a_3 == True:
   print(pay_account3_n+' Unlocked')

def pay_unlock_account_4():
  global pay_account4pw
  global pay_account4
  global pay_account4_n
  pay_update_accounts()
  pay_u_a_4 = pay_unlock(pay_account4, pay_account4pw, pay_unlockTime)
  if pay_u_a_4 == False:
    if pay_account4pw == '':
     pay_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account4_n+' Passphrase Denied: '+pay_account4pw_r)
    elif pay_account4pw != '':
     print('Unlock Failure With Account '+pay_account4_n+' Passphrase Denied: '+pay_account4pw)
  if pay_u_a_4 == True:
   print(pay_account4_n+' Unlocked')

def pay_unlock_account_5():
  global pay_account5pw
  global pay_account5
  global pay_account5_n
  pay_update_accounts()
  pay_u_a_5 = pay_unlock(pay_account5, pay_account5pw, pay_unlockTime)
  if pay_u_a_5 == False:
    if pay_account5pw == '':
     pay_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account5_n+' Passphrase Denied: '+pay_account5pw_r)
    elif pay_account5pw != '':
     print('Unlock Failure With Account '+pay_account5_n+' Passphrase Denied: '+pay_account5pw)
  if pay_u_a_5 == True:
   print(pay_account5_n+' Unlocked')

def pay_unlock_account_6():
  global pay_account6pw
  global pay_account6
  global pay_account6_n
  pay_update_accounts()
  pay_u_a_6 = pay_unlock(pay_account6, pay_account6pw, pay_unlockTime)
  if pay_u_a_6 == False:
    if pay_account6pw == '':
     pay_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+pay_account6_n+' Passphrase Denied: '+pay_account6pw_r)
    elif pay_account6pw != '':
     print('Unlock Failure With Account '+pay_account6_n+' Passphrase Denied: '+pay_account6pw)
  if pay_u_a_6 == True:
   print(pay_account6_n+' Unlocked')

def pay_unlock_account(pay_ua_accountNumber):
 pay_update_accounts()
 pay_ua_account_number = pay_ua_accountNumber
 pay_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if pay_ua_account_number == pay_ua_input[0]:
  pay_unlock_account_0()
 if pay_ua_account_number == pay_ua_input[1]:
  pay_unlock_account_1()
 if pay_ua_account_number == pay_ua_input[2]:
  pay_unlock_account_2()
 if pay_ua_account_number == pay_ua_input[3]:
  pay_unlock_account_3()
 if pay_ua_account_number == pay_ua_input[4]:
  pay_unlock_account_4()
 if pay_ua_account_number == pay_ua_input[5]:
  pay_unlock_account_5()
 if pay_ua_account_number == pay_ua_input[6]:
  pay_unlock_account_6()
 if pay_ua_account_number not in pay_ua_input:
  print('Must Integer Within Range '+pay_accounts_range+'.')
 

def pay_approve_between_accounts(fromAccount, toAccount, msgValue):
  pay_update_accounts()
  pay_a_0 = pay.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(pay_a_0)

def pay_approve(fromAccountNumber, toAddress, msgValue):
  pay_update_accounts()
  pay_unlock_account(fromAccountNumber)
  pay_a_1 = pay.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(pay_a_1)

def pay_transfer_between_accounts(fromAccount, toAccount, msgValue):
  pay_update_accounts()
  pay_unlock_account(fromAccount)
  pay_t_0 = pay.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(pay_t_0)

def pay_transfer(fromAccountNumber, toAddress, msgValue):
  pay_update_accounts()
  pay_unlock_account(fromAccountNumber)
  pay_t_1 = pay.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(pay_t_1)

def pay_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  pay_update_accounts()
  pay_unlock_account(callAccount)
  pay_tf_0 = pay.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(pay_tf_0)

def pay_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  pay_update_accounts()
  pay_unlock_account(callAccount)
  pay_tf_1 = pay.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(pay_tf_1)
  


def pay_help():
  print('Following Functions For '+pay_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * pay_unlock => web3.personal.unlockAccount
/ * pay_accounts => web3.personal.listAccounts
/ * pay_balance = web3.eth.getBalance
** pay => web3.eth.contract(abi=pay_abi, address=pay_address)
** / * pay_balanceOf => pay.call().balanceOf

~ Function Listing Below:
~ pay_update_accounts()
~ pay_update_balances() \n\r -- => pay_update_accounts()
~ pay_list_all_accounts() \n\r -- => pay_update_accounts()
~ pay_account_balance(accountNumber) \n\r -- => pay_update_balances() 
~ pay_list_all_account_balances() \n\r -- => pay_update_balances()
~ pay_unlock_all_accounts() \n\r -- => pay_unlock_account_0() \n\r -- => pay_unlock_account_1() \n\r -- => pay_unlock_account_2() \n\r -- => pay_unlock_account_3() \n\r -- => pay_unlock_account_4() \n\r -- => pay_unlock_account_5() \n\r -- => pay_unlock_account_6() 
~ pay_unlock_account_0() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account0, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_1() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account1, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_2() \n\r -- => pay_update_accounts() \n\r --/ *pay_w_unlock(pay_account2, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_3() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account3, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_4() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account4, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_5() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account5, pay_account0pw, pay_unlockTime)
~ pay_unlock_account_6() \n\r -- => pay_update_accounts() \n\r -- / *pay_w_unlock(pay_account6, pay_account0pw, pay_unlockTime)
~ pay_unlock_account(pay_ua_accountNumber) \n\r -- => pay_update_accounts() \n\r -- // pay_unlock_account_0() \n\r -- // pay_unlock_account_1() \n\r -- // pay_unlock_account_2() \n\r -- // pay_unlock_account_3() \n\r -- // pay_unlock_account_4() \n\r -- // pay_unlock_account_5() \n\r -- // pay_unlock_account_6()
~ pay_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(fromAccount) \n\r -- / ** pay.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ pay_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(fromAccountNumber) \n\r -- / ** pay.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ pay_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(fromAccount) \n\r -- / ** pay.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ pay_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(fromAccountNumber) \n\r -- / ** pay.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ pay_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(callAccount) \n\r / ** pay.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ pay_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => pay_update_accounts() \n\r -- => pay_unlock_account(callAccount) \n\r -- / ** pay.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ pay_help() <-- You Are Here. ''')