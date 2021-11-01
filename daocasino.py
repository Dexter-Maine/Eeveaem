#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global bet_account_0_a
global bet_account_1_a
global bet_account_2_a
global bet_account_3_a
global bet_account_4_a
global bet_account_5_a
global bet_account_6_a
global bet_address
global bet_abi
global bet
global bet_call_0
global bet_call_1
global bet_call_2
global bet_call_3
global bet_call_4
global bet_call_5
global bet_call_6
global bet_call_ab
global bet_accounts
global bet_account_0_pw
global bet_account_1_pw
global bet_account_2_pw
global bet_account_3_pw
global bet_account_4_pw
global bet_account_5_pw
global bet_account_6_pw
global bet_account_0_n
global bet_account_1_n
global bet_account_2_n
global bet_account_3_n
global bet_account_4_n
global bet_account_5_n
global bet_account_6_n
global bet_account1pw
global bet_account2pw
global bet_account3pw
global bet_account4pw
global bet_account5pw
global bet_account6pw
global bet_last_price
global bet_accounts_range
global bet_tokenName
global bet_last_ethereum_price
global bet_unlockTime
global bet_balance
global bet_balanceOf
global bet_unlock
global bet_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
bet_token_d = 1e18
_e_d = 1e18
bet_accounts_range = '[0, 6]'
bet_unlock = web3.personal.unlockAccount
bet_last_ethereum_price = 370.00
bet_last_price = 0.11
bet_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
bet_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
bet_tokenName = 'Dao.Casino Token'
bet_unlockTime = hex(10000) # Must be hex()
bet_account_0_a = bet_accounts[0]
bet_account_1_a = bet_accounts[1]
bet_account_2_a = bet_accounts[2]
bet_account_3_a = bet_accounts[3]
bet_account_4_a = bet_accounts[4]
bet_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
bet_account_6_a = bet_accounts[6]
# Supply Unlock Passwords For Transactions Below
bet_account_0_pw = 'GuildSkrypt2017!@#'
bet_account_1_pw = ''
bet_account_2_pw = 'GuildSkrypt2017!@#'
bet_account_3_pw = ''
bet_account_4_pw = ''
bet_account_5_pw = ''
bet_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
bet_account_0_n = 'Skotys Bittrex Account'
bet_account_1_n = 'Jeffs Account'
bet_account_2_n = 'Skrypts Bittrex Account'
bet_account_3_n = 'Skotys Personal Account'
bet_account_4_n = 'Unknown'
bet_account_5_n = 'Watched \'Bittrex\' Account.'
bet_account_6_n = 'Watched Account (1)'
# Contract Information Below :
bet_address = '0x8aA33A7899FCC8eA5fBe6A608A109c3893A1B8b2'
bet_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"seal","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"data","type":"uint256[]"}],"name":"fill","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"tokenAddress","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferAnyERC20Token","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"sealed","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
bet = web3.eth.contract(abi=bet_abi, address=bet_address)
bet_balanceOf = bet.call().balanceOf
# End Contract Information
def bet_update_accounts():
 global bet_account0
 global bet_account1
 global bet_account2
 global bet_account3
 global bet_account4
 global bet_account5
 global bet_account6
 global bet_account0_n
 global bet_account1_n
 global bet_account2_n
 global bet_account3_n
 global bet_account4_n
 global bet_account5_n
 global bet_account6_n
 global bet_account0pw
 global bet_account1pw
 global bet_account2pw
 global bet_account3pw
 global bet_account4pw
 global bet_account5pw
 global bet_account6pw
 bet_account0 = bet_account_0_a
 bet_account1 = bet_account_1_a
 bet_account2 = bet_account_2_a
 bet_account3 = bet_account_3_a
 bet_account4 = bet_account_4_a
 bet_account5 = bet_account_5_a
 bet_account6 = bet_account_6_a
 bet_account0_n = bet_account_0_n
 bet_account1_n = bet_account_1_n
 bet_account2_n = bet_account_2_n
 bet_account3_n = bet_account_3_n
 bet_account4_n = bet_account_4_n
 bet_account5_n = bet_account_5_n
 bet_account6_n = bet_account_6_n
 bet_account0pw = bet_account_0_pw
 bet_account1pw = bet_account_1_pw
 bet_account2pw = bet_account_2_pw
 bet_account3pw = bet_account_3_pw
 bet_account4pw = bet_account_4_pw
 bet_account5pw = bet_account_5_pw
 bet_account6pw = bet_account_6_pw
 print(bet_tokenName+' Accounts Updated.')
