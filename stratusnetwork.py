#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global snt_account_0_a
global snt_account_1_a
global snt_account_2_a
global snt_account_3_a
global snt_account_4_a
global snt_account_5_a
global snt_account_6_a
global snt_address
global snt_abi
global snt
global snt_call_0
global snt_call_1
global snt_call_2
global snt_call_3
global snt_call_4
global snt_call_5
global snt_call_6
global snt_call_ab
global snt_accounts
global snt_account_0_pw
global snt_account_1_pw
global snt_account_2_pw
global snt_account_3_pw
global snt_account_4_pw
global snt_account_5_pw
global snt_account_6_pw
global snt_account_0_n
global snt_account_1_n
global snt_account_2_n
global snt_account_3_n
global snt_account_4_n
global snt_account_5_n
global snt_account_6_n
global snt_account1pw
global snt_account2pw
global snt_account3pw
global snt_account4pw
global snt_account5pw
global snt_account6pw
global snt_last_price
global snt_accounts_range
global snt_tokenName
global snt_last_ethereum_price
global snt_unlockTime
global snt_balance
global snt_balanceOf
global snt_unlock
global snt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
snt_token_d = 1e18
_e_d = 1e18
snt_accounts_range = '[0, 6]'
snt_unlock = web3.personal.unlockAccount
snt_last_ethereum_price = 370.00
snt_last_price = 0.04
snt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
snt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
snt_tokenName = 'StratusNetwork Token'
snt_unlockTime = hex(10000) # Must be hex()
snt_account_0_a = snt_accounts[0]
snt_account_1_a = snt_accounts[1]
snt_account_2_a = snt_accounts[2]
snt_account_3_a = snt_accounts[3]
snt_account_4_a = snt_accounts[4]
snt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
snt_account_6_a = snt_accounts[6]
# Supply Unlock Passwords For Transactions Below
snt_account_0_pw = 'GuildSkrypt2017!@#'
snt_account_1_pw = ''
snt_account_2_pw = 'GuildSkrypt2017!@#'
snt_account_3_pw = ''
snt_account_4_pw = ''
snt_account_5_pw = ''
snt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
snt_account_0_n = 'Skotys Bittrex Account'
snt_account_1_n = 'Jeffs Account'
snt_account_2_n = 'Skrypts Bittrex Account'
snt_account_3_n = 'Skotys Personal Account'
snt_account_4_n = 'Unknown'
snt_account_5_n = 'Watched \'Bittrex\' Account.'
snt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
snt_address = '0x744d70FDBE2Ba4CF95131626614a1763DF805B9'
snt_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creationBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_blockNumber","type":"uint256"}],"name":"balanceOfAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_cloneTokenName","type":"string"},{"name":"_cloneDecimalUnits","type":"uint8"},{"name":"_cloneTokenSymbol","type":"string"},{"name":"_snapshotBlock","type":"uint256"},{"name":"_transfersEnabled","type":"bool"}],"name":"createCloneToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"generateTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_blockNumber","type":"uint256"}],"name":"totalSupplyAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentSnapShotBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroyTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"}],"name":"claimTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_transfersEnabled","type":"bool"}],"name":"enableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[{"name":"_tokenFactory","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_token","type":"address"},{"indexed":true,"name":"_controller","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"ClaimedTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_cloneToken","type":"address"},{"indexed":false,"name":"_snapshotBlock","type":"uint256"}],"name":"NewCloneToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Approval","type":"event"}]
snt = web3.eth.contract(abi=snt_abi, address=snt_address)
snt_balanceOf = snt.call().balanceOf
# End Contract Information
def snt_update_accounts():
 global snt_account0
 global snt_account1
 global snt_account2
 global snt_account3
 global snt_account4
 global snt_account5
 global snt_account6
 global snt_account0_n
 global snt_account1_n
 global snt_account2_n
 global snt_account3_n
 global snt_account4_n
 global snt_account5_n
 global snt_account6_n
 global snt_account0pw
 global snt_account1pw
 global snt_account2pw
 global snt_account3pw
 global snt_account4pw
 global snt_account5pw
 global snt_account6pw
 snt_account0 = snt_account_0_a
 snt_account1 = snt_account_1_a
 snt_account2 = snt_account_2_a
 snt_account3 = snt_account_3_a
 snt_account4 = snt_account_4_a
 snt_account5 = snt_account_5_a
 snt_account6 = snt_account_6_a
 snt_account0_n = snt_account_0_n
 snt_account1_n = snt_account_1_n
 snt_account2_n = snt_account_2_n
 snt_account3_n = snt_account_3_n
 snt_account4_n = snt_account_4_n
 snt_account5_n = snt_account_5_n
 snt_account6_n = snt_account_6_n
 snt_account0pw = snt_account_0_pw
 snt_account1pw = snt_account_1_pw
 snt_account2pw = snt_account_2_pw
 snt_account3pw = snt_account_3_pw
 snt_account4pw = snt_account_4_pw
 snt_account5pw = snt_account_5_pw
 snt_account6pw = snt_account_6_pw
 print(snt_tokenName+' Accounts Updated.')
