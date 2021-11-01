#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global ptoy_account_0_a
global ptoy_account_1_a
global ptoy_account_2_a
global ptoy_account_3_a
global ptoy_account_4_a
global ptoy_account_5_a
global ptoy_account_6_a
global ptoy_address
global ptoy_abi
global ptoy
global ptoy_call_0
global ptoy_call_1
global ptoy_call_2
global ptoy_call_3
global ptoy_call_4
global ptoy_call_5
global ptoy_call_6
global ptoy_call_ab
global ptoy_accounts
global ptoy_account_0_pw
global ptoy_account_1_pw
global ptoy_account_2_pw
global ptoy_account_3_pw
global ptoy_account_4_pw
global ptoy_account_5_pw
global ptoy_account_6_pw
global ptoy_account_0_n
global ptoy_account_1_n
global ptoy_account_2_n
global ptoy_account_3_n
global ptoy_account_4_n
global ptoy_account_5_n
global ptoy_account_6_n
global ptoy_account1pw
global ptoy_account2pw
global ptoy_account3pw
global ptoy_account4pw
global ptoy_account5pw
global ptoy_account6pw
global ptoy_last_price
global ptoy_accounts_range
global ptoy_tokenName
global ptoy_last_ethereum_price
global ptoy_unlockTime
global ptoy_balance
global ptoy_balanceOf
global ptoy_unlock
global ptoy_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
ptoy_token_d = 1e8
_e_d = 1e18
ptoy_accounts_range = '[0, 6]'
ptoy_unlock = web3.personal.unlockAccount
ptoy_last_ethereum_price = 370.00
ptoy_last_price = 0.36
ptoy_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
ptoy_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
ptoy_tokenName = 'Patientory Token'
ptoy_unlockTime = hex(10000) # Must be hex()
ptoy_account_0_a = ptoy_accounts[0]
ptoy_account_1_a = ptoy_accounts[1]
ptoy_account_2_a = ptoy_accounts[2]
ptoy_account_3_a = ptoy_accounts[3]
ptoy_account_4_a = ptoy_accounts[4]
ptoy_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
ptoy_account_6_a = ptoy_accounts[6]
# Supply Unlock Passwords For Transactions Below
ptoy_account_0_pw = 'GuildSkrypt2017!@#'
ptoy_account_1_pw = ''
ptoy_account_2_pw = 'GuildSkrypt2017!@#'
ptoy_account_3_pw = ''
ptoy_account_4_pw = ''
ptoy_account_5_pw = ''
ptoy_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
ptoy_account_0_n = 'Skotys Bittrex Account'
ptoy_account_1_n = 'Jeffs Account'
ptoy_account_2_n = 'Skrypts Bittrex Account'
ptoy_account_3_n = 'Skotys Personal Account'
ptoy_account_4_n = 'Unknown'
ptoy_account_5_n = 'Watched \'Bittrex\' Account.'
ptoy_account_6_n = 'Watched Account (1)'
# Contract Information Below :
ptoy_address = '0x8Ae4BF2C33a8e667de34B54938B0ccD03Eb8CC06'
ptoy_abi = [{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"state","type":"bool"}],"name":"setTransferAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setReleaseAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"receiver","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"mintAgents","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"state","type":"bool"}],"name":"setMintAgent","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"upgrade","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"}],"name":"setTokenInformation","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"releaseTokenTransfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getUpgradeState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"transferAgents","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"released","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"canUpgrade","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"addApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalUpgraded","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"releaseAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"agent","type":"address"}],"name":"setUpgradeAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"subApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"master","type":"address"}],"name":"setUpgradeMaster","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_initialSupply","type":"uint256"},{"name":"_decimals","type":"uint256"},{"name":"_mintable","type":"bool"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newName","type":"string"},{"indexed":false,"name":"newSymbol","type":"string"}],"name":"UpdatedTokenInformation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Upgrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"agent","type":"address"}],"name":"UpgradeAgentSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"addr","type":"address"},{"indexed":false,"name":"state","type":"bool"}],"name":"MintingAgentChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"receiver","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
ptoy = web3.eth.contract(abi=ptoy_abi, address=ptoy_address)
ptoy_balanceOf = ptoy.call().balanceOf
# End Contract Information
def ptoy_update_accounts():
 global ptoy_account0
 global ptoy_account1
 global ptoy_account2
 global ptoy_account3
 global ptoy_account4
 global ptoy_account5
 global ptoy_account6
 global ptoy_account0_n
 global ptoy_account1_n
 global ptoy_account2_n
 global ptoy_account3_n
 global ptoy_account4_n
 global ptoy_account5_n
 global ptoy_account6_n
 global ptoy_account0pw
 global ptoy_account1pw
 global ptoy_account2pw
 global ptoy_account3pw
 global ptoy_account4pw
 global ptoy_account5pw
 global ptoy_account6pw
 ptoy_account0 = ptoy_account_0_a
 ptoy_account1 = ptoy_account_1_a
 ptoy_account2 = ptoy_account_2_a
 ptoy_account3 = ptoy_account_3_a
 ptoy_account4 = ptoy_account_4_a
 ptoy_account5 = ptoy_account_5_a
 ptoy_account6 = ptoy_account_6_a
 ptoy_account0_n = ptoy_account_0_n
 ptoy_account1_n = ptoy_account_1_n
 ptoy_account2_n = ptoy_account_2_n
 ptoy_account3_n = ptoy_account_3_n
 ptoy_account4_n = ptoy_account_4_n
 ptoy_account5_n = ptoy_account_5_n
 ptoy_account6_n = ptoy_account_6_n
 ptoy_account0pw = ptoy_account_0_pw
 ptoy_account1pw = ptoy_account_1_pw
 ptoy_account2pw = ptoy_account_2_pw
 ptoy_account3pw = ptoy_account_3_pw
 ptoy_account4pw = ptoy_account_4_pw
 ptoy_account5pw = ptoy_account_5_pw
 ptoy_account6pw = ptoy_account_6_pw
 print(ptoy_tokenName+' Accounts Updated.')
