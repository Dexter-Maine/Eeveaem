#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global cfi_account_0_a
global cfi_account_1_a
global cfi_account_2_a
global cfi_account_3_a
global cfi_account_4_a
global cfi_account_5_a
global cfi_account_6_a
global cfi_address
global cfi_abi
global cfi
global cfi_call_0
global cfi_call_1
global cfi_call_2
global cfi_call_3
global cfi_call_4
global cfi_call_5
global cfi_call_6
global cfi_call_ab
global cfi_accounts
global cfi_account_0_pw
global cfi_account_1_pw
global cfi_account_2_pw
global cfi_account_3_pw
global cfi_account_4_pw
global cfi_account_5_pw
global cfi_account_6_pw
global cfi_account_0_n
global cfi_account_1_n
global cfi_account_2_n
global cfi_account_3_n
global cfi_account_4_n
global cfi_account_5_n
global cfi_account_6_n
global cfi_account1pw
global cfi_account2pw
global cfi_account3pw
global cfi_account4pw
global cfi_account5pw
global cfi_account6pw
global cfi_last_price
global cfi_accounts_range
global cfi_tokenName
global cfi_last_ethereum_price
global cfi_unlockTime
global cfi_balance
global cfi_balanceOf
global cfi_unlock
global cfi_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
cfi_token_d = 1e18
_e_d = 1e18
cfi_accounts_range = '[0, 6]'
cfi_unlock = web3.personal.unlockAccount
cfi_last_ethereum_price = 370.00
cfi_last_price = 0.25
cfi_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
cfi_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
cfi_tokenName = 'Cofound.it Token'
cfi_unlockTime = hex(10000) # Must be hex()
cfi_account_0_a = cfi_accounts[0]
cfi_account_1_a = cfi_accounts[1]
cfi_account_2_a = cfi_accounts[2]
cfi_account_3_a = cfi_accounts[3]
cfi_account_4_a = cfi_accounts[4]
cfi_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
cfi_account_6_a = cfi_accounts[6]
# Supply Unlock Passwords For Transactions Below
cfi_account_0_pw = 'GuildSkrypt2017!@#'
cfi_account_1_pw = ''
cfi_account_2_pw = 'GuildSkrypt2017!@#'
cfi_account_3_pw = ''
cfi_account_4_pw = ''
cfi_account_5_pw = ''
cfi_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
cfi_account_0_n = 'Skotys Bittrex Account'
cfi_account_1_n = 'Jeffs Account'
cfi_account_2_n = 'Skrypts Bittrex Account'
cfi_account_3_n = 'Skotys Personal Account'
cfi_account_4_n = 'Unknown'
cfi_account_5_n = 'Watched \'Bittrex\' Account.'
cfi_account_6_n = 'Watched Account (1)'
# Contract Information Below :
cfi_address = '0x12FEF5e57bF45873Cd9B62E9DBd7BFb99e32D73e'
cfi_abi = [{"constant":true,"inputs":[{"name":"_querryAddress","type":"address"}],"name":"isRestrictedAddress","outputs":[{"name":"answer","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newRestrictedAddress","type":"address"}],"name":"editRestrictedAddress","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFrozenUntilBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"icoContractAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_frozenUntilBlock","type":"uint256"},{"name":"_reason","type":"string"}],"name":"freezeTransfersUntil","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_reason","type":"string"}],"name":"mintTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_icoAddress","type":"address"}],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_frozenUntilBlock","type":"uint256"},{"indexed":false,"name":"_reason","type":"string"}],"name":"TokenFrozen","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
cfi = web3.eth.contract(abi=cfi_abi, address=cfi_address)
cfi_balanceOf = cfi.call().balanceOf
# End Contract Information
def cfi_update_accounts():
 global cfi_account0
 global cfi_account1
 global cfi_account2
 global cfi_account3
 global cfi_account4
 global cfi_account5
 global cfi_account6
 global cfi_account0_n
 global cfi_account1_n
 global cfi_account2_n
 global cfi_account3_n
 global cfi_account4_n
 global cfi_account5_n
 global cfi_account6_n
 global cfi_account0pw
 global cfi_account1pw
 global cfi_account2pw
 global cfi_account3pw
 global cfi_account4pw
 global cfi_account5pw
 global cfi_account6pw
 cfi_account0 = cfi_account_0_a
 cfi_account1 = cfi_account_1_a
 cfi_account2 = cfi_account_2_a
 cfi_account3 = cfi_account_3_a
 cfi_account4 = cfi_account_4_a
 cfi_account5 = cfi_account_5_a
 cfi_account6 = cfi_account_6_a
 cfi_account0_n = cfi_account_0_n
 cfi_account1_n = cfi_account_1_n
 cfi_account2_n = cfi_account_2_n
 cfi_account3_n = cfi_account_3_n
 cfi_account4_n = cfi_account_4_n
 cfi_account5_n = cfi_account_5_n
 cfi_account6_n = cfi_account_6_n
 cfi_account0pw = cfi_account_0_pw
 cfi_account1pw = cfi_account_1_pw
 cfi_account2pw = cfi_account_2_pw
 cfi_account3pw = cfi_account_3_pw
 cfi_account4pw = cfi_account_4_pw
 cfi_account5pw = cfi_account_5_pw
 cfi_account6pw = cfi_account_6_pw
 print(cfi_tokenName+' Accounts Updated.')
