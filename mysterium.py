#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global myst_account_0_a
global myst_account_1_a
global myst_account_2_a
global myst_account_3_a
global myst_account_4_a
global myst_account_5_a
global myst_account_6_a
global myst_address
global myst_abi
global myst
global myst_call_0
global myst_call_1
global myst_call_2
global myst_call_3
global myst_call_4
global myst_call_5
global myst_call_6
global myst_call_ab
global myst_accounts
global myst_account_0_pw
global myst_account_1_pw
global myst_account_2_pw
global myst_account_3_pw
global myst_account_4_pw
global myst_account_5_pw
global myst_account_6_pw
global myst_account_0_n
global myst_account_1_n
global myst_account_2_n
global myst_account_3_n
global myst_account_4_n
global myst_account_5_n
global myst_account_6_n
global myst_account1pw
global myst_account2pw
global myst_account3pw
global myst_account4pw
global myst_account5pw
global myst_account6pw
global myst_last_price
global myst_accounts_range
global myst_tokenName
global myst_last_ethereum_price
global myst_unlockTime
global myst_balance
global myst_balanceOf
global myst_unlock
global myst_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
myst_token_d = 1e8
_e_d = 1e18
myst_accounts_range = '[0, 6]'
myst_unlock = web3.personal.unlockAccount
myst_last_ethereum_price = 370.00
myst_last_price = 1.53
myst_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
myst_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
myst_tokenName = 'Mysterium Token'
myst_unlockTime = hex(10000) # Must be hex()
myst_account_0_a = myst_accounts[0]
myst_account_1_a = myst_accounts[1]
myst_account_2_a = myst_accounts[2]
myst_account_3_a = myst_accounts[3]
myst_account_4_a = myst_accounts[4]
myst_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
myst_account_6_a = myst_accounts[6]
# Supply Unlock Passwords For Transactions Below
myst_account_0_pw = 'GuildSkrypt2017!@#'
myst_account_1_pw = ''
myst_account_2_pw = 'GuildSkrypt2017!@#'
myst_account_3_pw = ''
myst_account_4_pw = ''
myst_account_5_pw = ''
myst_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
myst_account_0_n = 'Skotys Bittrex Account'
myst_account_1_n = 'Jeffs Account'
myst_account_2_n = 'Skrypts Bittrex Account'
myst_account_3_n = 'Skotys Personal Account'
myst_account_4_n = 'Unknown'
myst_account_5_n = 'Watched \'Bittrex\' Account.'
myst_account_6_n = 'Watched Account (1)'
# Contract Information Below :
myst_address = '0xa645264C5603E96c3b0B078cdab68733794B0A71'
myst_abi = [{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"state","type":"bool"}],"name":"setTransferAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setReleaseAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"receiver","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"mintAgents","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"state","type":"bool"}],"name":"setMintAgent","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"upgrade","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"}],"name":"setTokenInformation","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"releaseTokenTransfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getUpgradeState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"transferAgents","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"released","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"canUpgrade","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"addApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalUpgraded","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"releaseAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"agent","type":"address"}],"name":"setUpgradeAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"subApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"master","type":"address"}],"name":"setUpgradeMaster","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_initialSupply","type":"uint256"},{"name":"_decimals","type":"uint256"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newName","type":"string"},{"indexed":false,"name":"newSymbol","type":"string"}],"name":"UpdatedTokenInformation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Upgrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"agent","type":"address"}],"name":"UpgradeAgentSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"receiver","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
myst = web3.eth.contract(abi=myst_abi, address=myst_address)
myst_balanceOf = myst.call().balanceOf
# End Contract Information
def myst_update_accounts():
 global myst_account0
 global myst_account1
 global myst_account2
 global myst_account3
 global myst_account4
 global myst_account5
 global myst_account6
 global myst_account0_n
 global myst_account1_n
 global myst_account2_n
 global myst_account3_n
 global myst_account4_n
 global myst_account5_n
 global myst_account6_n
 global myst_account0pw
 global myst_account1pw
 global myst_account2pw
 global myst_account3pw
 global myst_account4pw
 global myst_account5pw
 global myst_account6pw
 myst_account0 = myst_account_0_a
 myst_account1 = myst_account_1_a
 myst_account2 = myst_account_2_a
 myst_account3 = myst_account_3_a
 myst_account4 = myst_account_4_a
 myst_account5 = myst_account_5_a
 myst_account6 = myst_account_6_a
 myst_account0_n = myst_account_0_n
 myst_account1_n = myst_account_1_n
 myst_account2_n = myst_account_2_n
 myst_account3_n = myst_account_3_n
 myst_account4_n = myst_account_4_n
 myst_account5_n = myst_account_5_n
 myst_account6_n = myst_account_6_n
 myst_account0pw = myst_account_0_pw
 myst_account1pw = myst_account_1_pw
 myst_account2pw = myst_account_2_pw
 myst_account3pw = myst_account_3_pw
 myst_account4pw = myst_account_4_pw
 myst_account5pw = myst_account_5_pw
 myst_account6pw = myst_account_6_pw
 print(myst_tokenName+' Accounts Updated.')
