#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global tkn_account_0_a
global tkn_account_1_a
global tkn_account_2_a
global tkn_account_3_a
global tkn_account_4_a
global tkn_account_5_a
global tkn_account_6_a
global tkn_address
global tkn_abi
global tkn
global tkn_call_0
global tkn_call_1
global tkn_call_2
global tkn_call_3
global tkn_call_4
global tkn_call_5
global tkn_call_6
global tkn_call_ab
global tkn_accounts
global tkn_account_0_pw
global tkn_account_1_pw
global tkn_account_2_pw
global tkn_account_3_pw
global tkn_account_4_pw
global tkn_account_5_pw
global tkn_account_6_pw
global tkn_account_0_n
global tkn_account_1_n
global tkn_account_2_n
global tkn_account_3_n
global tkn_account_4_n
global tkn_account_5_n
global tkn_account_6_n
global tkn_account1pw
global tkn_account2pw
global tkn_account3pw
global tkn_account4pw
global tkn_account5pw
global tkn_account6pw
global tkn_last_price
global tkn_accounts_range
global tkn_tokenName
global tkn_last_ethereum_price
global tkn_unlocktkn
global tkn_balance
global tkn_balanceOf
global tkn_unlock
global tkn_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
tkn_token_d = 1e8
_e_d = 1e18
tkn_accounts_range = '[0, 6]'
tkn_unlock = web3.personal.unlockAccount
tkn_last_ethereum_price = 370.00
tkn_last_price = 2.02
tkn_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
tkn_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
tkn_tokenName = 'TokenCard Token'
tkn_unlocktkn = hex(10000) # Must be hex()
tkn_account_0_a = tkn_accounts[0]
tkn_account_1_a = tkn_accounts[1]
tkn_account_2_a = tkn_accounts[2]
tkn_account_3_a = tkn_accounts[3]
tkn_account_4_a = tkn_accounts[4]
tkn_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
tkn_account_6_a = tkn_accounts[6]
# Supply Unlock Passwords For Transactions Below
tkn_account_0_pw = 'GuildSkrypt2017!@#'
tkn_account_1_pw = ''
tkn_account_2_pw = 'GuildSkrypt2017!@#'
tkn_account_3_pw = ''
tkn_account_4_pw = ''
tkn_account_5_pw = ''
tkn_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
tkn_account_0_n = 'Skotys Bittrex Account'
tkn_account_1_n = 'Jeffs Account'
tkn_account_2_n = 'Skrypts Bittrex Account'
tkn_account_3_n = 'Skotys Personal Account'
tkn_account_4_n = 'Unknown'
tkn_account_5_n = 'Watched \'Bittrex\' Account.'
tkn_account_6_n = 'Watched Account (1)'
# Contract Information Below :
tkn_address = '0xaAAf91D9b90dF800Df4F55c205fd6989c977E73a'
tkn_abi = [{"constant":false,"inputs":[],"name":"Launch","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lockedTokenHolder","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalizeRemainders","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"lockTokenHolder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"claimOwnerSupply","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint256"}],"name":"burn","outputs":[{"name":"result","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"neverPauseAgain","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"currentSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"launched","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"day","type":"uint256"}],"name":"setOwnerFreeDay","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenholder","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"mintingDone","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"pausingMechanismLocked","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_controller","type":"address"}],"name":"setController","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"remaindersSet","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"data","type":"uint256[]"}],"name":"multiMint","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"remainingOwner","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"changeOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"completeMinting","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ownerTokensFreeDay","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"claimAuctionableTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_remainingOwner","type":"uint256"},{"name":"_remainingAuctionable","type":"uint256"}],"name":"setRemainders","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"remainingAuctionable","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"}],"name":"claimTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_th","type":"address"}],"name":"setTokenHolder","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"controller","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"token","type":"address"},{"indexed":false,"name":"to","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"logTokenTransfer","type":"event"}]
tkn = web3.eth.contract(abi=tkn_abi, address=tkn_address)
tkn_balanceOf = tkn.call().balanceOf
# End Contract Information
def tkn_update_accounts():
 global tkn_account0
 global tkn_account1
 global tkn_account2
 global tkn_account3
 global tkn_account4
 global tkn_account5
 global tkn_account6
 global tkn_account0_n
 global tkn_account1_n
 global tkn_account2_n
 global tkn_account3_n
 global tkn_account4_n
 global tkn_account5_n
 global tkn_account6_n
 global tkn_account0pw
 global tkn_account1pw
 global tkn_account2pw
 global tkn_account3pw
 global tkn_account4pw
 global tkn_account5pw
 global tkn_account6pw
 tkn_account0 = tkn_account_0_a
 tkn_account1 = tkn_account_1_a
 tkn_account2 = tkn_account_2_a
 tkn_account3 = tkn_account_3_a
 tkn_account4 = tkn_account_4_a
 tkn_account5 = tkn_account_5_a
 tkn_account6 = tkn_account_6_a
 tkn_account0_n = tkn_account_0_n
 tkn_account1_n = tkn_account_1_n
 tkn_account2_n = tkn_account_2_n
 tkn_account3_n = tkn_account_3_n
 tkn_account4_n = tkn_account_4_n
 tkn_account5_n = tkn_account_5_n
 tkn_account6_n = tkn_account_6_n
 tkn_account0pw = tkn_account_0_pw
 tkn_account1pw = tkn_account_1_pw
 tkn_account2pw = tkn_account_2_pw
 tkn_account3pw = tkn_account_3_pw
 tkn_account4pw = tkn_account_4_pw
 tkn_account5pw = tkn_account_5_pw
 tkn_account6pw = tkn_account_6_pw
 print(tkn_tokenName+' Accounts Updated.')