def cfi_update_balances():
 global cfi_call_0
 global cfi_call_1
 global cfi_call_2
 global cfi_call_3
 global cfi_call_4
 global cfi_call_5
 global cfi_call_6
 global cfi_w_call_0
 global cfi_w_call_1
 global cfi_w_call_2
 global cfi_w_call_3
 global cfi_w_call_4
 global cfi_w_call_5
 global cfi_w_call_6
 cfi_update_accounts()
 print('Updating '+cfi_tokenName+' Balances Please Wait...')
 cfi_call_0 = cfi_balanceOf(cfi_account0)
 cfi_call_1 = cfi_balanceOf(cfi_account1)
 cfi_call_2 = cfi_balanceOf(cfi_account2)
 cfi_call_3 = cfi_balanceOf(cfi_account3)
 cfi_call_4 = cfi_balanceOf(cfi_account4)
 cfi_call_5 = cfi_balanceOf(cfi_account5)
 cfi_call_6 = cfi_balanceOf(cfi_account6)
 cfi_w_call_0 = cfi_balance(cfi_account0)
 cfi_w_call_1 = cfi_balance(cfi_account1)
 cfi_w_call_2 = cfi_balance(cfi_account2)
 cfi_w_call_3 = cfi_balance(cfi_account3)
 cfi_w_call_4 = cfi_balance(cfi_account4)
 cfi_w_call_5 = cfi_balance(cfi_account5)
 cfi_w_call_6 = cfi_balance(cfi_account6)
 print(cfi_tokenName+' Balances Updated.')
def cfi_list_all_accounts():
 cfi_update_accounts()
 print(cfi_tokenName+' '+cfi_account0_n+': '+cfi_account0)
 print(cfi_tokenName+' '+cfi_account1_n+': '+cfi_account1)
 print(cfi_tokenName+' '+cfi_account2_n+': '+cfi_account2)
 print(cfi_tokenName+' '+cfi_account3_n+': '+cfi_account3)
 print(cfi_tokenName+' '+cfi_account4_n+': '+cfi_account4)
 print(cfi_tokenName+' '+cfi_account5_n+': '+cfi_account5)
 print(cfi_tokenName+' '+cfi_account6_n+': '+cfi_account6)

