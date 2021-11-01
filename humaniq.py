#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global hmq_account_0_a
global hmq_account_1_a
global hmq_account_2_a
global hmq_account_3_a
global hmq_account_4_a
global hmq_account_5_a
global hmq_account_6_a
global hmq_address
global hmq_abi
global hmq
global hmq_call_0
global hmq_call_1
global hmq_call_2
global hmq_call_3
global hmq_call_4
global hmq_call_5
global hmq_call_6
global hmq_call_ab
global hmq_accounts
global hmq_account_0_pw
global hmq_account_1_pw
global hmq_account_2_pw
global hmq_account_3_pw
global hmq_account_4_pw
global hmq_account_5_pw
global hmq_account_6_pw
global hmq_account_0_n
global hmq_account_1_n
global hmq_account_2_n
global hmq_account_3_n
global hmq_account_4_n
global hmq_account_5_n
global hmq_account_6_n
global hmq_account1pw
global hmq_account2pw
global hmq_account3pw
global hmq_account4pw
global hmq_account5pw
global hmq_account6pw
global hmq_last_price
global hmq_accounts_range
global hmq_tokenName
global hmq_last_ethereum_price
global hmq_unlockTime
global hmq_balance
global hmq_balanceOf
global hmq_unlock
global hmq_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
hmq_token_d = 1e8
_e_d = 1e18
hmq_accounts_range = '[0, 6]'
hmq_unlock = web3.personal.unlockAccount
hmq_last_ethereum_price = 370.00
hmq_last_price = 0.16
hmq_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
hmq_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
hmq_tokenName = 'Humaniq Token'
hmq_unlockTime = hex(10000) # Must be hex()
hmq_account_0_a = hmq_accounts[0]
hmq_account_1_a = hmq_accounts[1]
hmq_account_2_a = hmq_accounts[2]
hmq_account_3_a = hmq_accounts[3]
hmq_account_4_a = hmq_accounts[4]
hmq_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
hmq_account_6_a = hmq_accounts[6]
# Supply Unlock Passwords For Transactions Below
hmq_account_0_pw = 'GuildSkrypt2017!@#'
hmq_account_1_pw = ''
hmq_account_2_pw = 'GuildSkrypt2017!@#'
hmq_account_3_pw = ''
hmq_account_4_pw = ''
hmq_account_5_pw = ''
hmq_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
hmq_account_0_n = 'Skotys Bittrex Account'
hmq_account_1_n = 'Jeffs Account'
hmq_account_2_n = 'Skrypts Bittrex Account'
hmq_account_3_n = 'Skotys Personal Account'
hmq_account_4_n = 'Unknown'
hmq_account_5_n = 'Watched \'Bittrex\' Account.'
hmq_account_6_n = 'Watched Account (1)'
# Contract Information Below :
hmq_address = '0xcbCC0F036ED4788F63FC0fEE32873d6A7487b908'
hmq_abi = [{"constant":true,"inputs":[],"name":"preICOSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minter","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"allocationAddressPreICO","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ICOSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newAddress","type":"address"}],"name":"changeMultisig","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"maxTotalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newAddress","type":"address"}],"name":"changeMinter","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_for","type":"address"},{"name":"tokenCount","type":"uint256"}],"name":"issueTokens","outputs":[{"name":"","type":"bool"}],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"multisig","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"founder","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"allocationAddressICO","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newAddress","type":"address"}],"name":"changeFounder","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"founderAddress","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Issuance","type":"event"}]
hmq = web3.eth.contract(abi=hmq_abi, address=hmq_address)
hmq_balanceOf = hmq.call().balanceOf
# End Contract Information
def hmq_update_accounts():
 global hmq_account0
 global hmq_account1
 global hmq_account2
 global hmq_account3
 global hmq_account4
 global hmq_account5
 global hmq_account6
 global hmq_account0_n
 global hmq_account1_n
 global hmq_account2_n
 global hmq_account3_n
 global hmq_account4_n
 global hmq_account5_n
 global hmq_account6_n
 global hmq_account0pw
 global hmq_account1pw
 global hmq_account2pw
 global hmq_account3pw
 global hmq_account4pw
 global hmq_account5pw
 global hmq_account6pw
 hmq_account0 = hmq_account_0_a
 hmq_account1 = hmq_account_1_a
 hmq_account2 = hmq_account_2_a
 hmq_account3 = hmq_account_3_a
 hmq_account4 = hmq_account_4_a
 hmq_account5 = hmq_account_5_a
 hmq_account6 = hmq_account_6_a
 hmq_account0_n = hmq_account_0_n
 hmq_account1_n = hmq_account_1_n
 hmq_account2_n = hmq_account_2_n
 hmq_account3_n = hmq_account_3_n
 hmq_account4_n = hmq_account_4_n
 hmq_account5_n = hmq_account_5_n
 hmq_account6_n = hmq_account_6_n
 hmq_account0pw = hmq_account_0_pw
 hmq_account1pw = hmq_account_1_pw
 hmq_account2pw = hmq_account_2_pw
 hmq_account3pw = hmq_account_3_pw
 hmq_account4pw = hmq_account_4_pw
 hmq_account5pw = hmq_account_5_pw
 hmq_account6pw = hmq_account_6_pw
 print(hmq_tokenName+' Accounts Updated.')
