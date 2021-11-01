#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global ant_account_0_a
global ant_account_1_a
global ant_account_2_a
global ant_account_3_a
global ant_account_4_a
global ant_account_5_a
global ant_account_6_a
global ant_address
global ant_abi
global ant
global ant_call_0
global ant_call_1
global ant_call_2
global ant_call_3
global ant_call_4
global ant_call_5
global ant_call_6
global ant_call_ab
global ant_accounts
global ant_account_0_pw
global ant_account_1_pw
global ant_account_2_pw
global ant_account_3_pw
global ant_account_4_pw
global ant_account_5_pw
global ant_account_6_pw
global ant_account_0_n
global ant_account_1_n
global ant_account_2_n
global ant_account_3_n
global ant_account_4_n
global ant_account_5_n
global ant_account_6_n
global ant_account1pw
global ant_account2pw
global ant_account3pw
global ant_account4pw
global ant_account5pw
global ant_account6pw
global ant_last_price
global ant_accounts_range
global ant_tokenName
global ant_last_ethereum_price
global ant_unlockTime
global ant_balance
global ant_balanceOf
global ant_unlock
global ant_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
ant_token_d = 1e18
_e_d = 1e18
ant_accounts_range = '[0, 6]'
ant_unlock = web3.personal.unlockAccount
ant_last_ethereum_price = 370.00
ant_last_price = 3.11
ant_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
ant_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
ant_tokenName = 'Aragon Network Token'
ant_unlockTime = hex(10000) # Must be hex()
ant_account_0_a = ant_accounts[0]
ant_account_1_a = ant_accounts[1]
ant_account_2_a = ant_accounts[2]
ant_account_3_a = ant_accounts[3]
ant_account_4_a = ant_accounts[4]
ant_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
ant_account_6_a = ant_accounts[6]
# Supply Unlock Passwords For Transactions Below
ant_account_0_pw = 'GuildSkrypt2017!@#'
ant_account_1_pw = ''
ant_account_2_pw = 'GuildSkrypt2017!@#'
ant_account_3_pw = ''
ant_account_4_pw = ''
ant_account_5_pw = ''
ant_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
ant_account_0_n = 'Skotys Bittrex Account'
ant_account_1_n = 'Jeffs Account'
ant_account_2_n = 'Skrypts Bittrex Account'
ant_account_3_n = 'Skotys Personal Account'
ant_account_4_n = 'Unknown'
ant_account_5_n = 'Watched \'Bittrex\' Account.'
ant_account_6_n = 'Watched Account (1)'
# Contract Information Below :
ant_address = '0x960b236A07cf122663c4303350609A66A7B288C0'
ant_abi = [{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_start","type":"uint64"},{"name":"_cliff","type":"uint64"},{"name":"_vesting","type":"uint64"}],"name":"grantVestedTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"}],"name":"tokenGrantsCount","outputs":[{"name":"index","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"}],"name":"spendableBalanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creationBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_allowed","type":"bool"}],"name":"setCanCreateGrants","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"grants","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"},{"name":"start","type":"uint64"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_blockNumber","type":"uint256"}],"name":"balanceOfAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"tokenGrant","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"vested","type":"uint256"},{"name":"start","type":"uint64"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_cloneTokenName","type":"string"},{"name":"_cloneDecimalUnits","type":"uint8"},{"name":"_cloneTokenSymbol","type":"string"},{"name":"_snapshotBlock","type":"uint256"},{"name":"_transfersEnabled","type":"bool"}],"name":"createCloneToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"}],"name":"lastTokenIsTransferableDate","outputs":[{"name":"date","type":"uint64"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"generateTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_blockNumber","type":"uint256"}],"name":"totalSupplyAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentSnapShotBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"},{"name":"time","type":"uint64"}],"name":"transferableTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroyTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"revokeTokenGrant","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_transfersEnabled","type":"bool"}],"name":"enableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newWhitelister","type":"address"}],"name":"changeVestingWhitelister","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_tokenFactory","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"start","type":"uint64"},{"indexed":false,"name":"cliff","type":"uint64"},{"indexed":false,"name":"vesting","type":"uint64"}],"name":"NewTokenGrant","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_cloneToken","type":"address"},{"indexed":false,"name":"_snapshotBlock","type":"uint256"}],"name":"NewCloneToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
ant = web3.eth.contract(abi=ant_abi, address=ant_address)
ant_balanceOf = ant.call().balanceOf
# End Contract Information
def ant_update_accounts():
 global ant_account0
 global ant_account1
 global ant_account2
 global ant_account3
 global ant_account4
 global ant_account5
 global ant_account6
 global ant_account0_n
 global ant_account1_n
 global ant_account2_n
 global ant_account3_n
 global ant_account4_n
 global ant_account5_n
 global ant_account6_n
 global ant_account0pw
 global ant_account1pw
 global ant_account2pw
 global ant_account3pw
 global ant_account4pw
 global ant_account5pw
 global ant_account6pw
 ant_account0 = ant_account_0_a
 ant_account1 = ant_account_1_a
 ant_account2 = ant_account_2_a
 ant_account3 = ant_account_3_a
 ant_account4 = ant_account_4_a
 ant_account5 = ant_account_5_a
 ant_account6 = ant_account_6_a
 ant_account0_n = ant_account_0_n
 ant_account1_n = ant_account_1_n
 ant_account2_n = ant_account_2_n
 ant_account3_n = ant_account_3_n
 ant_account4_n = ant_account_4_n
 ant_account5_n = ant_account_5_n
 ant_account6_n = ant_account_6_n
 ant_account0pw = ant_account_0_pw
 ant_account1pw = ant_account_1_pw
 ant_account2pw = ant_account_2_pw
 ant_account3pw = ant_account_3_pw
 ant_account4pw = ant_account_4_pw
 ant_account5pw = ant_account_5_pw
 ant_account6pw = ant_account_6_pw
 print(ant_tokenName+' Accounts Updated.')
