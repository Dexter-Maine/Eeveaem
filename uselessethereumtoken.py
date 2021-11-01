#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global uet_account_0_a
global uet_account_1_a
global uet_account_2_a
global uet_account_3_a
global uet_account_4_a
global uet_account_5_a
global uet_account_6_a
global uet_address
global uet_abi
global uet
global uet_call_0
global uet_call_1
global uet_call_2
global uet_call_3
global uet_call_4
global uet_call_5
global uet_call_6
global uet_call_ab
global uet_accounts
global uet_account_0_pw
global uet_account_1_pw
global uet_account_2_pw
global uet_account_3_pw
global uet_account_4_pw
global uet_account_5_pw
global uet_account_6_pw
global uet_account_0_n
global uet_account_1_n
global uet_account_2_n
global uet_account_3_n
global uet_account_4_n
global uet_account_5_n
global uet_account_6_n
global uet_account1pw
global uet_account2pw
global uet_account3pw
global uet_account4pw
global uet_account5pw
global uet_account6pw
global uet_last_price
global uet_accounts_range
global uet_tokenName
global uet_last_ethereum_price
global uet_unlockuet
global uet_balance
global uet_balanceOf
global uet_unlock
global uet_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
uet_token_d = 1e18
_e_d = 1e18
uet_accounts_range = '[0, 6]'
uet_unlock = web3.personal.unlockAccount
uet_last_ethereum_price = 370.00
uet_last_price = 0.02
uet_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
uet_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
uet_tokenName = 'UselessEthereum Token'
uet_unlockuet = hex(10000) # Must be hex()
uet_account_0_a = uet_accounts[0]
uet_account_1_a = uet_accounts[1]
uet_account_2_a = uet_accounts[2]
uet_account_3_a = uet_accounts[3]
uet_account_4_a = uet_accounts[4]
uet_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
uet_account_6_a = uet_accounts[6]
# Supply Unlock Passwords For Transactions Below
uet_account_0_pw = 'GuildSkrypt2017!@#'
uet_account_1_pw = ''
uet_account_2_pw = 'GuildSkrypt2017!@#'
uet_account_3_pw = ''
uet_account_4_pw = ''
uet_account_5_pw = ''
uet_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
uet_account_0_n = 'Skotys Bittrex Account'
uet_account_1_n = 'Jeffs Account'
uet_account_2_n = 'Skrypts Bittrex Account'
uet_account_3_n = 'Skotys Personal Account'
uet_account_4_n = 'Unknown'
uet_account_5_n = 'Watched \'Bittrex\' Account.'
uet_account_6_n = 'Watched Account (1)'
# Contract Information Below :
uet_address = '0x27f706edde3aD952EF647Dd67E24e38CD0803DD6'
uet_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalContribution","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"disablePurchasing","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"enablePurchasing","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalBonusTokensIssued","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getStats","outputs":[{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"purchasingAllowed","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_tokenContract","type":"address"}],"name":"withdrawForeignTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
uet = web3.eth.contract(abi=uet_abi, address=uet_address)
uet_balanceOf = uet.call().balanceOf
# End Contract Information
def uet_update_accounts():
 global uet_account0
 global uet_account1
 global uet_account2
 global uet_account3
 global uet_account4
 global uet_account5
 global uet_account6
 global uet_account0_n
 global uet_account1_n
 global uet_account2_n
 global uet_account3_n
 global uet_account4_n
 global uet_account5_n
 global uet_account6_n
 global uet_account0pw
 global uet_account1pw
 global uet_account2pw
 global uet_account3pw
 global uet_account4pw
 global uet_account5pw
 global uet_account6pw
 uet_account0 = uet_account_0_a
 uet_account1 = uet_account_1_a
 uet_account2 = uet_account_2_a
 uet_account3 = uet_account_3_a
 uet_account4 = uet_account_4_a
 uet_account5 = uet_account_5_a
 uet_account6 = uet_account_6_a
 uet_account0_n = uet_account_0_n
 uet_account1_n = uet_account_1_n
 uet_account2_n = uet_account_2_n
 uet_account3_n = uet_account_3_n
 uet_account4_n = uet_account_4_n
 uet_account5_n = uet_account_5_n
 uet_account6_n = uet_account_6_n
 uet_account0pw = uet_account_0_pw
 uet_account1pw = uet_account_1_pw
 uet_account2pw = uet_account_2_pw
 uet_account3pw = uet_account_3_pw
 uet_account4pw = uet_account_4_pw
 uet_account5pw = uet_account_5_pw
 uet_account6pw = uet_account_6_pw
 print(uet_tokenName+' Accounts Updated.')