def cfi_account_balance(accountNumber):
 cfi_update_balances()
 cfi_ab_account_number = accountNumber
 cfi_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if cfi_ab_account_number == cfi_ab_input[0]:
  print('Calling '+cfi_account0_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account0_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_0 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_0 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[1]:
  print('Calling '+cfi_account1_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account1_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_1 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_1 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[2]:
  print('Calling '+cfi_account2_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account2_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_2 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_2 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[3]:
  print('Calling '+cfi_account3_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account3_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_3 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_3 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[4]:
  print('Calling '+cfi_account4_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account4_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_4 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_4 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[5]:
  print('Calling '+cfi_account5_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account5_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_5 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_5 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number == cfi_ab_input[6]:
  print('Calling '+cfi_account6_n+' '+cfi_tokenName+' Balance: ')
  print(cfi_account6_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_6 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_6 / cfi_token_d * cfi_last_price))
 if cfi_ab_account_number not in cfi_ab_input:
  print('Must Integer Within Range '+cfi_accounts_range+'.')

def cfi_list_all_account_balances():
 cfi_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+cfi_tokenName+' Balance: ')
 print(cfi_account0_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_0 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_0 / cfi_token_d * cfi_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(cfi_account0_n+': Ethereum Balance '+str(cfi_w_call_0 / _e_d)+' $'+str(cfi_w_call_0 / _e_d * cfi_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+cfi_tokenName+' Balance: ')
 print(cfi_account1_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_1 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_1 / cfi_token_d * cfi_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(cfi_account1_n+': Ethereum Balance '+str(cfi_w_call_1 / _e_d)+' $'+str(cfi_w_call_1 / _e_d * cfi_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+cfi_tokenName+' Balance: ')
 print(cfi_account2_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_2 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_2 / cfi_token_d * cfi_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(cfi_account2_n+': Ethereum Balance '+str(cfi_w_call_2 / _e_d)+' $'+str(cfi_w_call_2 / _e_d * cfi_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+cfi_tokenName+' Balance: ')
 print(cfi_account3_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_3 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_3 / cfi_token_d * cfi_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(cfi_account3_n+': Ethereum Balance '+str(cfi_w_call_3 / _e_d)+' $'+str(cfi_w_call_3 / _e_d * cfi_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+cfi_tokenName+' Balance: ')
 print(cfi_account4_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_4 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_4 / cfi_token_d * cfi_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(cfi_account4_n+': Ethereum Balance '+str(cfi_w_call_4 / _e_d)+' $'+str(cfi_w_call_4 / _e_d * cfi_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+cfi_tokenName+' Balance: ')
 print(cfi_account5_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_5 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_5 / cfi_token_d * cfi_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(cfi_account5_n+': Ethereum Balance '+str(cfi_w_call_5 / _e_d)+' $'+str(cfi_w_call_5 /_e_d * cfi_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+cfi_tokenName+' Balance: ')
 print(cfi_account6_n+': '+cfi_tokenName+' Balance: '+str(cfi_call_6 / cfi_token_d)+' Usd/'+cfi_tokenName+' Balance: $'+str(cfi_call_6 / cfi_token_d * cfi_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(cfi_account6_n+': Ethereum Balance '+str(cfi_w_call_6 / _e_d)+' $'+str(cfi_w_call_6 / _e_d * cfi_last_ethereum_price))
def cfi_unlock_all_accounts():
  cfi_unlock_account_0()
  cfi_unlock_account_1()
  cfi_unlock_account_2()
  cfi_unlock_account_3()
  cfi_unlock_account_4()
  cfi_unlock_account_5()
  cfi_unlock_account_6()


def cfi_unlock_account_0():
  global cfi_account0pw
  global cfi_account0
  global cfi_account0_n
  cfi_update_accounts()
  cfi_u_a_0 = cfi_w_unlock(cfi_account0, cfi_account0pw, cfi_unlockTime)
  if cfi_u_a_0 == False:
    if cfi_account0pw == '':
     cfi_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account0_n+' Passphrase Denied: '+cfi_account0pw_r)
    elif cfi_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+cfi_account0_n+' Passphrase Denied: '+cfi_account0pw)
  if cfi_u_a_0 == True:
   print(cfi_account0_n+' Unlocked')

def cfi_unlock_account_1():
  global cfi_account1pw
  global cfi_account1
  global cfi_account1_n
  cfi_update_accounts()
  cfi_u_a_1 = cfi_unlock(cfi_account1, cfi_account1pw, cfi_unlockTime)
  if cfi_u_a_1 == False:
    if cfi_account1pw == '':
     cfi_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account1_n+' Passphrase Denied: '+cfi_account1pw_r)
    elif cfi_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+cfi_account1_n+' Passphrase Denied: '+cfi_account1pw)
  if cfi_u_a_1 == True:
   print(cfi_account1_n+' Unlocked')

def cfi_unlock_account_2():
  global cfi_account2pw
  global cfi_account2
  global cfi_account2_n
  cfi_update_accounts()
  cfi_u_a_2 = cfi_unlock(cfi_account2, cfi_account2pw, cfi_unlockTime)
  if cfi_u_a_2 == False:
    if cfi_account2pw == '':
     cfi_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account2_n+' Passphrase Denied: '+cfi_account2pw_r)
    elif cfi_account2pw != '':
     print('Unlock Failure With Account '+cfi_account2_n+' Passphrase Denied: '+cfi_account2pw)
  if cfi_u_a_2 == True:
   print(cfi_account2_n+' Unlocked')

def cfi_unlock_account_3():
  global cfi_account3pw
  global cfi_account3
  global cfi_account3_n
  cfi_update_accounts()
  cfi_u_a_3 = cfi_unlock(cfi_account3, cfi_account3pw, cfi_unlockTime)
  if cfi_u_a_3 == False:
    if cfi_account3pw == '':
     cfi_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account3_n+' Passphrase Denied: '+cfi_account3pw_r)
    elif cfi_account3pw != '':
     print('Unlock Failure With Account '+cfi_account3_n+' Passphrase Denied: '+cfi_account3pw)
  if cfi_u_a_3 == True:
   print(cfi_account3_n+' Unlocked')

def cfi_unlock_account_4():
  global cfi_account4pw
  global cfi_account4
  global cfi_account4_n
  cfi_update_accounts()
  cfi_u_a_4 = cfi_unlock(cfi_account4, cfi_account4pw, cfi_unlockTime)
  if cfi_u_a_4 == False:
    if cfi_account4pw == '':
     cfi_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account4_n+' Passphrase Denied: '+cfi_account4pw_r)
    elif cfi_account4pw != '':
     print('Unlock Failure With Account '+cfi_account4_n+' Passphrase Denied: '+cfi_account4pw)
  if cfi_u_a_4 == True:
   print(cfi_account4_n+' Unlocked')

def cfi_unlock_account_5():
  global cfi_account5pw
  global cfi_account5
  global cfi_account5_n
  cfi_update_accounts()
  cfi_u_a_5 = cfi_unlock(cfi_account5, cfi_account5pw, cfi_unlockTime)
  if cfi_u_a_5 == False:
    if cfi_account5pw == '':
     cfi_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account5_n+' Passphrase Denied: '+cfi_account5pw_r)
    elif cfi_account5pw != '':
     print('Unlock Failure With Account '+cfi_account5_n+' Passphrase Denied: '+cfi_account5pw)
  if cfi_u_a_5 == True:
   print(cfi_account5_n+' Unlocked')

def cfi_unlock_account_6():
  global cfi_account6pw
  global cfi_account6
  global cfi_account6_n
  cfi_update_accounts()
  cfi_u_a_6 = cfi_unlock(cfi_account6, cfi_account6pw, cfi_unlockTime)
  if cfi_u_a_6 == False:
    if cfi_account6pw == '':
     cfi_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cfi_account6_n+' Passphrase Denied: '+cfi_account6pw_r)
    elif cfi_account6pw != '':
     print('Unlock Failure With Account '+cfi_account6_n+' Passphrase Denied: '+cfi_account6pw)
  if cfi_u_a_6 == True:
   print(cfi_account6_n+' Unlocked')

def cfi_unlock_account(cfi_ua_accountNumber):
 cfi_update_accounts()
 cfi_ua_account_number = cfi_ua_accountNumber
 cfi_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if cfi_ua_account_number == cfi_ua_input[0]:
  cfi_unlock_account_0()
 if cfi_ua_account_number == cfi_ua_input[1]:
  cfi_unlock_account_1()
 if cfi_ua_account_number == cfi_ua_input[2]:
  cfi_unlock_account_2()
 if cfi_ua_account_number == cfi_ua_input[3]:
  cfi_unlock_account_3()
 if cfi_ua_account_number == cfi_ua_input[4]:
  cfi_unlock_account_4()
 if cfi_ua_account_number == cfi_ua_input[5]:
  cfi_unlock_account_5()
 if cfi_ua_account_number == cfi_ua_input[6]:
  cfi_unlock_account_6()
 if cfi_ua_account_number not in cfi_ua_input:
  print('Must Integer Within Range '+cfi_accounts_range+'.')
 

def cfi_approve_between_accounts(fromAccount, toAccount, msgValue):
  cfi_update_accounts()
  cfi_a_0 = cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(cfi_a_0)

def cfi_approve(fromAccountNumber, toAddress, msgValue):
  cfi_update_accounts()
  cfi_unlock_account(fromAccountNumber)
  cfi_a_1 = cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(cfi_a_1)

def cfi_transfer_between_accounts(fromAccount, toAccount, msgValue):
  cfi_update_accounts()
  cfi_unlock_account(fromAccount)
  cfi_t_0 = cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(cfi_t_0)

def cfi_transfer(fromAccountNumber, toAddress, msgValue):
  cfi_update_accounts()
  cfi_unlock_account(fromAccountNumber)
  cfi_t_1 = cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(cfi_t_1)

def cfi_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  cfi_update_accounts()
  cfi_unlock_account(callAccount)
  cfi_tf_0 = cfi.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(cfi_tf_0)

def cfi_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  cfi_update_accounts()
  cfi_unlock_account(callAccount)
  cfi_tf_1 = cfi.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(cfi_tf_1)
  


def cfi_help():
  print('Following Functions For '+cfi_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * cfi_unlock => web3.personal.unlockAccount
/ * cfi_accounts => web3.personal.listAccounts
/ * cfi_balance = web3.eth.getBalance
** cfi => web3.eth.contract(abi=cfi_abi, address=cfi_address)
** / * cfi_balanceOf => cfi.call().balanceOf

~ Function Listing Below:
~ cfi_update_accounts()
~ cfi_update_balances() \n\r -- => cfi_update_accounts()
~ cfi_list_all_accounts() \n\r -- => cfi_update_accounts()
~ cfi_account_balance(accountNumber) \n\r -- => cfi_update_balances() 
~ cfi_list_all_account_balances() \n\r -- => cfi_update_balances()
~ cfi_unlock_all_accounts() \n\r -- => cfi_unlock_account_0() \n\r -- => cfi_unlock_account_1() \n\r -- => cfi_unlock_account_2() \n\r -- => cfi_unlock_account_3() \n\r -- => cfi_unlock_account_4() \n\r -- => cfi_unlock_account_5() \n\r -- => cfi_unlock_account_6() 
~ cfi_unlock_account_0() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account0, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_1() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account1, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_2() \n\r -- => cfi_update_accounts() \n\r --/ *cfi_w_unlock(cfi_account2, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_3() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account3, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_4() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account4, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_5() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account5, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account_6() \n\r -- => cfi_update_accounts() \n\r -- / *cfi_w_unlock(cfi_account6, cfi_account0pw, cfi_unlockTime)
~ cfi_unlock_account(cfi_ua_accountNumber) \n\r -- => cfi_update_accounts() \n\r -- // cfi_unlock_account_0() \n\r -- // cfi_unlock_account_1() \n\r -- // cfi_unlock_account_2() \n\r -- // cfi_unlock_account_3() \n\r -- // cfi_unlock_account_4() \n\r -- // cfi_unlock_account_5() \n\r -- // cfi_unlock_account_6()
~ cfi_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(fromAccount) \n\r -- / ** cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ cfi_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(fromAccountNumber) \n\r -- / ** cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ cfi_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(fromAccount) \n\r -- / ** cfi.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ cfi_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(fromAccountNumber) \n\r -- / ** cfi.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ cfi_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(callAccount) \n\r / ** cfi.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ cfi_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => cfi_update_accounts() \n\r -- => cfi_unlock_account(callAccount) \n\r -- / ** cfi.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ cfi_help() <-- You Are Here. ''')