def ptoy_update_balances():
 global ptoy_call_0
 global ptoy_call_1
 global ptoy_call_2
 global ptoy_call_3
 global ptoy_call_4
 global ptoy_call_5
 global ptoy_call_6
 global ptoy_w_call_0
 global ptoy_w_call_1
 global ptoy_w_call_2
 global ptoy_w_call_3
 global ptoy_w_call_4
 global ptoy_w_call_5
 global ptoy_w_call_6
 ptoy_update_accounts()
 print('Updating '+ptoy_tokenName+' Balances Please Wait...')
 ptoy_call_0 = ptoy_balanceOf(ptoy_account0)
 ptoy_call_1 = ptoy_balanceOf(ptoy_account1)
 ptoy_call_2 = ptoy_balanceOf(ptoy_account2)
 ptoy_call_3 = ptoy_balanceOf(ptoy_account3)
 ptoy_call_4 = ptoy_balanceOf(ptoy_account4)
 ptoy_call_5 = ptoy_balanceOf(ptoy_account5)
 ptoy_call_6 = ptoy_balanceOf(ptoy_account6)
 ptoy_w_call_0 = ptoy_balance(ptoy_account0)
 ptoy_w_call_1 = ptoy_balance(ptoy_account1)
 ptoy_w_call_2 = ptoy_balance(ptoy_account2)
 ptoy_w_call_3 = ptoy_balance(ptoy_account3)
 ptoy_w_call_4 = ptoy_balance(ptoy_account4)
 ptoy_w_call_5 = ptoy_balance(ptoy_account5)
 ptoy_w_call_6 = ptoy_balance(ptoy_account6)
 print(ptoy_tokenName+' Balances Updated.')
def ptoy_list_all_accounts():
 ptoy_update_accounts()
 print(ptoy_tokenName+' '+ptoy_account0_n+': '+ptoy_account0)
 print(ptoy_tokenName+' '+ptoy_account1_n+': '+ptoy_account1)
 print(ptoy_tokenName+' '+ptoy_account2_n+': '+ptoy_account2)
 print(ptoy_tokenName+' '+ptoy_account3_n+': '+ptoy_account3)
 print(ptoy_tokenName+' '+ptoy_account4_n+': '+ptoy_account4)
 print(ptoy_tokenName+' '+ptoy_account5_n+': '+ptoy_account5)
 print(ptoy_tokenName+' '+ptoy_account6_n+': '+ptoy_account6)

