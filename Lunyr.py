#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global lun_account_0_a
global lun_account_1_a
global lun_account_2_a
global lun_account_3_a
global lun_account_4_a
global lun_account_5_a
global lun_account_6_a
global lun_address
global lun_abi
global lun
global lun_call_0
global lun_call_1
global lun_call_2
global lun_call_3
global lun_call_4
global lun_call_5
global lun_call_6
global lun_call_ab
global lun_accounts
global lun_account_0_pw
global lun_account_1_pw
global lun_account_2_pw
global lun_account_3_pw
global lun_account_4_pw
global lun_account_5_pw
global lun_account_6_pw
global lun_account_0_n
global lun_account_1_n
global lun_account_2_n
global lun_account_3_n
global lun_account_4_n
global lun_account_5_n
global lun_account_6_n
global lun_account1pw
global lun_account2pw
global lun_account3pw
global lun_account4pw
global lun_account5pw
global lun_account6pw
global lun_last_price
global lun_accounts_range
global lun_tokenName
global lun_last_ethereum_price
global lun_unlockTime
global lun_balance
global lun_balanceOf
global lun_unlock
global lun_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
lun_token_d = 1e18
_e_d = 1e18
lun_accounts_range = '[0, 6]'
lun_unlock = web3.personal.unlockAccount
lun_last_ethereum_price = 370.00
lun_last_price = 13.12
lun_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
lun_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
lun_tokenName = 'Lunyr Token'
lun_unlockTime = hex(10000) # Must be hex()
lun_account_0_a = lun_accounts[0]
lun_account_1_a = lun_accounts[1]
lun_account_2_a = lun_accounts[2]
lun_account_3_a = lun_accounts[3]
lun_account_4_a = lun_accounts[4]
lun_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
lun_account_6_a = lun_accounts[6]
# Supply Unlock Passwords For Transactions Below
lun_account_0_pw = 'GuildSkrypt2017!@#'
lun_account_1_pw = ''
lun_account_2_pw = 'GuildSkrypt2017!@#'
lun_account_3_pw = ''
lun_account_4_pw = ''
lun_account_5_pw = ''
lun_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
lun_account_0_n = 'Skotys Bittrex Account'
lun_account_1_n = 'Jeffs Account'
lun_account_2_n = 'Skrypts Bittrex Account'
lun_account_3_n = 'Skotys Personal Account'
lun_account_4_n = 'Unknown'
lun_account_5_n = 'Watched \'Bittrex\' Account.'
lun_account_6_n = 'Watched Account (1)'
# Contract Information Below :
lun_address = '0xfa05A73FfE78ef8f1a739473e462c54bae6567D9'
lun_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"vaultPercentOfTotal","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getState","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"crowdfundPercentOfTotal","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalizeCrowdfunding","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationMax","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lunyrPercentOfTotal","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"value","type":"uint256"}],"name":"upgrade","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeAgent","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"upgradeMaster","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"finalizedCrowdfunding","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"hundredPercent","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isLunyrToken","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lunyrMultisig","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingEndBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokenCreationMin","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalUpgraded","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"fundingStartBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"agent","type":"address"}],"name":"setUpgradeAgent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"create","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"newWallet","type":"address"}],"name":"setMultiSigWallet","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"timeVault","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokensPerEther","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"master","type":"address"}],"name":"setUpgradeMaster","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_lunyrMultisig","type":"address"},{"name":"_upgradeMaster","type":"address"},{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingEndBlock","type":"uint256"}],"payable":false,"type":"constructor"},{"payable":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Upgrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Refund","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"sender","type":"address"},{"indexed":false,"name":"upgradeAgent","type":"address"}],"name":"UpgradeFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"agent","type":"address"}],"name":"UpgradeAgentSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]
lun = web3.eth.contract(abi=lun_abi, address=lun_address)
lun_balanceOf = lun.call().balanceOf
# End Contract Information
def lun_update_accounts():
 global lun_account0
 global lun_account1
 global lun_account2
 global lun_account3
 global lun_account4
 global lun_account5
 global lun_account6
 global lun_account0_n
 global lun_account1_n
 global lun_account2_n
 global lun_account3_n
 global lun_account4_n
 global lun_account5_n
 global lun_account6_n
 global lun_account0pw
 global lun_account1pw
 global lun_account2pw
 global lun_account3pw
 global lun_account4pw
 global lun_account5pw
 global lun_account6pw
 lun_account0 = lun_account_0_a
 lun_account1 = lun_account_1_a
 lun_account2 = lun_account_2_a
 lun_account3 = lun_account_3_a
 lun_account4 = lun_account_4_a
 lun_account5 = lun_account_5_a
 lun_account6 = lun_account_6_a
 lun_account0_n = lun_account_0_n
 lun_account1_n = lun_account_1_n
 lun_account2_n = lun_account_2_n
 lun_account3_n = lun_account_3_n
 lun_account4_n = lun_account_4_n
 lun_account5_n = lun_account_5_n
 lun_account6_n = lun_account_6_n
 lun_account0pw = lun_account_0_pw
 lun_account1pw = lun_account_1_pw
 lun_account2pw = lun_account_2_pw
 lun_account3pw = lun_account_3_pw
 lun_account4pw = lun_account_4_pw
 lun_account5pw = lun_account_5_pw
 lun_account6pw = lun_account_6_pw
 print(lun_tokenName+' Accounts Updated.')
