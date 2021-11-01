#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global skin_account_0_a
global skin_account_1_a
global skin_account_2_a
global skin_account_3_a
global skin_account_4_a
global skin_account_5_a
global skin_account_6_a
global skin_address
global skin_abi
global skin
global skin_call_0
global skin_call_1
global skin_call_2
global skin_call_3
global skin_call_4
global skin_call_5
global skin_call_6
global skin_call_ab
global skin_accounts
global skin_account_0_pw
global skin_account_1_pw
global skin_account_2_pw
global skin_account_3_pw
global skin_account_4_pw
global skin_account_5_pw
global skin_account_6_pw
global skin_account_0_n
global skin_account_1_n
global skin_account_2_n
global skin_account_3_n
global skin_account_4_n
global skin_account_5_n
global skin_account_6_n
global skin_account1pw
global skin_account2pw
global skin_account3pw
global skin_account4pw
global skin_account5pw
global skin_account6pw
global skin_last_price
global skin_accounts_range
global skin_tokenName
global skin_last_ethereum_price
global skin_unlockTime
global skin_balance
global skin_balanceOf
global skin_unlock
global skin_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
skin_token_d = 1e6
_e_d = 1e18
skin_accounts_range = '[0, 6]'
skin_unlock = web3.personal.unlockAccount
skin_last_ethereum_price = 370.00
skin_last_price = 0.02
skin_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
skin_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
skin_tokenName = 'SkinCoin Token'
skin_unlockTime = hex(10000) # Must be hex()
skin_account_0_a = skin_accounts[0]
skin_account_1_a = skin_accounts[1]
skin_account_2_a = skin_accounts[2]
skin_account_3_a = skin_accounts[3]
skin_account_4_a = skin_accounts[4]
skin_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
skin_account_6_a = skin_accounts[6]
# Supply Unlock Passwords For Transactions Below
skin_account_0_pw = 'GuildSkrypt2017!@#'
skin_account_1_pw = ''
skin_account_2_pw = 'GuildSkrypt2017!@#'
skin_account_3_pw = ''
skin_account_4_pw = ''
skin_account_5_pw = ''
skin_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
skin_account_0_n = 'Skotys Bittrex Account'
skin_account_1_n = 'Jeffs Account'
skin_account_2_n = 'Skrypts Bittrex Account'
skin_account_3_n = 'Skotys Personal Account'
skin_account_4_n = 'Unknown'
skin_account_5_n = 'Watched \'Bittrex\' Account.'
skin_account_6_n = 'Watched Account (1)'
# Contract Information Below :
skin_address = '0x2bDC0D42996017fCe214b21607a515DA41A9E0C5'
skin_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
skin = web3.eth.contract(abi=skin_abi, address=skin_address)
skin_balanceOf = skin.call().balanceOf
# End Contract Information
def skin_update_accounts():
 global skin_account0
 global skin_account1
 global skin_account2
 global skin_account3
 global skin_account4
 global skin_account5
 global skin_account6
 global skin_account0_n
 global skin_account1_n
 global skin_account2_n
 global skin_account3_n
 global skin_account4_n
 global skin_account5_n
 global skin_account6_n
 global skin_account0pw
 global skin_account1pw
 global skin_account2pw
 global skin_account3pw
 global skin_account4pw
 global skin_account5pw
 global skin_account6pw
 skin_account0 = skin_account_0_a
 skin_account1 = skin_account_1_a
 skin_account2 = skin_account_2_a
 skin_account3 = skin_account_3_a
 skin_account4 = skin_account_4_a
 skin_account5 = skin_account_5_a
 skin_account6 = skin_account_6_a
 skin_account0_n = skin_account_0_n
 skin_account1_n = skin_account_1_n
 skin_account2_n = skin_account_2_n
 skin_account3_n = skin_account_3_n
 skin_account4_n = skin_account_4_n
 skin_account5_n = skin_account_5_n
 skin_account6_n = skin_account_6_n
 skin_account0pw = skin_account_0_pw
 skin_account1pw = skin_account_1_pw
 skin_account2pw = skin_account_2_pw
 skin_account3pw = skin_account_3_pw
 skin_account4pw = skin_account_4_pw
 skin_account5pw = skin_account_5_pw
 skin_account6pw = skin_account_6_pw
 print(skin_tokenName+' Accounts Updated.')