def ptoy_account_balance(accountNumber):
 ptoy_update_balances()
 ptoy_ab_account_number = accountNumber
 ptoy_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if ptoy_ab_account_number == ptoy_ab_input[0]:
  print('Calling '+ptoy_account0_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account0_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_0 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_0 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[1]:
  print('Calling '+ptoy_account1_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account1_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_1 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_1 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[2]:
  print('Calling '+ptoy_account2_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account2_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_2 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_2 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[3]:
  print('Calling '+ptoy_account3_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account3_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_3 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_3 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[4]:
  print('Calling '+ptoy_account4_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account4_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_4 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_4 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[5]:
  print('Calling '+ptoy_account5_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account5_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_5 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_5 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number == ptoy_ab_input[6]:
  print('Calling '+ptoy_account6_n+' '+ptoy_tokenName+' Balance: ')
  print(ptoy_account6_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_6 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_6 / ptoy_token_d * ptoy_last_price))
 if ptoy_ab_account_number not in ptoy_ab_input:
  print('Must Integer Within Range '+ptoy_accounts_range+'.')

def ptoy_list_all_account_balances():
 ptoy_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account0_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_0 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_0 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(ptoy_account0_n+': Ethereum Balance '+str(ptoy_w_call_0 / _e_d)+' $'+str(ptoy_w_call_0 / _e_d * ptoy_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account1_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_1 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_1 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(ptoy_account1_n+': Ethereum Balance '+str(ptoy_w_call_1 / _e_d)+' $'+str(ptoy_w_call_1 / _e_d * ptoy_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account2_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_2 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_2 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(ptoy_account2_n+': Ethereum Balance '+str(ptoy_w_call_2 / _e_d)+' $'+str(ptoy_w_call_2 / _e_d * ptoy_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account3_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_3 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_3 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(ptoy_account3_n+': Ethereum Balance '+str(ptoy_w_call_3 / _e_d)+' $'+str(ptoy_w_call_3 / _e_d * ptoy_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account4_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_4 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_4 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(ptoy_account4_n+': Ethereum Balance '+str(ptoy_w_call_4 / _e_d)+' $'+str(ptoy_w_call_4 / _e_d * ptoy_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account5_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_5 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_5 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(ptoy_account5_n+': Ethereum Balance '+str(ptoy_w_call_5 / _e_d)+' $'+str(ptoy_w_call_5 /_e_d * ptoy_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+ptoy_tokenName+' Balance: ')
 print(ptoy_account6_n+': '+ptoy_tokenName+' Balance: '+str(ptoy_call_6 / ptoy_token_d)+' Usd/'+ptoy_tokenName+' Balance: $'+str(ptoy_call_6 / ptoy_token_d * ptoy_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(ptoy_account6_n+': Ethereum Balance '+str(ptoy_w_call_6 / _e_d)+' $'+str(ptoy_w_call_6 / _e_d * ptoy_last_ethereum_price))
def ptoy_unlock_all_accounts():
  ptoy_unlock_account_0()
  ptoy_unlock_account_1()
  ptoy_unlock_account_2()
  ptoy_unlock_account_3()
  ptoy_unlock_account_4()
  ptoy_unlock_account_5()
  ptoy_unlock_account_6()


def ptoy_unlock_account_0():
  global ptoy_account0pw
  global ptoy_account0
  global ptoy_account0_n
  ptoy_update_accounts()
  ptoy_u_a_0 = ptoy_w_unlock(ptoy_account0, ptoy_account0pw, ptoy_unlockTime)
  if ptoy_u_a_0 == False:
    if ptoy_account0pw == '':
     ptoy_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account0_n+' Passphrase Denied: '+ptoy_account0pw_r)
    elif ptoy_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ptoy_account0_n+' Passphrase Denied: '+ptoy_account0pw)
  if ptoy_u_a_0 == True:
   print(ptoy_account0_n+' Unlocked')

def ptoy_unlock_account_1():
  global ptoy_account1pw
  global ptoy_account1
  global ptoy_account1_n
  ptoy_update_accounts()
  ptoy_u_a_1 = ptoy_unlock(ptoy_account1, ptoy_account1pw, ptoy_unlockTime)
  if ptoy_u_a_1 == False:
    if ptoy_account1pw == '':
     ptoy_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account1_n+' Passphrase Denied: '+ptoy_account1pw_r)
    elif ptoy_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ptoy_account1_n+' Passphrase Denied: '+ptoy_account1pw)
  if ptoy_u_a_1 == True:
   print(ptoy_account1_n+' Unlocked')

def ptoy_unlock_account_2():
  global ptoy_account2pw
  global ptoy_account2
  global ptoy_account2_n
  ptoy_update_accounts()
  ptoy_u_a_2 = ptoy_unlock(ptoy_account2, ptoy_account2pw, ptoy_unlockTime)
  if ptoy_u_a_2 == False:
    if ptoy_account2pw == '':
     ptoy_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account2_n+' Passphrase Denied: '+ptoy_account2pw_r)
    elif ptoy_account2pw != '':
     print('Unlock Failure With Account '+ptoy_account2_n+' Passphrase Denied: '+ptoy_account2pw)
  if ptoy_u_a_2 == True:
   print(ptoy_account2_n+' Unlocked')

def ptoy_unlock_account_3():
  global ptoy_account3pw
  global ptoy_account3
  global ptoy_account3_n
  ptoy_update_accounts()
  ptoy_u_a_3 = ptoy_unlock(ptoy_account3, ptoy_account3pw, ptoy_unlockTime)
  if ptoy_u_a_3 == False:
    if ptoy_account3pw == '':
     ptoy_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account3_n+' Passphrase Denied: '+ptoy_account3pw_r)
    elif ptoy_account3pw != '':
     print('Unlock Failure With Account '+ptoy_account3_n+' Passphrase Denied: '+ptoy_account3pw)
  if ptoy_u_a_3 == True:
   print(ptoy_account3_n+' Unlocked')

def ptoy_unlock_account_4():
  global ptoy_account4pw
  global ptoy_account4
  global ptoy_account4_n
  ptoy_update_accounts()
  ptoy_u_a_4 = ptoy_unlock(ptoy_account4, ptoy_account4pw, ptoy_unlockTime)
  if ptoy_u_a_4 == False:
    if ptoy_account4pw == '':
     ptoy_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account4_n+' Passphrase Denied: '+ptoy_account4pw_r)
    elif ptoy_account4pw != '':
     print('Unlock Failure With Account '+ptoy_account4_n+' Passphrase Denied: '+ptoy_account4pw)
  if ptoy_u_a_4 == True:
   print(ptoy_account4_n+' Unlocked')

def ptoy_unlock_account_5():
  global ptoy_account5pw
  global ptoy_account5
  global ptoy_account5_n
  ptoy_update_accounts()
  ptoy_u_a_5 = ptoy_unlock(ptoy_account5, ptoy_account5pw, ptoy_unlockTime)
  if ptoy_u_a_5 == False:
    if ptoy_account5pw == '':
     ptoy_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account5_n+' Passphrase Denied: '+ptoy_account5pw_r)
    elif ptoy_account5pw != '':
     print('Unlock Failure With Account '+ptoy_account5_n+' Passphrase Denied: '+ptoy_account5pw)
  if ptoy_u_a_5 == True:
   print(ptoy_account5_n+' Unlocked')

def ptoy_unlock_account_6():
  global ptoy_account6pw
  global ptoy_account6
  global ptoy_account6_n
  ptoy_update_accounts()
  ptoy_u_a_6 = ptoy_unlock(ptoy_account6, ptoy_account6pw, ptoy_unlockTime)
  if ptoy_u_a_6 == False:
    if ptoy_account6pw == '':
     ptoy_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ptoy_account6_n+' Passphrase Denied: '+ptoy_account6pw_r)
    elif ptoy_account6pw != '':
     print('Unlock Failure With Account '+ptoy_account6_n+' Passphrase Denied: '+ptoy_account6pw)
  if ptoy_u_a_6 == True:
   print(ptoy_account6_n+' Unlocked')

def ptoy_unlock_account(ptoy_ua_accountNumber):
 ptoy_update_accounts()
 ptoy_ua_account_number = ptoy_ua_accountNumber
 ptoy_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if ptoy_ua_account_number == ptoy_ua_input[0]:
  ptoy_unlock_account_0()
 if ptoy_ua_account_number == ptoy_ua_input[1]:
  ptoy_unlock_account_1()
 if ptoy_ua_account_number == ptoy_ua_input[2]:
  ptoy_unlock_account_2()
 if ptoy_ua_account_number == ptoy_ua_input[3]:
  ptoy_unlock_account_3()
 if ptoy_ua_account_number == ptoy_ua_input[4]:
  ptoy_unlock_account_4()
 if ptoy_ua_account_number == ptoy_ua_input[5]:
  ptoy_unlock_account_5()
 if ptoy_ua_account_number == ptoy_ua_input[6]:
  ptoy_unlock_account_6()
 if ptoy_ua_account_number not in ptoy_ua_input:
  print('Must Integer Within Range '+ptoy_accounts_range+'.')
 

def ptoy_approve_between_accounts(fromAccount, toAccount, msgValue):
  ptoy_update_accounts()
  ptoy_a_0 = ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(ptoy_a_0)

def ptoy_approve(fromAccountNumber, toAddress, msgValue):
  ptoy_update_accounts()
  ptoy_unlock_account(fromAccountNumber)
  ptoy_a_1 = ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(ptoy_a_1)

def ptoy_transfer_between_accounts(fromAccount, toAccount, msgValue):
  ptoy_update_accounts()
  ptoy_unlock_account(fromAccount)
  ptoy_t_0 = ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(ptoy_t_0)

def ptoy_transfer(fromAccountNumber, toAddress, msgValue):
  ptoy_update_accounts()
  ptoy_unlock_account(fromAccountNumber)
  ptoy_t_1 = ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(ptoy_t_1)

def ptoy_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  ptoy_update_accounts()
  ptoy_unlock_account(callAccount)
  ptoy_tf_0 = ptoy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(ptoy_tf_0)

def ptoy_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  ptoy_update_accounts()
  ptoy_unlock_account(callAccount)
  ptoy_tf_1 = ptoy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(ptoy_tf_1)
  


def ptoy_help():
  print('Following Functions For '+ptoy_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * ptoy_unlock => web3.personal.unlockAccount
/ * ptoy_accounts => web3.personal.listAccounts
/ * ptoy_balance = web3.eth.getBalance
** ptoy => web3.eth.contract(abi=ptoy_abi, address=ptoy_address)
** / * ptoy_balanceOf => ptoy.call().balanceOf

~ Function Listing Below:
~ ptoy_update_accounts()
~ ptoy_update_balances() \n\r -- => ptoy_update_accounts()
~ ptoy_list_all_accounts() \n\r -- => ptoy_update_accounts()
~ ptoy_account_balance(accountNumber) \n\r -- => ptoy_update_balances() 
~ ptoy_list_all_account_balances() \n\r -- => ptoy_update_balances()
~ ptoy_unlock_all_accounts() \n\r -- => ptoy_unlock_account_0() \n\r -- => ptoy_unlock_account_1() \n\r -- => ptoy_unlock_account_2() \n\r -- => ptoy_unlock_account_3() \n\r -- => ptoy_unlock_account_4() \n\r -- => ptoy_unlock_account_5() \n\r -- => ptoy_unlock_account_6() 
~ ptoy_unlock_account_0() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account0, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_1() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account1, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_2() \n\r -- => ptoy_update_accounts() \n\r --/ *ptoy_w_unlock(ptoy_account2, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_3() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account3, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_4() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account4, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_5() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account5, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account_6() \n\r -- => ptoy_update_accounts() \n\r -- / *ptoy_w_unlock(ptoy_account6, ptoy_account0pw, ptoy_unlockTime)
~ ptoy_unlock_account(ptoy_ua_accountNumber) \n\r -- => ptoy_update_accounts() \n\r -- // ptoy_unlock_account_0() \n\r -- // ptoy_unlock_account_1() \n\r -- // ptoy_unlock_account_2() \n\r -- // ptoy_unlock_account_3() \n\r -- // ptoy_unlock_account_4() \n\r -- // ptoy_unlock_account_5() \n\r -- // ptoy_unlock_account_6()
~ ptoy_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(fromAccount) \n\r -- / ** ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ptoy_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(fromAccountNumber) \n\r -- / ** ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ptoy_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(fromAccount) \n\r -- / ** ptoy.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ ptoy_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(fromAccountNumber) \n\r -- / ** ptoy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ptoy_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(callAccount) \n\r / ** ptoy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ptoy_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ptoy_update_accounts() \n\r -- => ptoy_unlock_account(callAccount) \n\r -- / ** ptoy.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ ptoy_help() <-- You Are Here. ''')