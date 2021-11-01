#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global cvc_account_0_a
global cvc_account_1_a
global cvc_account_2_a
global cvc_account_3_a
global cvc_account_4_a
global cvc_account_5_a
global cvc_account_6_a
global cvc_address
global cvc_abi
global cvc
global cvc_call_0
global cvc_call_1
global cvc_call_2
global cvc_call_3
global cvc_call_4
global cvc_call_5
global cvc_call_6
global cvc_call_ab
global cvc_accounts
global cvc_account_0_pw
global cvc_account_1_pw
global cvc_account_2_pw
global cvc_account_3_pw
global cvc_account_4_pw
global cvc_account_5_pw
global cvc_account_6_pw
global cvc_account_0_n
global cvc_account_1_n
global cvc_account_2_n
global cvc_account_3_n
global cvc_account_4_n
global cvc_account_5_n
global cvc_account_6_n
global cvc_account1pw
global cvc_account2pw
global cvc_account3pw
global cvc_account4pw
global cvc_account5pw
global cvc_account6pw
global cvc_last_price
global cvc_accounts_range
global cvc_tokenName
global cvc_last_ethereum_price
global cvc_unlockTime
global cvc_balance
global cvc_balanceOf
global cvc_unlock
global cvc_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
cvc_token_d = 1e8
_e_d = 1e18
cvc_accounts_range = '[0, 6]'
cvc_unlock = web3.personal.unlockAccount
cvc_last_ethereum_price = 370.00
cvc_last_price = 0.49
cvc_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
cvc_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
cvc_tokenName = 'Civic Token'
cvc_unlockTime = hex(10000) # Must be hex()
cvc_account_0_a = cvc_accounts[0]
cvc_account_1_a = cvc_accounts[1]
cvc_account_2_a = cvc_accounts[2]
cvc_account_3_a = cvc_accounts[3]
cvc_account_4_a = cvc_accounts[4]
cvc_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
cvc_account_6_a = cvc_accounts[6]
# Supply Unlock Passwords For Transactions Below
cvc_account_0_pw = 'GuildSkrypt2017!@#'
cvc_account_1_pw = ''
cvc_account_2_pw = 'GuildSkrypt2017!@#'
cvc_account_3_pw = ''
cvc_account_4_pw = ''
cvc_account_5_pw = ''
cvc_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
cvc_account_0_n = 'Skotys Bittrex Account'
cvc_account_1_n = 'Jeffs Account'
cvc_account_2_n = 'Skrypts Bittrex Account'
cvc_account_3_n = 'Skotys Personal Account'
cvc_account_4_n = 'Unknown'
cvc_account_5_n = 'Watched \'Bittrex\' Account.'
cvc_account_6_n = 'Watched Account (1)'
# Contract Information Below :
cvc_address = '0x41e5560054824eA6B0732E656E3Ad64E20e94E45'
cvc_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"upgrade","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"}],"name":"setTokenInformation","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getUpgradeState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"canUpgrade","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalUpgraded","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"agent","type":"address"}],"name":"setUpgradeAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isToken","outputs":[{"name":"weAre","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"master","type":"address"}],"name":"setUpgradeMaster","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_owner","type":"address"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_totalSupply","type":"uint256"},{"name":"_decimals","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newName","type":"string"},{"indexed":false,"name":"newSymbol","type":"string"}],"name":"UpdatedTokenInformation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Upgrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"agent","type":"address"}],"name":"UpgradeAgentSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"upgradeMaster","type":"address"}],"name":"NewUpgradeMaster","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
cvc = web3.eth.contract(abi=cvc_abi, address=cvc_address)
cvc_balanceOf = cvc.call().balanceOf
# End Contract Information
def cvc_update_accounts():
 global cvc_account0
 global cvc_account1
 global cvc_account2
 global cvc_account3
 global cvc_account4
 global cvc_account5
 global cvc_account6
 global cvc_account0_n
 global cvc_account1_n
 global cvc_account2_n
 global cvc_account3_n
 global cvc_account4_n
 global cvc_account5_n
 global cvc_account6_n
 global cvc_account0pw
 global cvc_account1pw
 global cvc_account2pw
 global cvc_account3pw
 global cvc_account4pw
 global cvc_account5pw
 global cvc_account6pw
 cvc_account0 = cvc_account_0_a
 cvc_account1 = cvc_account_1_a
 cvc_account2 = cvc_account_2_a
 cvc_account3 = cvc_account_3_a
 cvc_account4 = cvc_account_4_a
 cvc_account5 = cvc_account_5_a
 cvc_account6 = cvc_account_6_a
 cvc_account0_n = cvc_account_0_n
 cvc_account1_n = cvc_account_1_n
 cvc_account2_n = cvc_account_2_n
 cvc_account3_n = cvc_account_3_n
 cvc_account4_n = cvc_account_4_n
 cvc_account5_n = cvc_account_5_n
 cvc_account6_n = cvc_account_6_n
 cvc_account0pw = cvc_account_0_pw
 cvc_account1pw = cvc_account_1_pw
 cvc_account2pw = cvc_account_2_pw
 cvc_account3pw = cvc_account_3_pw
 cvc_account4pw = cvc_account_4_pw
 cvc_account5pw = cvc_account_5_pw
 cvc_account6pw = cvc_account_6_pw
 print(cvc_tokenName+' Accounts Updated.')