def skin_update_balances():
 global skin_call_0
 global skin_call_1
 global skin_call_2
 global skin_call_3
 global skin_call_4
 global skin_call_5
 global skin_call_6
 global skin_w_call_0
 global skin_w_call_1
 global skin_w_call_2
 global skin_w_call_3
 global skin_w_call_4
 global skin_w_call_5
 global skin_w_call_6
 skin_update_accounts()
 print('Updating '+skin_tokenName+' Balances Please Wait...')
 skin_call_0 = skin_balanceOf(skin_account0)
 skin_call_1 = skin_balanceOf(skin_account1)
 skin_call_2 = skin_balanceOf(skin_account2)
 skin_call_3 = skin_balanceOf(skin_account3)
 skin_call_4 = skin_balanceOf(skin_account4)
 skin_call_5 = skin_balanceOf(skin_account5)
 skin_call_6 = skin_balanceOf(skin_account6)
 skin_w_call_0 = skin_balance(skin_account0)
 skin_w_call_1 = skin_balance(skin_account1)
 skin_w_call_2 = skin_balance(skin_account2)
 skin_w_call_3 = skin_balance(skin_account3)
 skin_w_call_4 = skin_balance(skin_account4)
 skin_w_call_5 = skin_balance(skin_account5)
 skin_w_call_6 = skin_balance(skin_account6)
 print(skin_tokenName+' Balances Updated.')
def skin_list_all_accounts():
 skin_update_accounts()
 print(skin_tokenName+' '+skin_account0_n+': '+skin_account0)
 print(skin_tokenName+' '+skin_account1_n+': '+skin_account1)
 print(skin_tokenName+' '+skin_account2_n+': '+skin_account2)
 print(skin_tokenName+' '+skin_account3_n+': '+skin_account3)
 print(skin_tokenName+' '+skin_account4_n+': '+skin_account4)
 print(skin_tokenName+' '+skin_account5_n+': '+skin_account5)
 print(skin_tokenName+' '+skin_account6_n+': '+skin_account6)

