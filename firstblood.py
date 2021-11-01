#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global st_account_0_a
global st_account_1_a
global st_account_2_a
global st_account_3_a
global st_account_4_a
global st_account_5_a
global st_account_6_a
global st_address
global st_abi
global st
global st_call_0
global st_call_1
global st_call_2
global st_call_3
global st_call_4
global st_call_5
global st_call_6
global st_call_ab
global st_accounts
global st_account_0_pw
global st_account_1_pw
global st_account_2_pw
global st_account_3_pw
global st_account_4_pw
global st_account_5_pw
global st_account_6_pw
global st_account_0_n
global st_account_1_n
global st_account_2_n
global st_account_3_n
global st_account_4_n
global st_account_5_n
global st_account_6_n
global st_account1pw
global st_account2pw
global st_account3pw
global st_account4pw
global st_account5pw
global st_account6pw
global st_last_price
global st_accounts_range
global st_tokenName
global st_last_ethereum_price
global st_unlockTime
global st_balance
global st_balanceOf
global st_unlock
global st_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
st_token_d = 1e18
_e_d = 1e18
st_accounts_range = '[0, 6]'
st_unlock = web3.personal.unlockAccount
st_last_ethereum_price = 370.00
st_last_price = 0.62
st_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
st_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
st_tokenName = 'FirstBlood Token'
st_unlockTime = hex(10000) # Must be hex()
st_account_0_a = st_accounts[0]
st_account_1_a = st_accounts[1]
st_account_2_a = st_accounts[2]
st_account_3_a = st_accounts[3]
st_account_4_a = st_accounts[4]
st_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
st_account_6_a = st_accounts[6]
# Supply Unlock Passwords For Transactions Below
st_account_0_pw = 'GuildSkrypt2017!@#'
st_account_1_pw = ''
st_account_2_pw = 'GuildSkrypt2017!@#'
st_account_3_pw = ''
st_account_4_pw = ''
st_account_5_pw = ''
st_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
st_account_0_n = 'Skotys Bittrex Account'
st_account_1_n = 'Jeffs Account'
st_account_2_n = 'Skrypts Bittrex Account'
st_account_3_n = 'Skotys Personal Account'
st_account_4_n = 'Unknown'
st_account_5_n = 'Watched \'Bittrex\' Account.'
st_account_6_n = 'Watched Account (1)'
# Contract Information Below :
st_address = '0xAf30D2a7E90d7DC361c8C4585e9BB7D2F6f15bc7'
st_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":true,"inputs":[],"name":"endBlock","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"bountyAllocated","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"signer","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"blockNumber","type":"uint256"}],"name":"testPrice","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"presaleEtherRaised","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"startBlock","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[],"name":"allocateBountyAndEcosystemTokens","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"founder","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[],"name":"halt","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"etherCap","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"ecosystemAllocated","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"founderAllocation","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"founderLockup","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"newFounder","type":"address"}],"name":"changeFounder","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":true,"inputs":[],"name":"founderAllocated","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"price","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"halted","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"allocateFounderTokens","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"ecosystemAllocation","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"transferLockup","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"presaleTokenSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[],"name":"unhalt","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"buyRecipient","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"buy","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"bountyAllocation","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"inputs":[{"name":"founderInput","type":"address"},{"name":"signerInput","type":"address"},{"name":"startBlockInput","type":"uint256"},{"name":"endBlockInput","type":"uint256"}],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"sender","type":"address"},{"indexed":false,"name":"eth","type":"uint256"},{"indexed":false,"name":"fbt","type":"uint256"}],"name":"Buy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"sender","type":"address"},{"indexed":false,"name":"to","type":"address"},{"indexed":false,"name":"eth","type":"uint256"}],"name":"Withdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"sender","type":"address"}],"name":"AllocateFounderTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"sender","type":"address"}],"name":"AllocateBountyAndEcosystemTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
st = web3.eth.contract(abi=st_abi, address=st_address)
st_balanceOf = st.call().balanceOf
# End Contract Information
def st_update_accounts():
 global st_account0
 global st_account1
 global st_account2
 global st_account3
 global st_account4
 global st_account5
 global st_account6
 global st_account0_n
 global st_account1_n
 global st_account2_n
 global st_account3_n
 global st_account4_n
 global st_account5_n
 global st_account6_n
 global st_account0pw
 global st_account1pw
 global st_account2pw
 global st_account3pw
 global st_account4pw
 global st_account5pw
 global st_account6pw
 st_account0 = st_account_0_a
 st_account1 = st_account_1_a
 st_account2 = st_account_2_a
 st_account3 = st_account_3_a
 st_account4 = st_account_4_a
 st_account5 = st_account_5_a
 st_account6 = st_account_6_a
 st_account0_n = st_account_0_n
 st_account1_n = st_account_1_n
 st_account2_n = st_account_2_n
 st_account3_n = st_account_3_n
 st_account4_n = st_account_4_n
 st_account5_n = st_account_5_n
 st_account6_n = st_account_6_n
 st_account0pw = st_account_0_pw
 st_account1pw = st_account_1_pw
 st_account2pw = st_account_2_pw
 st_account3pw = st_account_3_pw
 st_account4pw = st_account_4_pw
 st_account5pw = st_account_5_pw
 st_account6pw = st_account_6_pw
 print(st_tokenName+' Accounts Updated.')