def myst_update_balances():
 global myst_call_0
 global myst_call_1
 global myst_call_2
 global myst_call_3
 global myst_call_4
 global myst_call_5
 global myst_call_6
 global myst_w_call_0
 global myst_w_call_1
 global myst_w_call_2
 global myst_w_call_3
 global myst_w_call_4
 global myst_w_call_5
 global myst_w_call_6
 myst_update_accounts()
 print('Updating '+myst_tokenName+' Balances Please Wait...')
 myst_call_0 = myst_balanceOf(myst_account0)
 myst_call_1 = myst_balanceOf(myst_account1)
 myst_call_2 = myst_balanceOf(myst_account2)
 myst_call_3 = myst_balanceOf(myst_account3)
 myst_call_4 = myst_balanceOf(myst_account4)
 myst_call_5 = myst_balanceOf(myst_account5)
 myst_call_6 = myst_balanceOf(myst_account6)
 myst_w_call_0 = myst_balance(myst_account0)
 myst_w_call_1 = myst_balance(myst_account1)
 myst_w_call_2 = myst_balance(myst_account2)
 myst_w_call_3 = myst_balance(myst_account3)
 myst_w_call_4 = myst_balance(myst_account4)
 myst_w_call_5 = myst_balance(myst_account5)
 myst_w_call_6 = myst_balance(myst_account6)
 print(myst_tokenName+' Balances Updated.')
def myst_list_all_accounts():
 myst_update_accounts()
 print(myst_tokenName+' '+myst_account0_n+': '+myst_account0)
 print(myst_tokenName+' '+myst_account1_n+': '+myst_account1)
 print(myst_tokenName+' '+myst_account2_n+': '+myst_account2)
 print(myst_tokenName+' '+myst_account3_n+': '+myst_account3)
 print(myst_tokenName+' '+myst_account4_n+': '+myst_account4)
 print(myst_tokenName+' '+myst_account5_n+': '+myst_account5)
 print(myst_tokenName+' '+myst_account6_n+': '+myst_account6)