def snt_update_balances():
 global snt_call_0
 global snt_call_1
 global snt_call_2
 global snt_call_3
 global snt_call_4
 global snt_call_5
 global snt_call_6
 global snt_w_call_0
 global snt_w_call_1
 global snt_w_call_2
 global snt_w_call_3
 global snt_w_call_4
 global snt_w_call_5
 global snt_w_call_6
 snt_update_accounts()
 print('Updating '+snt_tokenName+' Balances Please Wait...')
 snt_call_0 = snt_balanceOf(snt_account0)
 snt_call_1 = snt_balanceOf(snt_account1)
 snt_call_2 = snt_balanceOf(snt_account2)
 snt_call_3 = snt_balanceOf(snt_account3)
 snt_call_4 = snt_balanceOf(snt_account4)
 snt_call_5 = snt_balanceOf(snt_account5)
 snt_call_6 = snt_balanceOf(snt_account6)
 snt_w_call_0 = snt_balance(snt_account0)
 snt_w_call_1 = snt_balance(snt_account1)
 snt_w_call_2 = snt_balance(snt_account2)
 snt_w_call_3 = snt_balance(snt_account3)
 snt_w_call_4 = snt_balance(snt_account4)
 snt_w_call_5 = snt_balance(snt_account5)
 snt_w_call_6 = snt_balance(snt_account6)
 print(snt_tokenName+' Balances Updated.')
def snt_list_all_accounts():
 snt_update_accounts()
 print(snt_tokenName+' '+snt_account0_n+': '+snt_account0)
 print(snt_tokenName+' '+snt_account1_n+': '+snt_account1)
 print(snt_tokenName+' '+snt_account2_n+': '+snt_account2)
 print(snt_tokenName+' '+snt_account3_n+': '+snt_account3)
 print(snt_tokenName+' '+snt_account4_n+': '+snt_account4)
 print(snt_tokenName+' '+snt_account5_n+': '+snt_account5)
 print(snt_tokenName+' '+snt_account6_n+': '+snt_account6)