def hmq_update_balances():
 global hmq_call_0
 global hmq_call_1
 global hmq_call_2
 global hmq_call_3
 global hmq_call_4
 global hmq_call_5
 global hmq_call_6
 global hmq_w_call_0
 global hmq_w_call_1
 global hmq_w_call_2
 global hmq_w_call_3
 global hmq_w_call_4
 global hmq_w_call_5
 global hmq_w_call_6
 hmq_update_accounts()
 print('Updating '+hmq_tokenName+' Balances Please Wait...')
 hmq_call_0 = hmq_balanceOf(hmq_account0)
 hmq_call_1 = hmq_balanceOf(hmq_account1)
 hmq_call_2 = hmq_balanceOf(hmq_account2)
 hmq_call_3 = hmq_balanceOf(hmq_account3)
 hmq_call_4 = hmq_balanceOf(hmq_account4)
 hmq_call_5 = hmq_balanceOf(hmq_account5)
 hmq_call_6 = hmq_balanceOf(hmq_account6)
 hmq_w_call_0 = hmq_balance(hmq_account0)
 hmq_w_call_1 = hmq_balance(hmq_account1)
 hmq_w_call_2 = hmq_balance(hmq_account2)
 hmq_w_call_3 = hmq_balance(hmq_account3)
 hmq_w_call_4 = hmq_balance(hmq_account4)
 hmq_w_call_5 = hmq_balance(hmq_account5)
 hmq_w_call_6 = hmq_balance(hmq_account6)
 print(hmq_tokenName+' Balances Updated.')
def hmq_list_all_accounts():
 hmq_update_accounts()
 print(hmq_tokenName+' '+hmq_account0_n+': '+hmq_account0)
 print(hmq_tokenName+' '+hmq_account1_n+': '+hmq_account1)
 print(hmq_tokenName+' '+hmq_account2_n+': '+hmq_account2)
 print(hmq_tokenName+' '+hmq_account3_n+': '+hmq_account3)
 print(hmq_tokenName+' '+hmq_account4_n+': '+hmq_account4)
 print(hmq_tokenName+' '+hmq_account5_n+': '+hmq_account5)
 print(hmq_tokenName+' '+hmq_account6_n+': '+hmq_account6)