def uet_update_balances():
 global uet_call_0
 global uet_call_1
 global uet_call_2
 global uet_call_3
 global uet_call_4
 global uet_call_5
 global uet_call_6
 global uet_w_call_0
 global uet_w_call_1
 global uet_w_call_2
 global uet_w_call_3
 global uet_w_call_4
 global uet_w_call_5
 global uet_w_call_6
 uet_update_accounts()
 print('Updating '+uet_tokenName+' Balances Please Wait...')
 uet_call_0 = uet_balanceOf(uet_account0)
 uet_call_1 = uet_balanceOf(uet_account1)
 uet_call_2 = uet_balanceOf(uet_account2)
 uet_call_3 = uet_balanceOf(uet_account3)
 uet_call_4 = uet_balanceOf(uet_account4)
 uet_call_5 = uet_balanceOf(uet_account5)
 uet_call_6 = uet_balanceOf(uet_account6)
 uet_w_call_0 = uet_balance(uet_account0)
 uet_w_call_1 = uet_balance(uet_account1)
 uet_w_call_2 = uet_balance(uet_account2)
 uet_w_call_3 = uet_balance(uet_account3)
 uet_w_call_4 = uet_balance(uet_account4)
 uet_w_call_5 = uet_balance(uet_account5)
 uet_w_call_6 = uet_balance(uet_account6)
 print(uet_tokenName+' Balances Updated.')
def uet_list_all_accounts():
 uet_update_accounts()
 print(uet_tokenName+' '+uet_account0_n+': '+uet_account0)
 print(uet_tokenName+' '+uet_account1_n+': '+uet_account1)
 print(uet_tokenName+' '+uet_account2_n+': '+uet_account2)
 print(uet_tokenName+' '+uet_account3_n+': '+uet_account3)
 print(uet_tokenName+' '+uet_account4_n+': '+uet_account4)
 print(uet_tokenName+' '+uet_account5_n+': '+uet_account5)
 print(uet_tokenName+' '+uet_account6_n+': '+uet_account6)