def lun_update_balances():
 global lun_call_0
 global lun_call_1
 global lun_call_2
 global lun_call_3
 global lun_call_4
 global lun_call_5
 global lun_call_6
 global lun_w_call_0
 global lun_w_call_1
 global lun_w_call_2
 global lun_w_call_3
 global lun_w_call_4
 global lun_w_call_5
 global lun_w_call_6
 lun_update_accounts()
 print('Updating '+lun_tokenName+' Balances Please Wait...')
 lun_call_0 = lun_balanceOf(lun_account0)
 lun_call_1 = lun_balanceOf(lun_account1)
 lun_call_2 = lun_balanceOf(lun_account2)
 lun_call_3 = lun_balanceOf(lun_account3)
 lun_call_4 = lun_balanceOf(lun_account4)
 lun_call_5 = lun_balanceOf(lun_account5)
 lun_call_6 = lun_balanceOf(lun_account6)
 lun_w_call_0 = lun_balance(lun_account0)
 lun_w_call_1 = lun_balance(lun_account1)
 lun_w_call_2 = lun_balance(lun_account2)
 lun_w_call_3 = lun_balance(lun_account3)
 lun_w_call_4 = lun_balance(lun_account4)
 lun_w_call_5 = lun_balance(lun_account5)
 lun_w_call_6 = lun_balance(lun_account6)
 print(lun_tokenName+' Balances Updated.')
def lun_list_all_accounts():
 lun_update_accounts()
 print(lun_tokenName+' '+lun_account0_n+': '+lun_account0)
 print(lun_tokenName+' '+lun_account1_n+': '+lun_account1)
 print(lun_tokenName+' '+lun_account2_n+': '+lun_account2)
 print(lun_tokenName+' '+lun_account3_n+': '+lun_account3)
 print(lun_tokenName+' '+lun_account4_n+': '+lun_account4)
 print(lun_tokenName+' '+lun_account5_n+': '+lun_account5)
 print(lun_tokenName+' '+lun_account6_n+': '+lun_account6)