def st_update_balances():
 global st_call_0
 global st_call_1
 global st_call_2
 global st_call_3
 global st_call_4
 global st_call_5
 global st_call_6
 global st_w_call_0
 global st_w_call_1
 global st_w_call_2
 global st_w_call_3
 global st_w_call_4
 global st_w_call_5
 global st_w_call_6
 st_update_accounts()
 print('Updating '+st_tokenName+' Balances Please Wait...')
 st_call_0 = st_balanceOf(st_account0)
 st_call_1 = st_balanceOf(st_account1)
 st_call_2 = st_balanceOf(st_account2)
 st_call_3 = st_balanceOf(st_account3)
 st_call_4 = st_balanceOf(st_account4)
 st_call_5 = st_balanceOf(st_account5)
 st_call_6 = st_balanceOf(st_account6)
 st_w_call_0 = st_balance(st_account0)
 st_w_call_1 = st_balance(st_account1)
 st_w_call_2 = st_balance(st_account2)
 st_w_call_3 = st_balance(st_account3)
 st_w_call_4 = st_balance(st_account4)
 st_w_call_5 = st_balance(st_account5)
 st_w_call_6 = st_balance(st_account6)
 print(st_tokenName+' Balances Updated.')
def st_list_all_accounts():
 st_update_accounts()
 print(st_tokenName+' '+st_account0_n+': '+st_account0)
 print(st_tokenName+' '+st_account1_n+': '+st_account1)
 print(st_tokenName+' '+st_account2_n+': '+st_account2)
 print(st_tokenName+' '+st_account3_n+': '+st_account3)
 print(st_tokenName+' '+st_account4_n+': '+st_account4)
 print(st_tokenName+' '+st_account5_n+': '+st_account5)
 print(st_tokenName+' '+st_account6_n+': '+st_account6)

