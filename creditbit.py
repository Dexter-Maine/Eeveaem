#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global crb_account_0_a
global crb_account_1_a
global crb_account_2_a
global crb_account_3_a
global crb_account_4_a
global crb_account_5_a
global crb_account_6_a
global crb_address
global crb_abi
global crb
global crb_call_0
global crb_call_1
global crb_call_2
global crb_call_3
global crb_call_4
global crb_call_5
global crb_call_6
global crb_call_ab
global crb_accounts
global crb_account_0_pw
global crb_account_1_pw
global crb_account_2_pw
global crb_account_3_pw
global crb_account_4_pw
global crb_account_5_pw
global crb_account_6_pw
global crb_account_0_n
global crb_account_1_n
global crb_account_2_n
global crb_account_3_n
global crb_account_4_n
global crb_account_5_n
global crb_account_6_n
global crb_account1pw
global crb_account2pw
global crb_account3pw
global crb_account4pw
global crb_account5pw
global crb_account6pw
global crb_last_price
global crb_accounts_range
global crb_tokenName
global crb_last_ethereum_price
global crb_unlockTime
global crb_balance
global crb_balanceOf
global crb_unlock
global crb_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
crb_token_d = 1e8
_e_d = 1e18
crb_accounts_range = '[0, 6]'
crb_unlock = web3.personal.unlockAccount
crb_last_ethereum_price = 370.00
crb_last_price = 0.69
crb_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
crb_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
crb_tokenName = 'CreditBIT Token'
crb_unlockTime = hex(10000) # Must be hex()
crb_account_0_a = crb_accounts[0]
crb_account_1_a = crb_accounts[1]
crb_account_2_a = crb_accounts[2]
crb_account_3_a = crb_accounts[3]
crb_account_4_a = crb_accounts[4]
crb_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
crb_account_6_a = crb_accounts[6]
# Supply Unlock Passwords For Transactions Below
crb_account_0_pw = 'GuildSkrypt2017!@#'
crb_account_1_pw = ''
crb_account_2_pw = 'GuildSkrypt2017!@#'
crb_account_3_pw = ''
crb_account_4_pw = ''
crb_account_5_pw = ''
crb_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
crb_account_0_n = 'Skotys Bittrex Account'
crb_account_1_n = 'Jeffs Account'
crb_account_2_n = 'Skrypts Bittrex Account'
crb_account_3_n = 'Skotys Personal Account'
crb_account_4_n = 'Unknown'
crb_account_5_n = 'Watched \'Bittrex\' Account.'
crb_account_6_n = 'Watched Account (1)'
# Contract Information Below :
crb_address = '0xAef38fBFBF932D1AeF3B808Bc8fBd8Cd8E1f8BC5'
crb_abi = [{"constant":true,"inputs":[],"name":"getCreditBondAddress","outputs":[{"name":"bondAddress","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_gameAddress","type":"address"}],"name":"setCreditGameAddress","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalLockedSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint256"},{"name":"_lockForBlocks","type":"uint256"}],"name":"lockBalance","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_reciever","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mintMigrationTokens","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lockdown","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_daoAddress","type":"address"}],"name":"setCreditDaoAddress","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creditDaoAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"lockedBalanceOf","outputs":[{"name":"avaliableBalance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"getAccountData","outputs":[{"name":"avaliableBalance","type":"uint256"},{"name":"lockedBalance","type":"uint256"},{"name":"bondMultiplier","type":"uint256"},{"name":"lockedUntilBlock","type":"uint256"},{"name":"lastBlockClaimed","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"claimBondReward","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"avaliableBalance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_champion","type":"address"},{"name":"_lockedTokenAmount","type":"uint256"},{"name":"_lockTime","type":"uint256"}],"name":"claimGameReward","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"dev","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creditGameAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_bondAddress","type":"address"}],"name":"setCreditBond","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"lockToken","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_mcAddress","type":"address"}],"name":"setCreditMcAddress","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint256"}],"name":"mintBonusTokensForGames","outputs":[{"name":"error","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalAvaliableSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"creditMcAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_owner","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_numberOfBlocks","type":"uint256"}],"name":"LockCredits","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_owner","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"UnlockCredits","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_owner","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
crb = web3.eth.contract(abi=crb_abi, address=crb_address)
crb_balanceOf = crb.call().balanceOf
# End Contract Information
def crb_update_accounts():
 global crb_account0
 global crb_account1
 global crb_account2
 global crb_account3
 global crb_account4
 global crb_account5
 global crb_account6
 global crb_account0_n
 global crb_account1_n
 global crb_account2_n
 global crb_account3_n
 global crb_account4_n
 global crb_account5_n
 global crb_account6_n
 global crb_account0pw
 global crb_account1pw
 global crb_account2pw
 global crb_account3pw
 global crb_account4pw
 global crb_account5pw
 global crb_account6pw
 crb_account0 = crb_account_0_a
 crb_account1 = crb_account_1_a
 crb_account2 = crb_account_2_a
 crb_account3 = crb_account_3_a
 crb_account4 = crb_account_4_a
 crb_account5 = crb_account_5_a
 crb_account6 = crb_account_6_a
 crb_account0_n = crb_account_0_n
 crb_account1_n = crb_account_1_n
 crb_account2_n = crb_account_2_n
 crb_account3_n = crb_account_3_n
 crb_account4_n = crb_account_4_n
 crb_account5_n = crb_account_5_n
 crb_account6_n = crb_account_6_n
 crb_account0pw = crb_account_0_pw
 crb_account1pw = crb_account_1_pw
 crb_account2pw = crb_account_2_pw
 crb_account3pw = crb_account_3_pw
 crb_account4pw = crb_account_4_pw
 crb_account5pw = crb_account_5_pw
 crb_account6pw = crb_account_6_pw
 print(crb_tokenName+' Accounts Updated.')
def crb_update_balances():
 global crb_call_0
 global crb_call_1
 global crb_call_2
 global crb_call_3
 global crb_call_4
 global crb_call_5
 global crb_call_6
 global crb_w_call_0
 global crb_w_call_1
 global crb_w_call_2
 global crb_w_call_3
 global crb_w_call_4
 global crb_w_call_5
 global crb_w_call_6
 crb_update_accounts()
 print('Updating '+crb_tokenName+' Balances Please Wait...')
 crb_call_0 = crb_balanceOf(crb_account0)
 crb_call_1 = crb_balanceOf(crb_account1)
 crb_call_2 = crb_balanceOf(crb_account2)
 crb_call_3 = crb_balanceOf(crb_account3)
 crb_call_4 = crb_balanceOf(crb_account4)
 crb_call_5 = crb_balanceOf(crb_account5)
 crb_call_6 = crb_balanceOf(crb_account6)
 crb_w_call_0 = crb_balance(crb_account0)
 crb_w_call_1 = crb_balance(crb_account1)
 crb_w_call_2 = crb_balance(crb_account2)
 crb_w_call_3 = crb_balance(crb_account3)
 crb_w_call_4 = crb_balance(crb_account4)
 crb_w_call_5 = crb_balance(crb_account5)
 crb_w_call_6 = crb_balance(crb_account6)
 print(crb_tokenName+' Balances Updated.')
def crb_list_all_accounts():
 crb_update_accounts()
 print(crb_tokenName+' '+crb_account0_n+': '+crb_account0)
 print(crb_tokenName+' '+crb_account1_n+': '+crb_account1)
 print(crb_tokenName+' '+crb_account2_n+': '+crb_account2)
 print(crb_tokenName+' '+crb_account3_n+': '+crb_account3)
 print(crb_tokenName+' '+crb_account4_n+': '+crb_account4)
 print(crb_tokenName+' '+crb_account5_n+': '+crb_account5)
 print(crb_tokenName+' '+crb_account6_n+': '+crb_account6)

def crb_account_balance(accountNumber):
 crb_update_balances()
 crb_ab_account_number = accountNumber
 crb_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if crb_ab_account_number == crb_ab_input[0]:
  print('Calling '+crb_account0_n+' '+crb_tokenName+' Balance: ')
  print(crb_account0_n+': '+crb_tokenName+' Balance: '+str(crb_call_0 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_0 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[1]:
  print('Calling '+crb_account1_n+' '+crb_tokenName+' Balance: ')
  print(crb_account1_n+': '+crb_tokenName+' Balance: '+str(crb_call_1 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_1 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[2]:
  print('Calling '+crb_account2_n+' '+crb_tokenName+' Balance: ')
  print(crb_account2_n+': '+crb_tokenName+' Balance: '+str(crb_call_2 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_2 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[3]:
  print('Calling '+crb_account3_n+' '+crb_tokenName+' Balance: ')
  print(crb_account3_n+': '+crb_tokenName+' Balance: '+str(crb_call_3 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_3 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[4]:
  print('Calling '+crb_account4_n+' '+crb_tokenName+' Balance: ')
  print(crb_account4_n+': '+crb_tokenName+' Balance: '+str(crb_call_4 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_4 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[5]:
  print('Calling '+crb_account5_n+' '+crb_tokenName+' Balance: ')
  print(crb_account5_n+': '+crb_tokenName+' Balance: '+str(crb_call_5 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_5 / crb_token_d * crb_last_price))
 if crb_ab_account_number == crb_ab_input[6]:
  print('Calling '+crb_account6_n+' '+crb_tokenName+' Balance: ')
  print(crb_account6_n+': '+crb_tokenName+' Balance: '+str(crb_call_6 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_6 / crb_token_d * crb_last_price))
 if crb_ab_account_number not in crb_ab_input:
  print('Must Integer Within Range '+crb_accounts_range+'.')

def crb_list_all_account_balances():
 crb_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+crb_tokenName+' Balance: ')
 print(crb_account0_n+': '+crb_tokenName+' Balance: '+str(crb_call_0 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_0 / crb_token_d * crb_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(crb_account0_n+': Ethereum Balance '+str(crb_w_call_0 / _e_d)+' $'+str(crb_w_call_0 / _e_d * crb_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+crb_tokenName+' Balance: ')
 print(crb_account1_n+': '+crb_tokenName+' Balance: '+str(crb_call_1 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_1 / crb_token_d * crb_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(crb_account1_n+': Ethereum Balance '+str(crb_w_call_1 / _e_d)+' $'+str(crb_w_call_1 / _e_d * crb_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+crb_tokenName+' Balance: ')
 print(crb_account2_n+': '+crb_tokenName+' Balance: '+str(crb_call_2 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_2 / crb_token_d * crb_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(crb_account2_n+': Ethereum Balance '+str(crb_w_call_2 / _e_d)+' $'+str(crb_w_call_2 / _e_d * crb_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+crb_tokenName+' Balance: ')
 print(crb_account3_n+': '+crb_tokenName+' Balance: '+str(crb_call_3 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_3 / crb_token_d * crb_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(crb_account3_n+': Ethereum Balance '+str(crb_w_call_3 / _e_d)+' $'+str(crb_w_call_3 / _e_d * crb_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+crb_tokenName+' Balance: ')
 print(crb_account4_n+': '+crb_tokenName+' Balance: '+str(crb_call_4 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_4 / crb_token_d * crb_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(crb_account4_n+': Ethereum Balance '+str(crb_w_call_4 / _e_d)+' $'+str(crb_w_call_4 / _e_d * crb_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+crb_tokenName+' Balance: ')
 print(crb_account5_n+': '+crb_tokenName+' Balance: '+str(crb_call_5 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_5 / crb_token_d * crb_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(crb_account5_n+': Ethereum Balance '+str(crb_w_call_5 / _e_d)+' $'+str(crb_w_call_5 /_e_d * crb_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+crb_tokenName+' Balance: ')
 print(crb_account6_n+': '+crb_tokenName+' Balance: '+str(crb_call_6 / crb_token_d)+' Usd/'+crb_tokenName+' Balance: $'+str(crb_call_6 / crb_token_d * crb_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(crb_account6_n+': Ethereum Balance '+str(crb_w_call_6 / _e_d)+' $'+str(crb_w_call_6 / _e_d * crb_last_ethereum_price))
def crb_unlock_all_accounts():
  crb_unlock_account_0()
  crb_unlock_account_1()
  crb_unlock_account_2()
  crb_unlock_account_3()
  crb_unlock_account_4()
  crb_unlock_account_5()
  crb_unlock_account_6()


def crb_unlock_account_0():
  global crb_account0pw
  global crb_account0
  global crb_account0_n
  crb_update_accounts()
  crb_u_a_0 = crb_w_unlock(crb_account0, crb_account0pw, crb_unlockTime)
  if crb_u_a_0 == False:
    if crb_account0pw == '':
     crb_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account0_n+' Passphrase Denied: '+crb_account0pw_r)
    elif crb_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+crb_account0_n+' Passphrase Denied: '+crb_account0pw)
  if crb_u_a_0 == True:
   print(crb_account0_n+' Unlocked')

def crb_unlock_account_1():
  global crb_account1pw
  global crb_account1
  global crb_account1_n
  crb_update_accounts()
  crb_u_a_1 = crb_unlock(crb_account1, crb_account1pw, crb_unlockTime)
  if crb_u_a_1 == False:
    if crb_account1pw == '':
     crb_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account1_n+' Passphrase Denied: '+crb_account1pw_r)
    elif crb_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+crb_account1_n+' Passphrase Denied: '+crb_account1pw)
  if crb_u_a_1 == True:
   print(crb_account1_n+' Unlocked')

def crb_unlock_account_2():
  global crb_account2pw
  global crb_account2
  global crb_account2_n
  crb_update_accounts()
  crb_u_a_2 = crb_unlock(crb_account2, crb_account2pw, crb_unlockTime)
  if crb_u_a_2 == False:
    if crb_account2pw == '':
     crb_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account2_n+' Passphrase Denied: '+crb_account2pw_r)
    elif crb_account2pw != '':
     print('Unlock Failure With Account '+crb_account2_n+' Passphrase Denied: '+crb_account2pw)
  if crb_u_a_2 == True:
   print(crb_account2_n+' Unlocked')

def crb_unlock_account_3():
  global crb_account3pw
  global crb_account3
  global crb_account3_n
  crb_update_accounts()
  crb_u_a_3 = crb_unlock(crb_account3, crb_account3pw, crb_unlockTime)
  if crb_u_a_3 == False:
    if crb_account3pw == '':
     crb_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account3_n+' Passphrase Denied: '+crb_account3pw_r)
    elif crb_account3pw != '':
     print('Unlock Failure With Account '+crb_account3_n+' Passphrase Denied: '+crb_account3pw)
  if crb_u_a_3 == True:
   print(crb_account3_n+' Unlocked')

def crb_unlock_account_4():
  global crb_account4pw
  global crb_account4
  global crb_account4_n
  crb_update_accounts()
  crb_u_a_4 = crb_unlock(crb_account4, crb_account4pw, crb_unlockTime)
  if crb_u_a_4 == False:
    if crb_account4pw == '':
     crb_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account4_n+' Passphrase Denied: '+crb_account4pw_r)
    elif crb_account4pw != '':
     print('Unlock Failure With Account '+crb_account4_n+' Passphrase Denied: '+crb_account4pw)
  if crb_u_a_4 == True:
   print(crb_account4_n+' Unlocked')

def crb_unlock_account_5():
  global crb_account5pw
  global crb_account5
  global crb_account5_n
  crb_update_accounts()
  crb_u_a_5 = crb_unlock(crb_account5, crb_account5pw, crb_unlockTime)
  if crb_u_a_5 == False:
    if crb_account5pw == '':
     crb_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account5_n+' Passphrase Denied: '+crb_account5pw_r)
    elif crb_account5pw != '':
     print('Unlock Failure With Account '+crb_account5_n+' Passphrase Denied: '+crb_account5pw)
  if crb_u_a_5 == True:
   print(crb_account5_n+' Unlocked')

def crb_unlock_account_6():
  global crb_account6pw
  global crb_account6
  global crb_account6_n
  crb_update_accounts()
  crb_u_a_6 = crb_unlock(crb_account6, crb_account6pw, crb_unlockTime)
  if crb_u_a_6 == False:
    if crb_account6pw == '':
     crb_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+crb_account6_n+' Passphrase Denied: '+crb_account6pw_r)
    elif crb_account6pw != '':
     print('Unlock Failure With Account '+crb_account6_n+' Passphrase Denied: '+crb_account6pw)
  if crb_u_a_6 == True:
   print(crb_account6_n+' Unlocked')

def crb_unlock_account(crb_ua_accountNumber):
 crb_update_accounts()
 crb_ua_account_number = crb_ua_accountNumber
 crb_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if crb_ua_account_number == crb_ua_input[0]:
  crb_unlock_account_0()
 if crb_ua_account_number == crb_ua_input[1]:
  crb_unlock_account_1()
 if crb_ua_account_number == crb_ua_input[2]:
  crb_unlock_account_2()
 if crb_ua_account_number == crb_ua_input[3]:
  crb_unlock_account_3()
 if crb_ua_account_number == crb_ua_input[4]:
  crb_unlock_account_4()
 if crb_ua_account_number == crb_ua_input[5]:
  crb_unlock_account_5()
 if crb_ua_account_number == crb_ua_input[6]:
  crb_unlock_account_6()
 if crb_ua_account_number not in crb_ua_input:
  print('Must Integer Within Range '+crb_accounts_range+'.')
 

def crb_approve_between_accounts(fromAccount, toAccount, msgValue):
  crb_update_accounts()
  crb_a_0 = crb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(crb_a_0)

def crb_approve(fromAccountNumber, toAddress, msgValue):
  crb_update_accounts()
  crb_unlock_account(fromAccountNumber)
  crb_a_1 = crb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(crb_a_1)

def crb_transfer_between_accounts(fromAccount, toAccount, msgValue):
  crb_update_accounts()
  crb_unlock_account(fromAccount)
  crb_t_0 = crb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(crb_t_0)

def crb_transfer(fromAccountNumber, toAddress, msgValue):
  crb_update_accounts()
  crb_unlock_account(fromAccountNumber)
  crb_t_1 = crb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(crb_t_1)

def crb_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  crb_update_accounts()
  crb_unlock_account(callAccount)
  crb_tf_0 = crb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(crb_tf_0)

def crb_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  crb_update_accounts()
  crb_unlock_account(callAccount)
  crb_tf_1 = crb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(crb_tf_1)
  


def crb_help():
  print('Following Functions For '+crb_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * crb_unlock => web3.personal.unlockAccount
/ * crb_accounts => web3.personal.listAccounts
/ * crb_balance = web3.eth.getBalance
** crb => web3.eth.contract(abi=crb_abi, address=crb_address)
** / * crb_balanceOf => crb.call().balanceOf

~ Function Listing Below:
~ crb_update_accounts()
~ crb_update_balances() \n\r -- => crb_update_accounts()
~ crb_list_all_accounts() \n\r -- => crb_update_accounts()
~ crb_account_balance(accountNumber) \n\r -- => crb_update_balances() 
~ crb_list_all_account_balances() \n\r -- => crb_update_balances()
~ crb_unlock_all_accounts() \n\r -- => crb_unlock_account_0() \n\r -- => crb_unlock_account_1() \n\r -- => crb_unlock_account_2() \n\r -- => crb_unlock_account_3() \n\r -- => crb_unlock_account_4() \n\r -- => crb_unlock_account_5() \n\r -- => crb_unlock_account_6() 
~ crb_unlock_account_0() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account0, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_1() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account1, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_2() \n\r -- => crb_update_accounts() \n\r --/ *crb_w_unlock(crb_account2, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_3() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account3, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_4() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account4, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_5() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account5, crb_account0pw, crb_unlockTime)
~ crb_unlock_account_6() \n\r -- => crb_update_accounts() \n\r -- / *crb_w_unlock(crb_account6, crb_account0pw, crb_unlockTime)
~ crb_unlock_account(crb_ua_accountNumber) \n\r -- => crb_update_accounts() \n\r -- // crb_unlock_account_0() \n\r -- // crb_unlock_account_1() \n\r -- // crb_unlock_account_2() \n\r -- // crb_unlock_account_3() \n\r -- // crb_unlock_account_4() \n\r -- // crb_unlock_account_5() \n\r -- // crb_unlock_account_6()
~ crb_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(fromAccount) \n\r -- / ** crb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ crb_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(fromAccountNumber) \n\r -- / ** crb.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ crb_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(fromAccount) \n\r -- / ** crb.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ crb_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(fromAccountNumber) \n\r -- / ** crb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ crb_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(callAccount) \n\r / ** crb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ crb_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => crb_update_accounts() \n\r -- => crb_unlock_account(callAccount) \n\r -- / ** crb.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ crb_help() <-- You Are Here. ''')