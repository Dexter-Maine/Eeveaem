#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global msp_account_0_a
global msp_account_1_a
global msp_account_2_a
global msp_account_3_a
global msp_account_4_a
global msp_account_5_a
global msp_account_6_a
global msp_address
global msp_abi
global msp
global msp_call_0
global msp_call_1
global msp_call_2
global msp_call_3
global msp_call_4
global msp_call_5
global msp_call_6
global msp_call_ab
global msp_accounts
global msp_account_0_pw
global msp_account_1_pw
global msp_account_2_pw
global msp_account_3_pw
global msp_account_4_pw
global msp_account_5_pw
global msp_account_6_pw
global msp_account_0_n
global msp_account_1_n
global msp_account_2_n
global msp_account_3_n
global msp_account_4_n
global msp_account_5_n
global msp_account_6_n
global msp_account1pw
global msp_account2pw
global msp_account3pw
global msp_account4pw
global msp_account5pw
global msp_account6pw
global msp_last_price
global msp_accounts_range
global msp_tokenName
global msp_last_ethereum_price
global msp_unlockTime
global msp_balance
global msp_balanceOf
global msp_unlock
global msp_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
msp_token_d = 1e18
_e_d = 1e18
msp_accounts_range = '[0, 6]'
msp_unlock = web3.personal.unlockAccount
msp_last_ethereum_price = 370.00
msp_last_price = 0.24
msp_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
msp_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
msp_tokenName = 'Mothership Token'
msp_unlockTime = hex(10000) # Must be hex()
msp_account_0_a = msp_accounts[0]
msp_account_1_a = msp_accounts[1]
msp_account_2_a = msp_accounts[2]
msp_account_3_a = msp_accounts[3]
msp_account_4_a = msp_accounts[4]
msp_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
msp_account_6_a = msp_accounts[6]
# Supply Unlock Passwords For Transactions Below
msp_account_0_pw = 'GuildSkrypt2017!@#'
msp_account_1_pw = ''
msp_account_2_pw = 'GuildSkrypt2017!@#'
msp_account_3_pw = ''
msp_account_4_pw = ''
msp_account_5_pw = ''
msp_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
msp_account_0_n = 'Skotys Bittrex Account'
msp_account_1_n = 'Jeffs Account'
msp_account_2_n = 'Skrypts Bittrex Account'
msp_account_3_n = 'Skotys Personal Account'
msp_account_4_n = 'Unknown'
msp_account_5_n = 'Watched \'Bittrex\' Account.'
msp_account_6_n = 'Watched Account (1)'
# Contract Information Below :
msp_address = '0x68AA3F232dA9bdC2343465545794ef3eEa5209BD'
msp_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creationBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"burner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_blockNumber","type":"uint256"}],"name":"balanceOfAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_cloneTokenName","type":"string"},{"name":"_cloneDecimalUnits","type":"uint8"},{"name":"_cloneTokenSymbol","type":"string"},{"name":"_snapshotBlock","type":"uint256"},{"name":"_transfersEnabled","type":"bool"}],"name":"createCloneToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newBurner","type":"address"}],"name":"changeBurner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"generateTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_blockNumber","type":"uint256"}],"name":"totalSupplyAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentSnapShotBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroyTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"}],"name":"claimTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_transfersEnabled","type":"bool"}],"name":"enableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[{"name":"_tokenFactory","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_token","type":"address"},{"indexed":true,"name":"_controller","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"ClaimedTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_cloneToken","type":"address"},{"indexed":false,"name":"_snapshotBlock","type":"uint256"}],"name":"NewCloneToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Approval","type":"event"}]
msp = web3.eth.contract(abi=msp_abi, address=msp_address)
msp_balanceOf = msp.call().balanceOf
# End Contract Information
def msp_update_accounts():
 global msp_account0
 global msp_account1
 global msp_account2
 global msp_account3
 global msp_account4
 global msp_account5
 global msp_account6
 global msp_account0_n
 global msp_account1_n
 global msp_account2_n
 global msp_account3_n
 global msp_account4_n
 global msp_account5_n
 global msp_account6_n
 global msp_account0pw
 global msp_account1pw
 global msp_account2pw
 global msp_account3pw
 global msp_account4pw
 global msp_account5pw
 global msp_account6pw
 msp_account0 = msp_account_0_a
 msp_account1 = msp_account_1_a
 msp_account2 = msp_account_2_a
 msp_account3 = msp_account_3_a
 msp_account4 = msp_account_4_a
 msp_account5 = msp_account_5_a
 msp_account6 = msp_account_6_a
 msp_account0_n = msp_account_0_n
 msp_account1_n = msp_account_1_n
 msp_account2_n = msp_account_2_n
 msp_account3_n = msp_account_3_n
 msp_account4_n = msp_account_4_n
 msp_account5_n = msp_account_5_n
 msp_account6_n = msp_account_6_n
 msp_account0pw = msp_account_0_pw
 msp_account1pw = msp_account_1_pw
 msp_account2pw = msp_account_2_pw
 msp_account3pw = msp_account_3_pw
 msp_account4pw = msp_account_4_pw
 msp_account5pw = msp_account_5_pw
 msp_account6pw = msp_account_6_pw
 print(msp_tokenName+' Accounts Updated.')
def msp_update_balances():
 global msp_call_0
 global msp_call_1
 global msp_call_2
 global msp_call_3
 global msp_call_4
 global msp_call_5
 global msp_call_6
 global msp_w_call_0
 global msp_w_call_1
 global msp_w_call_2
 global msp_w_call_3
 global msp_w_call_4
 global msp_w_call_5
 global msp_w_call_6
 msp_update_accounts()
 print('Updating '+msp_tokenName+' Balances Please Wait...')
 msp_call_0 = msp_balanceOf(msp_account0)
 msp_call_1 = msp_balanceOf(msp_account1)
 msp_call_2 = msp_balanceOf(msp_account2)
 msp_call_3 = msp_balanceOf(msp_account3)
 msp_call_4 = msp_balanceOf(msp_account4)
 msp_call_5 = msp_balanceOf(msp_account5)
 msp_call_6 = msp_balanceOf(msp_account6)
 msp_w_call_0 = msp_balance(msp_account0)
 msp_w_call_1 = msp_balance(msp_account1)
 msp_w_call_2 = msp_balance(msp_account2)
 msp_w_call_3 = msp_balance(msp_account3)
 msp_w_call_4 = msp_balance(msp_account4)
 msp_w_call_5 = msp_balance(msp_account5)
 msp_w_call_6 = msp_balance(msp_account6)
 print(msp_tokenName+' Balances Updated.')
def msp_list_all_accounts():
 msp_update_accounts()
 print(msp_tokenName+' '+msp_account0_n+': '+msp_account0)
 print(msp_tokenName+' '+msp_account1_n+': '+msp_account1)
 print(msp_tokenName+' '+msp_account2_n+': '+msp_account2)
 print(msp_tokenName+' '+msp_account3_n+': '+msp_account3)
 print(msp_tokenName+' '+msp_account4_n+': '+msp_account4)
 print(msp_tokenName+' '+msp_account5_n+': '+msp_account5)
 print(msp_tokenName+' '+msp_account6_n+': '+msp_account6)

def msp_account_balance(accountNumber):
 msp_update_balances()
 msp_ab_account_number = accountNumber
 msp_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if msp_ab_account_number == msp_ab_input[0]:
  print('Calling '+msp_account0_n+' '+msp_tokenName+' Balance: ')
  print(msp_account0_n+': '+msp_tokenName+' Balance: '+str(msp_call_0 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_0 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[1]:
  print('Calling '+msp_account1_n+' '+msp_tokenName+' Balance: ')
  print(msp_account1_n+': '+msp_tokenName+' Balance: '+str(msp_call_1 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_1 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[2]:
  print('Calling '+msp_account2_n+' '+msp_tokenName+' Balance: ')
  print(msp_account2_n+': '+msp_tokenName+' Balance: '+str(msp_call_2 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_2 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[3]:
  print('Calling '+msp_account3_n+' '+msp_tokenName+' Balance: ')
  print(msp_account3_n+': '+msp_tokenName+' Balance: '+str(msp_call_3 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_3 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[4]:
  print('Calling '+msp_account4_n+' '+msp_tokenName+' Balance: ')
  print(msp_account4_n+': '+msp_tokenName+' Balance: '+str(msp_call_4 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_4 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[5]:
  print('Calling '+msp_account5_n+' '+msp_tokenName+' Balance: ')
  print(msp_account5_n+': '+msp_tokenName+' Balance: '+str(msp_call_5 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_5 / msp_token_d * msp_last_price))
 if msp_ab_account_number == msp_ab_input[6]:
  print('Calling '+msp_account6_n+' '+msp_tokenName+' Balance: ')
  print(msp_account6_n+': '+msp_tokenName+' Balance: '+str(msp_call_6 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_6 / msp_token_d * msp_last_price))
 if msp_ab_account_number not in msp_ab_input:
  print('Must Integer Within Range '+msp_accounts_range+'.')

def msp_list_all_account_balances():
 msp_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+msp_tokenName+' Balance: ')
 print(msp_account0_n+': '+msp_tokenName+' Balance: '+str(msp_call_0 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_0 / msp_token_d * msp_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(msp_account0_n+': Ethereum Balance '+str(msp_w_call_0 / _e_d)+' $'+str(msp_w_call_0 / _e_d * msp_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+msp_tokenName+' Balance: ')
 print(msp_account1_n+': '+msp_tokenName+' Balance: '+str(msp_call_1 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_1 / msp_token_d * msp_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(msp_account1_n+': Ethereum Balance '+str(msp_w_call_1 / _e_d)+' $'+str(msp_w_call_1 / _e_d * msp_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+msp_tokenName+' Balance: ')
 print(msp_account2_n+': '+msp_tokenName+' Balance: '+str(msp_call_2 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_2 / msp_token_d * msp_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(msp_account2_n+': Ethereum Balance '+str(msp_w_call_2 / _e_d)+' $'+str(msp_w_call_2 / _e_d * msp_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+msp_tokenName+' Balance: ')
 print(msp_account3_n+': '+msp_tokenName+' Balance: '+str(msp_call_3 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_3 / msp_token_d * msp_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(msp_account3_n+': Ethereum Balance '+str(msp_w_call_3 / _e_d)+' $'+str(msp_w_call_3 / _e_d * msp_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+msp_tokenName+' Balance: ')
 print(msp_account4_n+': '+msp_tokenName+' Balance: '+str(msp_call_4 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_4 / msp_token_d * msp_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(msp_account4_n+': Ethereum Balance '+str(msp_w_call_4 / _e_d)+' $'+str(msp_w_call_4 / _e_d * msp_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+msp_tokenName+' Balance: ')
 print(msp_account5_n+': '+msp_tokenName+' Balance: '+str(msp_call_5 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_5 / msp_token_d * msp_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(msp_account5_n+': Ethereum Balance '+str(msp_w_call_5 / _e_d)+' $'+str(msp_w_call_5 /_e_d * msp_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+msp_tokenName+' Balance: ')
 print(msp_account6_n+': '+msp_tokenName+' Balance: '+str(msp_call_6 / msp_token_d)+' Usd/'+msp_tokenName+' Balance: $'+str(msp_call_6 / msp_token_d * msp_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(msp_account6_n+': Ethereum Balance '+str(msp_w_call_6 / _e_d)+' $'+str(msp_w_call_6 / _e_d * msp_last_ethereum_price))
def msp_unlock_all_accounts():
  msp_unlock_account_0()
  msp_unlock_account_1()
  msp_unlock_account_2()
  msp_unlock_account_3()
  msp_unlock_account_4()
  msp_unlock_account_5()
  msp_unlock_account_6()


def msp_unlock_account_0():
  global msp_account0pw
  global msp_account0
  global msp_account0_n
  msp_update_accounts()
  msp_u_a_0 = msp_w_unlock(msp_account0, msp_account0pw, msp_unlockTime)
  if msp_u_a_0 == False:
    if msp_account0pw == '':
     msp_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account0_n+' Passphrase Denied: '+msp_account0pw_r)
    elif msp_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+msp_account0_n+' Passphrase Denied: '+msp_account0pw)
  if msp_u_a_0 == True:
   print(msp_account0_n+' Unlocked')

def msp_unlock_account_1():
  global msp_account1pw
  global msp_account1
  global msp_account1_n
  msp_update_accounts()
  msp_u_a_1 = msp_unlock(msp_account1, msp_account1pw, msp_unlockTime)
  if msp_u_a_1 == False:
    if msp_account1pw == '':
     msp_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account1_n+' Passphrase Denied: '+msp_account1pw_r)
    elif msp_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+msp_account1_n+' Passphrase Denied: '+msp_account1pw)
  if msp_u_a_1 == True:
   print(msp_account1_n+' Unlocked')

def msp_unlock_account_2():
  global msp_account2pw
  global msp_account2
  global msp_account2_n
  msp_update_accounts()
  msp_u_a_2 = msp_unlock(msp_account2, msp_account2pw, msp_unlockTime)
  if msp_u_a_2 == False:
    if msp_account2pw == '':
     msp_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account2_n+' Passphrase Denied: '+msp_account2pw_r)
    elif msp_account2pw != '':
     print('Unlock Failure With Account '+msp_account2_n+' Passphrase Denied: '+msp_account2pw)
  if msp_u_a_2 == True:
   print(msp_account2_n+' Unlocked')

def msp_unlock_account_3():
  global msp_account3pw
  global msp_account3
  global msp_account3_n
  msp_update_accounts()
  msp_u_a_3 = msp_unlock(msp_account3, msp_account3pw, msp_unlockTime)
  if msp_u_a_3 == False:
    if msp_account3pw == '':
     msp_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account3_n+' Passphrase Denied: '+msp_account3pw_r)
    elif msp_account3pw != '':
     print('Unlock Failure With Account '+msp_account3_n+' Passphrase Denied: '+msp_account3pw)
  if msp_u_a_3 == True:
   print(msp_account3_n+' Unlocked')

def msp_unlock_account_4():
  global msp_account4pw
  global msp_account4
  global msp_account4_n
  msp_update_accounts()
  msp_u_a_4 = msp_unlock(msp_account4, msp_account4pw, msp_unlockTime)
  if msp_u_a_4 == False:
    if msp_account4pw == '':
     msp_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account4_n+' Passphrase Denied: '+msp_account4pw_r)
    elif msp_account4pw != '':
     print('Unlock Failure With Account '+msp_account4_n+' Passphrase Denied: '+msp_account4pw)
  if msp_u_a_4 == True:
   print(msp_account4_n+' Unlocked')

def msp_unlock_account_5():
  global msp_account5pw
  global msp_account5
  global msp_account5_n
  msp_update_accounts()
  msp_u_a_5 = msp_unlock(msp_account5, msp_account5pw, msp_unlockTime)
  if msp_u_a_5 == False:
    if msp_account5pw == '':
     msp_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account5_n+' Passphrase Denied: '+msp_account5pw_r)
    elif msp_account5pw != '':
     print('Unlock Failure With Account '+msp_account5_n+' Passphrase Denied: '+msp_account5pw)
  if msp_u_a_5 == True:
   print(msp_account5_n+' Unlocked')

def msp_unlock_account_6():
  global msp_account6pw
  global msp_account6
  global msp_account6_n
  msp_update_accounts()
  msp_u_a_6 = msp_unlock(msp_account6, msp_account6pw, msp_unlockTime)
  if msp_u_a_6 == False:
    if msp_account6pw == '':
     msp_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+msp_account6_n+' Passphrase Denied: '+msp_account6pw_r)
    elif msp_account6pw != '':
     print('Unlock Failure With Account '+msp_account6_n+' Passphrase Denied: '+msp_account6pw)
  if msp_u_a_6 == True:
   print(msp_account6_n+' Unlocked')

def msp_unlock_account(msp_ua_accountNumber):
 msp_update_accounts()
 msp_ua_account_number = msp_ua_accountNumber
 msp_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if msp_ua_account_number == msp_ua_input[0]:
  msp_unlock_account_0()
 if msp_ua_account_number == msp_ua_input[1]:
  msp_unlock_account_1()
 if msp_ua_account_number == msp_ua_input[2]:
  msp_unlock_account_2()
 if msp_ua_account_number == msp_ua_input[3]:
  msp_unlock_account_3()
 if msp_ua_account_number == msp_ua_input[4]:
  msp_unlock_account_4()
 if msp_ua_account_number == msp_ua_input[5]:
  msp_unlock_account_5()
 if msp_ua_account_number == msp_ua_input[6]:
  msp_unlock_account_6()
 if msp_ua_account_number not in msp_ua_input:
  print('Must Integer Within Range '+msp_accounts_range+'.')
 

def msp_approve_between_accounts(fromAccount, toAccount, msgValue):
  msp_update_accounts()
  msp_a_0 = msp.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(msp_a_0)

def msp_approve(fromAccountNumber, toAddress, msgValue):
  msp_update_accounts()
  msp_unlock_account(fromAccountNumber)
  msp_a_1 = msp.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(msp_a_1)

def msp_transfer_between_accounts(fromAccount, toAccount, msgValue):
  msp_update_accounts()
  msp_unlock_account(fromAccount)
  msp_t_0 = msp.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(msp_t_0)

def msp_transfer(fromAccountNumber, toAddress, msgValue):
  msp_update_accounts()
  msp_unlock_account(fromAccountNumber)
  msp_t_1 = msp.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(msp_t_1)

def msp_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  msp_update_accounts()
  msp_unlock_account(callAccount)
  msp_tf_0 = msp.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(msp_tf_0)

def msp_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  msp_update_accounts()
  msp_unlock_account(callAccount)
  msp_tf_1 = msp.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(msp_tf_1)
  


def msp_help():
  print('Following Functions For '+msp_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * msp_unlock => web3.personal.unlockAccount
/ * msp_accounts => web3.personal.listAccounts
/ * msp_balance = web3.eth.getBalance
** msp => web3.eth.contract(abi=msp_abi, address=msp_address)
** / * msp_balanceOf => msp.call().balanceOf

~ Function Listing Below:
~ msp_update_accounts()
~ msp_update_balances() \n\r -- => msp_update_accounts()
~ msp_list_all_accounts() \n\r -- => msp_update_accounts()
~ msp_account_balance(accountNumber) \n\r -- => msp_update_balances() 
~ msp_list_all_account_balances() \n\r -- => msp_update_balances()
~ msp_unlock_all_accounts() \n\r -- => msp_unlock_account_0() \n\r -- => msp_unlock_account_1() \n\r -- => msp_unlock_account_2() \n\r -- => msp_unlock_account_3() \n\r -- => msp_unlock_account_4() \n\r -- => msp_unlock_account_5() \n\r -- => msp_unlock_account_6() 
~ msp_unlock_account_0() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account0, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_1() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account1, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_2() \n\r -- => msp_update_accounts() \n\r --/ *msp_w_unlock(msp_account2, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_3() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account3, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_4() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account4, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_5() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account5, msp_account0pw, msp_unlockTime)
~ msp_unlock_account_6() \n\r -- => msp_update_accounts() \n\r -- / *msp_w_unlock(msp_account6, msp_account0pw, msp_unlockTime)
~ msp_unlock_account(msp_ua_accountNumber) \n\r -- => msp_update_accounts() \n\r -- // msp_unlock_account_0() \n\r -- // msp_unlock_account_1() \n\r -- // msp_unlock_account_2() \n\r -- // msp_unlock_account_3() \n\r -- // msp_unlock_account_4() \n\r -- // msp_unlock_account_5() \n\r -- // msp_unlock_account_6()
~ msp_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(fromAccount) \n\r -- / ** msp.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ msp_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(fromAccountNumber) \n\r -- / ** msp.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ msp_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(fromAccount) \n\r -- / ** msp.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ msp_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(fromAccountNumber) \n\r -- / ** msp.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ msp_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(callAccount) \n\r / ** msp.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ msp_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => msp_update_accounts() \n\r -- => msp_unlock_account(callAccount) \n\r -- / ** msp.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ msp_help() <-- You Are Here. ''')