def myst_account_balance(accountNumber):
 myst_update_balances()
 myst_ab_account_number = accountNumber
 myst_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if myst_ab_account_number == myst_ab_input[0]:
  print('Calling '+myst_account0_n+' '+myst_tokenName+' Balance: ')
  print(myst_account0_n+': '+myst_tokenName+' Balance: '+str(myst_call_0 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_0 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[1]:
  print('Calling '+myst_account1_n+' '+myst_tokenName+' Balance: ')
  print(myst_account1_n+': '+myst_tokenName+' Balance: '+str(myst_call_1 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_1 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[2]:
  print('Calling '+myst_account2_n+' '+myst_tokenName+' Balance: ')
  print(myst_account2_n+': '+myst_tokenName+' Balance: '+str(myst_call_2 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_2 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[3]:
  print('Calling '+myst_account3_n+' '+myst_tokenName+' Balance: ')
  print(myst_account3_n+': '+myst_tokenName+' Balance: '+str(myst_call_3 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_3 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[4]:
  print('Calling '+myst_account4_n+' '+myst_tokenName+' Balance: ')
  print(myst_account4_n+': '+myst_tokenName+' Balance: '+str(myst_call_4 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_4 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[5]:
  print('Calling '+myst_account5_n+' '+myst_tokenName+' Balance: ')
  print(myst_account5_n+': '+myst_tokenName+' Balance: '+str(myst_call_5 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_5 / myst_token_d * myst_last_price))
 if myst_ab_account_number == myst_ab_input[6]:
  print('Calling '+myst_account6_n+' '+myst_tokenName+' Balance: ')
  print(myst_account6_n+': '+myst_tokenName+' Balance: '+str(myst_call_6 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_6 / myst_token_d * myst_last_price))
 if myst_ab_account_number not in myst_ab_input:
  print('Must Integer Within Range '+myst_accounts_range+'.')

def myst_list_all_account_balances():
 myst_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+myst_tokenName+' Balance: ')
 print(myst_account0_n+': '+myst_tokenName+' Balance: '+str(myst_call_0 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_0 / myst_token_d * myst_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(myst_account0_n+': Ethereum Balance '+str(myst_w_call_0 / _e_d)+' $'+str(myst_w_call_0 / _e_d * myst_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+myst_tokenName+' Balance: ')
 print(myst_account1_n+': '+myst_tokenName+' Balance: '+str(myst_call_1 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_1 / myst_token_d * myst_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(myst_account1_n+': Ethereum Balance '+str(myst_w_call_1 / _e_d)+' $'+str(myst_w_call_1 / _e_d * myst_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+myst_tokenName+' Balance: ')
 print(myst_account2_n+': '+myst_tokenName+' Balance: '+str(myst_call_2 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_2 / myst_token_d * myst_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(myst_account2_n+': Ethereum Balance '+str(myst_w_call_2 / _e_d)+' $'+str(myst_w_call_2 / _e_d * myst_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+myst_tokenName+' Balance: ')
 print(myst_account3_n+': '+myst_tokenName+' Balance: '+str(myst_call_3 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_3 / myst_token_d * myst_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(myst_account3_n+': Ethereum Balance '+str(myst_w_call_3 / _e_d)+' $'+str(myst_w_call_3 / _e_d * myst_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+myst_tokenName+' Balance: ')
 print(myst_account4_n+': '+myst_tokenName+' Balance: '+str(myst_call_4 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_4 / myst_token_d * myst_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(myst_account4_n+': Ethereum Balance '+str(myst_w_call_4 / _e_d)+' $'+str(myst_w_call_4 / _e_d * myst_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+myst_tokenName+' Balance: ')
 print(myst_account5_n+': '+myst_tokenName+' Balance: '+str(myst_call_5 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_5 / myst_token_d * myst_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(myst_account5_n+': Ethereum Balance '+str(myst_w_call_5 / _e_d)+' $'+str(myst_w_call_5 /_e_d * myst_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+myst_tokenName+' Balance: ')
 print(myst_account6_n+': '+myst_tokenName+' Balance: '+str(myst_call_6 / myst_token_d)+' Usd/'+myst_tokenName+' Balance: $'+str(myst_call_6 / myst_token_d * myst_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(myst_account6_n+': Ethereum Balance '+str(myst_w_call_6 / _e_d)+' $'+str(myst_w_call_6 / _e_d * myst_last_ethereum_price))
def myst_unlock_all_accounts():
  myst_unlock_account_0()
  myst_unlock_account_1()
  myst_unlock_account_2()
  myst_unlock_account_3()
  myst_unlock_account_4()
  myst_unlock_account_5()
  myst_unlock_account_6()


def myst_unlock_account_0():
  global myst_account0pw
  global myst_account0
  global myst_account0_n
  myst_update_accounts()
  myst_u_a_0 = myst_w_unlock(myst_account0, myst_account0pw, myst_unlockTime)
  if myst_u_a_0 == False:
    if myst_account0pw == '':
     myst_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account0_n+' Passphrase Denied: '+myst_account0pw_r)
    elif myst_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+myst_account0_n+' Passphrase Denied: '+myst_account0pw)
  if myst_u_a_0 == True:
   print(myst_account0_n+' Unlocked')

def myst_unlock_account_1():
  global myst_account1pw
  global myst_account1
  global myst_account1_n
  myst_update_accounts()
  myst_u_a_1 = myst_unlock(myst_account1, myst_account1pw, myst_unlockTime)
  if myst_u_a_1 == False:
    if myst_account1pw == '':
     myst_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account1_n+' Passphrase Denied: '+myst_account1pw_r)
    elif myst_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+myst_account1_n+' Passphrase Denied: '+myst_account1pw)
  if myst_u_a_1 == True:
   print(myst_account1_n+' Unlocked')

def myst_unlock_account_2():
  global myst_account2pw
  global myst_account2
  global myst_account2_n
  myst_update_accounts()
  myst_u_a_2 = myst_unlock(myst_account2, myst_account2pw, myst_unlockTime)
  if myst_u_a_2 == False:
    if myst_account2pw == '':
     myst_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account2_n+' Passphrase Denied: '+myst_account2pw_r)
    elif myst_account2pw != '':
     print('Unlock Failure With Account '+myst_account2_n+' Passphrase Denied: '+myst_account2pw)
  if myst_u_a_2 == True:
   print(myst_account2_n+' Unlocked')

def myst_unlock_account_3():
  global myst_account3pw
  global myst_account3
  global myst_account3_n
  myst_update_accounts()
  myst_u_a_3 = myst_unlock(myst_account3, myst_account3pw, myst_unlockTime)
  if myst_u_a_3 == False:
    if myst_account3pw == '':
     myst_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account3_n+' Passphrase Denied: '+myst_account3pw_r)
    elif myst_account3pw != '':
     print('Unlock Failure With Account '+myst_account3_n+' Passphrase Denied: '+myst_account3pw)
  if myst_u_a_3 == True:
   print(myst_account3_n+' Unlocked')

def myst_unlock_account_4():
  global myst_account4pw
  global myst_account4
  global myst_account4_n
  myst_update_accounts()
  myst_u_a_4 = myst_unlock(myst_account4, myst_account4pw, myst_unlockTime)
  if myst_u_a_4 == False:
    if myst_account4pw == '':
     myst_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account4_n+' Passphrase Denied: '+myst_account4pw_r)
    elif myst_account4pw != '':
     print('Unlock Failure With Account '+myst_account4_n+' Passphrase Denied: '+myst_account4pw)
  if myst_u_a_4 == True:
   print(myst_account4_n+' Unlocked')

def myst_unlock_account_5():
  global myst_account5pw
  global myst_account5
  global myst_account5_n
  myst_update_accounts()
  myst_u_a_5 = myst_unlock(myst_account5, myst_account5pw, myst_unlockTime)
  if myst_u_a_5 == False:
    if myst_account5pw == '':
     myst_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account5_n+' Passphrase Denied: '+myst_account5pw_r)
    elif myst_account5pw != '':
     print('Unlock Failure With Account '+myst_account5_n+' Passphrase Denied: '+myst_account5pw)
  if myst_u_a_5 == True:
   print(myst_account5_n+' Unlocked')

def myst_unlock_account_6():
  global myst_account6pw
  global myst_account6
  global myst_account6_n
  myst_update_accounts()
  myst_u_a_6 = myst_unlock(myst_account6, myst_account6pw, myst_unlockTime)
  if myst_u_a_6 == False:
    if myst_account6pw == '':
     myst_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+myst_account6_n+' Passphrase Denied: '+myst_account6pw_r)
    elif myst_account6pw != '':
     print('Unlock Failure With Account '+myst_account6_n+' Passphrase Denied: '+myst_account6pw)
  if myst_u_a_6 == True:
   print(myst_account6_n+' Unlocked')

def myst_unlock_account(myst_ua_accountNumber):
 myst_update_accounts()
 myst_ua_account_number = myst_ua_accountNumber
 myst_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if myst_ua_account_number == myst_ua_input[0]:
  myst_unlock_account_0()
 if myst_ua_account_number == myst_ua_input[1]:
  myst_unlock_account_1()
 if myst_ua_account_number == myst_ua_input[2]:
  myst_unlock_account_2()
 if myst_ua_account_number == myst_ua_input[3]:
  myst_unlock_account_3()
 if myst_ua_account_number == myst_ua_input[4]:
  myst_unlock_account_4()
 if myst_ua_account_number == myst_ua_input[5]:
  myst_unlock_account_5()
 if myst_ua_account_number == myst_ua_input[6]:
  myst_unlock_account_6()
 if myst_ua_account_number not in myst_ua_input:
  print('Must Integer Within Range '+myst_accounts_range+'.')
 

def myst_approve_between_accounts(fromAccount, toAccount, msgValue):
  myst_update_accounts()
  myst_a_0 = myst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(myst_a_0)

def myst_approve(fromAccountNumber, toAddress, msgValue):
  myst_update_accounts()
  myst_unlock_account(fromAccountNumber)
  myst_a_1 = myst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(myst_a_1)

def myst_transfer_between_accounts(fromAccount, toAccount, msgValue):
  myst_update_accounts()
  myst_unlock_account(fromAccount)
  myst_t_0 = myst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(myst_t_0)

def myst_transfer(fromAccountNumber, toAddress, msgValue):
  myst_update_accounts()
  myst_unlock_account(fromAccountNumber)
  myst_t_1 = myst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(myst_t_1)

def myst_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  myst_update_accounts()
  myst_unlock_account(callAccount)
  myst_tf_0 = myst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(myst_tf_0)

def myst_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  myst_update_accounts()
  myst_unlock_account(callAccount)
  myst_tf_1 = myst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(myst_tf_1)
  


def myst_help():
  print('Following Functions For '+myst_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * myst_unlock => web3.personal.unlockAccount
/ * myst_accounts => web3.personal.listAccounts
/ * myst_balance = web3.eth.getBalance
** myst => web3.eth.contract(abi=myst_abi, address=myst_address)
** / * myst_balanceOf => myst.call().balanceOf

~ Function Listing Below:
~ myst_update_accounts()
~ myst_update_balances() \n\r -- => myst_update_accounts()
~ myst_list_all_accounts() \n\r -- => myst_update_accounts()
~ myst_account_balance(accountNumber) \n\r -- => myst_update_balances() 
~ myst_list_all_account_balances() \n\r -- => myst_update_balances()
~ myst_unlock_all_accounts() \n\r -- => myst_unlock_account_0() \n\r -- => myst_unlock_account_1() \n\r -- => myst_unlock_account_2() \n\r -- => myst_unlock_account_3() \n\r -- => myst_unlock_account_4() \n\r -- => myst_unlock_account_5() \n\r -- => myst_unlock_account_6() 
~ myst_unlock_account_0() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account0, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_1() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account1, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_2() \n\r -- => myst_update_accounts() \n\r --/ *myst_w_unlock(myst_account2, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_3() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account3, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_4() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account4, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_5() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account5, myst_account0pw, myst_unlockTime)
~ myst_unlock_account_6() \n\r -- => myst_update_accounts() \n\r -- / *myst_w_unlock(myst_account6, myst_account0pw, myst_unlockTime)
~ myst_unlock_account(myst_ua_accountNumber) \n\r -- => myst_update_accounts() \n\r -- // myst_unlock_account_0() \n\r -- // myst_unlock_account_1() \n\r -- // myst_unlock_account_2() \n\r -- // myst_unlock_account_3() \n\r -- // myst_unlock_account_4() \n\r -- // myst_unlock_account_5() \n\r -- // myst_unlock_account_6()
~ myst_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(fromAccount) \n\r -- / ** myst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ myst_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(fromAccountNumber) \n\r -- / ** myst.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ myst_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(fromAccount) \n\r -- / ** myst.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ myst_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(fromAccountNumber) \n\r -- / ** myst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ myst_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(callAccount) \n\r / ** myst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ myst_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => myst_update_accounts() \n\r -- => myst_unlock_account(callAccount) \n\r -- / ** myst.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ myst_help() <-- You Are Here. ''')