def st_account_balance(accountNumber):
 st_update_balances()
 st_ab_account_number = accountNumber
 st_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if st_ab_account_number == st_ab_input[0]:
  print('Calling '+st_account0_n+' '+st_tokenName+' Balance: ')
  print(st_account0_n+': '+st_tokenName+' Balance: '+str(st_call_0 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_0 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[1]:
  print('Calling '+st_account1_n+' '+st_tokenName+' Balance: ')
  print(st_account1_n+': '+st_tokenName+' Balance: '+str(st_call_1 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_1 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[2]:
  print('Calling '+st_account2_n+' '+st_tokenName+' Balance: ')
  print(st_account2_n+': '+st_tokenName+' Balance: '+str(st_call_2 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_2 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[3]:
  print('Calling '+st_account3_n+' '+st_tokenName+' Balance: ')
  print(st_account3_n+': '+st_tokenName+' Balance: '+str(st_call_3 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_3 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[4]:
  print('Calling '+st_account4_n+' '+st_tokenName+' Balance: ')
  print(st_account4_n+': '+st_tokenName+' Balance: '+str(st_call_4 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_4 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[5]:
  print('Calling '+st_account5_n+' '+st_tokenName+' Balance: ')
  print(st_account5_n+': '+st_tokenName+' Balance: '+str(st_call_5 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_5 / st_token_d * st_last_price))
 if st_ab_account_number == st_ab_input[6]:
  print('Calling '+st_account6_n+' '+st_tokenName+' Balance: ')
  print(st_account6_n+': '+st_tokenName+' Balance: '+str(st_call_6 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_6 / st_token_d * st_last_price))
 if st_ab_account_number not in st_ab_input:
  print('Must Integer Within Range '+st_accounts_range+'.')

def st_list_all_account_balances():
 st_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+st_tokenName+' Balance: ')
 print(st_account0_n+': '+st_tokenName+' Balance: '+str(st_call_0 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_0 / st_token_d * st_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(st_account0_n+': Ethereum Balance '+str(st_w_call_0 / _e_d)+' $'+str(st_w_call_0 / _e_d * st_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+st_tokenName+' Balance: ')
 print(st_account1_n+': '+st_tokenName+' Balance: '+str(st_call_1 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_1 / st_token_d * st_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(st_account1_n+': Ethereum Balance '+str(st_w_call_1 / _e_d)+' $'+str(st_w_call_1 / _e_d * st_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+st_tokenName+' Balance: ')
 print(st_account2_n+': '+st_tokenName+' Balance: '+str(st_call_2 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_2 / st_token_d * st_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(st_account2_n+': Ethereum Balance '+str(st_w_call_2 / _e_d)+' $'+str(st_w_call_2 / _e_d * st_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+st_tokenName+' Balance: ')
 print(st_account3_n+': '+st_tokenName+' Balance: '+str(st_call_3 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_3 / st_token_d * st_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(st_account3_n+': Ethereum Balance '+str(st_w_call_3 / _e_d)+' $'+str(st_w_call_3 / _e_d * st_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+st_tokenName+' Balance: ')
 print(st_account4_n+': '+st_tokenName+' Balance: '+str(st_call_4 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_4 / st_token_d * st_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(st_account4_n+': Ethereum Balance '+str(st_w_call_4 / _e_d)+' $'+str(st_w_call_4 / _e_d * st_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+st_tokenName+' Balance: ')
 print(st_account5_n+': '+st_tokenName+' Balance: '+str(st_call_5 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_5 / st_token_d * st_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(st_account5_n+': Ethereum Balance '+str(st_w_call_5 / _e_d)+' $'+str(st_w_call_5 /_e_d * st_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+st_tokenName+' Balance: ')
 print(st_account6_n+': '+st_tokenName+' Balance: '+str(st_call_6 / st_token_d)+' Usd/'+st_tokenName+' Balance: $'+str(st_call_6 / st_token_d * st_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(st_account6_n+': Ethereum Balance '+str(st_w_call_6 / _e_d)+' $'+str(st_w_call_6 / _e_d * st_last_ethereum_price))
def st_unlock_all_accounts():
  st_unlock_account_0()
  st_unlock_account_1()
  st_unlock_account_2()
  st_unlock_account_3()
  st_unlock_account_4()
  st_unlock_account_5()
  st_unlock_account_6()


def st_unlock_account_0():
  global st_account0pw
  global st_account0
  global st_account0_n
  st_update_accounts()
  st_u_a_0 = st_w_unlock(st_account0, st_account0pw, st_unlockTime)
  if st_u_a_0 == False:
    if st_account0pw == '':
     st_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account0_n+' Passphrase Denied: '+st_account0pw_r)
    elif st_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+st_account0_n+' Passphrase Denied: '+st_account0pw)
  if st_u_a_0 == True:
   print(st_account0_n+' Unlocked')

def st_unlock_account_1():
  global st_account1pw
  global st_account1
  global st_account1_n
  st_update_accounts()
  st_u_a_1 = st_unlock(st_account1, st_account1pw, st_unlockTime)
  if st_u_a_1 == False:
    if st_account1pw == '':
     st_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account1_n+' Passphrase Denied: '+st_account1pw_r)
    elif st_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+st_account1_n+' Passphrase Denied: '+st_account1pw)
  if st_u_a_1 == True:
   print(st_account1_n+' Unlocked')

def st_unlock_account_2():
  global st_account2pw
  global st_account2
  global st_account2_n
  st_update_accounts()
  st_u_a_2 = st_unlock(st_account2, st_account2pw, st_unlockTime)
  if st_u_a_2 == False:
    if st_account2pw == '':
     st_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account2_n+' Passphrase Denied: '+st_account2pw_r)
    elif st_account2pw != '':
     print('Unlock Failure With Account '+st_account2_n+' Passphrase Denied: '+st_account2pw)
  if st_u_a_2 == True:
   print(st_account2_n+' Unlocked')

def st_unlock_account_3():
  global st_account3pw
  global st_account3
  global st_account3_n
  st_update_accounts()
  st_u_a_3 = st_unlock(st_account3, st_account3pw, st_unlockTime)
  if st_u_a_3 == False:
    if st_account3pw == '':
     st_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account3_n+' Passphrase Denied: '+st_account3pw_r)
    elif st_account3pw != '':
     print('Unlock Failure With Account '+st_account3_n+' Passphrase Denied: '+st_account3pw)
  if st_u_a_3 == True:
   print(st_account3_n+' Unlocked')

def st_unlock_account_4():
  global st_account4pw
  global st_account4
  global st_account4_n
  st_update_accounts()
  st_u_a_4 = st_unlock(st_account4, st_account4pw, st_unlockTime)
  if st_u_a_4 == False:
    if st_account4pw == '':
     st_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account4_n+' Passphrase Denied: '+st_account4pw_r)
    elif st_account4pw != '':
     print('Unlock Failure With Account '+st_account4_n+' Passphrase Denied: '+st_account4pw)
  if st_u_a_4 == True:
   print(st_account4_n+' Unlocked')

def st_unlock_account_5():
  global st_account5pw
  global st_account5
  global st_account5_n
  st_update_accounts()
  st_u_a_5 = st_unlock(st_account5, st_account5pw, st_unlockTime)
  if st_u_a_5 == False:
    if st_account5pw == '':
     st_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account5_n+' Passphrase Denied: '+st_account5pw_r)
    elif st_account5pw != '':
     print('Unlock Failure With Account '+st_account5_n+' Passphrase Denied: '+st_account5pw)
  if st_u_a_5 == True:
   print(st_account5_n+' Unlocked')

def st_unlock_account_6():
  global st_account6pw
  global st_account6
  global st_account6_n
  st_update_accounts()
  st_u_a_6 = st_unlock(st_account6, st_account6pw, st_unlockTime)
  if st_u_a_6 == False:
    if st_account6pw == '':
     st_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+st_account6_n+' Passphrase Denied: '+st_account6pw_r)
    elif st_account6pw != '':
     print('Unlock Failure With Account '+st_account6_n+' Passphrase Denied: '+st_account6pw)
  if st_u_a_6 == True:
   print(st_account6_n+' Unlocked')

def st_unlock_account(st_ua_accountNumber):
 st_update_accounts()
 st_ua_account_number = st_ua_accountNumber
 st_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if st_ua_account_number == st_ua_input[0]:
  st_unlock_account_0()
 if st_ua_account_number == st_ua_input[1]:
  st_unlock_account_1()
 if st_ua_account_number == st_ua_input[2]:
  st_unlock_account_2()
 if st_ua_account_number == st_ua_input[3]:
  st_unlock_account_3()
 if st_ua_account_number == st_ua_input[4]:
  st_unlock_account_4()
 if st_ua_account_number == st_ua_input[5]:
  st_unlock_account_5()
 if st_ua_account_number == st_ua_input[6]:
  st_unlock_account_6()
 if st_ua_account_number not in st_ua_input:
  print('Must Integer Within Range '+st_accounts_range+'.')
 

def st_approve_between_accounts(fromAccount, toAccount, msgValue):
  st_update_accounts()
  st_a_0 = st.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(st_a_0)

def st_approve(fromAccountNumber, toAddress, msgValue):
  st_update_accounts()
  st_unlock_account(fromAccountNumber)
  st_a_1 = st.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(st_a_1)

def st_transfer_between_accounts(fromAccount, toAccount, msgValue):
  st_update_accounts()
  st_unlock_account(fromAccount)
  st_t_0 = st.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(st_t_0)

def st_transfer(fromAccountNumber, toAddress, msgValue):
  st_update_accounts()
  st_unlock_account(fromAccountNumber)
  st_t_1 = st.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(st_t_1)

def st_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  st_update_accounts()
  st_unlock_account(callAccount)
  st_tf_0 = st.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(st_tf_0)

def st_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  st_update_accounts()
  st_unlock_account(callAccount)
  st_tf_1 = st.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(st_tf_1)
  


def st_help():
  print('Following Functions For '+st_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * st_unlock => web3.personal.unlockAccount
/ * st_accounts => web3.personal.listAccounts
/ * st_balance = web3.eth.getBalance
** st => web3.eth.contract(abi=st_abi, address=st_address)
** / * st_balanceOf => st.call().balanceOf

~ Function Listing Below:
~ st_update_accounts()
~ st_update_balances() \n\r -- => st_update_accounts()
~ st_list_all_accounts() \n\r -- => st_update_accounts()
~ st_account_balance(accountNumber) \n\r -- => st_update_balances() 
~ st_list_all_account_balances() \n\r -- => st_update_balances()
~ st_unlock_all_accounts() \n\r -- => st_unlock_account_0() \n\r -- => st_unlock_account_1() \n\r -- => st_unlock_account_2() \n\r -- => st_unlock_account_3() \n\r -- => st_unlock_account_4() \n\r -- => st_unlock_account_5() \n\r -- => st_unlock_account_6() 
~ st_unlock_account_0() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account0, st_account0pw, st_unlockTime)
~ st_unlock_account_1() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account1, st_account0pw, st_unlockTime)
~ st_unlock_account_2() \n\r -- => st_update_accounts() \n\r --/ *st_w_unlock(st_account2, st_account0pw, st_unlockTime)
~ st_unlock_account_3() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account3, st_account0pw, st_unlockTime)
~ st_unlock_account_4() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account4, st_account0pw, st_unlockTime)
~ st_unlock_account_5() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account5, st_account0pw, st_unlockTime)
~ st_unlock_account_6() \n\r -- => st_update_accounts() \n\r -- / *st_w_unlock(st_account6, st_account0pw, st_unlockTime)
~ st_unlock_account(st_ua_accountNumber) \n\r -- => st_update_accounts() \n\r -- // st_unlock_account_0() \n\r -- // st_unlock_account_1() \n\r -- // st_unlock_account_2() \n\r -- // st_unlock_account_3() \n\r -- // st_unlock_account_4() \n\r -- // st_unlock_account_5() \n\r -- // st_unlock_account_6()
~ st_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(fromAccount) \n\r -- / ** st.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ st_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(fromAccountNumber) \n\r -- / ** st.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ st_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(fromAccount) \n\r -- / ** st.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ st_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(fromAccountNumber) \n\r -- / ** st.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ st_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(callAccount) \n\r / ** st.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ st_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => st_update_accounts() \n\r -- => st_unlock_account(callAccount) \n\r -- / ** st.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ st_help() <-- You Are Here. ''')