def snt_account_balance(accountNumber):
 snt_update_balances()
 snt_ab_account_number = accountNumber
 snt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if snt_ab_account_number == snt_ab_input[0]:
  print('Calling '+snt_account0_n+' '+snt_tokenName+' Balance: ')
  print(snt_account0_n+': '+snt_tokenName+' Balance: '+str(snt_call_0 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_0 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[1]:
  print('Calling '+snt_account1_n+' '+snt_tokenName+' Balance: ')
  print(snt_account1_n+': '+snt_tokenName+' Balance: '+str(snt_call_1 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_1 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[2]:
  print('Calling '+snt_account2_n+' '+snt_tokenName+' Balance: ')
  print(snt_account2_n+': '+snt_tokenName+' Balance: '+str(snt_call_2 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_2 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[3]:
  print('Calling '+snt_account3_n+' '+snt_tokenName+' Balance: ')
  print(snt_account3_n+': '+snt_tokenName+' Balance: '+str(snt_call_3 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_3 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[4]:
  print('Calling '+snt_account4_n+' '+snt_tokenName+' Balance: ')
  print(snt_account4_n+': '+snt_tokenName+' Balance: '+str(snt_call_4 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_4 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[5]:
  print('Calling '+snt_account5_n+' '+snt_tokenName+' Balance: ')
  print(snt_account5_n+': '+snt_tokenName+' Balance: '+str(snt_call_5 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_5 / snt_token_d * snt_last_price))
 if snt_ab_account_number == snt_ab_input[6]:
  print('Calling '+snt_account6_n+' '+snt_tokenName+' Balance: ')
  print(snt_account6_n+': '+snt_tokenName+' Balance: '+str(snt_call_6 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_6 / snt_token_d * snt_last_price))
 if snt_ab_account_number not in snt_ab_input:
  print('Must Integer Within Range '+snt_accounts_range+'.')

def snt_list_all_account_balances():
 snt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+snt_tokenName+' Balance: ')
 print(snt_account0_n+': '+snt_tokenName+' Balance: '+str(snt_call_0 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_0 / snt_token_d * snt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(snt_account0_n+': Ethereum Balance '+str(snt_w_call_0 / _e_d)+' $'+str(snt_w_call_0 / _e_d * snt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+snt_tokenName+' Balance: ')
 print(snt_account1_n+': '+snt_tokenName+' Balance: '+str(snt_call_1 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_1 / snt_token_d * snt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(snt_account1_n+': Ethereum Balance '+str(snt_w_call_1 / _e_d)+' $'+str(snt_w_call_1 / _e_d * snt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+snt_tokenName+' Balance: ')
 print(snt_account2_n+': '+snt_tokenName+' Balance: '+str(snt_call_2 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_2 / snt_token_d * snt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(snt_account2_n+': Ethereum Balance '+str(snt_w_call_2 / _e_d)+' $'+str(snt_w_call_2 / _e_d * snt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+snt_tokenName+' Balance: ')
 print(snt_account3_n+': '+snt_tokenName+' Balance: '+str(snt_call_3 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_3 / snt_token_d * snt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(snt_account3_n+': Ethereum Balance '+str(snt_w_call_3 / _e_d)+' $'+str(snt_w_call_3 / _e_d * snt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+snt_tokenName+' Balance: ')
 print(snt_account4_n+': '+snt_tokenName+' Balance: '+str(snt_call_4 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_4 / snt_token_d * snt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(snt_account4_n+': Ethereum Balance '+str(snt_w_call_4 / _e_d)+' $'+str(snt_w_call_4 / _e_d * snt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+snt_tokenName+' Balance: ')
 print(snt_account5_n+': '+snt_tokenName+' Balance: '+str(snt_call_5 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_5 / snt_token_d * snt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(snt_account5_n+': Ethereum Balance '+str(snt_w_call_5 / _e_d)+' $'+str(snt_w_call_5 /_e_d * snt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+snt_tokenName+' Balance: ')
 print(snt_account6_n+': '+snt_tokenName+' Balance: '+str(snt_call_6 / snt_token_d)+' Usd/'+snt_tokenName+' Balance: $'+str(snt_call_6 / snt_token_d * snt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(snt_account6_n+': Ethereum Balance '+str(snt_w_call_6 / _e_d)+' $'+str(snt_w_call_6 / _e_d * snt_last_ethereum_price))
def snt_unlock_all_accounts():
  snt_unlock_account_0()
  snt_unlock_account_1()
  snt_unlock_account_2()
  snt_unlock_account_3()
  snt_unlock_account_4()
  snt_unlock_account_5()
  snt_unlock_account_6()


def snt_unlock_account_0():
  global snt_account0pw
  global snt_account0
  global snt_account0_n
  snt_update_accounts()
  snt_u_a_0 = snt_w_unlock(snt_account0, snt_account0pw, snt_unlockTime)
  if snt_u_a_0 == False:
    if snt_account0pw == '':
     snt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account0_n+' Passphrase Denied: '+snt_account0pw_r)
    elif snt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snt_account0_n+' Passphrase Denied: '+snt_account0pw)
  if snt_u_a_0 == True:
   print(snt_account0_n+' Unlocked')

def snt_unlock_account_1():
  global snt_account1pw
  global snt_account1
  global snt_account1_n
  snt_update_accounts()
  snt_u_a_1 = snt_unlock(snt_account1, snt_account1pw, snt_unlockTime)
  if snt_u_a_1 == False:
    if snt_account1pw == '':
     snt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account1_n+' Passphrase Denied: '+snt_account1pw_r)
    elif snt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+snt_account1_n+' Passphrase Denied: '+snt_account1pw)
  if snt_u_a_1 == True:
   print(snt_account1_n+' Unlocked')

def snt_unlock_account_2():
  global snt_account2pw
  global snt_account2
  global snt_account2_n
  snt_update_accounts()
  snt_u_a_2 = snt_unlock(snt_account2, snt_account2pw, snt_unlockTime)
  if snt_u_a_2 == False:
    if snt_account2pw == '':
     snt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account2_n+' Passphrase Denied: '+snt_account2pw_r)
    elif snt_account2pw != '':
     print('Unlock Failure With Account '+snt_account2_n+' Passphrase Denied: '+snt_account2pw)
  if snt_u_a_2 == True:
   print(snt_account2_n+' Unlocked')

def snt_unlock_account_3():
  global snt_account3pw
  global snt_account3
  global snt_account3_n
  snt_update_accounts()
  snt_u_a_3 = snt_unlock(snt_account3, snt_account3pw, snt_unlockTime)
  if snt_u_a_3 == False:
    if snt_account3pw == '':
     snt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account3_n+' Passphrase Denied: '+snt_account3pw_r)
    elif snt_account3pw != '':
     print('Unlock Failure With Account '+snt_account3_n+' Passphrase Denied: '+snt_account3pw)
  if snt_u_a_3 == True:
   print(snt_account3_n+' Unlocked')

def snt_unlock_account_4():
  global snt_account4pw
  global snt_account4
  global snt_account4_n
  snt_update_accounts()
  snt_u_a_4 = snt_unlock(snt_account4, snt_account4pw, snt_unlockTime)
  if snt_u_a_4 == False:
    if snt_account4pw == '':
     snt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account4_n+' Passphrase Denied: '+snt_account4pw_r)
    elif snt_account4pw != '':
     print('Unlock Failure With Account '+snt_account4_n+' Passphrase Denied: '+snt_account4pw)
  if snt_u_a_4 == True:
   print(snt_account4_n+' Unlocked')

def snt_unlock_account_5():
  global snt_account5pw
  global snt_account5
  global snt_account5_n
  snt_update_accounts()
  snt_u_a_5 = snt_unlock(snt_account5, snt_account5pw, snt_unlockTime)
  if snt_u_a_5 == False:
    if snt_account5pw == '':
     snt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account5_n+' Passphrase Denied: '+snt_account5pw_r)
    elif snt_account5pw != '':
     print('Unlock Failure With Account '+snt_account5_n+' Passphrase Denied: '+snt_account5pw)
  if snt_u_a_5 == True:
   print(snt_account5_n+' Unlocked')

def snt_unlock_account_6():
  global snt_account6pw
  global snt_account6
  global snt_account6_n
  snt_update_accounts()
  snt_u_a_6 = snt_unlock(snt_account6, snt_account6pw, snt_unlockTime)
  if snt_u_a_6 == False:
    if snt_account6pw == '':
     snt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+snt_account6_n+' Passphrase Denied: '+snt_account6pw_r)
    elif snt_account6pw != '':
     print('Unlock Failure With Account '+snt_account6_n+' Passphrase Denied: '+snt_account6pw)
  if snt_u_a_6 == True:
   print(snt_account6_n+' Unlocked')

def snt_unlock_account(snt_ua_accountNumber):
 snt_update_accounts()
 snt_ua_account_number = snt_ua_accountNumber
 snt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if snt_ua_account_number == snt_ua_input[0]:
  snt_unlock_account_0()
 if snt_ua_account_number == snt_ua_input[1]:
  snt_unlock_account_1()
 if snt_ua_account_number == snt_ua_input[2]:
  snt_unlock_account_2()
 if snt_ua_account_number == snt_ua_input[3]:
  snt_unlock_account_3()
 if snt_ua_account_number == snt_ua_input[4]:
  snt_unlock_account_4()
 if snt_ua_account_number == snt_ua_input[5]:
  snt_unlock_account_5()
 if snt_ua_account_number == snt_ua_input[6]:
  snt_unlock_account_6()
 if snt_ua_account_number not in snt_ua_input:
  print('Must Integer Within Range '+snt_accounts_range+'.')
 

def snt_approve_between_accounts(fromAccount, toAccount, msgValue):
  snt_update_accounts()
  snt_a_0 = snt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(snt_a_0)

def snt_approve(fromAccountNumber, toAddress, msgValue):
  snt_update_accounts()
  snt_unlock_account(fromAccountNumber)
  snt_a_1 = snt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(snt_a_1)

def snt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  snt_update_accounts()
  snt_unlock_account(fromAccount)
  snt_t_0 = snt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(snt_t_0)

def snt_transfer(fromAccountNumber, toAddress, msgValue):
  snt_update_accounts()
  snt_unlock_account(fromAccountNumber)
  snt_t_1 = snt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(snt_t_1)

def snt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  snt_update_accounts()
  snt_unlock_account(callAccount)
  snt_tf_0 = snt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(snt_tf_0)

def snt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  snt_update_accounts()
  snt_unlock_account(callAccount)
  snt_tf_1 = snt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(snt_tf_1)
  


def snt_help():
  print('Following Functions For '+snt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * snt_unlock => web3.personal.unlockAccount
/ * snt_accounts => web3.personal.listAccounts
/ * snt_balance = web3.eth.getBalance
** snt => web3.eth.contract(abi=snt_abi, address=snt_address)
** / * snt_balanceOf => snt.call().balanceOf

~ Function Listing Below:
~ snt_update_accounts()
~ snt_update_balances() \n\r -- => snt_update_accounts()
~ snt_list_all_accounts() \n\r -- => snt_update_accounts()
~ snt_account_balance(accountNumber) \n\r -- => snt_update_balances() 
~ snt_list_all_account_balances() \n\r -- => snt_update_balances()
~ snt_unlock_all_accounts() \n\r -- => snt_unlock_account_0() \n\r -- => snt_unlock_account_1() \n\r -- => snt_unlock_account_2() \n\r -- => snt_unlock_account_3() \n\r -- => snt_unlock_account_4() \n\r -- => snt_unlock_account_5() \n\r -- => snt_unlock_account_6() 
~ snt_unlock_account_0() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account0, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_1() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account1, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_2() \n\r -- => snt_update_accounts() \n\r --/ *snt_w_unlock(snt_account2, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_3() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account3, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_4() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account4, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_5() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account5, snt_account0pw, snt_unlockTime)
~ snt_unlock_account_6() \n\r -- => snt_update_accounts() \n\r -- / *snt_w_unlock(snt_account6, snt_account0pw, snt_unlockTime)
~ snt_unlock_account(snt_ua_accountNumber) \n\r -- => snt_update_accounts() \n\r -- // snt_unlock_account_0() \n\r -- // snt_unlock_account_1() \n\r -- // snt_unlock_account_2() \n\r -- // snt_unlock_account_3() \n\r -- // snt_unlock_account_4() \n\r -- // snt_unlock_account_5() \n\r -- // snt_unlock_account_6()
~ snt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(fromAccount) \n\r -- / ** snt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(fromAccountNumber) \n\r -- / ** snt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ snt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(fromAccount) \n\r -- / ** snt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ snt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(fromAccountNumber) \n\r -- / ** snt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(callAccount) \n\r / ** snt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ snt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => snt_update_accounts() \n\r -- => snt_unlock_account(callAccount) \n\r -- / ** snt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ snt_help() <-- You Are Here. ''')