def uet_account_balance(accountNumber):
 uet_update_balances()
 uet_ab_account_number = accountNumber
 uet_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if uet_ab_account_number == uet_ab_input[0]:
  print('Calling '+uet_account0_n+' '+uet_tokenName+' Balance: ')
  print(uet_account0_n+': '+uet_tokenName+' Balance: '+str(uet_call_0 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_0 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[1]:
  print('Calling '+uet_account1_n+' '+uet_tokenName+' Balance: ')
  print(uet_account1_n+': '+uet_tokenName+' Balance: '+str(uet_call_1 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_1 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[2]:
  print('Calling '+uet_account2_n+' '+uet_tokenName+' Balance: ')
  print(uet_account2_n+': '+uet_tokenName+' Balance: '+str(uet_call_2 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_2 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[3]:
  print('Calling '+uet_account3_n+' '+uet_tokenName+' Balance: ')
  print(uet_account3_n+': '+uet_tokenName+' Balance: '+str(uet_call_3 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_3 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[4]:
  print('Calling '+uet_account4_n+' '+uet_tokenName+' Balance: ')
  print(uet_account4_n+': '+uet_tokenName+' Balance: '+str(uet_call_4 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_4 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[5]:
  print('Calling '+uet_account5_n+' '+uet_tokenName+' Balance: ')
  print(uet_account5_n+': '+uet_tokenName+' Balance: '+str(uet_call_5 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_5 / uet_token_d * uet_last_price))
 if uet_ab_account_number == uet_ab_input[6]:
  print('Calling '+uet_account6_n+' '+uet_tokenName+' Balance: ')
  print(uet_account6_n+': '+uet_tokenName+' Balance: '+str(uet_call_6 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_6 / uet_token_d * uet_last_price))
 if uet_ab_account_number not in uet_ab_input:
  print('Must Integer Within Range '+uet_accounts_range+'.')

def uet_list_all_account_balances():
 uet_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+uet_tokenName+' Balance: ')
 print(uet_account0_n+': '+uet_tokenName+' Balance: '+str(uet_call_0 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_0 / uet_token_d * uet_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(uet_account0_n+': Ethereum Balance '+str(uet_w_call_0 / _e_d)+' $'+str(uet_w_call_0 / _e_d * uet_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+uet_tokenName+' Balance: ')
 print(uet_account1_n+': '+uet_tokenName+' Balance: '+str(uet_call_1 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_1 / uet_token_d * uet_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(uet_account1_n+': Ethereum Balance '+str(uet_w_call_1 / _e_d)+' $'+str(uet_w_call_1 / _e_d * uet_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+uet_tokenName+' Balance: ')
 print(uet_account2_n+': '+uet_tokenName+' Balance: '+str(uet_call_2 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_2 / uet_token_d * uet_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(uet_account2_n+': Ethereum Balance '+str(uet_w_call_2 / _e_d)+' $'+str(uet_w_call_2 / _e_d * uet_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+uet_tokenName+' Balance: ')
 print(uet_account3_n+': '+uet_tokenName+' Balance: '+str(uet_call_3 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_3 / uet_token_d * uet_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(uet_account3_n+': Ethereum Balance '+str(uet_w_call_3 / _e_d)+' $'+str(uet_w_call_3 / _e_d * uet_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+uet_tokenName+' Balance: ')
 print(uet_account4_n+': '+uet_tokenName+' Balance: '+str(uet_call_4 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_4 / uet_token_d * uet_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(uet_account4_n+': Ethereum Balance '+str(uet_w_call_4 / _e_d)+' $'+str(uet_w_call_4 / _e_d * uet_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+uet_tokenName+' Balance: ')
 print(uet_account5_n+': '+uet_tokenName+' Balance: '+str(uet_call_5 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_5 / uet_token_d * uet_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(uet_account5_n+': Ethereum Balance '+str(uet_w_call_5 / _e_d)+' $'+str(uet_w_call_5 /_e_d * uet_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+uet_tokenName+' Balance: ')
 print(uet_account6_n+': '+uet_tokenName+' Balance: '+str(uet_call_6 / uet_token_d)+' Usd/'+uet_tokenName+' Balance: $'+str(uet_call_6 / uet_token_d * uet_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(uet_account6_n+': Ethereum Balance '+str(uet_w_call_6 / _e_d)+' $'+str(uet_w_call_6 / _e_d * uet_last_ethereum_price))
def uet_unlock_all_accounts():
  uet_unlock_account_0()
  uet_unlock_account_1()
  uet_unlock_account_2()
  uet_unlock_account_3()
  uet_unlock_account_4()
  uet_unlock_account_5()
  uet_unlock_account_6()


def uet_unlock_account_0():
  global uet_account0pw
  global uet_account0
  global uet_account0_n
  uet_update_accounts()
  uet_u_a_0 = uet_w_unlock(uet_account0, uet_account0pw, uet_unlockuet)
  if uet_u_a_0 == False:
    if uet_account0pw == '':
     uet_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account0_n+' Passphrase Denied: '+uet_account0pw_r)
    elif uet_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+uet_account0_n+' Passphrase Denied: '+uet_account0pw)
  if uet_u_a_0 == True:
   print(uet_account0_n+' Unlocked')

def uet_unlock_account_1():
  global uet_account1pw
  global uet_account1
  global uet_account1_n
  uet_update_accounts()
  uet_u_a_1 = uet_unlock(uet_account1, uet_account1pw, uet_unlockuet)
  if uet_u_a_1 == False:
    if uet_account1pw == '':
     uet_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account1_n+' Passphrase Denied: '+uet_account1pw_r)
    elif uet_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+uet_account1_n+' Passphrase Denied: '+uet_account1pw)
  if uet_u_a_1 == True:
   print(uet_account1_n+' Unlocked')

def uet_unlock_account_2():
  global uet_account2pw
  global uet_account2
  global uet_account2_n
  uet_update_accounts()
  uet_u_a_2 = uet_unlock(uet_account2, uet_account2pw, uet_unlockuet)
  if uet_u_a_2 == False:
    if uet_account2pw == '':
     uet_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account2_n+' Passphrase Denied: '+uet_account2pw_r)
    elif uet_account2pw != '':
     print('Unlock Failure With Account '+uet_account2_n+' Passphrase Denied: '+uet_account2pw)
  if uet_u_a_2 == True:
   print(uet_account2_n+' Unlocked')

def uet_unlock_account_3():
  global uet_account3pw
  global uet_account3
  global uet_account3_n
  uet_update_accounts()
  uet_u_a_3 = uet_unlock(uet_account3, uet_account3pw, uet_unlockuet)
  if uet_u_a_3 == False:
    if uet_account3pw == '':
     uet_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account3_n+' Passphrase Denied: '+uet_account3pw_r)
    elif uet_account3pw != '':
     print('Unlock Failure With Account '+uet_account3_n+' Passphrase Denied: '+uet_account3pw)
  if uet_u_a_3 == True:
   print(uet_account3_n+' Unlocked')

def uet_unlock_account_4():
  global uet_account4pw
  global uet_account4
  global uet_account4_n
  uet_update_accounts()
  uet_u_a_4 = uet_unlock(uet_account4, uet_account4pw, uet_unlockuet)
  if uet_u_a_4 == False:
    if uet_account4pw == '':
     uet_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account4_n+' Passphrase Denied: '+uet_account4pw_r)
    elif uet_account4pw != '':
     print('Unlock Failure With Account '+uet_account4_n+' Passphrase Denied: '+uet_account4pw)
  if uet_u_a_4 == True:
   print(uet_account4_n+' Unlocked')

def uet_unlock_account_5():
  global uet_account5pw
  global uet_account5
  global uet_account5_n
  uet_update_accounts()
  uet_u_a_5 = uet_unlock(uet_account5, uet_account5pw, uet_unlockuet)
  if uet_u_a_5 == False:
    if uet_account5pw == '':
     uet_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account5_n+' Passphrase Denied: '+uet_account5pw_r)
    elif uet_account5pw != '':
     print('Unlock Failure With Account '+uet_account5_n+' Passphrase Denied: '+uet_account5pw)
  if uet_u_a_5 == True:
   print(uet_account5_n+' Unlocked')

def uet_unlock_account_6():
  global uet_account6pw
  global uet_account6
  global uet_account6_n
  uet_update_accounts()
  uet_u_a_6 = uet_unlock(uet_account6, uet_account6pw, uet_unlockuet)
  if uet_u_a_6 == False:
    if uet_account6pw == '':
     uet_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+uet_account6_n+' Passphrase Denied: '+uet_account6pw_r)
    elif uet_account6pw != '':
     print('Unlock Failure With Account '+uet_account6_n+' Passphrase Denied: '+uet_account6pw)
  if uet_u_a_6 == True:
   print(uet_account6_n+' Unlocked')

def uet_unlock_account(uet_ua_accountNumber):
 uet_update_accounts()
 uet_ua_account_number = uet_ua_accountNumber
 uet_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if uet_ua_account_number == uet_ua_input[0]:
  uet_unlock_account_0()
 if uet_ua_account_number == uet_ua_input[1]:
  uet_unlock_account_1()
 if uet_ua_account_number == uet_ua_input[2]:
  uet_unlock_account_2()
 if uet_ua_account_number == uet_ua_input[3]:
  uet_unlock_account_3()
 if uet_ua_account_number == uet_ua_input[4]:
  uet_unlock_account_4()
 if uet_ua_account_number == uet_ua_input[5]:
  uet_unlock_account_5()
 if uet_ua_account_number == uet_ua_input[6]:
  uet_unlock_account_6()
 if uet_ua_account_number not in uet_ua_input:
  print('Must Integer Within Range '+uet_accounts_range+'.')
 

def uet_approve_between_accounts(fromAccount, toAccount, msgValue):
  uet_update_accounts()
  uet_a_0 = uet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(uet_a_0)

def uet_approve(fromAccountNumber, toAddress, msgValue):
  uet_update_accounts()
  uet_unlock_account(fromAccountNumber)
  uet_a_1 = uet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(uet_a_1)

def uet_transfer_between_accounts(fromAccount, toAccount, msgValue):
  uet_update_accounts()
  uet_unlock_account(fromAccount)
  uet_t_0 = uet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(uet_t_0)

def uet_transfer(fromAccountNumber, toAddress, msgValue):
  uet_update_accounts()
  uet_unlock_account(fromAccountNumber)
  uet_t_1 = uet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(uet_t_1)

def uet_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  uet_update_accounts()
  uet_unlock_account(callAccount)
  uet_tf_0 = uet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(uet_tf_0)

def uet_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  uet_update_accounts()
  uet_unlock_account(callAccount)
  uet_tf_1 = uet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(uet_tf_1)
  


def uet_help():
  print('Following Functions For '+uet_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * uet_unlock => web3.personal.unlockAccount
/ * uet_accounts => web3.personal.listAccounts
/ * uet_balance = web3.eth.getBalance
** uet => web3.eth.contract(abi=uet_abi, address=uet_address)
** / * uet_balanceOf => uet.call().balanceOf

~ Function Listing Below:
~ uet_update_accounts()
~ uet_update_balances() \n\r -- => uet_update_accounts()
~ uet_list_all_accounts() \n\r -- => uet_update_accounts()
~ uet_account_balance(accountNumber) \n\r -- => uet_update_balances() 
~ uet_list_all_account_balances() \n\r -- => uet_update_balances()
~ uet_unlock_all_accounts() \n\r -- => uet_unlock_account_0() \n\r -- => uet_unlock_account_1() \n\r -- => uet_unlock_account_2() \n\r -- => uet_unlock_account_3() \n\r -- => uet_unlock_account_4() \n\r -- => uet_unlock_account_5() \n\r -- => uet_unlock_account_6() 
~ uet_unlock_account_0() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account0, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_1() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account1, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_2() \n\r -- => uet_update_accounts() \n\r --/ *uet_w_unlock(uet_account2, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_3() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account3, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_4() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account4, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_5() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account5, uet_account0pw, uet_unlockuet)
~ uet_unlock_account_6() \n\r -- => uet_update_accounts() \n\r -- / *uet_w_unlock(uet_account6, uet_account0pw, uet_unlockuet)
~ uet_unlock_account(uet_ua_accountNumber) \n\r -- => uet_update_accounts() \n\r -- // uet_unlock_account_0() \n\r -- // uet_unlock_account_1() \n\r -- // uet_unlock_account_2() \n\r -- // uet_unlock_account_3() \n\r -- // uet_unlock_account_4() \n\r -- // uet_unlock_account_5() \n\r -- // uet_unlock_account_6()
~ uet_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(fromAccount) \n\r -- / ** uet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ uet_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(fromAccountNumber) \n\r -- / ** uet.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ uet_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(fromAccount) \n\r -- / ** uet.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ uet_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(fromAccountNumber) \n\r -- / ** uet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ uet_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(callAccount) \n\r / ** uet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ uet_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => uet_update_accounts() \n\r -- => uet_unlock_account(callAccount) \n\r -- / ** uet.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ uet_help() <-- You Are Here. ''')