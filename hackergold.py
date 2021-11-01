#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global hkg_account_0_a
global hkg_account_1_a
global hkg_account_2_a
global hkg_account_3_a
global hkg_account_4_a
global hkg_account_5_a
global hkg_account_6_a
global hkg_address
global hkg_abi
global hkg
global hkg_call_0
global hkg_call_1
global hkg_call_2
global hkg_call_3
global hkg_call_4
global hkg_call_5
global hkg_call_6
global hkg_call_ab
global hkg_accounts
global hkg_account_0_pw
global hkg_account_1_pw
global hkg_account_2_pw
global hkg_account_3_pw
global hkg_account_4_pw
global hkg_account_5_pw
global hkg_account_6_pw
global hkg_account_0_n
global hkg_account_1_n
global hkg_account_2_n
global hkg_account_3_n
global hkg_account_4_n
global hkg_account_5_n
global hkg_account_6_n
global hkg_account1pw
global hkg_account2pw
global hkg_account3pw
global hkg_account4pw
global hkg_account5pw
global hkg_account6pw
global hkg_last_price
global hkg_accounts_range
global hkg_tokenName
global hkg_last_ethereum_price
global hkg_unlockTime
global hkg_balance
global hkg_balanceOf
global hkg_unlock
global hkg_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
hkg_token_d = 1e3
_e_d = 1e18
hkg_accounts_range = '[0, 6]'
hkg_unlock = web3.personal.unlockAccount
hkg_last_ethereum_price = 370.00
hkg_last_price = 0.04
hkg_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
hkg_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
hkg_tokenName = 'HackerGold Token'
hkg_unlockTime = hex(10000) # Must be hex()
hkg_account_0_a = hkg_accounts[0]
hkg_account_1_a = hkg_accounts[1]
hkg_account_2_a = hkg_accounts[2]
hkg_account_3_a = hkg_accounts[3]
hkg_account_4_a = hkg_accounts[4]
hkg_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
hkg_account_6_a = hkg_accounts[6]
# Supply Unlock Passwords For Transactions Below
hkg_account_0_pw = 'GuildSkrypt2017!@#'
hkg_account_1_pw = ''
hkg_account_2_pw = 'GuildSkrypt2017!@#'
hkg_account_3_pw = ''
hkg_account_4_pw = ''
hkg_account_5_pw = ''
hkg_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
hkg_account_0_n = 'Skotys Bittrex Account'
hkg_account_1_n = 'Jeffs Account'
hkg_account_2_n = 'Skrypts Bittrex Account'
hkg_account_3_n = 'Skotys Personal Account'
hkg_account_4_n = 'Unknown'
hkg_account_5_n = 'Watched \'Bittrex\' Account.'
hkg_account_6_n = 'Watched Account (1)'
# Contract Information Below :
hkg_address = '0x14F37B574242D366558dB61f3335289a5035c506'
hkg_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"holder","type":"address"}],"name":"createHKG","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getPrice","outputs":[{"name":"result","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getNow","outputs":[{"name":"result","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getTotalSupply","outputs":[{"name":"result","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getTotalValue","outputs":[{"name":"result","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"multisig","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
hkg = web3.eth.contract(abi=hkg_abi, address=hkg_address)
hkg_balanceOf = hkg.call().balanceOf
# End Contract Information
def hkg_update_accounts():
 global hkg_account0
 global hkg_account1
 global hkg_account2
 global hkg_account3
 global hkg_account4
 global hkg_account5
 global hkg_account6
 global hkg_account0_n
 global hkg_account1_n
 global hkg_account2_n
 global hkg_account3_n
 global hkg_account4_n
 global hkg_account5_n
 global hkg_account6_n
 global hkg_account0pw
 global hkg_account1pw
 global hkg_account2pw
 global hkg_account3pw
 global hkg_account4pw
 global hkg_account5pw
 global hkg_account6pw
 hkg_account0 = hkg_account_0_a
 hkg_account1 = hkg_account_1_a
 hkg_account2 = hkg_account_2_a
 hkg_account3 = hkg_account_3_a
 hkg_account4 = hkg_account_4_a
 hkg_account5 = hkg_account_5_a
 hkg_account6 = hkg_account_6_a
 hkg_account0_n = hkg_account_0_n
 hkg_account1_n = hkg_account_1_n
 hkg_account2_n = hkg_account_2_n
 hkg_account3_n = hkg_account_3_n
 hkg_account4_n = hkg_account_4_n
 hkg_account5_n = hkg_account_5_n
 hkg_account6_n = hkg_account_6_n
 hkg_account0pw = hkg_account_0_pw
 hkg_account1pw = hkg_account_1_pw
 hkg_account2pw = hkg_account_2_pw
 hkg_account3pw = hkg_account_3_pw
 hkg_account4pw = hkg_account_4_pw
 hkg_account5pw = hkg_account_5_pw
 hkg_account6pw = hkg_account_6_pw
 print(hkg_tokenName+' Accounts Updated.')
def hkg_update_balances():
 global hkg_call_0
 global hkg_call_1
 global hkg_call_2
 global hkg_call_3
 global hkg_call_4
 global hkg_call_5
 global hkg_call_6
 global hkg_w_call_0
 global hkg_w_call_1
 global hkg_w_call_2
 global hkg_w_call_3
 global hkg_w_call_4
 global hkg_w_call_5
 global hkg_w_call_6
 hkg_update_accounts()
 print('Updating '+hkg_tokenName+' Balances Please Wait...')
 hkg_call_0 = hkg_balanceOf(hkg_account0)
 hkg_call_1 = hkg_balanceOf(hkg_account1)
 hkg_call_2 = hkg_balanceOf(hkg_account2)
 hkg_call_3 = hkg_balanceOf(hkg_account3)
 hkg_call_4 = hkg_balanceOf(hkg_account4)
 hkg_call_5 = hkg_balanceOf(hkg_account5)
 hkg_call_6 = hkg_balanceOf(hkg_account6)
 hkg_w_call_0 = hkg_balance(hkg_account0)
 hkg_w_call_1 = hkg_balance(hkg_account1)
 hkg_w_call_2 = hkg_balance(hkg_account2)
 hkg_w_call_3 = hkg_balance(hkg_account3)
 hkg_w_call_4 = hkg_balance(hkg_account4)
 hkg_w_call_5 = hkg_balance(hkg_account5)
 hkg_w_call_6 = hkg_balance(hkg_account6)
 print(hkg_tokenName+' Balances Updated.')
def hkg_list_all_accounts():
 hkg_update_accounts()
 print(hkg_tokenName+' '+hkg_account0_n+': '+hkg_account0)
 print(hkg_tokenName+' '+hkg_account1_n+': '+hkg_account1)
 print(hkg_tokenName+' '+hkg_account2_n+': '+hkg_account2)
 print(hkg_tokenName+' '+hkg_account3_n+': '+hkg_account3)
 print(hkg_tokenName+' '+hkg_account4_n+': '+hkg_account4)
 print(hkg_tokenName+' '+hkg_account5_n+': '+hkg_account5)
 print(hkg_tokenName+' '+hkg_account6_n+': '+hkg_account6)

def hkg_account_balance(accountNumber):
 hkg_update_balances()
 hkg_ab_account_number = accountNumber
 hkg_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if hkg_ab_account_number == hkg_ab_input[0]:
  print('Calling '+hkg_account0_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account0_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_0 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_0 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[1]:
  print('Calling '+hkg_account1_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account1_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_1 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_1 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[2]:
  print('Calling '+hkg_account2_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account2_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_2 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_2 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[3]:
  print('Calling '+hkg_account3_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account3_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_3 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_3 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[4]:
  print('Calling '+hkg_account4_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account4_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_4 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_4 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[5]:
  print('Calling '+hkg_account5_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account5_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_5 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_5 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number == hkg_ab_input[6]:
  print('Calling '+hkg_account6_n+' '+hkg_tokenName+' Balance: ')
  print(hkg_account6_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_6 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_6 / hkg_token_d * hkg_last_price))
 if hkg_ab_account_number not in hkg_ab_input:
  print('Must Integer Within Range '+hkg_accounts_range+'.')

def hkg_list_all_account_balances():
 hkg_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+hkg_tokenName+' Balance: ')
 print(hkg_account0_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_0 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_0 / hkg_token_d * hkg_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(hkg_account0_n+': Ethereum Balance '+str(hkg_w_call_0 / _e_d)+' $'+str(hkg_w_call_0 / _e_d * hkg_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+hkg_tokenName+' Balance: ')
 print(hkg_account1_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_1 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_1 / hkg_token_d * hkg_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(hkg_account1_n+': Ethereum Balance '+str(hkg_w_call_1 / _e_d)+' $'+str(hkg_w_call_1 / _e_d * hkg_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+hkg_tokenName+' Balance: ')
 print(hkg_account2_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_2 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_2 / hkg_token_d * hkg_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(hkg_account2_n+': Ethereum Balance '+str(hkg_w_call_2 / _e_d)+' $'+str(hkg_w_call_2 / _e_d * hkg_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+hkg_tokenName+' Balance: ')
 print(hkg_account3_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_3 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_3 / hkg_token_d * hkg_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(hkg_account3_n+': Ethereum Balance '+str(hkg_w_call_3 / _e_d)+' $'+str(hkg_w_call_3 / _e_d * hkg_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+hkg_tokenName+' Balance: ')
 print(hkg_account4_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_4 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_4 / hkg_token_d * hkg_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(hkg_account4_n+': Ethereum Balance '+str(hkg_w_call_4 / _e_d)+' $'+str(hkg_w_call_4 / _e_d * hkg_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+hkg_tokenName+' Balance: ')
 print(hkg_account5_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_5 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_5 / hkg_token_d * hkg_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(hkg_account5_n+': Ethereum Balance '+str(hkg_w_call_5 / _e_d)+' $'+str(hkg_w_call_5 /_e_d * hkg_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+hkg_tokenName+' Balance: ')
 print(hkg_account6_n+': '+hkg_tokenName+' Balance: '+str(hkg_call_6 / hkg_token_d)+' Usd/'+hkg_tokenName+' Balance: $'+str(hkg_call_6 / hkg_token_d * hkg_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(hkg_account6_n+': Ethereum Balance '+str(hkg_w_call_6 / _e_d)+' $'+str(hkg_w_call_6 / _e_d * hkg_last_ethereum_price))
def hkg_unlock_all_accounts():
  hkg_unlock_account_0()
  hkg_unlock_account_1()
  hkg_unlock_account_2()
  hkg_unlock_account_3()
  hkg_unlock_account_4()
  hkg_unlock_account_5()
  hkg_unlock_account_6()


def hkg_unlock_account_0():
  global hkg_account0pw
  global hkg_account0
  global hkg_account0_n
  hkg_update_accounts()
  hkg_u_a_0 = hkg_w_unlock(hkg_account0, hkg_account0pw, hkg_unlockTime)
  if hkg_u_a_0 == False:
    if hkg_account0pw == '':
     hkg_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account0_n+' Passphrase Denied: '+hkg_account0pw_r)
    elif hkg_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+hkg_account0_n+' Passphrase Denied: '+hkg_account0pw)
  if hkg_u_a_0 == True:
   print(hkg_account0_n+' Unlocked')

def hkg_unlock_account_1():
  global hkg_account1pw
  global hkg_account1
  global hkg_account1_n
  hkg_update_accounts()
  hkg_u_a_1 = hkg_unlock(hkg_account1, hkg_account1pw, hkg_unlockTime)
  if hkg_u_a_1 == False:
    if hkg_account1pw == '':
     hkg_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account1_n+' Passphrase Denied: '+hkg_account1pw_r)
    elif hkg_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+hkg_account1_n+' Passphrase Denied: '+hkg_account1pw)
  if hkg_u_a_1 == True:
   print(hkg_account1_n+' Unlocked')

def hkg_unlock_account_2():
  global hkg_account2pw
  global hkg_account2
  global hkg_account2_n
  hkg_update_accounts()
  hkg_u_a_2 = hkg_unlock(hkg_account2, hkg_account2pw, hkg_unlockTime)
  if hkg_u_a_2 == False:
    if hkg_account2pw == '':
     hkg_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account2_n+' Passphrase Denied: '+hkg_account2pw_r)
    elif hkg_account2pw != '':
     print('Unlock Failure With Account '+hkg_account2_n+' Passphrase Denied: '+hkg_account2pw)
  if hkg_u_a_2 == True:
   print(hkg_account2_n+' Unlocked')

def hkg_unlock_account_3():
  global hkg_account3pw
  global hkg_account3
  global hkg_account3_n
  hkg_update_accounts()
  hkg_u_a_3 = hkg_unlock(hkg_account3, hkg_account3pw, hkg_unlockTime)
  if hkg_u_a_3 == False:
    if hkg_account3pw == '':
     hkg_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account3_n+' Passphrase Denied: '+hkg_account3pw_r)
    elif hkg_account3pw != '':
     print('Unlock Failure With Account '+hkg_account3_n+' Passphrase Denied: '+hkg_account3pw)
  if hkg_u_a_3 == True:
   print(hkg_account3_n+' Unlocked')

def hkg_unlock_account_4():
  global hkg_account4pw
  global hkg_account4
  global hkg_account4_n
  hkg_update_accounts()
  hkg_u_a_4 = hkg_unlock(hkg_account4, hkg_account4pw, hkg_unlockTime)
  if hkg_u_a_4 == False:
    if hkg_account4pw == '':
     hkg_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account4_n+' Passphrase Denied: '+hkg_account4pw_r)
    elif hkg_account4pw != '':
     print('Unlock Failure With Account '+hkg_account4_n+' Passphrase Denied: '+hkg_account4pw)
  if hkg_u_a_4 == True:
   print(hkg_account4_n+' Unlocked')

def hkg_unlock_account_5():
  global hkg_account5pw
  global hkg_account5
  global hkg_account5_n
  hkg_update_accounts()
  hkg_u_a_5 = hkg_unlock(hkg_account5, hkg_account5pw, hkg_unlockTime)
  if hkg_u_a_5 == False:
    if hkg_account5pw == '':
     hkg_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account5_n+' Passphrase Denied: '+hkg_account5pw_r)
    elif hkg_account5pw != '':
     print('Unlock Failure With Account '+hkg_account5_n+' Passphrase Denied: '+hkg_account5pw)
  if hkg_u_a_5 == True:
   print(hkg_account5_n+' Unlocked')

def hkg_unlock_account_6():
  global hkg_account6pw
  global hkg_account6
  global hkg_account6_n
  hkg_update_accounts()
  hkg_u_a_6 = hkg_unlock(hkg_account6, hkg_account6pw, hkg_unlockTime)
  if hkg_u_a_6 == False:
    if hkg_account6pw == '':
     hkg_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hkg_account6_n+' Passphrase Denied: '+hkg_account6pw_r)
    elif hkg_account6pw != '':
     print('Unlock Failure With Account '+hkg_account6_n+' Passphrase Denied: '+hkg_account6pw)
  if hkg_u_a_6 == True:
   print(hkg_account6_n+' Unlocked')

def hkg_unlock_account(hkg_ua_accountNumber):
 hkg_update_accounts()
 hkg_ua_account_number = hkg_ua_accountNumber
 hkg_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if hkg_ua_account_number == hkg_ua_input[0]:
  hkg_unlock_account_0()
 if hkg_ua_account_number == hkg_ua_input[1]:
  hkg_unlock_account_1()
 if hkg_ua_account_number == hkg_ua_input[2]:
  hkg_unlock_account_2()
 if hkg_ua_account_number == hkg_ua_input[3]:
  hkg_unlock_account_3()
 if hkg_ua_account_number == hkg_ua_input[4]:
  hkg_unlock_account_4()
 if hkg_ua_account_number == hkg_ua_input[5]:
  hkg_unlock_account_5()
 if hkg_ua_account_number == hkg_ua_input[6]:
  hkg_unlock_account_6()
 if hkg_ua_account_number not in hkg_ua_input:
  print('Must Integer Within Range '+hkg_accounts_range+'.')
 

def hkg_approve_between_accounts(fromAccount, toAccount, msgValue):
  hkg_update_accounts()
  hkg_a_0 = hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(hkg_a_0)

def hkg_approve(fromAccountNumber, toAddress, msgValue):
  hkg_update_accounts()
  hkg_unlock_account(fromAccountNumber)
  hkg_a_1 = hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(hkg_a_1)

def hkg_transfer_between_accounts(fromAccount, toAccount, msgValue):
  hkg_update_accounts()
  hkg_unlock_account(fromAccount)
  hkg_t_0 = hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(hkg_t_0)

def hkg_transfer(fromAccountNumber, toAddress, msgValue):
  hkg_update_accounts()
  hkg_unlock_account(fromAccountNumber)
  hkg_t_1 = hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(hkg_t_1)

def hkg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  hkg_update_accounts()
  hkg_unlock_account(callAccount)
  hkg_tf_0 = hkg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(hkg_tf_0)

def hkg_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  hkg_update_accounts()
  hkg_unlock_account(callAccount)
  hkg_tf_1 = hkg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(hkg_tf_1)
  


def hkg_help():
  print('Following Functions For '+hkg_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * hkg_unlock => web3.personal.unlockAccount
/ * hkg_accounts => web3.personal.listAccounts
/ * hkg_balance = web3.eth.getBalance
** hkg => web3.eth.contract(abi=hkg_abi, address=hkg_address)
** / * hkg_balanceOf => hkg.call().balanceOf

~ Function Listing Below:
~ hkg_update_accounts()
~ hkg_update_balances() \n\r -- => hkg_update_accounts()
~ hkg_list_all_accounts() \n\r -- => hkg_update_accounts()
~ hkg_account_balance(accountNumber) \n\r -- => hkg_update_balances() 
~ hkg_list_all_account_balances() \n\r -- => hkg_update_balances()
~ hkg_unlock_all_accounts() \n\r -- => hkg_unlock_account_0() \n\r -- => hkg_unlock_account_1() \n\r -- => hkg_unlock_account_2() \n\r -- => hkg_unlock_account_3() \n\r -- => hkg_unlock_account_4() \n\r -- => hkg_unlock_account_5() \n\r -- => hkg_unlock_account_6() 
~ hkg_unlock_account_0() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account0, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_1() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account1, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_2() \n\r -- => hkg_update_accounts() \n\r --/ *hkg_w_unlock(hkg_account2, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_3() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account3, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_4() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account4, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_5() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account5, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account_6() \n\r -- => hkg_update_accounts() \n\r -- / *hkg_w_unlock(hkg_account6, hkg_account0pw, hkg_unlockTime)
~ hkg_unlock_account(hkg_ua_accountNumber) \n\r -- => hkg_update_accounts() \n\r -- // hkg_unlock_account_0() \n\r -- // hkg_unlock_account_1() \n\r -- // hkg_unlock_account_2() \n\r -- // hkg_unlock_account_3() \n\r -- // hkg_unlock_account_4() \n\r -- // hkg_unlock_account_5() \n\r -- // hkg_unlock_account_6()
~ hkg_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(fromAccount) \n\r -- / ** hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ hkg_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(fromAccountNumber) \n\r -- / ** hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ hkg_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(fromAccount) \n\r -- / ** hkg.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ hkg_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(fromAccountNumber) \n\r -- / ** hkg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ hkg_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(callAccount) \n\r / ** hkg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ hkg_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => hkg_update_accounts() \n\r -- => hkg_unlock_account(callAccount) \n\r -- / ** hkg.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ hkg_help() <-- You Are Here. ''')