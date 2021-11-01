#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global plr_account_0_a
global plr_account_1_a
global plr_account_2_a
global plr_account_3_a
global plr_account_4_a
global plr_account_5_a
global plr_account_6_a
global plr_address
global plr_abi
global plr
global plr_call_0
global plr_call_1
global plr_call_2
global plr_call_3
global plr_call_4
global plr_call_5
global plr_call_6
global plr_call_ab
global plr_accounts
global plr_account_0_pw
global plr_account_1_pw
global plr_account_2_pw
global plr_account_3_pw
global plr_account_4_pw
global plr_account_5_pw
global plr_account_6_pw
global plr_account_0_n
global plr_account_1_n
global plr_account_2_n
global plr_account_3_n
global plr_account_4_n
global plr_account_5_n
global plr_account_6_n
global plr_account1pw
global plr_account2pw
global plr_account3pw
global plr_account4pw
global plr_account5pw
global plr_account6pw
global plr_last_price
global plr_accounts_range
global plr_tokenName
global plr_last_ethereum_price
global plr_unlockTime
global plr_balance
global plr_balanceOf
global plr_unlock
global plr_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
plr_token_d = 1e18
_e_d = 1e18
plr_accounts_range = '[0, 6]'
plr_unlock = web3.personal.unlockAccount
plr_last_ethereum_price = 370.00
plr_last_price = 0.08
plr_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
plr_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
plr_tokenName = 'Pillar Token'
plr_unlockTime = hex(10000) # Must be hex()
plr_account_0_a = plr_accounts[0]
plr_account_1_a = plr_accounts[1]
plr_account_2_a = plr_accounts[2]
plr_account_3_a = plr_accounts[3]
plr_account_4_a = plr_accounts[4]
plr_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
plr_account_6_a = plr_accounts[6]
# Supply Unlock Passwords For Transactions Below
plr_account_0_pw = 'GuildSkrypt2017!@#'
plr_account_1_pw = ''
plr_account_2_pw = 'GuildSkrypt2017!@#'
plr_account_3_pw = ''
plr_account_4_pw = ''
plr_account_5_pw = ''
plr_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
plr_account_0_n = 'Skotys Bittrex Account'
plr_account_1_n = 'Jeffs Account'
plr_account_2_n = 'Skrypts Bittrex Account'
plr_account_3_n = 'Skotys Personal Account'
plr_account_4_n = 'Unknown'
plr_account_5_n = 'Watched \'Bittrex\' Account.'
plr_account_6_n = 'Watched Account (1)'
# Contract Information Below :
plr_address = '0xe3818504c1B32bF1557b16C238B2E01Fd3149C17'
plr_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"futureSaleVault","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"maxPresaleTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"numberOfTokensLeft","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lockedTeamAllocationTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minTokensForSale","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"twentyThirtyTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"purchase","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"teamAllocation","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"unlockedTeamStorageVault","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenPrice","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_tokens","type":"uint256"}],"name":"allocateTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"futureTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"twentyThirtyVault","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"twentyThirtyAllocation","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"allocateForRefund","outputs":[{"name":"","type":"uint256"}],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"unsoldTokens","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unPauseTokenSale","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"unlockedTeamAllocationTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"pillarTokenFactory","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"futureSaleAllocation","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalAvailableForSale","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingStopBlock","type":"uint256"}],"name":"startTokenSale","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pauseTokenSale","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_pillarTokenFactory","type":"address"},{"name":"_icedWallet","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Refund","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Migrate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_from","type":"address"},{"indexed":false,"name":"_value","type":"uint256"},{"indexed":false,"name":"_total","type":"uint256"}],"name":"MoneyAddedForRefund","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
plr = web3.eth.contract(abi=plr_abi, address=plr_address)
plr_balanceOf = plr.call().balanceOf
# End Contract Information
def plr_update_accounts():
 global plr_account0
 global plr_account1
 global plr_account2
 global plr_account3
 global plr_account4
 global plr_account5
 global plr_account6
 global plr_account0_n
 global plr_account1_n
 global plr_account2_n
 global plr_account3_n
 global plr_account4_n
 global plr_account5_n
 global plr_account6_n
 global plr_account0pw
 global plr_account1pw
 global plr_account2pw
 global plr_account3pw
 global plr_account4pw
 global plr_account5pw
 global plr_account6pw
 plr_account0 = plr_account_0_a
 plr_account1 = plr_account_1_a
 plr_account2 = plr_account_2_a
 plr_account3 = plr_account_3_a
 plr_account4 = plr_account_4_a
 plr_account5 = plr_account_5_a
 plr_account6 = plr_account_6_a
 plr_account0_n = plr_account_0_n
 plr_account1_n = plr_account_1_n
 plr_account2_n = plr_account_2_n
 plr_account3_n = plr_account_3_n
 plr_account4_n = plr_account_4_n
 plr_account5_n = plr_account_5_n
 plr_account6_n = plr_account_6_n
 plr_account0pw = plr_account_0_pw
 plr_account1pw = plr_account_1_pw
 plr_account2pw = plr_account_2_pw
 plr_account3pw = plr_account_3_pw
 plr_account4pw = plr_account_4_pw
 plr_account5pw = plr_account_5_pw
 plr_account6pw = plr_account_6_pw
 print(plr_tokenName+' Accounts Updated.')