def cvc_update_balances():
 global cvc_call_0
 global cvc_call_1
 global cvc_call_2
 global cvc_call_3
 global cvc_call_4
 global cvc_call_5
 global cvc_call_6
 global cvc_w_call_0
 global cvc_w_call_1
 global cvc_w_call_2
 global cvc_w_call_3
 global cvc_w_call_4
 global cvc_w_call_5
 global cvc_w_call_6
 cvc_update_accounts()
 print('Updating '+cvc_tokenName+' Balances Please Wait...')
 cvc_call_0 = cvc_balanceOf(cvc_account0)
 cvc_call_1 = cvc_balanceOf(cvc_account1)
 cvc_call_2 = cvc_balanceOf(cvc_account2)
 cvc_call_3 = cvc_balanceOf(cvc_account3)
 cvc_call_4 = cvc_balanceOf(cvc_account4)
 cvc_call_5 = cvc_balanceOf(cvc_account5)
 cvc_call_6 = cvc_balanceOf(cvc_account6)
 cvc_w_call_0 = cvc_balance(cvc_account0)
 cvc_w_call_1 = cvc_balance(cvc_account1)
 cvc_w_call_2 = cvc_balance(cvc_account2)
 cvc_w_call_3 = cvc_balance(cvc_account3)
 cvc_w_call_4 = cvc_balance(cvc_account4)
 cvc_w_call_5 = cvc_balance(cvc_account5)
 cvc_w_call_6 = cvc_balance(cvc_account6)
 print(cvc_tokenName+' Balances Updated.')
def cvc_list_all_accounts():
 cvc_update_accounts()
 print(cvc_tokenName+' '+cvc_account0_n+': '+cvc_account0)
 print(cvc_tokenName+' '+cvc_account1_n+': '+cvc_account1)
 print(cvc_tokenName+' '+cvc_account2_n+': '+cvc_account2)
 print(cvc_tokenName+' '+cvc_account3_n+': '+cvc_account3)
 print(cvc_tokenName+' '+cvc_account4_n+': '+cvc_account4)
 print(cvc_tokenName+' '+cvc_account5_n+': '+cvc_account5)
 print(cvc_tokenName+' '+cvc_account6_n+': '+cvc_account6)

