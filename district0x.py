#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global dnt_account_0_a
global dnt_account_1_a
global dnt_account_2_a
global dnt_account_3_a
global dnt_account_4_a
global dnt_account_5_a
global dnt_account_6_a
global dnt_address
global dnt_abi
global dnt
global dnt_call_0
global dnt_call_1
global dnt_call_2
global dnt_call_3
global dnt_call_4
global dnt_call_5
global dnt_call_6
global dnt_call_ab
global dnt_accounts
global dnt_account_0_pw
global dnt_account_1_pw
global dnt_account_2_pw
global dnt_account_3_pw
global dnt_account_4_pw
global dnt_account_5_pw
global dnt_account_6_pw
global dnt_account_0_n
global dnt_account_1_n
global dnt_account_2_n
global dnt_account_3_n
global dnt_account_4_n
global dnt_account_5_n
global dnt_account_6_n
global dnt_account1pw
global dnt_account2pw
global dnt_account3pw
global dnt_account4pw
global dnt_account5pw
global dnt_account6pw
global dnt_last_price
global dnt_accounts_range
global dnt_tokenName
global dnt_last_ethereum_price
global dnt_unlockTime
global dnt_balance
global dnt_balanceOf
global dnt_unlock
global dnt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
dnt_token_d = 1e18
_e_d = 1e18
dnt_accounts_range = '[0, 6]'
dnt_unlock = web3.personal.unlockAccount
dnt_last_ethereum_price = 370.00
dnt_last_price = 0.11
dnt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
dnt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
dnt_tokenName = 'district0x Token'
dnt_unlockTime = hex(10000) # Must be hex()
dnt_account_0_a = dnt_accounts[0]
dnt_account_1_a = dnt_accounts[1]
dnt_account_2_a = dnt_accounts[2]
dnt_account_3_a = dnt_accounts[3]
dnt_account_4_a = dnt_accounts[4]
dnt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
dnt_account_6_a = dnt_accounts[6]
# Supply Unlock Passwords For Transactions Below
dnt_account_0_pw = 'GuildSkrypt2017!@#'
dnt_account_1_pw = ''
dnt_account_2_pw = 'GuildSkrypt2017!@#'
dnt_account_3_pw = ''
dnt_account_4_pw = ''
dnt_account_5_pw = ''
dnt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
dnt_account_0_n = 'Skotys Bittrex Account'
dnt_account_1_n = 'Jeffs Account'
dnt_account_2_n = 'Skrypts Bittrex Account'
dnt_account_3_n = 'Skotys Personal Account'
dnt_account_4_n = 'Unknown'
dnt_account_5_n = 'Watched \'Bittrex\' Account.'
dnt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
dnt_address = '0x0AbdAce70D3790235af448C88547603b945604ea'
dnt_abi = [{"constant":true,"inputs":[{"name":"_holder","type":"address"}],"name":"tokenGrantsCount","outputs":[{"name":"index","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creationBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"grants","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"},{"name":"start","type":"uint64"},{"name":"revokable","type":"bool"},{"name":"burnsOnRevoke","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_blockNumber","type":"uint256"}],"name":"balanceOfAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"tokenGrant","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"vested","type":"uint256"},{"name":"start","type":"uint64"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"},{"name":"revokable","type":"bool"},{"name":"burnsOnRevoke","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_cloneTokenName","type":"string"},{"name":"_cloneDecimalUnits","type":"uint8"},{"name":"_cloneTokenSymbol","type":"string"},{"name":"_snapshotBlock","type":"uint256"},{"name":"_transfersEnabled","type":"bool"}],"name":"createCloneToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_claimer","type":"address"}],"name":"claimTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"}],"name":"lastTokenIsTransferableDate","outputs":[{"name":"date","type":"uint64"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentToken","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"generateTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"grantsController","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_start","type":"uint64"},{"name":"_cliff","type":"uint64"},{"name":"_vesting","type":"uint64"},{"name":"_revokable","type":"bool"},{"name":"_burnsOnRevoke","type":"bool"}],"name":"grantVestedTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_blockNumber","type":"uint256"}],"name":"totalSupplyAt","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"parentSnapShotBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holder","type":"address"}],"name":"revokeAllTokenGrants","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"},{"name":"time","type":"uint64"}],"name":"transferableTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroyTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"tokens","type":"uint256"},{"name":"time","type":"uint256"},{"name":"start","type":"uint256"},{"name":"cliff","type":"uint256"},{"name":"vesting","type":"uint256"}],"name":"calculateVestedTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newController","type":"address"}],"name":"changeGrantsController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"revokeTokenGrant","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_transfersEnabled","type":"bool"}],"name":"enableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[{"name":"_controller","type":"address"},{"name":"_tokenFactory","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"grantId","type":"uint256"}],"name":"NewTokenGrant","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_token","type":"address"},{"indexed":true,"name":"_claimer","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"ClaimedTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_cloneToken","type":"address"},{"indexed":false,"name":"_snapshotBlock","type":"uint256"}],"name":"NewCloneToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Approval","type":"event"}]
dnt = web3.eth.contract(abi=dnt_abi, address=dnt_address)
dnt_balanceOf = dnt.call().balanceOf
# End Contract Information
def dnt_update_accounts():
 global dnt_account0
 global dnt_account1
 global dnt_account2
 global dnt_account3
 global dnt_account4
 global dnt_account5
 global dnt_account6
 global dnt_account0_n
 global dnt_account1_n
 global dnt_account2_n
 global dnt_account3_n
 global dnt_account4_n
 global dnt_account5_n
 global dnt_account6_n
 global dnt_account0pw
 global dnt_account1pw
 global dnt_account2pw
 global dnt_account3pw
 global dnt_account4pw
 global dnt_account5pw
 global dnt_account6pw
 dnt_account0 = dnt_account_0_a
 dnt_account1 = dnt_account_1_a
 dnt_account2 = dnt_account_2_a
 dnt_account3 = dnt_account_3_a
 dnt_account4 = dnt_account_4_a
 dnt_account5 = dnt_account_5_a
 dnt_account6 = dnt_account_6_a
 dnt_account0_n = dnt_account_0_n
 dnt_account1_n = dnt_account_1_n
 dnt_account2_n = dnt_account_2_n
 dnt_account3_n = dnt_account_3_n
 dnt_account4_n = dnt_account_4_n
 dnt_account5_n = dnt_account_5_n
 dnt_account6_n = dnt_account_6_n
 dnt_account0pw = dnt_account_0_pw
 dnt_account1pw = dnt_account_1_pw
 dnt_account2pw = dnt_account_2_pw
 dnt_account3pw = dnt_account_3_pw
 dnt_account4pw = dnt_account_4_pw
 dnt_account5pw = dnt_account_5_pw
 dnt_account6pw = dnt_account_6_pw
 print(dnt_tokenName+' Accounts Updated.')
def dnt_update_balances():
 global dnt_call_0
 global dnt_call_1
 global dnt_call_2
 global dnt_call_3
 global dnt_call_4
 global dnt_call_5
 global dnt_call_6
 global dnt_w_call_0
 global dnt_w_call_1
 global dnt_w_call_2
 global dnt_w_call_3
 global dnt_w_call_4
 global dnt_w_call_5
 global dnt_w_call_6
 dnt_update_accounts()
 print('Updating '+dnt_tokenName+' Balances Please Wait...')
 dnt_call_0 = dnt_balanceOf(dnt_account0)
 dnt_call_1 = dnt_balanceOf(dnt_account1)
 dnt_call_2 = dnt_balanceOf(dnt_account2)
 dnt_call_3 = dnt_balanceOf(dnt_account3)
 dnt_call_4 = dnt_balanceOf(dnt_account4)
 dnt_call_5 = dnt_balanceOf(dnt_account5)
 dnt_call_6 = dnt_balanceOf(dnt_account6)
 dnt_w_call_0 = dnt_balance(dnt_account0)
 dnt_w_call_1 = dnt_balance(dnt_account1)
 dnt_w_call_2 = dnt_balance(dnt_account2)
 dnt_w_call_3 = dnt_balance(dnt_account3)
 dnt_w_call_4 = dnt_balance(dnt_account4)
 dnt_w_call_5 = dnt_balance(dnt_account5)
 dnt_w_call_6 = dnt_balance(dnt_account6)
 print(dnt_tokenName+' Balances Updated.')
def dnt_list_all_accounts():
 dnt_update_accounts()
 print(dnt_tokenName+' '+dnt_account0_n+': '+dnt_account0)
 print(dnt_tokenName+' '+dnt_account1_n+': '+dnt_account1)
 print(dnt_tokenName+' '+dnt_account2_n+': '+dnt_account2)
 print(dnt_tokenName+' '+dnt_account3_n+': '+dnt_account3)
 print(dnt_tokenName+' '+dnt_account4_n+': '+dnt_account4)
 print(dnt_tokenName+' '+dnt_account5_n+': '+dnt_account5)
 print(dnt_tokenName+' '+dnt_account6_n+': '+dnt_account6)

def dnt_account_balance(accountNumber):
 dnt_update_balances()
 dnt_ab_account_number = accountNumber
 dnt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if dnt_ab_account_number == dnt_ab_input[0]:
  print('Calling '+dnt_account0_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account0_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_0 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_0 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[1]:
  print('Calling '+dnt_account1_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account1_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_1 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_1 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[2]:
  print('Calling '+dnt_account2_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account2_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_2 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_2 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[3]:
  print('Calling '+dnt_account3_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account3_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_3 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_3 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[4]:
  print('Calling '+dnt_account4_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account4_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_4 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_4 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[5]:
  print('Calling '+dnt_account5_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account5_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_5 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_5 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number == dnt_ab_input[6]:
  print('Calling '+dnt_account6_n+' '+dnt_tokenName+' Balance: ')
  print(dnt_account6_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_6 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_6 / dnt_token_d * dnt_last_price))
 if dnt_ab_account_number not in dnt_ab_input:
  print('Must Integer Within Range '+dnt_accounts_range+'.')

def dnt_list_all_account_balances():
 dnt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+dnt_tokenName+' Balance: ')
 print(dnt_account0_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_0 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_0 / dnt_token_d * dnt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(dnt_account0_n+': Ethereum Balance '+str(dnt_w_call_0 / _e_d)+' $'+str(dnt_w_call_0 / _e_d * dnt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+dnt_tokenName+' Balance: ')
 print(dnt_account1_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_1 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_1 / dnt_token_d * dnt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(dnt_account1_n+': Ethereum Balance '+str(dnt_w_call_1 / _e_d)+' $'+str(dnt_w_call_1 / _e_d * dnt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+dnt_tokenName+' Balance: ')
 print(dnt_account2_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_2 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_2 / dnt_token_d * dnt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(dnt_account2_n+': Ethereum Balance '+str(dnt_w_call_2 / _e_d)+' $'+str(dnt_w_call_2 / _e_d * dnt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+dnt_tokenName+' Balance: ')
 print(dnt_account3_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_3 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_3 / dnt_token_d * dnt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(dnt_account3_n+': Ethereum Balance '+str(dnt_w_call_3 / _e_d)+' $'+str(dnt_w_call_3 / _e_d * dnt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+dnt_tokenName+' Balance: ')
 print(dnt_account4_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_4 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_4 / dnt_token_d * dnt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(dnt_account4_n+': Ethereum Balance '+str(dnt_w_call_4 / _e_d)+' $'+str(dnt_w_call_4 / _e_d * dnt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+dnt_tokenName+' Balance: ')
 print(dnt_account5_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_5 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_5 / dnt_token_d * dnt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(dnt_account5_n+': Ethereum Balance '+str(dnt_w_call_5 / _e_d)+' $'+str(dnt_w_call_5 /_e_d * dnt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+dnt_tokenName+' Balance: ')
 print(dnt_account6_n+': '+dnt_tokenName+' Balance: '+str(dnt_call_6 / dnt_token_d)+' Usd/'+dnt_tokenName+' Balance: $'+str(dnt_call_6 / dnt_token_d * dnt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(dnt_account6_n+': Ethereum Balance '+str(dnt_w_call_6 / _e_d)+' $'+str(dnt_w_call_6 / _e_d * dnt_last_ethereum_price))
def dnt_unlock_all_accounts():
  dnt_unlock_account_0()
  dnt_unlock_account_1()
  dnt_unlock_account_2()
  dnt_unlock_account_3()
  dnt_unlock_account_4()
  dnt_unlock_account_5()
  dnt_unlock_account_6()


def dnt_unlock_account_0():
  global dnt_account0pw
  global dnt_account0
  global dnt_account0_n
  dnt_update_accounts()
  dnt_u_a_0 = dnt_w_unlock(dnt_account0, dnt_account0pw, dnt_unlockTime)
  if dnt_u_a_0 == False:
    if dnt_account0pw == '':
     dnt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account0_n+' Passphrase Denied: '+dnt_account0pw_r)
    elif dnt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+dnt_account0_n+' Passphrase Denied: '+dnt_account0pw)
  if dnt_u_a_0 == True:
   print(dnt_account0_n+' Unlocked')

def dnt_unlock_account_1():
  global dnt_account1pw
  global dnt_account1
  global dnt_account1_n
  dnt_update_accounts()
  dnt_u_a_1 = dnt_unlock(dnt_account1, dnt_account1pw, dnt_unlockTime)
  if dnt_u_a_1 == False:
    if dnt_account1pw == '':
     dnt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account1_n+' Passphrase Denied: '+dnt_account1pw_r)
    elif dnt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+dnt_account1_n+' Passphrase Denied: '+dnt_account1pw)
  if dnt_u_a_1 == True:
   print(dnt_account1_n+' Unlocked')

def dnt_unlock_account_2():
  global dnt_account2pw
  global dnt_account2
  global dnt_account2_n
  dnt_update_accounts()
  dnt_u_a_2 = dnt_unlock(dnt_account2, dnt_account2pw, dnt_unlockTime)
  if dnt_u_a_2 == False:
    if dnt_account2pw == '':
     dnt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account2_n+' Passphrase Denied: '+dnt_account2pw_r)
    elif dnt_account2pw != '':
     print('Unlock Failure With Account '+dnt_account2_n+' Passphrase Denied: '+dnt_account2pw)
  if dnt_u_a_2 == True:
   print(dnt_account2_n+' Unlocked')

def dnt_unlock_account_3():
  global dnt_account3pw
  global dnt_account3
  global dnt_account3_n
  dnt_update_accounts()
  dnt_u_a_3 = dnt_unlock(dnt_account3, dnt_account3pw, dnt_unlockTime)
  if dnt_u_a_3 == False:
    if dnt_account3pw == '':
     dnt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account3_n+' Passphrase Denied: '+dnt_account3pw_r)
    elif dnt_account3pw != '':
     print('Unlock Failure With Account '+dnt_account3_n+' Passphrase Denied: '+dnt_account3pw)
  if dnt_u_a_3 == True:
   print(dnt_account3_n+' Unlocked')

def dnt_unlock_account_4():
  global dnt_account4pw
  global dnt_account4
  global dnt_account4_n
  dnt_update_accounts()
  dnt_u_a_4 = dnt_unlock(dnt_account4, dnt_account4pw, dnt_unlockTime)
  if dnt_u_a_4 == False:
    if dnt_account4pw == '':
     dnt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account4_n+' Passphrase Denied: '+dnt_account4pw_r)
    elif dnt_account4pw != '':
     print('Unlock Failure With Account '+dnt_account4_n+' Passphrase Denied: '+dnt_account4pw)
  if dnt_u_a_4 == True:
   print(dnt_account4_n+' Unlocked')

def dnt_unlock_account_5():
  global dnt_account5pw
  global dnt_account5
  global dnt_account5_n
  dnt_update_accounts()
  dnt_u_a_5 = dnt_unlock(dnt_account5, dnt_account5pw, dnt_unlockTime)
  if dnt_u_a_5 == False:
    if dnt_account5pw == '':
     dnt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account5_n+' Passphrase Denied: '+dnt_account5pw_r)
    elif dnt_account5pw != '':
     print('Unlock Failure With Account '+dnt_account5_n+' Passphrase Denied: '+dnt_account5pw)
  if dnt_u_a_5 == True:
   print(dnt_account5_n+' Unlocked')

def dnt_unlock_account_6():
  global dnt_account6pw
  global dnt_account6
  global dnt_account6_n
  dnt_update_accounts()
  dnt_u_a_6 = dnt_unlock(dnt_account6, dnt_account6pw, dnt_unlockTime)
  if dnt_u_a_6 == False:
    if dnt_account6pw == '':
     dnt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+dnt_account6_n+' Passphrase Denied: '+dnt_account6pw_r)
    elif dnt_account6pw != '':
     print('Unlock Failure With Account '+dnt_account6_n+' Passphrase Denied: '+dnt_account6pw)
  if dnt_u_a_6 == True:
   print(dnt_account6_n+' Unlocked')

def dnt_unlock_account(dnt_ua_accountNumber):
 dnt_update_accounts()
 dnt_ua_account_number = dnt_ua_accountNumber
 dnt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if dnt_ua_account_number == dnt_ua_input[0]:
  dnt_unlock_account_0()
 if dnt_ua_account_number == dnt_ua_input[1]:
  dnt_unlock_account_1()
 if dnt_ua_account_number == dnt_ua_input[2]:
  dnt_unlock_account_2()
 if dnt_ua_account_number == dnt_ua_input[3]:
  dnt_unlock_account_3()
 if dnt_ua_account_number == dnt_ua_input[4]:
  dnt_unlock_account_4()
 if dnt_ua_account_number == dnt_ua_input[5]:
  dnt_unlock_account_5()
 if dnt_ua_account_number == dnt_ua_input[6]:
  dnt_unlock_account_6()
 if dnt_ua_account_number not in dnt_ua_input:
  print('Must Integer Within Range '+dnt_accounts_range+'.')
 

def dnt_approve_between_accounts(fromAccount, toAccount, msgValue):
  dnt_update_accounts()
  dnt_a_0 = dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(dnt_a_0)

def dnt_approve(fromAccountNumber, toAddress, msgValue):
  dnt_update_accounts()
  dnt_unlock_account(fromAccountNumber)
  dnt_a_1 = dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(dnt_a_1)

def dnt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  dnt_update_accounts()
  dnt_unlock_account(fromAccount)
  dnt_t_0 = dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(dnt_t_0)

def dnt_transfer(fromAccountNumber, toAddress, msgValue):
  dnt_update_accounts()
  dnt_unlock_account(fromAccountNumber)
  dnt_t_1 = dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(dnt_t_1)

def dnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  dnt_update_accounts()
  dnt_unlock_account(callAccount)
  dnt_tf_0 = dnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(dnt_tf_0)

def dnt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  dnt_update_accounts()
  dnt_unlock_account(callAccount)
  dnt_tf_1 = dnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(dnt_tf_1)
  


def dnt_help():
  print('Following Functions For '+dnt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * dnt_unlock => web3.personal.unlockAccount
/ * dnt_accounts => web3.personal.listAccounts
/ * dnt_balance = web3.eth.getBalance
** dnt => web3.eth.contract(abi=dnt_abi, address=dnt_address)
** / * dnt_balanceOf => dnt.call().balanceOf

~ Function Listing Below:
~ dnt_update_accounts()
~ dnt_update_balances() \n\r -- => dnt_update_accounts()
~ dnt_list_all_accounts() \n\r -- => dnt_update_accounts()
~ dnt_account_balance(accountNumber) \n\r -- => dnt_update_balances() 
~ dnt_list_all_account_balances() \n\r -- => dnt_update_balances()
~ dnt_unlock_all_accounts() \n\r -- => dnt_unlock_account_0() \n\r -- => dnt_unlock_account_1() \n\r -- => dnt_unlock_account_2() \n\r -- => dnt_unlock_account_3() \n\r -- => dnt_unlock_account_4() \n\r -- => dnt_unlock_account_5() \n\r -- => dnt_unlock_account_6() 
~ dnt_unlock_account_0() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account0, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_1() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account1, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_2() \n\r -- => dnt_update_accounts() \n\r --/ *dnt_w_unlock(dnt_account2, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_3() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account3, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_4() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account4, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_5() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account5, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account_6() \n\r -- => dnt_update_accounts() \n\r -- / *dnt_w_unlock(dnt_account6, dnt_account0pw, dnt_unlockTime)
~ dnt_unlock_account(dnt_ua_accountNumber) \n\r -- => dnt_update_accounts() \n\r -- // dnt_unlock_account_0() \n\r -- // dnt_unlock_account_1() \n\r -- // dnt_unlock_account_2() \n\r -- // dnt_unlock_account_3() \n\r -- // dnt_unlock_account_4() \n\r -- // dnt_unlock_account_5() \n\r -- // dnt_unlock_account_6()
~ dnt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(fromAccount) \n\r -- / ** dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ dnt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(fromAccountNumber) \n\r -- / ** dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ dnt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(fromAccount) \n\r -- / ** dnt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ dnt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(fromAccountNumber) \n\r -- / ** dnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ dnt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(callAccount) \n\r / ** dnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ dnt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => dnt_update_accounts() \n\r -- => dnt_unlock_account(callAccount) \n\r -- / ** dnt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ dnt_help() <-- You Are Here. ''')