def lun_account_balance(accountNumber):
 lun_update_balances()
 lun_ab_account_number = accountNumber
 lun_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if lun_ab_account_number == lun_ab_input[0]:
  print('Calling '+lun_account0_n+' '+lun_tokenName+' Balance: ')
  print(lun_account0_n+': '+lun_tokenName+' Balance: '+str(lun_call_0 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_0 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[1]:
  print('Calling '+lun_account1_n+' '+lun_tokenName+' Balance: ')
  print(lun_account1_n+': '+lun_tokenName+' Balance: '+str(lun_call_1 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_1 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[2]:
  print('Calling '+lun_account2_n+' '+lun_tokenName+' Balance: ')
  print(lun_account2_n+': '+lun_tokenName+' Balance: '+str(lun_call_2 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_2 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[3]:
  print('Calling '+lun_account3_n+' '+lun_tokenName+' Balance: ')
  print(lun_account3_n+': '+lun_tokenName+' Balance: '+str(lun_call_3 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_3 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[4]:
  print('Calling '+lun_account4_n+' '+lun_tokenName+' Balance: ')
  print(lun_account4_n+': '+lun_tokenName+' Balance: '+str(lun_call_4 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_4 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[5]:
  print('Calling '+lun_account5_n+' '+lun_tokenName+' Balance: ')
  print(lun_account5_n+': '+lun_tokenName+' Balance: '+str(lun_call_5 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_5 / lun_token_d * lun_last_price))
 if lun_ab_account_number == lun_ab_input[6]:
  print('Calling '+lun_account6_n+' '+lun_tokenName+' Balance: ')
  print(lun_account6_n+': '+lun_tokenName+' Balance: '+str(lun_call_6 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_6 / lun_token_d * lun_last_price))
 if lun_ab_account_number not in lun_ab_input:
  print('Must Integer Within Range '+lun_accounts_range+'.')

def lun_list_all_account_balances():
 lun_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+lun_tokenName+' Balance: ')
 print(lun_account0_n+': '+lun_tokenName+' Balance: '+str(lun_call_0 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_0 / lun_token_d * lun_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(lun_account0_n+': Ethereum Balance '+str(lun_w_call_0 / _e_d)+' $'+str(lun_w_call_0 / _e_d * lun_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+lun_tokenName+' Balance: ')
 print(lun_account1_n+': '+lun_tokenName+' Balance: '+str(lun_call_1 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_1 / lun_token_d * lun_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(lun_account1_n+': Ethereum Balance '+str(lun_w_call_1 / _e_d)+' $'+str(lun_w_call_1 / _e_d * lun_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+lun_tokenName+' Balance: ')
 print(lun_account2_n+': '+lun_tokenName+' Balance: '+str(lun_call_2 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_2 / lun_token_d * lun_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(lun_account2_n+': Ethereum Balance '+str(lun_w_call_2 / _e_d)+' $'+str(lun_w_call_2 / _e_d * lun_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+lun_tokenName+' Balance: ')
 print(lun_account3_n+': '+lun_tokenName+' Balance: '+str(lun_call_3 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_3 / lun_token_d * lun_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(lun_account3_n+': Ethereum Balance '+str(lun_w_call_3 / _e_d)+' $'+str(lun_w_call_3 / _e_d * lun_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+lun_tokenName+' Balance: ')
 print(lun_account4_n+': '+lun_tokenName+' Balance: '+str(lun_call_4 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_4 / lun_token_d * lun_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(lun_account4_n+': Ethereum Balance '+str(lun_w_call_4 / _e_d)+' $'+str(lun_w_call_4 / _e_d * lun_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+lun_tokenName+' Balance: ')
 print(lun_account5_n+': '+lun_tokenName+' Balance: '+str(lun_call_5 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_5 / lun_token_d * lun_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(lun_account5_n+': Ethereum Balance '+str(lun_w_call_5 / _e_d)+' $'+str(lun_w_call_5 /_e_d * lun_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+lun_tokenName+' Balance: ')
 print(lun_account6_n+': '+lun_tokenName+' Balance: '+str(lun_call_6 / lun_token_d)+' Usd/'+lun_tokenName+' Balance: $'+str(lun_call_6 / lun_token_d * lun_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(lun_account6_n+': Ethereum Balance '+str(lun_w_call_6 / _e_d)+' $'+str(lun_w_call_6 / _e_d * lun_last_ethereum_price))
def lun_unlock_all_accounts():
  lun_unlock_account_0()
  lun_unlock_account_1()
  lun_unlock_account_2()
  lun_unlock_account_3()
  lun_unlock_account_4()
  lun_unlock_account_5()
  lun_unlock_account_6()


def lun_unlock_account_0():
  global lun_account0pw
  global lun_account0
  global lun_account0_n
  lun_update_accounts()
  lun_u_a_0 = lun_w_unlock(lun_account0, lun_account0pw, lun_unlockTime)
  if lun_u_a_0 == False:
    if lun_account0pw == '':
     lun_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account0_n+' Passphrase Denied: '+lun_account0pw_r)
    elif lun_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+lun_account0_n+' Passphrase Denied: '+lun_account0pw)
  if lun_u_a_0 == True:
   print(lun_account0_n+' Unlocked')

def lun_unlock_account_1():
  global lun_account1pw
  global lun_account1
  global lun_account1_n
  lun_update_accounts()
  lun_u_a_1 = lun_unlock(lun_account1, lun_account1pw, lun_unlockTime)
  if lun_u_a_1 == False:
    if lun_account1pw == '':
     lun_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account1_n+' Passphrase Denied: '+lun_account1pw_r)
    elif lun_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+lun_account1_n+' Passphrase Denied: '+lun_account1pw)
  if lun_u_a_1 == True:
   print(lun_account1_n+' Unlocked')

def lun_unlock_account_2():
  global lun_account2pw
  global lun_account2
  global lun_account2_n
  lun_update_accounts()
  lun_u_a_2 = lun_unlock(lun_account2, lun_account2pw, lun_unlockTime)
  if lun_u_a_2 == False:
    if lun_account2pw == '':
     lun_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account2_n+' Passphrase Denied: '+lun_account2pw_r)
    elif lun_account2pw != '':
     print('Unlock Failure With Account '+lun_account2_n+' Passphrase Denied: '+lun_account2pw)
  if lun_u_a_2 == True:
   print(lun_account2_n+' Unlocked')

def lun_unlock_account_3():
  global lun_account3pw
  global lun_account3
  global lun_account3_n
  lun_update_accounts()
  lun_u_a_3 = lun_unlock(lun_account3, lun_account3pw, lun_unlockTime)
  if lun_u_a_3 == False:
    if lun_account3pw == '':
     lun_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account3_n+' Passphrase Denied: '+lun_account3pw_r)
    elif lun_account3pw != '':
     print('Unlock Failure With Account '+lun_account3_n+' Passphrase Denied: '+lun_account3pw)
  if lun_u_a_3 == True:
   print(lun_account3_n+' Unlocked')

def lun_unlock_account_4():
  global lun_account4pw
  global lun_account4
  global lun_account4_n
  lun_update_accounts()
  lun_u_a_4 = lun_unlock(lun_account4, lun_account4pw, lun_unlockTime)
  if lun_u_a_4 == False:
    if lun_account4pw == '':
     lun_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account4_n+' Passphrase Denied: '+lun_account4pw_r)
    elif lun_account4pw != '':
     print('Unlock Failure With Account '+lun_account4_n+' Passphrase Denied: '+lun_account4pw)
  if lun_u_a_4 == True:
   print(lun_account4_n+' Unlocked')

def lun_unlock_account_5():
  global lun_account5pw
  global lun_account5
  global lun_account5_n
  lun_update_accounts()
  lun_u_a_5 = lun_unlock(lun_account5, lun_account5pw, lun_unlockTime)
  if lun_u_a_5 == False:
    if lun_account5pw == '':
     lun_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account5_n+' Passphrase Denied: '+lun_account5pw_r)
    elif lun_account5pw != '':
     print('Unlock Failure With Account '+lun_account5_n+' Passphrase Denied: '+lun_account5pw)
  if lun_u_a_5 == True:
   print(lun_account5_n+' Unlocked')

def lun_unlock_account_6():
  global lun_account6pw
  global lun_account6
  global lun_account6_n
  lun_update_accounts()
  lun_u_a_6 = lun_unlock(lun_account6, lun_account6pw, lun_unlockTime)
  if lun_u_a_6 == False:
    if lun_account6pw == '':
     lun_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+lun_account6_n+' Passphrase Denied: '+lun_account6pw_r)
    elif lun_account6pw != '':
     print('Unlock Failure With Account '+lun_account6_n+' Passphrase Denied: '+lun_account6pw)
  if lun_u_a_6 == True:
   print(lun_account6_n+' Unlocked')

def lun_unlock_account(lun_ua_accountNumber):
 lun_update_accounts()
 lun_ua_account_number = lun_ua_accountNumber
 lun_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if lun_ua_account_number == lun_ua_input[0]:
  lun_unlock_account_0()
 if lun_ua_account_number == lun_ua_input[1]:
  lun_unlock_account_1()
 if lun_ua_account_number == lun_ua_input[2]:
  lun_unlock_account_2()
 if lun_ua_account_number == lun_ua_input[3]:
  lun_unlock_account_3()
 if lun_ua_account_number == lun_ua_input[4]:
  lun_unlock_account_4()
 if lun_ua_account_number == lun_ua_input[5]:
  lun_unlock_account_5()
 if lun_ua_account_number == lun_ua_input[6]:
  lun_unlock_account_6()
 if lun_ua_account_number not in lun_ua_input:
  print('Must Integer Within Range '+lun_accounts_range+'.')
 

def lun_approve_between_accounts(fromAccount, toAccount, msgValue):
  lun_update_accounts()
  lun_a_0 = lun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(lun_a_0)

def lun_approve(fromAccountNumber, toAddress, msgValue):
  lun_update_accounts()
  lun_unlock_account(fromAccountNumber)
  lun_a_1 = lun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(lun_a_1)

def lun_transfer_between_accounts(fromAccount, toAccount, msgValue):
  lun_update_accounts()
  lun_unlock_account(fromAccount)
  lun_t_0 = lun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(lun_t_0)

def lun_transfer(fromAccountNumber, toAddress, msgValue):
  lun_update_accounts()
  lun_unlock_account(fromAccountNumber)
  lun_t_1 = lun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(lun_t_1)

def lun_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  lun_update_accounts()
  lun_unlock_account(callAccount)
  lun_tf_0 = lun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(lun_tf_0)

def lun_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  lun_update_accounts()
  lun_unlock_account(callAccount)
  lun_tf_1 = lun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(lun_tf_1)
  


def lun_help():
  print('Following Functions For '+lun_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * lun_unlock => web3.personal.unlockAccount
/ * lun_accounts => web3.personal.listAccounts
/ * lun_balance = web3.eth.getBalance
** lun => web3.eth.contract(abi=lun_abi, address=lun_address)
** / * lun_balanceOf => lun.call().balanceOf

~ Function Listing Below:
~ lun_update_accounts()
~ lun_update_balances() \n\r -- => lun_update_accounts()
~ lun_list_all_accounts() \n\r -- => lun_update_accounts()
~ lun_account_balance(accountNumber) \n\r -- => lun_update_balances() 
~ lun_list_all_account_balances() \n\r -- => lun_update_balances()
~ lun_unlock_all_accounts() \n\r -- => lun_unlock_account_0() \n\r -- => lun_unlock_account_1() \n\r -- => lun_unlock_account_2() \n\r -- => lun_unlock_account_3() \n\r -- => lun_unlock_account_4() \n\r -- => lun_unlock_account_5() \n\r -- => lun_unlock_account_6() 
~ lun_unlock_account_0() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account0, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_1() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account1, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_2() \n\r -- => lun_update_accounts() \n\r --/ *lun_w_unlock(lun_account2, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_3() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account3, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_4() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account4, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_5() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account5, lun_account0pw, lun_unlockTime)
~ lun_unlock_account_6() \n\r -- => lun_update_accounts() \n\r -- / *lun_w_unlock(lun_account6, lun_account0pw, lun_unlockTime)
~ lun_unlock_account(lun_ua_accountNumber) \n\r -- => lun_update_accounts() \n\r -- // lun_unlock_account_0() \n\r -- // lun_unlock_account_1() \n\r -- // lun_unlock_account_2() \n\r -- // lun_unlock_account_3() \n\r -- // lun_unlock_account_4() \n\r -- // lun_unlock_account_5() \n\r -- // lun_unlock_account_6()
~ lun_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(fromAccount) \n\r -- / ** lun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ lun_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(fromAccountNumber) \n\r -- / ** lun.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ lun_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(fromAccount) \n\r -- / ** lun.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ lun_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(fromAccountNumber) \n\r -- / ** lun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ lun_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(callAccount) \n\r / ** lun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ lun_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => lun_update_accounts() \n\r -- => lun_unlock_account(callAccount) \n\r -- / ** lun.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ lun_help() <-- You Are Here. ''')