def cvc_account_balance(accountNumber):
 cvc_update_balances()
 cvc_ab_account_number = accountNumber
 cvc_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if cvc_ab_account_number == cvc_ab_input[0]:
  print('Calling '+cvc_account0_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account0_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_0 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_0 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[1]:
  print('Calling '+cvc_account1_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account1_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_1 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_1 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[2]:
  print('Calling '+cvc_account2_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account2_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_2 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_2 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[3]:
  print('Calling '+cvc_account3_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account3_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_3 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_3 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[4]:
  print('Calling '+cvc_account4_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account4_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_4 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_4 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[5]:
  print('Calling '+cvc_account5_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account5_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_5 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_5 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number == cvc_ab_input[6]:
  print('Calling '+cvc_account6_n+' '+cvc_tokenName+' Balance: ')
  print(cvc_account6_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_6 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_6 / cvc_token_d * cvc_last_price))
 if cvc_ab_account_number not in cvc_ab_input:
  print('Must Integer Within Range '+cvc_accounts_range+'.')

def cvc_list_all_account_balances():
 cvc_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+cvc_tokenName+' Balance: ')
 print(cvc_account0_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_0 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_0 / cvc_token_d * cvc_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(cvc_account0_n+': Ethereum Balance '+str(cvc_w_call_0 / _e_d)+' $'+str(cvc_w_call_0 / _e_d * cvc_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+cvc_tokenName+' Balance: ')
 print(cvc_account1_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_1 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_1 / cvc_token_d * cvc_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(cvc_account1_n+': Ethereum Balance '+str(cvc_w_call_1 / _e_d)+' $'+str(cvc_w_call_1 / _e_d * cvc_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+cvc_tokenName+' Balance: ')
 print(cvc_account2_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_2 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_2 / cvc_token_d * cvc_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(cvc_account2_n+': Ethereum Balance '+str(cvc_w_call_2 / _e_d)+' $'+str(cvc_w_call_2 / _e_d * cvc_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+cvc_tokenName+' Balance: ')
 print(cvc_account3_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_3 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_3 / cvc_token_d * cvc_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(cvc_account3_n+': Ethereum Balance '+str(cvc_w_call_3 / _e_d)+' $'+str(cvc_w_call_3 / _e_d * cvc_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+cvc_tokenName+' Balance: ')
 print(cvc_account4_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_4 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_4 / cvc_token_d * cvc_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(cvc_account4_n+': Ethereum Balance '+str(cvc_w_call_4 / _e_d)+' $'+str(cvc_w_call_4 / _e_d * cvc_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+cvc_tokenName+' Balance: ')
 print(cvc_account5_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_5 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_5 / cvc_token_d * cvc_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(cvc_account5_n+': Ethereum Balance '+str(cvc_w_call_5 / _e_d)+' $'+str(cvc_w_call_5 /_e_d * cvc_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+cvc_tokenName+' Balance: ')
 print(cvc_account6_n+': '+cvc_tokenName+' Balance: '+str(cvc_call_6 / cvc_token_d)+' Usd/'+cvc_tokenName+' Balance: $'+str(cvc_call_6 / cvc_token_d * cvc_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(cvc_account6_n+': Ethereum Balance '+str(cvc_w_call_6 / _e_d)+' $'+str(cvc_w_call_6 / _e_d * cvc_last_ethereum_price))
def cvc_unlock_all_accounts():
  cvc_unlock_account_0()
  cvc_unlock_account_1()
  cvc_unlock_account_2()
  cvc_unlock_account_3()
  cvc_unlock_account_4()
  cvc_unlock_account_5()
  cvc_unlock_account_6()


def cvc_unlock_account_0():
  global cvc_account0pw
  global cvc_account0
  global cvc_account0_n
  cvc_update_accounts()
  cvc_u_a_0 = cvc_w_unlock(cvc_account0, cvc_account0pw, cvc_unlockTime)
  if cvc_u_a_0 == False:
    if cvc_account0pw == '':
     cvc_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account0_n+' Passphrase Denied: '+cvc_account0pw_r)
    elif cvc_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+cvc_account0_n+' Passphrase Denied: '+cvc_account0pw)
  if cvc_u_a_0 == True:
   print(cvc_account0_n+' Unlocked')

def cvc_unlock_account_1():
  global cvc_account1pw
  global cvc_account1
  global cvc_account1_n
  cvc_update_accounts()
  cvc_u_a_1 = cvc_unlock(cvc_account1, cvc_account1pw, cvc_unlockTime)
  if cvc_u_a_1 == False:
    if cvc_account1pw == '':
     cvc_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account1_n+' Passphrase Denied: '+cvc_account1pw_r)
    elif cvc_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+cvc_account1_n+' Passphrase Denied: '+cvc_account1pw)
  if cvc_u_a_1 == True:
   print(cvc_account1_n+' Unlocked')

def cvc_unlock_account_2():
  global cvc_account2pw
  global cvc_account2
  global cvc_account2_n
  cvc_update_accounts()
  cvc_u_a_2 = cvc_unlock(cvc_account2, cvc_account2pw, cvc_unlockTime)
  if cvc_u_a_2 == False:
    if cvc_account2pw == '':
     cvc_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account2_n+' Passphrase Denied: '+cvc_account2pw_r)
    elif cvc_account2pw != '':
     print('Unlock Failure With Account '+cvc_account2_n+' Passphrase Denied: '+cvc_account2pw)
  if cvc_u_a_2 == True:
   print(cvc_account2_n+' Unlocked')

def cvc_unlock_account_3():
  global cvc_account3pw
  global cvc_account3
  global cvc_account3_n
  cvc_update_accounts()
  cvc_u_a_3 = cvc_unlock(cvc_account3, cvc_account3pw, cvc_unlockTime)
  if cvc_u_a_3 == False:
    if cvc_account3pw == '':
     cvc_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account3_n+' Passphrase Denied: '+cvc_account3pw_r)
    elif cvc_account3pw != '':
     print('Unlock Failure With Account '+cvc_account3_n+' Passphrase Denied: '+cvc_account3pw)
  if cvc_u_a_3 == True:
   print(cvc_account3_n+' Unlocked')

def cvc_unlock_account_4():
  global cvc_account4pw
  global cvc_account4
  global cvc_account4_n
  cvc_update_accounts()
  cvc_u_a_4 = cvc_unlock(cvc_account4, cvc_account4pw, cvc_unlockTime)
  if cvc_u_a_4 == False:
    if cvc_account4pw == '':
     cvc_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account4_n+' Passphrase Denied: '+cvc_account4pw_r)
    elif cvc_account4pw != '':
     print('Unlock Failure With Account '+cvc_account4_n+' Passphrase Denied: '+cvc_account4pw)
  if cvc_u_a_4 == True:
   print(cvc_account4_n+' Unlocked')

def cvc_unlock_account_5():
  global cvc_account5pw
  global cvc_account5
  global cvc_account5_n
  cvc_update_accounts()
  cvc_u_a_5 = cvc_unlock(cvc_account5, cvc_account5pw, cvc_unlockTime)
  if cvc_u_a_5 == False:
    if cvc_account5pw == '':
     cvc_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account5_n+' Passphrase Denied: '+cvc_account5pw_r)
    elif cvc_account5pw != '':
     print('Unlock Failure With Account '+cvc_account5_n+' Passphrase Denied: '+cvc_account5pw)
  if cvc_u_a_5 == True:
   print(cvc_account5_n+' Unlocked')

def cvc_unlock_account_6():
  global cvc_account6pw
  global cvc_account6
  global cvc_account6_n
  cvc_update_accounts()
  cvc_u_a_6 = cvc_unlock(cvc_account6, cvc_account6pw, cvc_unlockTime)
  if cvc_u_a_6 == False:
    if cvc_account6pw == '':
     cvc_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+cvc_account6_n+' Passphrase Denied: '+cvc_account6pw_r)
    elif cvc_account6pw != '':
     print('Unlock Failure With Account '+cvc_account6_n+' Passphrase Denied: '+cvc_account6pw)
  if cvc_u_a_6 == True:
   print(cvc_account6_n+' Unlocked')

def cvc_unlock_account(cvc_ua_accountNumber):
 cvc_update_accounts()
 cvc_ua_account_number = cvc_ua_accountNumber
 cvc_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if cvc_ua_account_number == cvc_ua_input[0]:
  cvc_unlock_account_0()
 if cvc_ua_account_number == cvc_ua_input[1]:
  cvc_unlock_account_1()
 if cvc_ua_account_number == cvc_ua_input[2]:
  cvc_unlock_account_2()
 if cvc_ua_account_number == cvc_ua_input[3]:
  cvc_unlock_account_3()
 if cvc_ua_account_number == cvc_ua_input[4]:
  cvc_unlock_account_4()
 if cvc_ua_account_number == cvc_ua_input[5]:
  cvc_unlock_account_5()
 if cvc_ua_account_number == cvc_ua_input[6]:
  cvc_unlock_account_6()
 if cvc_ua_account_number not in cvc_ua_input:
  print('Must Integer Within Range '+cvc_accounts_range+'.')
 

def cvc_approve_between_accounts(fromAccount, toAccount, msgValue):
  cvc_update_accounts()
  cvc_a_0 = cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(cvc_a_0)

def cvc_approve(fromAccountNumber, toAddress, msgValue):
  cvc_update_accounts()
  cvc_unlock_account(fromAccountNumber)
  cvc_a_1 = cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(cvc_a_1)

def cvc_transfer_between_accounts(fromAccount, toAccount, msgValue):
  cvc_update_accounts()
  cvc_unlock_account(fromAccount)
  cvc_t_0 = cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(cvc_t_0)

def cvc_transfer(fromAccountNumber, toAddress, msgValue):
  cvc_update_accounts()
  cvc_unlock_account(fromAccountNumber)
  cvc_t_1 = cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(cvc_t_1)

def cvc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  cvc_update_accounts()
  cvc_unlock_account(callAccount)
  cvc_tf_0 = cvc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(cvc_tf_0)

def cvc_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  cvc_update_accounts()
  cvc_unlock_account(callAccount)
  cvc_tf_1 = cvc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(cvc_tf_1)
  


def cvc_help():
  print('Following Functions For '+cvc_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * cvc_unlock => web3.personal.unlockAccount
/ * cvc_accounts => web3.personal.listAccounts
/ * cvc_balance = web3.eth.getBalance
** cvc => web3.eth.contract(abi=cvc_abi, address=cvc_address)
** / * cvc_balanceOf => cvc.call().balanceOf

~ Function Listing Below:
~ cvc_update_accounts()
~ cvc_update_balances() \n\r -- => cvc_update_accounts()
~ cvc_list_all_accounts() \n\r -- => cvc_update_accounts()
~ cvc_account_balance(accountNumber) \n\r -- => cvc_update_balances() 
~ cvc_list_all_account_balances() \n\r -- => cvc_update_balances()
~ cvc_unlock_all_accounts() \n\r -- => cvc_unlock_account_0() \n\r -- => cvc_unlock_account_1() \n\r -- => cvc_unlock_account_2() \n\r -- => cvc_unlock_account_3() \n\r -- => cvc_unlock_account_4() \n\r -- => cvc_unlock_account_5() \n\r -- => cvc_unlock_account_6() 
~ cvc_unlock_account_0() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account0, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_1() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account1, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_2() \n\r -- => cvc_update_accounts() \n\r --/ *cvc_w_unlock(cvc_account2, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_3() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account3, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_4() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account4, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_5() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account5, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account_6() \n\r -- => cvc_update_accounts() \n\r -- / *cvc_w_unlock(cvc_account6, cvc_account0pw, cvc_unlockTime)
~ cvc_unlock_account(cvc_ua_accountNumber) \n\r -- => cvc_update_accounts() \n\r -- // cvc_unlock_account_0() \n\r -- // cvc_unlock_account_1() \n\r -- // cvc_unlock_account_2() \n\r -- // cvc_unlock_account_3() \n\r -- // cvc_unlock_account_4() \n\r -- // cvc_unlock_account_5() \n\r -- // cvc_unlock_account_6()
~ cvc_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(fromAccount) \n\r -- / ** cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ cvc_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(fromAccountNumber) \n\r -- / ** cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ cvc_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(fromAccount) \n\r -- / ** cvc.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ cvc_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(fromAccountNumber) \n\r -- / ** cvc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ cvc_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(callAccount) \n\r / ** cvc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ cvc_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => cvc_update_accounts() \n\r -- => cvc_unlock_account(callAccount) \n\r -- / ** cvc.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ cvc_help() <-- You Are Here. ''')