def plr_update_balances():
 global plr_call_0
 global plr_call_1
 global plr_call_2
 global plr_call_3
 global plr_call_4
 global plr_call_5
 global plr_call_6
 global plr_w_call_0
 global plr_w_call_1
 global plr_w_call_2
 global plr_w_call_3
 global plr_w_call_4
 global plr_w_call_5
 global plr_w_call_6
 plr_update_accounts()
 print('Updating '+plr_tokenName+' Balances Please Wait...')
 plr_call_0 = plr_balanceOf(plr_account0)
 plr_call_1 = plr_balanceOf(plr_account1)
 plr_call_2 = plr_balanceOf(plr_account2)
 plr_call_3 = plr_balanceOf(plr_account3)
 plr_call_4 = plr_balanceOf(plr_account4)
 plr_call_5 = plr_balanceOf(plr_account5)
 plr_call_6 = plr_balanceOf(plr_account6)
 plr_w_call_0 = plr_balance(plr_account0)
 plr_w_call_1 = plr_balance(plr_account1)
 plr_w_call_2 = plr_balance(plr_account2)
 plr_w_call_3 = plr_balance(plr_account3)
 plr_w_call_4 = plr_balance(plr_account4)
 plr_w_call_5 = plr_balance(plr_account5)
 plr_w_call_6 = plr_balance(plr_account6)
 print(plr_tokenName+' Balances Updated.')
def plr_list_all_accounts():
 plr_update_accounts()
 print(plr_tokenName+' '+plr_account0_n+': '+plr_account0)
 print(plr_tokenName+' '+plr_account1_n+': '+plr_account1)
 print(plr_tokenName+' '+plr_account2_n+': '+plr_account2)
 print(plr_tokenName+' '+plr_account3_n+': '+plr_account3)
 print(plr_tokenName+' '+plr_account4_n+': '+plr_account4)
 print(plr_tokenName+' '+plr_account5_n+': '+plr_account5)
 print(plr_tokenName+' '+plr_account6_n+': '+plr_account6)