def ant_update_balances():
 global ant_call_0
 global ant_call_1
 global ant_call_2
 global ant_call_3
 global ant_call_4
 global ant_call_5
 global ant_call_6
 global ant_w_call_0
 global ant_w_call_1
 global ant_w_call_2
 global ant_w_call_3
 global ant_w_call_4
 global ant_w_call_5
 global ant_w_call_6
 ant_update_accounts()
 print('Updating '+ant_tokenName+' Balances Please Wait...')
 ant_call_0 = ant_balanceOf(ant_account0)
 ant_call_1 = ant_balanceOf(ant_account1)
 ant_call_2 = ant_balanceOf(ant_account2)
 ant_call_3 = ant_balanceOf(ant_account3)
 ant_call_4 = ant_balanceOf(ant_account4)
 ant_call_5 = ant_balanceOf(ant_account5)
 ant_call_6 = ant_balanceOf(ant_account6)
 ant_w_call_0 = ant_balance(ant_account0)
 ant_w_call_1 = ant_balance(ant_account1)
 ant_w_call_2 = ant_balance(ant_account2)
 ant_w_call_3 = ant_balance(ant_account3)
 ant_w_call_4 = ant_balance(ant_account4)
 ant_w_call_5 = ant_balance(ant_account5)
 ant_w_call_6 = ant_balance(ant_account6)
 print(ant_tokenName+' Balances Updated.')
def ant_list_all_accounts():
 ant_update_accounts()
 print(ant_tokenName+' '+ant_account0_n+': '+ant_account0)
 print(ant_tokenName+' '+ant_account1_n+': '+ant_account1)
 print(ant_tokenName+' '+ant_account2_n+': '+ant_account2)
 print(ant_tokenName+' '+ant_account3_n+': '+ant_account3)
 print(ant_tokenName+' '+ant_account4_n+': '+ant_account4)
 print(ant_tokenName+' '+ant_account5_n+': '+ant_account5)
 print(ant_tokenName+' '+ant_account6_n+': '+ant_account6)