def bet_update_balances():
 global bet_call_0
 global bet_call_1
 global bet_call_2
 global bet_call_3
 global bet_call_4
 global bet_call_5
 global bet_call_6
 global bet_w_call_0
 global bet_w_call_1
 global bet_w_call_2
 global bet_w_call_3
 global bet_w_call_4
 global bet_w_call_5
 global bet_w_call_6
 bet_update_accounts()
 print('Updating '+bet_tokenName+' Balances Please Wait...')
 bet_call_0 = bet_balanceOf(bet_account0)
 bet_call_1 = bet_balanceOf(bet_account1)
 bet_call_2 = bet_balanceOf(bet_account2)
 bet_call_3 = bet_balanceOf(bet_account3)
 bet_call_4 = bet_balanceOf(bet_account4)
 bet_call_5 = bet_balanceOf(bet_account5)
 bet_call_6 = bet_balanceOf(bet_account6)
 bet_w_call_0 = bet_balance(bet_account0)
 bet_w_call_1 = bet_balance(bet_account1)
 bet_w_call_2 = bet_balance(bet_account2)
 bet_w_call_3 = bet_balance(bet_account3)
 bet_w_call_4 = bet_balance(bet_account4)
 bet_w_call_5 = bet_balance(bet_account5)
 bet_w_call_6 = bet_balance(bet_account6)
 print(bet_tokenName+' Balances Updated.')
def bet_list_all_accounts():
 bet_update_accounts()
 print(bet_tokenName+' '+bet_account0_n+': '+bet_account0)
 print(bet_tokenName+' '+bet_account1_n+': '+bet_account1)
 print(bet_tokenName+' '+bet_account2_n+': '+bet_account2)
 print(bet_tokenName+' '+bet_account3_n+': '+bet_account3)
 print(bet_tokenName+' '+bet_account4_n+': '+bet_account4)
 print(bet_tokenName+' '+bet_account5_n+': '+bet_account5)
 print(bet_tokenName+' '+bet_account6_n+': '+bet_account6)