def hmq_account_balance(accountNumber):
 hmq_update_balances()
 hmq_ab_account_number = accountNumber
 hmq_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if hmq_ab_account_number == hmq_ab_input[0]:
  print('Calling '+hmq_account0_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account0_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_0 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_0 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[1]:
  print('Calling '+hmq_account1_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account1_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_1 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_1 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[2]:
  print('Calling '+hmq_account2_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account2_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_2 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_2 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[3]:
  print('Calling '+hmq_account3_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account3_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_3 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_3 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[4]:
  print('Calling '+hmq_account4_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account4_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_4 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_4 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[5]:
  print('Calling '+hmq_account5_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account5_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_5 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_5 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number == hmq_ab_input[6]:
  print('Calling '+hmq_account6_n+' '+hmq_tokenName+' Balance: ')
  print(hmq_account6_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_6 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_6 / hmq_token_d * hmq_last_price))
 if hmq_ab_account_number not in hmq_ab_input:
  print('Must Integer Within Range '+hmq_accounts_range+'.')

def hmq_list_all_account_balances():
 hmq_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+hmq_tokenName+' Balance: ')
 print(hmq_account0_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_0 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_0 / hmq_token_d * hmq_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(hmq_account0_n+': Ethereum Balance '+str(hmq_w_call_0 / _e_d)+' $'+str(hmq_w_call_0 / _e_d * hmq_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+hmq_tokenName+' Balance: ')
 print(hmq_account1_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_1 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_1 / hmq_token_d * hmq_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(hmq_account1_n+': Ethereum Balance '+str(hmq_w_call_1 / _e_d)+' $'+str(hmq_w_call_1 / _e_d * hmq_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+hmq_tokenName+' Balance: ')
 print(hmq_account2_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_2 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_2 / hmq_token_d * hmq_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(hmq_account2_n+': Ethereum Balance '+str(hmq_w_call_2 / _e_d)+' $'+str(hmq_w_call_2 / _e_d * hmq_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+hmq_tokenName+' Balance: ')
 print(hmq_account3_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_3 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_3 / hmq_token_d * hmq_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(hmq_account3_n+': Ethereum Balance '+str(hmq_w_call_3 / _e_d)+' $'+str(hmq_w_call_3 / _e_d * hmq_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+hmq_tokenName+' Balance: ')
 print(hmq_account4_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_4 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_4 / hmq_token_d * hmq_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(hmq_account4_n+': Ethereum Balance '+str(hmq_w_call_4 / _e_d)+' $'+str(hmq_w_call_4 / _e_d * hmq_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+hmq_tokenName+' Balance: ')
 print(hmq_account5_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_5 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_5 / hmq_token_d * hmq_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(hmq_account5_n+': Ethereum Balance '+str(hmq_w_call_5 / _e_d)+' $'+str(hmq_w_call_5 /_e_d * hmq_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+hmq_tokenName+' Balance: ')
 print(hmq_account6_n+': '+hmq_tokenName+' Balance: '+str(hmq_call_6 / hmq_token_d)+' Usd/'+hmq_tokenName+' Balance: $'+str(hmq_call_6 / hmq_token_d * hmq_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(hmq_account6_n+': Ethereum Balance '+str(hmq_w_call_6 / _e_d)+' $'+str(hmq_w_call_6 / _e_d * hmq_last_ethereum_price))
def hmq_unlock_all_accounts():
  hmq_unlock_account_0()
  hmq_unlock_account_1()
  hmq_unlock_account_2()
  hmq_unlock_account_3()
  hmq_unlock_account_4()
  hmq_unlock_account_5()
  hmq_unlock_account_6()


def hmq_unlock_account_0():
  global hmq_account0pw
  global hmq_account0
  global hmq_account0_n
  hmq_update_accounts()
  hmq_u_a_0 = hmq_w_unlock(hmq_account0, hmq_account0pw, hmq_unlockTime)
  if hmq_u_a_0 == False:
    if hmq_account0pw == '':
     hmq_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account0_n+' Passphrase Denied: '+hmq_account0pw_r)
    elif hmq_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+hmq_account0_n+' Passphrase Denied: '+hmq_account0pw)
  if hmq_u_a_0 == True:
   print(hmq_account0_n+' Unlocked')

def hmq_unlock_account_1():
  global hmq_account1pw
  global hmq_account1
  global hmq_account1_n
  hmq_update_accounts()
  hmq_u_a_1 = hmq_unlock(hmq_account1, hmq_account1pw, hmq_unlockTime)
  if hmq_u_a_1 == False:
    if hmq_account1pw == '':
     hmq_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account1_n+' Passphrase Denied: '+hmq_account1pw_r)
    elif hmq_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+hmq_account1_n+' Passphrase Denied: '+hmq_account1pw)
  if hmq_u_a_1 == True:
   print(hmq_account1_n+' Unlocked')

def hmq_unlock_account_2():
  global hmq_account2pw
  global hmq_account2
  global hmq_account2_n
  hmq_update_accounts()
  hmq_u_a_2 = hmq_unlock(hmq_account2, hmq_account2pw, hmq_unlockTime)
  if hmq_u_a_2 == False:
    if hmq_account2pw == '':
     hmq_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account2_n+' Passphrase Denied: '+hmq_account2pw_r)
    elif hmq_account2pw != '':
     print('Unlock Failure With Account '+hmq_account2_n+' Passphrase Denied: '+hmq_account2pw)
  if hmq_u_a_2 == True:
   print(hmq_account2_n+' Unlocked')

def hmq_unlock_account_3():
  global hmq_account3pw
  global hmq_account3
  global hmq_account3_n
  hmq_update_accounts()
  hmq_u_a_3 = hmq_unlock(hmq_account3, hmq_account3pw, hmq_unlockTime)
  if hmq_u_a_3 == False:
    if hmq_account3pw == '':
     hmq_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account3_n+' Passphrase Denied: '+hmq_account3pw_r)
    elif hmq_account3pw != '':
     print('Unlock Failure With Account '+hmq_account3_n+' Passphrase Denied: '+hmq_account3pw)
  if hmq_u_a_3 == True:
   print(hmq_account3_n+' Unlocked')

def hmq_unlock_account_4():
  global hmq_account4pw
  global hmq_account4
  global hmq_account4_n
  hmq_update_accounts()
  hmq_u_a_4 = hmq_unlock(hmq_account4, hmq_account4pw, hmq_unlockTime)
  if hmq_u_a_4 == False:
    if hmq_account4pw == '':
     hmq_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account4_n+' Passphrase Denied: '+hmq_account4pw_r)
    elif hmq_account4pw != '':
     print('Unlock Failure With Account '+hmq_account4_n+' Passphrase Denied: '+hmq_account4pw)
  if hmq_u_a_4 == True:
   print(hmq_account4_n+' Unlocked')

def hmq_unlock_account_5():
  global hmq_account5pw
  global hmq_account5
  global hmq_account5_n
  hmq_update_accounts()
  hmq_u_a_5 = hmq_unlock(hmq_account5, hmq_account5pw, hmq_unlockTime)
  if hmq_u_a_5 == False:
    if hmq_account5pw == '':
     hmq_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account5_n+' Passphrase Denied: '+hmq_account5pw_r)
    elif hmq_account5pw != '':
     print('Unlock Failure With Account '+hmq_account5_n+' Passphrase Denied: '+hmq_account5pw)
  if hmq_u_a_5 == True:
   print(hmq_account5_n+' Unlocked')

def hmq_unlock_account_6():
  global hmq_account6pw
  global hmq_account6
  global hmq_account6_n
  hmq_update_accounts()
  hmq_u_a_6 = hmq_unlock(hmq_account6, hmq_account6pw, hmq_unlockTime)
  if hmq_u_a_6 == False:
    if hmq_account6pw == '':
     hmq_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+hmq_account6_n+' Passphrase Denied: '+hmq_account6pw_r)
    elif hmq_account6pw != '':
     print('Unlock Failure With Account '+hmq_account6_n+' Passphrase Denied: '+hmq_account6pw)
  if hmq_u_a_6 == True:
   print(hmq_account6_n+' Unlocked')

def hmq_unlock_account(hmq_ua_accountNumber):
 hmq_update_accounts()
 hmq_ua_account_number = hmq_ua_accountNumber
 hmq_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if hmq_ua_account_number == hmq_ua_input[0]:
  hmq_unlock_account_0()
 if hmq_ua_account_number == hmq_ua_input[1]:
  hmq_unlock_account_1()
 if hmq_ua_account_number == hmq_ua_input[2]:
  hmq_unlock_account_2()
 if hmq_ua_account_number == hmq_ua_input[3]:
  hmq_unlock_account_3()
 if hmq_ua_account_number == hmq_ua_input[4]:
  hmq_unlock_account_4()
 if hmq_ua_account_number == hmq_ua_input[5]:
  hmq_unlock_account_5()
 if hmq_ua_account_number == hmq_ua_input[6]:
  hmq_unlock_account_6()
 if hmq_ua_account_number not in hmq_ua_input:
  print('Must Integer Within Range '+hmq_accounts_range+'.')
 

def hmq_approve_between_accounts(fromAccount, toAccount, msgValue):
  hmq_update_accounts()
  hmq_a_0 = hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(hmq_a_0)

def hmq_approve(fromAccountNumber, toAddress, msgValue):
  hmq_update_accounts()
  hmq_unlock_account(fromAccountNumber)
  hmq_a_1 = hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(hmq_a_1)

def hmq_transfer_between_accounts(fromAccount, toAccount, msgValue):
  hmq_update_accounts()
  hmq_unlock_account(fromAccount)
  hmq_t_0 = hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(hmq_t_0)

def hmq_transfer(fromAccountNumber, toAddress, msgValue):
  hmq_update_accounts()
  hmq_unlock_account(fromAccountNumber)
  hmq_t_1 = hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(hmq_t_1)

def hmq_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  hmq_update_accounts()
  hmq_unlock_account(callAccount)
  hmq_tf_0 = hmq.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(hmq_tf_0)

def hmq_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  hmq_update_accounts()
  hmq_unlock_account(callAccount)
  hmq_tf_1 = hmq.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(hmq_tf_1)
  


def hmq_help():
  print('Following Functions For '+hmq_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * hmq_unlock => web3.personal.unlockAccount
/ * hmq_accounts => web3.personal.listAccounts
/ * hmq_balance = web3.eth.getBalance
** hmq => web3.eth.contract(abi=hmq_abi, address=hmq_address)
** / * hmq_balanceOf => hmq.call().balanceOf

~ Function Listing Below:
~ hmq_update_accounts()
~ hmq_update_balances() \n\r -- => hmq_update_accounts()
~ hmq_list_all_accounts() \n\r -- => hmq_update_accounts()
~ hmq_account_balance(accountNumber) \n\r -- => hmq_update_balances() 
~ hmq_list_all_account_balances() \n\r -- => hmq_update_balances()
~ hmq_unlock_all_accounts() \n\r -- => hmq_unlock_account_0() \n\r -- => hmq_unlock_account_1() \n\r -- => hmq_unlock_account_2() \n\r -- => hmq_unlock_account_3() \n\r -- => hmq_unlock_account_4() \n\r -- => hmq_unlock_account_5() \n\r -- => hmq_unlock_account_6() 
~ hmq_unlock_account_0() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account0, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_1() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account1, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_2() \n\r -- => hmq_update_accounts() \n\r --/ *hmq_w_unlock(hmq_account2, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_3() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account3, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_4() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account4, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_5() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account5, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account_6() \n\r -- => hmq_update_accounts() \n\r -- / *hmq_w_unlock(hmq_account6, hmq_account0pw, hmq_unlockTime)
~ hmq_unlock_account(hmq_ua_accountNumber) \n\r -- => hmq_update_accounts() \n\r -- // hmq_unlock_account_0() \n\r -- // hmq_unlock_account_1() \n\r -- // hmq_unlock_account_2() \n\r -- // hmq_unlock_account_3() \n\r -- // hmq_unlock_account_4() \n\r -- // hmq_unlock_account_5() \n\r -- // hmq_unlock_account_6()
~ hmq_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(fromAccount) \n\r -- / ** hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ hmq_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(fromAccountNumber) \n\r -- / ** hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ hmq_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(fromAccount) \n\r -- / ** hmq.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ hmq_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(fromAccountNumber) \n\r -- / ** hmq.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ hmq_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(callAccount) \n\r / ** hmq.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ hmq_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => hmq_update_accounts() \n\r -- => hmq_unlock_account(callAccount) \n\r -- / ** hmq.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ hmq_help() <-- You Are Here. ''')