def ant_account_balance(accountNumber):
 ant_update_balances()
 ant_ab_account_number = accountNumber
 ant_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if ant_ab_account_number == ant_ab_input[0]:
  print('Calling '+ant_account0_n+' '+ant_tokenName+' Balance: ')
  print(ant_account0_n+': '+ant_tokenName+' Balance: '+str(ant_call_0 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_0 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[1]:
  print('Calling '+ant_account1_n+' '+ant_tokenName+' Balance: ')
  print(ant_account1_n+': '+ant_tokenName+' Balance: '+str(ant_call_1 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_1 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[2]:
  print('Calling '+ant_account2_n+' '+ant_tokenName+' Balance: ')
  print(ant_account2_n+': '+ant_tokenName+' Balance: '+str(ant_call_2 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_2 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[3]:
  print('Calling '+ant_account3_n+' '+ant_tokenName+' Balance: ')
  print(ant_account3_n+': '+ant_tokenName+' Balance: '+str(ant_call_3 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_3 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[4]:
  print('Calling '+ant_account4_n+' '+ant_tokenName+' Balance: ')
  print(ant_account4_n+': '+ant_tokenName+' Balance: '+str(ant_call_4 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_4 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[5]:
  print('Calling '+ant_account5_n+' '+ant_tokenName+' Balance: ')
  print(ant_account5_n+': '+ant_tokenName+' Balance: '+str(ant_call_5 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_5 / ant_token_d * ant_last_price))
 if ant_ab_account_number == ant_ab_input[6]:
  print('Calling '+ant_account6_n+' '+ant_tokenName+' Balance: ')
  print(ant_account6_n+': '+ant_tokenName+' Balance: '+str(ant_call_6 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_6 / ant_token_d * ant_last_price))
 if ant_ab_account_number not in ant_ab_input:
  print('Must Integer Within Range '+ant_accounts_range+'.')

def ant_list_all_account_balances():
 ant_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+ant_tokenName+' Balance: ')
 print(ant_account0_n+': '+ant_tokenName+' Balance: '+str(ant_call_0 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_0 / ant_token_d * ant_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(ant_account0_n+': Ethereum Balance '+str(ant_w_call_0 / _e_d)+' $'+str(ant_w_call_0 / _e_d * ant_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+ant_tokenName+' Balance: ')
 print(ant_account1_n+': '+ant_tokenName+' Balance: '+str(ant_call_1 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_1 / ant_token_d * ant_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(ant_account1_n+': Ethereum Balance '+str(ant_w_call_1 / _e_d)+' $'+str(ant_w_call_1 / _e_d * ant_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+ant_tokenName+' Balance: ')
 print(ant_account2_n+': '+ant_tokenName+' Balance: '+str(ant_call_2 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_2 / ant_token_d * ant_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(ant_account2_n+': Ethereum Balance '+str(ant_w_call_2 / _e_d)+' $'+str(ant_w_call_2 / _e_d * ant_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+ant_tokenName+' Balance: ')
 print(ant_account3_n+': '+ant_tokenName+' Balance: '+str(ant_call_3 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_3 / ant_token_d * ant_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(ant_account3_n+': Ethereum Balance '+str(ant_w_call_3 / _e_d)+' $'+str(ant_w_call_3 / _e_d * ant_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+ant_tokenName+' Balance: ')
 print(ant_account4_n+': '+ant_tokenName+' Balance: '+str(ant_call_4 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_4 / ant_token_d * ant_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(ant_account4_n+': Ethereum Balance '+str(ant_w_call_4 / _e_d)+' $'+str(ant_w_call_4 / _e_d * ant_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+ant_tokenName+' Balance: ')
 print(ant_account5_n+': '+ant_tokenName+' Balance: '+str(ant_call_5 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_5 / ant_token_d * ant_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(ant_account5_n+': Ethereum Balance '+str(ant_w_call_5 / _e_d)+' $'+str(ant_w_call_5 /_e_d * ant_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+ant_tokenName+' Balance: ')
 print(ant_account6_n+': '+ant_tokenName+' Balance: '+str(ant_call_6 / ant_token_d)+' Usd/'+ant_tokenName+' Balance: $'+str(ant_call_6 / ant_token_d * ant_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(ant_account6_n+': Ethereum Balance '+str(ant_w_call_6 / _e_d)+' $'+str(ant_w_call_6 / _e_d * ant_last_ethereum_price))
def ant_unlock_all_accounts():
  ant_unlock_account_0()
  ant_unlock_account_1()
  ant_unlock_account_2()
  ant_unlock_account_3()
  ant_unlock_account_4()
  ant_unlock_account_5()
  ant_unlock_account_6()


def ant_unlock_account_0():
  global ant_account0pw
  global ant_account0
  global ant_account0_n
  ant_update_accounts()
  ant_u_a_0 = ant_w_unlock(ant_account0, ant_account0pw, ant_unlockTime)
  if ant_u_a_0 == False:
    if ant_account0pw == '':
     ant_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account0_n+' Passphrase Denied: '+ant_account0pw_r)
    elif ant_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ant_account0_n+' Passphrase Denied: '+ant_account0pw)
  if ant_u_a_0 == True:
   print(ant_account0_n+' Unlocked')

def ant_unlock_account_1():
  global ant_account1pw
  global ant_account1
  global ant_account1_n
  ant_update_accounts()
  ant_u_a_1 = ant_unlock(ant_account1, ant_account1pw, ant_unlockTime)
  if ant_u_a_1 == False:
    if ant_account1pw == '':
     ant_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account1_n+' Passphrase Denied: '+ant_account1pw_r)
    elif ant_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ant_account1_n+' Passphrase Denied: '+ant_account1pw)
  if ant_u_a_1 == True:
   print(ant_account1_n+' Unlocked')

def ant_unlock_account_2():
  global ant_account2pw
  global ant_account2
  global ant_account2_n
  ant_update_accounts()
  ant_u_a_2 = ant_unlock(ant_account2, ant_account2pw, ant_unlockTime)
  if ant_u_a_2 == False:
    if ant_account2pw == '':
     ant_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account2_n+' Passphrase Denied: '+ant_account2pw_r)
    elif ant_account2pw != '':
     print('Unlock Failure With Account '+ant_account2_n+' Passphrase Denied: '+ant_account2pw)
  if ant_u_a_2 == True:
   print(ant_account2_n+' Unlocked')

def ant_unlock_account_3():
  global ant_account3pw
  global ant_account3
  global ant_account3_n
  ant_update_accounts()
  ant_u_a_3 = ant_unlock(ant_account3, ant_account3pw, ant_unlockTime)
  if ant_u_a_3 == False:
    if ant_account3pw == '':
     ant_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account3_n+' Passphrase Denied: '+ant_account3pw_r)
    elif ant_account3pw != '':
     print('Unlock Failure With Account '+ant_account3_n+' Passphrase Denied: '+ant_account3pw)
  if ant_u_a_3 == True:
   print(ant_account3_n+' Unlocked')

def ant_unlock_account_4():
  global ant_account4pw
  global ant_account4
  global ant_account4_n
  ant_update_accounts()
  ant_u_a_4 = ant_unlock(ant_account4, ant_account4pw, ant_unlockTime)
  if ant_u_a_4 == False:
    if ant_account4pw == '':
     ant_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account4_n+' Passphrase Denied: '+ant_account4pw_r)
    elif ant_account4pw != '':
     print('Unlock Failure With Account '+ant_account4_n+' Passphrase Denied: '+ant_account4pw)
  if ant_u_a_4 == True:
   print(ant_account4_n+' Unlocked')

def ant_unlock_account_5():
  global ant_account5pw
  global ant_account5
  global ant_account5_n
  ant_update_accounts()
  ant_u_a_5 = ant_unlock(ant_account5, ant_account5pw, ant_unlockTime)
  if ant_u_a_5 == False:
    if ant_account5pw == '':
     ant_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account5_n+' Passphrase Denied: '+ant_account5pw_r)
    elif ant_account5pw != '':
     print('Unlock Failure With Account '+ant_account5_n+' Passphrase Denied: '+ant_account5pw)
  if ant_u_a_5 == True:
   print(ant_account5_n+' Unlocked')

def ant_unlock_account_6():
  global ant_account6pw
  global ant_account6
  global ant_account6_n
  ant_update_accounts()
  ant_u_a_6 = ant_unlock(ant_account6, ant_account6pw, ant_unlockTime)
  if ant_u_a_6 == False:
    if ant_account6pw == '':
     ant_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ant_account6_n+' Passphrase Denied: '+ant_account6pw_r)
    elif ant_account6pw != '':
     print('Unlock Failure With Account '+ant_account6_n+' Passphrase Denied: '+ant_account6pw)
  if ant_u_a_6 == True:
   print(ant_account6_n+' Unlocked')

def ant_unlock_account(ant_ua_accountNumber):
 ant_update_accounts()
 ant_ua_account_number = ant_ua_accountNumber
 ant_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if ant_ua_account_number == ant_ua_input[0]:
  ant_unlock_account_0()
 if ant_ua_account_number == ant_ua_input[1]:
  ant_unlock_account_1()
 if ant_ua_account_number == ant_ua_input[2]:
  ant_unlock_account_2()
 if ant_ua_account_number == ant_ua_input[3]:
  ant_unlock_account_3()
 if ant_ua_account_number == ant_ua_input[4]:
  ant_unlock_account_4()
 if ant_ua_account_number == ant_ua_input[5]:
  ant_unlock_account_5()
 if ant_ua_account_number == ant_ua_input[6]:
  ant_unlock_account_6()
 if ant_ua_account_number not in ant_ua_input:
  print('Must Integer Within Range '+ant_accounts_range+'.')
 

def ant_approve_between_accounts(fromAccount, toAccount, msgValue):
  ant_update_accounts()
  ant_a_0 = ant.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(ant_a_0)

def ant_approve(fromAccountNumber, toAddress, msgValue):
  ant_update_accounts()
  ant_unlock_account(fromAccountNumber)
  ant_a_1 = ant.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(ant_a_1)

def ant_transfer_between_accounts(fromAccount, toAccount, msgValue):
  ant_update_accounts()
  ant_unlock_account(fromAccount)
  ant_t_0 = ant.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(ant_t_0)

def ant_transfer(fromAccountNumber, toAddress, msgValue):
  ant_update_accounts()
  ant_unlock_account(fromAccountNumber)
  ant_t_1 = ant.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(ant_t_1)

def ant_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  ant_update_accounts()
  ant_unlock_account(callAccount)
  ant_tf_0 = ant.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(ant_tf_0)

def ant_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  ant_update_accounts()
  ant_unlock_account(callAccount)
  ant_tf_1 = ant.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(ant_tf_1)
  


def ant_help():
  print('Following Functions For '+ant_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * ant_unlock => web3.personal.unlockAccount
/ * ant_accounts => web3.personal.listAccounts
/ * ant_balance = web3.eth.getBalance
** ant => web3.eth.contract(abi=ant_abi, address=ant_address)
** / * ant_balanceOf => ant.call().balanceOf

~ Function Listing Below:
~ ant_update_accounts()
~ ant_update_balances() \n\r -- => ant_update_accounts()
~ ant_list_all_accounts() \n\r -- => ant_update_accounts()
~ ant_account_balance(accountNumber) \n\r -- => ant_update_balances() 
~ ant_list_all_account_balances() \n\r -- => ant_update_balances()
~ ant_unlock_all_accounts() \n\r -- => ant_unlock_account_0() \n\r -- => ant_unlock_account_1() \n\r -- => ant_unlock_account_2() \n\r -- => ant_unlock_account_3() \n\r -- => ant_unlock_account_4() \n\r -- => ant_unlock_account_5() \n\r -- => ant_unlock_account_6() 
~ ant_unlock_account_0() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account0, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_1() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account1, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_2() \n\r -- => ant_update_accounts() \n\r --/ *ant_w_unlock(ant_account2, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_3() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account3, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_4() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account4, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_5() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account5, ant_account0pw, ant_unlockTime)
~ ant_unlock_account_6() \n\r -- => ant_update_accounts() \n\r -- / *ant_w_unlock(ant_account6, ant_account0pw, ant_unlockTime)
~ ant_unlock_account(ant_ua_accountNumber) \n\r -- => ant_update_accounts() \n\r -- // ant_unlock_account_0() \n\r -- // ant_unlock_account_1() \n\r -- // ant_unlock_account_2() \n\r -- // ant_unlock_account_3() \n\r -- // ant_unlock_account_4() \n\r -- // ant_unlock_account_5() \n\r -- // ant_unlock_account_6()
~ ant_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(fromAccount) \n\r -- / ** ant.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ant_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(fromAccountNumber) \n\r -- / ** ant.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ant_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(fromAccount) \n\r -- / ** ant.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ ant_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(fromAccountNumber) \n\r -- / ** ant.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ant_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(callAccount) \n\r / ** ant.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ant_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ant_update_accounts() \n\r -- => ant_unlock_account(callAccount) \n\r -- / ** ant.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ ant_help() <-- You Are Here. ''')