def tkn_update_balances():
 global tkn_call_0
 global tkn_call_1
 global tkn_call_2
 global tkn_call_3
 global tkn_call_4
 global tkn_call_5
 global tkn_call_6
 global tkn_w_call_0
 global tkn_w_call_1
 global tkn_w_call_2
 global tkn_w_call_3
 global tkn_w_call_4
 global tkn_w_call_5
 global tkn_w_call_6
 tkn_update_accounts()
 print('Updating '+tkn_tokenName+' Balances Please Wait...')
 tkn_call_0 = tkn_balanceOf(tkn_account0)
 tkn_call_1 = tkn_balanceOf(tkn_account1)
 tkn_call_2 = tkn_balanceOf(tkn_account2)
 tkn_call_3 = tkn_balanceOf(tkn_account3)
 tkn_call_4 = tkn_balanceOf(tkn_account4)
 tkn_call_5 = tkn_balanceOf(tkn_account5)
 tkn_call_6 = tkn_balanceOf(tkn_account6)
 tkn_w_call_0 = tkn_balance(tkn_account0)
 tkn_w_call_1 = tkn_balance(tkn_account1)
 tkn_w_call_2 = tkn_balance(tkn_account2)
 tkn_w_call_3 = tkn_balance(tkn_account3)
 tkn_w_call_4 = tkn_balance(tkn_account4)
 tkn_w_call_5 = tkn_balance(tkn_account5)
 tkn_w_call_6 = tkn_balance(tkn_account6)
 print(tkn_tokenName+' Balances Updated.')
def tkn_list_all_accounts():
 tkn_update_accounts()
 print(tkn_tokenName+' '+tkn_account0_n+': '+tkn_account0)
 print(tkn_tokenName+' '+tkn_account1_n+': '+tkn_account1)
 print(tkn_tokenName+' '+tkn_account2_n+': '+tkn_account2)
 print(tkn_tokenName+' '+tkn_account3_n+': '+tkn_account3)
 print(tkn_tokenName+' '+tkn_account4_n+': '+tkn_account4)
 print(tkn_tokenName+' '+tkn_account5_n+': '+tkn_account5)
 print(tkn_tokenName+' '+tkn_account6_n+': '+tkn_account6)