def skin_account_balance(accountNumber):
 skin_update_balances()
 skin_ab_account_number = accountNumber
 skin_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if skin_ab_account_number == skin_ab_input[0]:
  print('Calling '+skin_account0_n+' '+skin_tokenName+' Balance: ')
  print(skin_account0_n+': '+skin_tokenName+' Balance: '+str(skin_call_0 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_0 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[1]:
  print('Calling '+skin_account1_n+' '+skin_tokenName+' Balance: ')
  print(skin_account1_n+': '+skin_tokenName+' Balance: '+str(skin_call_1 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_1 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[2]:
  print('Calling '+skin_account2_n+' '+skin_tokenName+' Balance: ')
  print(skin_account2_n+': '+skin_tokenName+' Balance: '+str(skin_call_2 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_2 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[3]:
  print('Calling '+skin_account3_n+' '+skin_tokenName+' Balance: ')
  print(skin_account3_n+': '+skin_tokenName+' Balance: '+str(skin_call_3 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_3 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[4]:
  print('Calling '+skin_account4_n+' '+skin_tokenName+' Balance: ')
  print(skin_account4_n+': '+skin_tokenName+' Balance: '+str(skin_call_4 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_4 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[5]:
  print('Calling '+skin_account5_n+' '+skin_tokenName+' Balance: ')
  print(skin_account5_n+': '+skin_tokenName+' Balance: '+str(skin_call_5 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_5 / skin_token_d * skin_last_price))
 if skin_ab_account_number == skin_ab_input[6]:
  print('Calling '+skin_account6_n+' '+skin_tokenName+' Balance: ')
  print(skin_account6_n+': '+skin_tokenName+' Balance: '+str(skin_call_6 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_6 / skin_token_d * skin_last_price))
 if skin_ab_account_number not in skin_ab_input:
  print('Must Integer Within Range '+skin_accounts_range+'.')

def skin_list_all_account_balances():
 skin_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+skin_tokenName+' Balance: ')
 print(skin_account0_n+': '+skin_tokenName+' Balance: '+str(skin_call_0 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_0 / skin_token_d * skin_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(skin_account0_n+': Ethereum Balance '+str(skin_w_call_0 / _e_d)+' $'+str(skin_w_call_0 / _e_d * skin_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+skin_tokenName+' Balance: ')
 print(skin_account1_n+': '+skin_tokenName+' Balance: '+str(skin_call_1 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_1 / skin_token_d * skin_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(skin_account1_n+': Ethereum Balance '+str(skin_w_call_1 / _e_d)+' $'+str(skin_w_call_1 / _e_d * skin_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+skin_tokenName+' Balance: ')
 print(skin_account2_n+': '+skin_tokenName+' Balance: '+str(skin_call_2 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_2 / skin_token_d * skin_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(skin_account2_n+': Ethereum Balance '+str(skin_w_call_2 / _e_d)+' $'+str(skin_w_call_2 / _e_d * skin_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+skin_tokenName+' Balance: ')
 print(skin_account3_n+': '+skin_tokenName+' Balance: '+str(skin_call_3 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_3 / skin_token_d * skin_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(skin_account3_n+': Ethereum Balance '+str(skin_w_call_3 / _e_d)+' $'+str(skin_w_call_3 / _e_d * skin_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+skin_tokenName+' Balance: ')
 print(skin_account4_n+': '+skin_tokenName+' Balance: '+str(skin_call_4 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_4 / skin_token_d * skin_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(skin_account4_n+': Ethereum Balance '+str(skin_w_call_4 / _e_d)+' $'+str(skin_w_call_4 / _e_d * skin_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+skin_tokenName+' Balance: ')
 print(skin_account5_n+': '+skin_tokenName+' Balance: '+str(skin_call_5 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_5 / skin_token_d * skin_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(skin_account5_n+': Ethereum Balance '+str(skin_w_call_5 / _e_d)+' $'+str(skin_w_call_5 /_e_d * skin_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+skin_tokenName+' Balance: ')
 print(skin_account6_n+': '+skin_tokenName+' Balance: '+str(skin_call_6 / skin_token_d)+' Usd/'+skin_tokenName+' Balance: $'+str(skin_call_6 / skin_token_d * skin_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(skin_account6_n+': Ethereum Balance '+str(skin_w_call_6 / _e_d)+' $'+str(skin_w_call_6 / _e_d * skin_last_ethereum_price))
def skin_unlock_all_accounts():
  skin_unlock_account_0()
  skin_unlock_account_1()
  skin_unlock_account_2()
  skin_unlock_account_3()
  skin_unlock_account_4()
  skin_unlock_account_5()
  skin_unlock_account_6()


def skin_unlock_account_0():
  global skin_account0pw
  global skin_account0
  global skin_account0_n
  skin_update_accounts()
  skin_u_a_0 = skin_w_unlock(skin_account0, skin_account0pw, skin_unlockTime)
  if skin_u_a_0 == False:
    if skin_account0pw == '':
     skin_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account0_n+' Passphrase Denied: '+skin_account0pw_r)
    elif skin_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+skin_account0_n+' Passphrase Denied: '+skin_account0pw)
  if skin_u_a_0 == True:
   print(skin_account0_n+' Unlocked')

def skin_unlock_account_1():
  global skin_account1pw
  global skin_account1
  global skin_account1_n
  skin_update_accounts()
  skin_u_a_1 = skin_unlock(skin_account1, skin_account1pw, skin_unlockTime)
  if skin_u_a_1 == False:
    if skin_account1pw == '':
     skin_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account1_n+' Passphrase Denied: '+skin_account1pw_r)
    elif skin_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+skin_account1_n+' Passphrase Denied: '+skin_account1pw)
  if skin_u_a_1 == True:
   print(skin_account1_n+' Unlocked')

def skin_unlock_account_2():
  global skin_account2pw
  global skin_account2
  global skin_account2_n
  skin_update_accounts()
  skin_u_a_2 = skin_unlock(skin_account2, skin_account2pw, skin_unlockTime)
  if skin_u_a_2 == False:
    if skin_account2pw == '':
     skin_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account2_n+' Passphrase Denied: '+skin_account2pw_r)
    elif skin_account2pw != '':
     print('Unlock Failure With Account '+skin_account2_n+' Passphrase Denied: '+skin_account2pw)
  if skin_u_a_2 == True:
   print(skin_account2_n+' Unlocked')

def skin_unlock_account_3():
  global skin_account3pw
  global skin_account3
  global skin_account3_n
  skin_update_accounts()
  skin_u_a_3 = skin_unlock(skin_account3, skin_account3pw, skin_unlockTime)
  if skin_u_a_3 == False:
    if skin_account3pw == '':
     skin_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account3_n+' Passphrase Denied: '+skin_account3pw_r)
    elif skin_account3pw != '':
     print('Unlock Failure With Account '+skin_account3_n+' Passphrase Denied: '+skin_account3pw)
  if skin_u_a_3 == True:
   print(skin_account3_n+' Unlocked')

def skin_unlock_account_4():
  global skin_account4pw
  global skin_account4
  global skin_account4_n
  skin_update_accounts()
  skin_u_a_4 = skin_unlock(skin_account4, skin_account4pw, skin_unlockTime)
  if skin_u_a_4 == False:
    if skin_account4pw == '':
     skin_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account4_n+' Passphrase Denied: '+skin_account4pw_r)
    elif skin_account4pw != '':
     print('Unlock Failure With Account '+skin_account4_n+' Passphrase Denied: '+skin_account4pw)
  if skin_u_a_4 == True:
   print(skin_account4_n+' Unlocked')

def skin_unlock_account_5():
  global skin_account5pw
  global skin_account5
  global skin_account5_n
  skin_update_accounts()
  skin_u_a_5 = skin_unlock(skin_account5, skin_account5pw, skin_unlockTime)
  if skin_u_a_5 == False:
    if skin_account5pw == '':
     skin_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account5_n+' Passphrase Denied: '+skin_account5pw_r)
    elif skin_account5pw != '':
     print('Unlock Failure With Account '+skin_account5_n+' Passphrase Denied: '+skin_account5pw)
  if skin_u_a_5 == True:
   print(skin_account5_n+' Unlocked')

def skin_unlock_account_6():
  global skin_account6pw
  global skin_account6
  global skin_account6_n
  skin_update_accounts()
  skin_u_a_6 = skin_unlock(skin_account6, skin_account6pw, skin_unlockTime)
  if skin_u_a_6 == False:
    if skin_account6pw == '':
     skin_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+skin_account6_n+' Passphrase Denied: '+skin_account6pw_r)
    elif skin_account6pw != '':
     print('Unlock Failure With Account '+skin_account6_n+' Passphrase Denied: '+skin_account6pw)
  if skin_u_a_6 == True:
   print(skin_account6_n+' Unlocked')

def skin_unlock_account(skin_ua_accountNumber):
 skin_update_accounts()
 skin_ua_account_number = skin_ua_accountNumber
 skin_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if skin_ua_account_number == skin_ua_input[0]:
  skin_unlock_account_0()
 if skin_ua_account_number == skin_ua_input[1]:
  skin_unlock_account_1()
 if skin_ua_account_number == skin_ua_input[2]:
  skin_unlock_account_2()
 if skin_ua_account_number == skin_ua_input[3]:
  skin_unlock_account_3()
 if skin_ua_account_number == skin_ua_input[4]:
  skin_unlock_account_4()
 if skin_ua_account_number == skin_ua_input[5]:
  skin_unlock_account_5()
 if skin_ua_account_number == skin_ua_input[6]:
  skin_unlock_account_6()
 if skin_ua_account_number not in skin_ua_input:
  print('Must Integer Within Range '+skin_accounts_range+'.')
 

def skin_approve_between_accounts(fromAccount, toAccount, msgValue):
  skin_update_accounts()
  skin_a_0 = skin.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(skin_a_0)

def skin_approve(fromAccountNumber, toAddress, msgValue):
  skin_update_accounts()
  skin_unlock_account(fromAccountNumber)
  skin_a_1 = skin.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(skin_a_1)

def skin_transfer_between_accounts(fromAccount, toAccount, msgValue):
  skin_update_accounts()
  skin_unlock_account(fromAccount)
  skin_t_0 = skin.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(skin_t_0)

def skin_transfer(fromAccountNumber, toAddress, msgValue):
  skin_update_accounts()
  skin_unlock_account(fromAccountNumber)
  skin_t_1 = skin.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(skin_t_1)

def skin_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  skin_update_accounts()
  skin_unlock_account(callAccount)
  skin_tf_0 = skin.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(skin_tf_0)

def skin_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  skin_update_accounts()
  skin_unlock_account(callAccount)
  skin_tf_1 = skin.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(skin_tf_1)
  


def skin_help():
  print('Following Functions For '+skin_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * skin_unlock => web3.personal.unlockAccount
/ * skin_accounts => web3.personal.listAccounts
/ * skin_balance = web3.eth.getBalance
** skin => web3.eth.contract(abi=skin_abi, address=skin_address)
** / * skin_balanceOf => skin.call().balanceOf

~ Function Listing Below:
~ skin_update_accounts()
~ skin_update_balances() \n\r -- => skin_update_accounts()
~ skin_list_all_accounts() \n\r -- => skin_update_accounts()
~ skin_account_balance(accountNumber) \n\r -- => skin_update_balances() 
~ skin_list_all_account_balances() \n\r -- => skin_update_balances()
~ skin_unlock_all_accounts() \n\r -- => skin_unlock_account_0() \n\r -- => skin_unlock_account_1() \n\r -- => skin_unlock_account_2() \n\r -- => skin_unlock_account_3() \n\r -- => skin_unlock_account_4() \n\r -- => skin_unlock_account_5() \n\r -- => skin_unlock_account_6() 
~ skin_unlock_account_0() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account0, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_1() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account1, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_2() \n\r -- => skin_update_accounts() \n\r --/ *skin_w_unlock(skin_account2, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_3() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account3, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_4() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account4, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_5() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account5, skin_account0pw, skin_unlockTime)
~ skin_unlock_account_6() \n\r -- => skin_update_accounts() \n\r -- / *skin_w_unlock(skin_account6, skin_account0pw, skin_unlockTime)
~ skin_unlock_account(skin_ua_accountNumber) \n\r -- => skin_update_accounts() \n\r -- // skin_unlock_account_0() \n\r -- // skin_unlock_account_1() \n\r -- // skin_unlock_account_2() \n\r -- // skin_unlock_account_3() \n\r -- // skin_unlock_account_4() \n\r -- // skin_unlock_account_5() \n\r -- // skin_unlock_account_6()
~ skin_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(fromAccount) \n\r -- / ** skin.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ skin_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(fromAccountNumber) \n\r -- / ** skin.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ skin_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(fromAccount) \n\r -- / ** skin.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ skin_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(fromAccountNumber) \n\r -- / ** skin.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ skin_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(callAccount) \n\r / ** skin.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ skin_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => skin_update_accounts() \n\r -- => skin_unlock_account(callAccount) \n\r -- / ** skin.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ skin_help() <-- You Are Here. ''')