def bet_account_balance(accountNumber):
 bet_update_balances()
 bet_ab_account_number = accountNumber
 bet_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if bet_ab_account_number == bet_ab_input[0]:
  print('Calling '+bet_account0_n+' '+bet_tokenName+' Balance: ')
  print(bet_account0_n+': '+bet_tokenName+' Balance: '+str(bet_call_0 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_0 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[1]:
  print('Calling '+bet_account1_n+' '+bet_tokenName+' Balance: ')
  print(bet_account1_n+': '+bet_tokenName+' Balance: '+str(bet_call_1 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_1 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[2]:
  print('Calling '+bet_account2_n+' '+bet_tokenName+' Balance: ')
  print(bet_account2_n+': '+bet_tokenName+' Balance: '+str(bet_call_2 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_2 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[3]:
  print('Calling '+bet_account3_n+' '+bet_tokenName+' Balance: ')
  print(bet_account3_n+': '+bet_tokenName+' Balance: '+str(bet_call_3 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_3 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[4]:
  print('Calling '+bet_account4_n+' '+bet_tokenName+' Balance: ')
  print(bet_account4_n+': '+bet_tokenName+' Balance: '+str(bet_call_4 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_4 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[5]:
  print('Calling '+bet_account5_n+' '+bet_tokenName+' Balance: ')
  print(bet_account5_n+': '+bet_tokenName+' Balance: '+str(bet_call_5 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_5 / bet_token_d * bet_last_price))
 if bet_ab_account_number == bet_ab_input[6]:
  print('Calling '+bet_account6_n+' '+bet_tokenName+' Balance: ')
  print(bet_account6_n+': '+bet_tokenName+' Balance: '+str(bet_call_6 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_6 / bet_token_d * bet_last_price))
 if bet_ab_account_number not in bet_ab_input:
  print('Must Integer Within Range '+bet_accounts_range+'.')

def bet_list_all_account_balances():
 bet_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+bet_tokenName+' Balance: ')
 print(bet_account0_n+': '+bet_tokenName+' Balance: '+str(bet_call_0 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_0 / bet_token_d * bet_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(bet_account0_n+': Ethereum Balance '+str(bet_w_call_0 / _e_d)+' $'+str(bet_w_call_0 / _e_d * bet_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+bet_tokenName+' Balance: ')
 print(bet_account1_n+': '+bet_tokenName+' Balance: '+str(bet_call_1 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_1 / bet_token_d * bet_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(bet_account1_n+': Ethereum Balance '+str(bet_w_call_1 / _e_d)+' $'+str(bet_w_call_1 / _e_d * bet_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+bet_tokenName+' Balance: ')
 print(bet_account2_n+': '+bet_tokenName+' Balance: '+str(bet_call_2 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_2 / bet_token_d * bet_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(bet_account2_n+': Ethereum Balance '+str(bet_w_call_2 / _e_d)+' $'+str(bet_w_call_2 / _e_d * bet_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+bet_tokenName+' Balance: ')
 print(bet_account3_n+': '+bet_tokenName+' Balance: '+str(bet_call_3 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_3 / bet_token_d * bet_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(bet_account3_n+': Ethereum Balance '+str(bet_w_call_3 / _e_d)+' $'+str(bet_w_call_3 / _e_d * bet_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+bet_tokenName+' Balance: ')
 print(bet_account4_n+': '+bet_tokenName+' Balance: '+str(bet_call_4 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_4 / bet_token_d * bet_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(bet_account4_n+': Ethereum Balance '+str(bet_w_call_4 / _e_d)+' $'+str(bet_w_call_4 / _e_d * bet_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+bet_tokenName+' Balance: ')
 print(bet_account5_n+': '+bet_tokenName+' Balance: '+str(bet_call_5 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_5 / bet_token_d * bet_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(bet_account5_n+': Ethereum Balance '+str(bet_w_call_5 / _e_d)+' $'+str(bet_w_call_5 /_e_d * bet_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+bet_tokenName+' Balance: ')
 print(bet_account6_n+': '+bet_tokenName+' Balance: '+str(bet_call_6 / bet_token_d)+' Usd/'+bet_tokenName+' Balance: $'+str(bet_call_6 / bet_token_d * bet_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(bet_account6_n+': Ethereum Balance '+str(bet_w_call_6 / _e_d)+' $'+str(bet_w_call_6 / _e_d * bet_last_ethereum_price))
def bet_unlock_all_accounts():
  bet_unlock_account_0()
  bet_unlock_account_1()
  bet_unlock_account_2()
  bet_unlock_account_3()
  bet_unlock_account_4()
  bet_unlock_account_5()
  bet_unlock_account_6()


def bet_unlock_account_0():
  global bet_account0pw
  global bet_account0
  global bet_account0_n
  bet_update_accounts()
  bet_u_a_0 = bet_w_unlock(bet_account0, bet_account0pw, bet_unlockTime)
  if bet_u_a_0 == False:
    if bet_account0pw == '':
     bet_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account0_n+' Passphrase Denied: '+bet_account0pw_r)
    elif bet_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bet_account0_n+' Passphrase Denied: '+bet_account0pw)
  if bet_u_a_0 == True:
   print(bet_account0_n+' Unlocked')

def bet_unlock_account_1():
  global bet_account1pw
  global bet_account1
  global bet_account1_n
  bet_update_accounts()
  bet_u_a_1 = bet_unlock(bet_account1, bet_account1pw, bet_unlockTime)
  if bet_u_a_1 == False:
    if bet_account1pw == '':
     bet_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account1_n+' Passphrase Denied: '+bet_account1pw_r)
    elif bet_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+bet_account1_n+' Passphrase Denied: '+bet_account1pw)
  if bet_u_a_1 == True:
   print(bet_account1_n+' Unlocked')

def bet_unlock_account_2():
  global bet_account2pw
  global bet_account2
  global bet_account2_n
  bet_update_accounts()
  bet_u_a_2 = bet_unlock(bet_account2, bet_account2pw, bet_unlockTime)
  if bet_u_a_2 == False:
    if bet_account2pw == '':
     bet_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account2_n+' Passphrase Denied: '+bet_account2pw_r)
    elif bet_account2pw != '':
     print('Unlock Failure With Account '+bet_account2_n+' Passphrase Denied: '+bet_account2pw)
  if bet_u_a_2 == True:
   print(bet_account2_n+' Unlocked')

def bet_unlock_account_3():
  global bet_account3pw
  global bet_account3
  global bet_account3_n
  bet_update_accounts()
  bet_u_a_3 = bet_unlock(bet_account3, bet_account3pw, bet_unlockTime)
  if bet_u_a_3 == False:
    if bet_account3pw == '':
     bet_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account3_n+' Passphrase Denied: '+bet_account3pw_r)
    elif bet_account3pw != '':
     print('Unlock Failure With Account '+bet_account3_n+' Passphrase Denied: '+bet_account3pw)
  if bet_u_a_3 == True:
   print(bet_account3_n+' Unlocked')

def bet_unlock_account_4():
  global bet_account4pw
  global bet_account4
  global bet_account4_n
  bet_update_accounts()
  bet_u_a_4 = bet_unlock(bet_account4, bet_account4pw, bet_unlockTime)
  if bet_u_a_4 == False:
    if bet_account4pw == '':
     bet_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account4_n+' Passphrase Denied: '+bet_account4pw_r)
    elif bet_account4pw != '':
     print('Unlock Failure With Account '+bet_account4_n+' Passphrase Denied: '+bet_account4pw)
  if bet_u_a_4 == True:
   print(bet_account4_n+' Unlocked')

def bet_unlock_account_5():
  global bet_account5pw
  global bet_account5
  global bet_account5_n
  bet_update_accounts()
  bet_u_a_5 = bet_unlock(bet_account5, bet_account5pw, bet_unlockTime)
  if bet_u_a_5 == False:
    if bet_account5pw == '':
     bet_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account5_n+' Passphrase Denied: '+bet_account5pw_r)
    elif bet_account5pw != '':
     print('Unlock Failure With Account '+bet_account5_n+' Passphrase Denied: '+bet_account5pw)
  if bet_u_a_5 == True:
   print(bet_account5_n+' Unlocked')

def bet_unlock_account_6():
  global bet_account6pw
  global bet_account6
  global bet_account6_n
  bet_update_accounts()
  bet_u_a_6 = bet_unlock(bet_account6, bet_account6pw, bet_unlockTime)
  if bet_u_a_6 == False:
    if bet_account6pw == '':
     bet_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+bet_account6_n+' Passphrase Denied: '+bet_account6pw_r)
    elif bet_account6pw != '':
     print('Unlock Failure With Account '+bet_account6_n+' Passphrase Denied: '+bet_account6pw)
  if bet_u_a_6 == True:
   print(bet_account6_n+' Unlocked')

def bet_unlock_account(bet_ua_accountNumber):
 bet_update_accounts()
 bet_ua_account_number = bet_ua_accountNumber
 bet_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if bet_ua_account_number == bet_ua_input[0]:
  bet_unlock_account_0()
 if bet_ua_account_number == bet_ua_input[1]:
  bet_unlock_account_1()
 if bet_ua_account_number == bet_ua_input[2]:
  bet_unlock_account_2()
 if bet_ua_account_number == bet_ua_input[3]:
  bet_unlock_account_3()
 if bet_ua_account_number == bet_ua_input[4]:
  bet_unlock_account_4()
 if bet_ua_account_number == bet_ua_input[5]:
  bet_unlock_account_5()
 if bet_ua_account_number == bet_ua_input[6]:
  bet_unlock_account_6()
 if bet_ua_account_number not in bet_ua_input:
  print('Must Integer Within Range '+bet_accounts_range+'.')
 

def bet_approve_between_accounts(fromAccount, toAccount, msgValue):
  bet_update_accounts()
  bet_a_0 = bet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(bet_a_0)

def bet_approve(fromAccountNumber, toAddress, msgValue):
  bet_update_accounts()
  bet_unlock_account(fromAccountNumber)
  bet_a_1 = bet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(bet_a_1)

def bet_transfer_between_accounts(fromAccount, toAccount, msgValue):
  bet_update_accounts()
  bet_unlock_account(fromAccount)
  bet_t_0 = bet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(bet_t_0)

def bet_transfer(fromAccountNumber, toAddress, msgValue):
  bet_update_accounts()
  bet_unlock_account(fromAccountNumber)
  bet_t_1 = bet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(bet_t_1)

def bet_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  bet_update_accounts()
  bet_unlock_account(callAccount)
  bet_tf_0 = bet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(bet_tf_0)

def bet_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  bet_update_accounts()
  bet_unlock_account(callAccount)
  bet_tf_1 = bet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(bet_tf_1)
  


def bet_help():
  print('Following Functions For '+bet_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * bet_unlock => web3.personal.unlockAccount
/ * bet_accounts => web3.personal.listAccounts
/ * bet_balance = web3.eth.getBalance
** bet => web3.eth.contract(abi=bet_abi, address=bet_address)
** / * bet_balanceOf => bet.call().balanceOf

~ Function Listing Below:
~ bet_update_accounts()
~ bet_update_balances() \n\r -- => bet_update_accounts()
~ bet_list_all_accounts() \n\r -- => bet_update_accounts()
~ bet_account_balance(accountNumber) \n\r -- => bet_update_balances() 
~ bet_list_all_account_balances() \n\r -- => bet_update_balances()
~ bet_unlock_all_accounts() \n\r -- => bet_unlock_account_0() \n\r -- => bet_unlock_account_1() \n\r -- => bet_unlock_account_2() \n\r -- => bet_unlock_account_3() \n\r -- => bet_unlock_account_4() \n\r -- => bet_unlock_account_5() \n\r -- => bet_unlock_account_6() 
~ bet_unlock_account_0() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account0, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_1() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account1, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_2() \n\r -- => bet_update_accounts() \n\r --/ *bet_w_unlock(bet_account2, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_3() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account3, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_4() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account4, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_5() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account5, bet_account0pw, bet_unlockTime)
~ bet_unlock_account_6() \n\r -- => bet_update_accounts() \n\r -- / *bet_w_unlock(bet_account6, bet_account0pw, bet_unlockTime)
~ bet_unlock_account(bet_ua_accountNumber) \n\r -- => bet_update_accounts() \n\r -- // bet_unlock_account_0() \n\r -- // bet_unlock_account_1() \n\r -- // bet_unlock_account_2() \n\r -- // bet_unlock_account_3() \n\r -- // bet_unlock_account_4() \n\r -- // bet_unlock_account_5() \n\r -- // bet_unlock_account_6()
~ bet_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(fromAccount) \n\r -- / ** bet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bet_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(fromAccountNumber) \n\r -- / ** bet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ bet_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(fromAccount) \n\r -- / ** bet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ bet_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(fromAccountNumber) \n\r -- / ** bet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bet_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(callAccount) \n\r / ** bet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ bet_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => bet_update_accounts() \n\r -- => bet_unlock_account(callAccount) \n\r -- / ** bet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ bet_help() <-- You Are Here. ''')