def tkn_account_balance(accountNumber):
 tkn_update_balances()
 tkn_ab_account_number = accountNumber
 tkn_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if tkn_ab_account_number == tkn_ab_input[0]:
  print('Calling '+tkn_account0_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account0_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_0 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_0 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[1]:
  print('Calling '+tkn_account1_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account1_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_1 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_1 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[2]:
  print('Calling '+tkn_account2_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account2_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_2 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_2 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[3]:
  print('Calling '+tkn_account3_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account3_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_3 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_3 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[4]:
  print('Calling '+tkn_account4_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account4_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_4 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_4 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[5]:
  print('Calling '+tkn_account5_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account5_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_5 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_5 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number == tkn_ab_input[6]:
  print('Calling '+tkn_account6_n+' '+tkn_tokenName+' Balance: ')
  print(tkn_account6_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_6 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_6 / tkn_token_d * tkn_last_price))
 if tkn_ab_account_number not in tkn_ab_input:
  print('Must Integer Within Range '+tkn_accounts_range+'.')

def tkn_list_all_account_balances():
 tkn_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+tkn_tokenName+' Balance: ')
 print(tkn_account0_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_0 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_0 / tkn_token_d * tkn_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(tkn_account0_n+': Ethereum Balance '+str(tkn_w_call_0 / _e_d)+' $'+str(tkn_w_call_0 / _e_d * tkn_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+tkn_tokenName+' Balance: ')
 print(tkn_account1_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_1 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_1 / tkn_token_d * tkn_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(tkn_account1_n+': Ethereum Balance '+str(tkn_w_call_1 / _e_d)+' $'+str(tkn_w_call_1 / _e_d * tkn_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+tkn_tokenName+' Balance: ')
 print(tkn_account2_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_2 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_2 / tkn_token_d * tkn_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(tkn_account2_n+': Ethereum Balance '+str(tkn_w_call_2 / _e_d)+' $'+str(tkn_w_call_2 / _e_d * tkn_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+tkn_tokenName+' Balance: ')
 print(tkn_account3_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_3 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_3 / tkn_token_d * tkn_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(tkn_account3_n+': Ethereum Balance '+str(tkn_w_call_3 / _e_d)+' $'+str(tkn_w_call_3 / _e_d * tkn_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+tkn_tokenName+' Balance: ')
 print(tkn_account4_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_4 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_4 / tkn_token_d * tkn_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(tkn_account4_n+': Ethereum Balance '+str(tkn_w_call_4 / _e_d)+' $'+str(tkn_w_call_4 / _e_d * tkn_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+tkn_tokenName+' Balance: ')
 print(tkn_account5_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_5 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_5 / tkn_token_d * tkn_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(tkn_account5_n+': Ethereum Balance '+str(tkn_w_call_5 / _e_d)+' $'+str(tkn_w_call_5 /_e_d * tkn_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+tkn_tokenName+' Balance: ')
 print(tkn_account6_n+': '+tkn_tokenName+' Balance: '+str(tkn_call_6 / tkn_token_d)+' Usd/'+tkn_tokenName+' Balance: $'+str(tkn_call_6 / tkn_token_d * tkn_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(tkn_account6_n+': Ethereum Balance '+str(tkn_w_call_6 / _e_d)+' $'+str(tkn_w_call_6 / _e_d * tkn_last_ethereum_price))
def tkn_unlock_all_accounts():
  tkn_unlock_account_0()
  tkn_unlock_account_1()
  tkn_unlock_account_2()
  tkn_unlock_account_3()
  tkn_unlock_account_4()
  tkn_unlock_account_5()
  tkn_unlock_account_6()


def tkn_unlock_account_0():
  global tkn_account0pw
  global tkn_account0
  global tkn_account0_n
  tkn_update_accounts()
  tkn_u_a_0 = tkn_w_unlock(tkn_account0, tkn_account0pw, tkn_unlocktkn)
  if tkn_u_a_0 == False:
    if tkn_account0pw == '':
     tkn_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account0_n+' Passphrase Denied: '+tkn_account0pw_r)
    elif tkn_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+tkn_account0_n+' Passphrase Denied: '+tkn_account0pw)
  if tkn_u_a_0 == True:
   print(tkn_account0_n+' Unlocked')

def tkn_unlock_account_1():
  global tkn_account1pw
  global tkn_account1
  global tkn_account1_n
  tkn_update_accounts()
  tkn_u_a_1 = tkn_unlock(tkn_account1, tkn_account1pw, tkn_unlocktkn)
  if tkn_u_a_1 == False:
    if tkn_account1pw == '':
     tkn_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account1_n+' Passphrase Denied: '+tkn_account1pw_r)
    elif tkn_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+tkn_account1_n+' Passphrase Denied: '+tkn_account1pw)
  if tkn_u_a_1 == True:
   print(tkn_account1_n+' Unlocked')

def tkn_unlock_account_2():
  global tkn_account2pw
  global tkn_account2
  global tkn_account2_n
  tkn_update_accounts()
  tkn_u_a_2 = tkn_unlock(tkn_account2, tkn_account2pw, tkn_unlocktkn)
  if tkn_u_a_2 == False:
    if tkn_account2pw == '':
     tkn_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account2_n+' Passphrase Denied: '+tkn_account2pw_r)
    elif tkn_account2pw != '':
     print('Unlock Failure With Account '+tkn_account2_n+' Passphrase Denied: '+tkn_account2pw)
  if tkn_u_a_2 == True:
   print(tkn_account2_n+' Unlocked')

def tkn_unlock_account_3():
  global tkn_account3pw
  global tkn_account3
  global tkn_account3_n
  tkn_update_accounts()
  tkn_u_a_3 = tkn_unlock(tkn_account3, tkn_account3pw, tkn_unlocktkn)
  if tkn_u_a_3 == False:
    if tkn_account3pw == '':
     tkn_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account3_n+' Passphrase Denied: '+tkn_account3pw_r)
    elif tkn_account3pw != '':
     print('Unlock Failure With Account '+tkn_account3_n+' Passphrase Denied: '+tkn_account3pw)
  if tkn_u_a_3 == True:
   print(tkn_account3_n+' Unlocked')

def tkn_unlock_account_4():
  global tkn_account4pw
  global tkn_account4
  global tkn_account4_n
  tkn_update_accounts()
  tkn_u_a_4 = tkn_unlock(tkn_account4, tkn_account4pw, tkn_unlocktkn)
  if tkn_u_a_4 == False:
    if tkn_account4pw == '':
     tkn_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account4_n+' Passphrase Denied: '+tkn_account4pw_r)
    elif tkn_account4pw != '':
     print('Unlock Failure With Account '+tkn_account4_n+' Passphrase Denied: '+tkn_account4pw)
  if tkn_u_a_4 == True:
   print(tkn_account4_n+' Unlocked')

def tkn_unlock_account_5():
  global tkn_account5pw
  global tkn_account5
  global tkn_account5_n
  tkn_update_accounts()
  tkn_u_a_5 = tkn_unlock(tkn_account5, tkn_account5pw, tkn_unlocktkn)
  if tkn_u_a_5 == False:
    if tkn_account5pw == '':
     tkn_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account5_n+' Passphrase Denied: '+tkn_account5pw_r)
    elif tkn_account5pw != '':
     print('Unlock Failure With Account '+tkn_account5_n+' Passphrase Denied: '+tkn_account5pw)
  if tkn_u_a_5 == True:
   print(tkn_account5_n+' Unlocked')

def tkn_unlock_account_6():
  global tkn_account6pw
  global tkn_account6
  global tkn_account6_n
  tkn_update_accounts()
  tkn_u_a_6 = tkn_unlock(tkn_account6, tkn_account6pw, tkn_unlocktkn)
  if tkn_u_a_6 == False:
    if tkn_account6pw == '':
     tkn_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+tkn_account6_n+' Passphrase Denied: '+tkn_account6pw_r)
    elif tkn_account6pw != '':
     print('Unlock Failure With Account '+tkn_account6_n+' Passphrase Denied: '+tkn_account6pw)
  if tkn_u_a_6 == True:
   print(tkn_account6_n+' Unlocked')

def tkn_unlock_account(tkn_ua_accountNumber):
 tkn_update_accounts()
 tkn_ua_account_number = tkn_ua_accountNumber
 tkn_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if tkn_ua_account_number == tkn_ua_input[0]:
  tkn_unlock_account_0()
 if tkn_ua_account_number == tkn_ua_input[1]:
  tkn_unlock_account_1()
 if tkn_ua_account_number == tkn_ua_input[2]:
  tkn_unlock_account_2()
 if tkn_ua_account_number == tkn_ua_input[3]:
  tkn_unlock_account_3()
 if tkn_ua_account_number == tkn_ua_input[4]:
  tkn_unlock_account_4()
 if tkn_ua_account_number == tkn_ua_input[5]:
  tkn_unlock_account_5()
 if tkn_ua_account_number == tkn_ua_input[6]:
  tkn_unlock_account_6()
 if tkn_ua_account_number not in tkn_ua_input:
  print('Must Integer Within Range '+tkn_accounts_range+'.')
 

def tkn_approve_between_accounts(fromAccount, toAccount, msgValue):
  tkn_update_accounts()
  tkn_a_0 = tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(tkn_a_0)

def tkn_approve(fromAccountNumber, toAddress, msgValue):
  tkn_update_accounts()
  tkn_unlock_account(fromAccountNumber)
  tkn_a_1 = tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(tkn_a_1)

def tkn_transfer_between_accounts(fromAccount, toAccount, msgValue):
  tkn_update_accounts()
  tkn_unlock_account(fromAccount)
  tkn_t_0 = tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(tkn_t_0)

def tkn_transfer(fromAccountNumber, toAddress, msgValue):
  tkn_update_accounts()
  tkn_unlock_account(fromAccountNumber)
  tkn_t_1 = tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(tkn_t_1)

def tkn_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  tkn_update_accounts()
  tkn_unlock_account(callAccount)
  tkn_tf_0 = tkn.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(tkn_tf_0)

def tkn_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  tkn_update_accounts()
  tkn_unlock_account(callAccount)
  tkn_tf_1 = tkn.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(tkn_tf_1)
  


def tkn_help():
  print('Following Functions For '+tkn_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * tkn_unlock => web3.personal.unlockAccount
/ * tkn_accounts => web3.personal.listAccounts
/ * tkn_balance = web3.eth.getBalance
** tkn => web3.eth.contract(abi=tkn_abi, address=tkn_address)
** / * tkn_balanceOf => tkn.call().balanceOf

~ Function Listing Below:
~ tkn_update_accounts()
~ tkn_update_balances() \n\r -- => tkn_update_accounts()
~ tkn_list_all_accounts() \n\r -- => tkn_update_accounts()
~ tkn_account_balance(accountNumber) \n\r -- => tkn_update_balances() 
~ tkn_list_all_account_balances() \n\r -- => tkn_update_balances()
~ tkn_unlock_all_accounts() \n\r -- => tkn_unlock_account_0() \n\r -- => tkn_unlock_account_1() \n\r -- => tkn_unlock_account_2() \n\r -- => tkn_unlock_account_3() \n\r -- => tkn_unlock_account_4() \n\r -- => tkn_unlock_account_5() \n\r -- => tkn_unlock_account_6() 
~ tkn_unlock_account_0() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account0, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_1() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account1, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_2() \n\r -- => tkn_update_accounts() \n\r --/ *tkn_w_unlock(tkn_account2, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_3() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account3, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_4() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account4, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_5() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account5, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account_6() \n\r -- => tkn_update_accounts() \n\r -- / *tkn_w_unlock(tkn_account6, tkn_account0pw, tkn_unlocktkn)
~ tkn_unlock_account(tkn_ua_accountNumber) \n\r -- => tkn_update_accounts() \n\r -- // tkn_unlock_account_0() \n\r -- // tkn_unlock_account_1() \n\r -- // tkn_unlock_account_2() \n\r -- // tkn_unlock_account_3() \n\r -- // tkn_unlock_account_4() \n\r -- // tkn_unlock_account_5() \n\r -- // tkn_unlock_account_6()
~ tkn_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(fromAccount) \n\r -- / ** tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ tkn_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(fromAccountNumber) \n\r -- / ** tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ tkn_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(fromAccount) \n\r -- / ** tkn.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ tkn_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(fromAccountNumber) \n\r -- / ** tkn.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ tkn_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(callAccount) \n\r / ** tkn.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ tkn_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => tkn_update_accounts() \n\r -- => tkn_unlock_account(callAccount) \n\r -- / ** tkn.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ tkn_help() <-- You Are Here. ''')