def plr_account_balance(accountNumber):
 plr_update_balances()
 plr_ab_account_number = accountNumber
 plr_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if plr_ab_account_number == plr_ab_input[0]:
  print('Calling '+plr_account0_n+' '+plr_tokenName+' Balance: ')
  print(plr_account0_n+': '+plr_tokenName+' Balance: '+str(plr_call_0 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_0 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[1]:
  print('Calling '+plr_account1_n+' '+plr_tokenName+' Balance: ')
  print(plr_account1_n+': '+plr_tokenName+' Balance: '+str(plr_call_1 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_1 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[2]:
  print('Calling '+plr_account2_n+' '+plr_tokenName+' Balance: ')
  print(plr_account2_n+': '+plr_tokenName+' Balance: '+str(plr_call_2 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_2 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[3]:
  print('Calling '+plr_account3_n+' '+plr_tokenName+' Balance: ')
  print(plr_account3_n+': '+plr_tokenName+' Balance: '+str(plr_call_3 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_3 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[4]:
  print('Calling '+plr_account4_n+' '+plr_tokenName+' Balance: ')
  print(plr_account4_n+': '+plr_tokenName+' Balance: '+str(plr_call_4 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_4 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[5]:
  print('Calling '+plr_account5_n+' '+plr_tokenName+' Balance: ')
  print(plr_account5_n+': '+plr_tokenName+' Balance: '+str(plr_call_5 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_5 / plr_token_d * plr_last_price))
 if plr_ab_account_number == plr_ab_input[6]:
  print('Calling '+plr_account6_n+' '+plr_tokenName+' Balance: ')
  print(plr_account6_n+': '+plr_tokenName+' Balance: '+str(plr_call_6 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_6 / plr_token_d * plr_last_price))
 if plr_ab_account_number not in plr_ab_input:
  print('Must Integer Within Range '+plr_accounts_range+'.')

def plr_list_all_account_balances():
 plr_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+plr_tokenName+' Balance: ')
 print(plr_account0_n+': '+plr_tokenName+' Balance: '+str(plr_call_0 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_0 / plr_token_d * plr_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(plr_account0_n+': Ethereum Balance '+str(plr_w_call_0 / _e_d)+' $'+str(plr_w_call_0 / _e_d * plr_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+plr_tokenName+' Balance: ')
 print(plr_account1_n+': '+plr_tokenName+' Balance: '+str(plr_call_1 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_1 / plr_token_d * plr_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(plr_account1_n+': Ethereum Balance '+str(plr_w_call_1 / _e_d)+' $'+str(plr_w_call_1 / _e_d * plr_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+plr_tokenName+' Balance: ')
 print(plr_account2_n+': '+plr_tokenName+' Balance: '+str(plr_call_2 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_2 / plr_token_d * plr_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(plr_account2_n+': Ethereum Balance '+str(plr_w_call_2 / _e_d)+' $'+str(plr_w_call_2 / _e_d * plr_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+plr_tokenName+' Balance: ')
 print(plr_account3_n+': '+plr_tokenName+' Balance: '+str(plr_call_3 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_3 / plr_token_d * plr_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(plr_account3_n+': Ethereum Balance '+str(plr_w_call_3 / _e_d)+' $'+str(plr_w_call_3 / _e_d * plr_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+plr_tokenName+' Balance: ')
 print(plr_account4_n+': '+plr_tokenName+' Balance: '+str(plr_call_4 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_4 / plr_token_d * plr_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(plr_account4_n+': Ethereum Balance '+str(plr_w_call_4 / _e_d)+' $'+str(plr_w_call_4 / _e_d * plr_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+plr_tokenName+' Balance: ')
 print(plr_account5_n+': '+plr_tokenName+' Balance: '+str(plr_call_5 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_5 / plr_token_d * plr_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(plr_account5_n+': Ethereum Balance '+str(plr_w_call_5 / _e_d)+' $'+str(plr_w_call_5 /_e_d * plr_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+plr_tokenName+' Balance: ')
 print(plr_account6_n+': '+plr_tokenName+' Balance: '+str(plr_call_6 / plr_token_d)+' Usd/'+plr_tokenName+' Balance: $'+str(plr_call_6 / plr_token_d * plr_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(plr_account6_n+': Ethereum Balance '+str(plr_w_call_6 / _e_d)+' $'+str(plr_w_call_6 / _e_d * plr_last_ethereum_price))
def plr_unlock_all_accounts():
  plr_unlock_account_0()
  plr_unlock_account_1()
  plr_unlock_account_2()
  plr_unlock_account_3()
  plr_unlock_account_4()
  plr_unlock_account_5()
  plr_unlock_account_6()


def plr_unlock_account_0():
  global plr_account0pw
  global plr_account0
  global plr_account0_n
  plr_update_accounts()
  plr_u_a_0 = plr_w_unlock(plr_account0, plr_account0pw, plr_unlockTime)
  if plr_u_a_0 == False:
    if plr_account0pw == '':
     plr_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account0_n+' Passphrase Denied: '+plr_account0pw_r)
    elif plr_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+plr_account0_n+' Passphrase Denied: '+plr_account0pw)
  if plr_u_a_0 == True:
   print(plr_account0_n+' Unlocked')

def plr_unlock_account_1():
  global plr_account1pw
  global plr_account1
  global plr_account1_n
  plr_update_accounts()
  plr_u_a_1 = plr_unlock(plr_account1, plr_account1pw, plr_unlockTime)
  if plr_u_a_1 == False:
    if plr_account1pw == '':
     plr_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account1_n+' Passphrase Denied: '+plr_account1pw_r)
    elif plr_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+plr_account1_n+' Passphrase Denied: '+plr_account1pw)
  if plr_u_a_1 == True:
   print(plr_account1_n+' Unlocked')

def plr_unlock_account_2():
  global plr_account2pw
  global plr_account2
  global plr_account2_n
  plr_update_accounts()
  plr_u_a_2 = plr_unlock(plr_account2, plr_account2pw, plr_unlockTime)
  if plr_u_a_2 == False:
    if plr_account2pw == '':
     plr_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account2_n+' Passphrase Denied: '+plr_account2pw_r)
    elif plr_account2pw != '':
     print('Unlock Failure With Account '+plr_account2_n+' Passphrase Denied: '+plr_account2pw)
  if plr_u_a_2 == True:
   print(plr_account2_n+' Unlocked')

def plr_unlock_account_3():
  global plr_account3pw
  global plr_account3
  global plr_account3_n
  plr_update_accounts()
  plr_u_a_3 = plr_unlock(plr_account3, plr_account3pw, plr_unlockTime)
  if plr_u_a_3 == False:
    if plr_account3pw == '':
     plr_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account3_n+' Passphrase Denied: '+plr_account3pw_r)
    elif plr_account3pw != '':
     print('Unlock Failure With Account '+plr_account3_n+' Passphrase Denied: '+plr_account3pw)
  if plr_u_a_3 == True:
   print(plr_account3_n+' Unlocked')

def plr_unlock_account_4():
  global plr_account4pw
  global plr_account4
  global plr_account4_n
  plr_update_accounts()
  plr_u_a_4 = plr_unlock(plr_account4, plr_account4pw, plr_unlockTime)
  if plr_u_a_4 == False:
    if plr_account4pw == '':
     plr_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account4_n+' Passphrase Denied: '+plr_account4pw_r)
    elif plr_account4pw != '':
     print('Unlock Failure With Account '+plr_account4_n+' Passphrase Denied: '+plr_account4pw)
  if plr_u_a_4 == True:
   print(plr_account4_n+' Unlocked')

def plr_unlock_account_5():
  global plr_account5pw
  global plr_account5
  global plr_account5_n
  plr_update_accounts()
  plr_u_a_5 = plr_unlock(plr_account5, plr_account5pw, plr_unlockTime)
  if plr_u_a_5 == False:
    if plr_account5pw == '':
     plr_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account5_n+' Passphrase Denied: '+plr_account5pw_r)
    elif plr_account5pw != '':
     print('Unlock Failure With Account '+plr_account5_n+' Passphrase Denied: '+plr_account5pw)
  if plr_u_a_5 == True:
   print(plr_account5_n+' Unlocked')

def plr_unlock_account_6():
  global plr_account6pw
  global plr_account6
  global plr_account6_n
  plr_update_accounts()
  plr_u_a_6 = plr_unlock(plr_account6, plr_account6pw, plr_unlockTime)
  if plr_u_a_6 == False:
    if plr_account6pw == '':
     plr_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+plr_account6_n+' Passphrase Denied: '+plr_account6pw_r)
    elif plr_account6pw != '':
     print('Unlock Failure With Account '+plr_account6_n+' Passphrase Denied: '+plr_account6pw)
  if plr_u_a_6 == True:
   print(plr_account6_n+' Unlocked')

def plr_unlock_account(plr_ua_accountNumber):
 plr_update_accounts()
 plr_ua_account_number = plr_ua_accountNumber
 plr_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if plr_ua_account_number == plr_ua_input[0]:
  plr_unlock_account_0()
 if plr_ua_account_number == plr_ua_input[1]:
  plr_unlock_account_1()
 if plr_ua_account_number == plr_ua_input[2]:
  plr_unlock_account_2()
 if plr_ua_account_number == plr_ua_input[3]:
  plr_unlock_account_3()
 if plr_ua_account_number == plr_ua_input[4]:
  plr_unlock_account_4()
 if plr_ua_account_number == plr_ua_input[5]:
  plr_unlock_account_5()
 if plr_ua_account_number == plr_ua_input[6]:
  plr_unlock_account_6()
 if plr_ua_account_number not in plr_ua_input:
  print('Must Integer Within Range '+plr_accounts_range+'.')
 

def plr_approve_between_accounts(fromAccount, toAccount, msgValue):
  plr_update_accounts()
  plr_a_0 = plr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(plr_a_0)

def plr_approve(fromAccountNumber, toAddress, msgValue):
  plr_update_accounts()
  plr_unlock_account(fromAccountNumber)
  plr_a_1 = plr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(plr_a_1)

def plr_transfer_between_accounts(fromAccount, toAccount, msgValue):
  plr_update_accounts()
  plr_unlock_account(fromAccount)
  plr_t_0 = plr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(plr_t_0)

def plr_transfer(fromAccountNumber, toAddress, msgValue):
  plr_update_accounts()
  plr_unlock_account(fromAccountNumber)
  plr_t_1 = plr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(plr_t_1)

def plr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  plr_update_accounts()
  plr_unlock_account(callAccount)
  plr_tf_0 = plr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(plr_tf_0)

def plr_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  plr_update_accounts()
  plr_unlock_account(callAccount)
  plr_tf_1 = plr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(plr_tf_1)
  


def plr_help():
  print('Following Functions For '+plr_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * plr_unlock => web3.personal.unlockAccount
/ * plr_accounts => web3.personal.listAccounts
/ * plr_balance = web3.eth.getBalance
** plr => web3.eth.contract(abi=plr_abi, address=plr_address)
** / * plr_balanceOf => plr.call().balanceOf

~ Function Listing Below:
~ plr_update_accounts()
~ plr_update_balances() \n\r -- => plr_update_accounts()
~ plr_list_all_accounts() \n\r -- => plr_update_accounts()
~ plr_account_balance(accountNumber) \n\r -- => plr_update_balances() 
~ plr_list_all_account_balances() \n\r -- => plr_update_balances()
~ plr_unlock_all_accounts() \n\r -- => plr_unlock_account_0() \n\r -- => plr_unlock_account_1() \n\r -- => plr_unlock_account_2() \n\r -- => plr_unlock_account_3() \n\r -- => plr_unlock_account_4() \n\r -- => plr_unlock_account_5() \n\r -- => plr_unlock_account_6() 
~ plr_unlock_account_0() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account0, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_1() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account1, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_2() \n\r -- => plr_update_accounts() \n\r --/ *plr_w_unlock(plr_account2, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_3() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account3, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_4() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account4, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_5() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account5, plr_account0pw, plr_unlockTime)
~ plr_unlock_account_6() \n\r -- => plr_update_accounts() \n\r -- / *plr_w_unlock(plr_account6, plr_account0pw, plr_unlockTime)
~ plr_unlock_account(plr_ua_accountNumber) \n\r -- => plr_update_accounts() \n\r -- // plr_unlock_account_0() \n\r -- // plr_unlock_account_1() \n\r -- // plr_unlock_account_2() \n\r -- // plr_unlock_account_3() \n\r -- // plr_unlock_account_4() \n\r -- // plr_unlock_account_5() \n\r -- // plr_unlock_account_6()
~ plr_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(fromAccount) \n\r -- / ** plr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ plr_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(fromAccountNumber) \n\r -- / ** plr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ plr_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(fromAccount) \n\r -- / ** plr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ plr_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(fromAccountNumber) \n\r -- / ** plr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ plr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(callAccount) \n\r / ** plr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ plr_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => plr_update_accounts() \n\r -- => plr_unlock_account(callAccount) \n\r -- / ** plr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ plr_help() <-- You Are Here. ''')