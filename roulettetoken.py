#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global rlt_account_0_a
global rlt_account_1_a
global rlt_account_2_a
global rlt_account_3_a
global rlt_account_4_a
global rlt_account_5_a
global rlt_account_6_a
global rlt_address
global rlt_abi
global rlt
global rlt_call_0
global rlt_call_1
global rlt_call_2
global rlt_call_3
global rlt_call_4
global rlt_call_5
global rlt_call_6
global rlt_call_ab
global rlt_accounts
global rlt_account_0_pw
global rlt_account_1_pw
global rlt_account_2_pw
global rlt_account_3_pw
global rlt_account_4_pw
global rlt_account_5_pw
global rlt_account_6_pw
global rlt_account_0_n
global rlt_account_1_n
global rlt_account_2_n
global rlt_account_3_n
global rlt_account_4_n
global rlt_account_5_n
global rlt_account_6_n
global rlt_account1pw
global rlt_account2pw
global rlt_account3pw
global rlt_account4pw
global rlt_account5pw
global rlt_account6pw
global rlt_last_price
global rlt_accounts_range
global rlt_tokenName
global rlt_last_ethereum_price
global rlt_unlockTime
global rlt_balance
global rlt_balanceOf
global rlt_unlock
global rlt_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
rlt_token_d = 1e10
_e_d = 1e18
rlt_accounts_range = '[0, 6]'
rlt_unlock = web3.personal.unlockAccount
rlt_last_ethereum_price = 370.00
rlt_last_price = 0.05
rlt_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
rlt_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
rlt_tokenName = 'Roulette Token'
rlt_unlockTime = hex(10000) # Must be hex()
rlt_account_0_a = rlt_accounts[0]
rlt_account_1_a = rlt_accounts[1]
rlt_account_2_a = rlt_accounts[2]
rlt_account_3_a = rlt_accounts[3]
rlt_account_4_a = rlt_accounts[4]
rlt_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
rlt_account_6_a = rlt_accounts[6]
# Supply Unlock Passwords For Transactions Below
rlt_account_0_pw = 'GuildSkrypt2017!@#'
rlt_account_1_pw = ''
rlt_account_2_pw = 'GuildSkrypt2017!@#'
rlt_account_3_pw = ''
rlt_account_4_pw = ''
rlt_account_5_pw = ''
rlt_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
rlt_account_0_n = 'Skotys Bittrex Account'
rlt_account_1_n = 'Jeffs Account'
rlt_account_2_n = 'Skrypts Bittrex Account'
rlt_account_3_n = 'Skotys Personal Account'
rlt_account_4_n = 'Unknown'
rlt_account_5_n = 'Watched \'Bittrex\' Account.'
rlt_account_6_n = 'Watched Account (1)'
# Contract Information Below :
rlt_address = '0xcCeD5B8288086BE8c38E23567e684C3740be4D48'
rlt_abi = [{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"tempTokensBalanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getListAddressHolders","outputs":[{"name":"","type":"address[]"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"player","type":"address"},{"name":"partner","type":"address"},{"name":"value_bet","type":"uint256"},{"name":"coef_player","type":"uint256"},{"name":"coef_partner","type":"uint256"}],"name":"emission","outputs":[{"name":"","type":"uint256"},{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"count","type":"uint256"},{"name":"period","type":"uint256"}],"name":"sendTempTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isOperationBlocked","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"supply","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"tempTokensPeriodOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"IsTransferFromOldContractDone","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_developer","type":"address"}],"name":"changeDeveloper","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getCountHolders","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_value","type":"uint256"}],"name":"changeMaxValueBetForEmission","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"infoICO","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"IsTransferTempFromOldContractDone","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_cost","type":"uint256"}],"name":"newCostToken","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"value","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_contract","type":"address"}],"name":"changeDividentContract","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"game","type":"address"}],"name":"deleteGame","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"index","type":"uint256"}],"name":"getItemTempHolders","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"costOfOneToken","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"}],"name":"returnTempTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_manager","type":"address"}],"name":"changeManager","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"isOperationAllowed","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"stopOperation","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"limit","type":"uint256"}],"name":"restoreAllPersistentTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_value","type":"uint256"}],"name":"changeMaxCoefPlayerForEmission","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"runICO","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"stopICO","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"index","type":"uint256"}],"name":"getItemHolders","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"startOperation","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"limit","type":"uint256"}],"name":"restoreAllTempTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getCountTempHolders","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"_allowance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getCostToken","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_value","type":"uint256"}],"name":"changeMaxCoefPartnerForEmission","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"gameListOf","outputs":[{"name":"value","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"initCountTokens","outputs":[{"name":"init_count","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getListTempHolders","outputs":[{"name":"","type":"address[]"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"new_game","type":"address"}],"name":"addNewGame","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"buyer","type":"address"},{"indexed":false,"name":"amountOfTokens","type":"uint256"}],"name":"TokenBuy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"bet","type":"uint256"},{"indexed":false,"name":"coef","type":"uint256"},{"indexed":false,"name":"decimals","type":"uint256"},{"indexed":false,"name":"cost_token","type":"uint256"}],"name":"Emission","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"recipient","type":"address"},{"indexed":false,"name":"count","type":"uint256"},{"indexed":false,"name":"start","type":"uint256"},{"indexed":false,"name":"end","type":"uint256"}],"name":"TempTokensSend","type":"event"}]
rlt = web3.eth.contract(abi=rlt_abi, address=rlt_address)
rlt_balanceOf = rlt.call().balanceOf
# End Contract Information
def rlt_update_accounts():
 global rlt_account0
 global rlt_account1
 global rlt_account2
 global rlt_account3
 global rlt_account4
 global rlt_account5
 global rlt_account6
 global rlt_account0_n
 global rlt_account1_n
 global rlt_account2_n
 global rlt_account3_n
 global rlt_account4_n
 global rlt_account5_n
 global rlt_account6_n
 global rlt_account0pw
 global rlt_account1pw
 global rlt_account2pw
 global rlt_account3pw
 global rlt_account4pw
 global rlt_account5pw
 global rlt_account6pw
 rlt_account0 = rlt_account_0_a
 rlt_account1 = rlt_account_1_a
 rlt_account2 = rlt_account_2_a
 rlt_account3 = rlt_account_3_a
 rlt_account4 = rlt_account_4_a
 rlt_account5 = rlt_account_5_a
 rlt_account6 = rlt_account_6_a
 rlt_account0_n = rlt_account_0_n
 rlt_account1_n = rlt_account_1_n
 rlt_account2_n = rlt_account_2_n
 rlt_account3_n = rlt_account_3_n
 rlt_account4_n = rlt_account_4_n
 rlt_account5_n = rlt_account_5_n
 rlt_account6_n = rlt_account_6_n
 rlt_account0pw = rlt_account_0_pw
 rlt_account1pw = rlt_account_1_pw
 rlt_account2pw = rlt_account_2_pw
 rlt_account3pw = rlt_account_3_pw
 rlt_account4pw = rlt_account_4_pw
 rlt_account5pw = rlt_account_5_pw
 rlt_account6pw = rlt_account_6_pw
 print(rlt_tokenName+' Accounts Updated.')
def rlt_update_balances():
 global rlt_call_0
 global rlt_call_1
 global rlt_call_2
 global rlt_call_3
 global rlt_call_4
 global rlt_call_5
 global rlt_call_6
 global rlt_w_call_0
 global rlt_w_call_1
 global rlt_w_call_2
 global rlt_w_call_3
 global rlt_w_call_4
 global rlt_w_call_5
 global rlt_w_call_6
 rlt_update_accounts()
 print('Updating '+rlt_tokenName+' Balances Please Wait...')
 rlt_call_0 = rlt_balanceOf(rlt_account0)
 rlt_call_1 = rlt_balanceOf(rlt_account1)
 rlt_call_2 = rlt_balanceOf(rlt_account2)
 rlt_call_3 = rlt_balanceOf(rlt_account3)
 rlt_call_4 = rlt_balanceOf(rlt_account4)
 rlt_call_5 = rlt_balanceOf(rlt_account5)
 rlt_call_6 = rlt_balanceOf(rlt_account6)
 rlt_w_call_0 = rlt_balance(rlt_account0)
 rlt_w_call_1 = rlt_balance(rlt_account1)
 rlt_w_call_2 = rlt_balance(rlt_account2)
 rlt_w_call_3 = rlt_balance(rlt_account3)
 rlt_w_call_4 = rlt_balance(rlt_account4)
 rlt_w_call_5 = rlt_balance(rlt_account5)
 rlt_w_call_6 = rlt_balance(rlt_account6)
 print(rlt_tokenName+' Balances Updated.')
def rlt_list_all_accounts():
 rlt_update_accounts()
 print(rlt_tokenName+' '+rlt_account0_n+': '+rlt_account0)
 print(rlt_tokenName+' '+rlt_account1_n+': '+rlt_account1)
 print(rlt_tokenName+' '+rlt_account2_n+': '+rlt_account2)
 print(rlt_tokenName+' '+rlt_account3_n+': '+rlt_account3)
 print(rlt_tokenName+' '+rlt_account4_n+': '+rlt_account4)
 print(rlt_tokenName+' '+rlt_account5_n+': '+rlt_account5)
 print(rlt_tokenName+' '+rlt_account6_n+': '+rlt_account6)

def rlt_account_balance(accountNumber):
 rlt_update_balances()
 rlt_ab_account_number = accountNumber
 rlt_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if rlt_ab_account_number == rlt_ab_input[0]:
  print('Calling '+rlt_account0_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account0_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_0 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_0 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[1]:
  print('Calling '+rlt_account1_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account1_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_1 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_1 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[2]:
  print('Calling '+rlt_account2_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account2_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_2 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_2 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[3]:
  print('Calling '+rlt_account3_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account3_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_3 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_3 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[4]:
  print('Calling '+rlt_account4_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account4_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_4 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_4 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[5]:
  print('Calling '+rlt_account5_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account5_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_5 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_5 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number == rlt_ab_input[6]:
  print('Calling '+rlt_account6_n+' '+rlt_tokenName+' Balance: ')
  print(rlt_account6_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_6 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_6 / rlt_token_d * rlt_last_price))
 if rlt_ab_account_number not in rlt_ab_input:
  print('Must Integer Within Range '+rlt_accounts_range+'.')

def rlt_list_all_account_balances():
 rlt_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+rlt_tokenName+' Balance: ')
 print(rlt_account0_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_0 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_0 / rlt_token_d * rlt_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(rlt_account0_n+': Ethereum Balance '+str(rlt_w_call_0 / _e_d)+' $'+str(rlt_w_call_0 / _e_d * rlt_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+rlt_tokenName+' Balance: ')
 print(rlt_account1_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_1 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_1 / rlt_token_d * rlt_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(rlt_account1_n+': Ethereum Balance '+str(rlt_w_call_1 / _e_d)+' $'+str(rlt_w_call_1 / _e_d * rlt_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+rlt_tokenName+' Balance: ')
 print(rlt_account2_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_2 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_2 / rlt_token_d * rlt_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(rlt_account2_n+': Ethereum Balance '+str(rlt_w_call_2 / _e_d)+' $'+str(rlt_w_call_2 / _e_d * rlt_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+rlt_tokenName+' Balance: ')
 print(rlt_account3_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_3 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_3 / rlt_token_d * rlt_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(rlt_account3_n+': Ethereum Balance '+str(rlt_w_call_3 / _e_d)+' $'+str(rlt_w_call_3 / _e_d * rlt_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+rlt_tokenName+' Balance: ')
 print(rlt_account4_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_4 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_4 / rlt_token_d * rlt_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(rlt_account4_n+': Ethereum Balance '+str(rlt_w_call_4 / _e_d)+' $'+str(rlt_w_call_4 / _e_d * rlt_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+rlt_tokenName+' Balance: ')
 print(rlt_account5_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_5 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_5 / rlt_token_d * rlt_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(rlt_account5_n+': Ethereum Balance '+str(rlt_w_call_5 / _e_d)+' $'+str(rlt_w_call_5 /_e_d * rlt_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+rlt_tokenName+' Balance: ')
 print(rlt_account6_n+': '+rlt_tokenName+' Balance: '+str(rlt_call_6 / rlt_token_d)+' Usd/'+rlt_tokenName+' Balance: $'+str(rlt_call_6 / rlt_token_d * rlt_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(rlt_account6_n+': Ethereum Balance '+str(rlt_w_call_6 / _e_d)+' $'+str(rlt_w_call_6 / _e_d * rlt_last_ethereum_price))
def rlt_unlock_all_accounts():
  rlt_unlock_account_0()
  rlt_unlock_account_1()
  rlt_unlock_account_2()
  rlt_unlock_account_3()
  rlt_unlock_account_4()
  rlt_unlock_account_5()
  rlt_unlock_account_6()


def rlt_unlock_account_0():
  global rlt_account0pw
  global rlt_account0
  global rlt_account0_n
  rlt_update_accounts()
  rlt_u_a_0 = rlt_w_unlock(rlt_account0, rlt_account0pw, rlt_unlockTime)
  if rlt_u_a_0 == False:
    if rlt_account0pw == '':
     rlt_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account0_n+' Passphrase Denied: '+rlt_account0pw_r)
    elif rlt_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rlt_account0_n+' Passphrase Denied: '+rlt_account0pw)
  if rlt_u_a_0 == True:
   print(rlt_account0_n+' Unlocked')

def rlt_unlock_account_1():
  global rlt_account1pw
  global rlt_account1
  global rlt_account1_n
  rlt_update_accounts()
  rlt_u_a_1 = rlt_unlock(rlt_account1, rlt_account1pw, rlt_unlockTime)
  if rlt_u_a_1 == False:
    if rlt_account1pw == '':
     rlt_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account1_n+' Passphrase Denied: '+rlt_account1pw_r)
    elif rlt_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+rlt_account1_n+' Passphrase Denied: '+rlt_account1pw)
  if rlt_u_a_1 == True:
   print(rlt_account1_n+' Unlocked')

def rlt_unlock_account_2():
  global rlt_account2pw
  global rlt_account2
  global rlt_account2_n
  rlt_update_accounts()
  rlt_u_a_2 = rlt_unlock(rlt_account2, rlt_account2pw, rlt_unlockTime)
  if rlt_u_a_2 == False:
    if rlt_account2pw == '':
     rlt_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account2_n+' Passphrase Denied: '+rlt_account2pw_r)
    elif rlt_account2pw != '':
     print('Unlock Failure With Account '+rlt_account2_n+' Passphrase Denied: '+rlt_account2pw)
  if rlt_u_a_2 == True:
   print(rlt_account2_n+' Unlocked')

def rlt_unlock_account_3():
  global rlt_account3pw
  global rlt_account3
  global rlt_account3_n
  rlt_update_accounts()
  rlt_u_a_3 = rlt_unlock(rlt_account3, rlt_account3pw, rlt_unlockTime)
  if rlt_u_a_3 == False:
    if rlt_account3pw == '':
     rlt_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account3_n+' Passphrase Denied: '+rlt_account3pw_r)
    elif rlt_account3pw != '':
     print('Unlock Failure With Account '+rlt_account3_n+' Passphrase Denied: '+rlt_account3pw)
  if rlt_u_a_3 == True:
   print(rlt_account3_n+' Unlocked')

def rlt_unlock_account_4():
  global rlt_account4pw
  global rlt_account4
  global rlt_account4_n
  rlt_update_accounts()
  rlt_u_a_4 = rlt_unlock(rlt_account4, rlt_account4pw, rlt_unlockTime)
  if rlt_u_a_4 == False:
    if rlt_account4pw == '':
     rlt_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account4_n+' Passphrase Denied: '+rlt_account4pw_r)
    elif rlt_account4pw != '':
     print('Unlock Failure With Account '+rlt_account4_n+' Passphrase Denied: '+rlt_account4pw)
  if rlt_u_a_4 == True:
   print(rlt_account4_n+' Unlocked')

def rlt_unlock_account_5():
  global rlt_account5pw
  global rlt_account5
  global rlt_account5_n
  rlt_update_accounts()
  rlt_u_a_5 = rlt_unlock(rlt_account5, rlt_account5pw, rlt_unlockTime)
  if rlt_u_a_5 == False:
    if rlt_account5pw == '':
     rlt_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account5_n+' Passphrase Denied: '+rlt_account5pw_r)
    elif rlt_account5pw != '':
     print('Unlock Failure With Account '+rlt_account5_n+' Passphrase Denied: '+rlt_account5pw)
  if rlt_u_a_5 == True:
   print(rlt_account5_n+' Unlocked')

def rlt_unlock_account_6():
  global rlt_account6pw
  global rlt_account6
  global rlt_account6_n
  rlt_update_accounts()
  rlt_u_a_6 = rlt_unlock(rlt_account6, rlt_account6pw, rlt_unlockTime)
  if rlt_u_a_6 == False:
    if rlt_account6pw == '':
     rlt_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+rlt_account6_n+' Passphrase Denied: '+rlt_account6pw_r)
    elif rlt_account6pw != '':
     print('Unlock Failure With Account '+rlt_account6_n+' Passphrase Denied: '+rlt_account6pw)
  if rlt_u_a_6 == True:
   print(rlt_account6_n+' Unlocked')

def rlt_unlock_account(rlt_ua_accountNumber):
 rlt_update_accounts()
 rlt_ua_account_number = rlt_ua_accountNumber
 rlt_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if rlt_ua_account_number == rlt_ua_input[0]:
  rlt_unlock_account_0()
 if rlt_ua_account_number == rlt_ua_input[1]:
  rlt_unlock_account_1()
 if rlt_ua_account_number == rlt_ua_input[2]:
  rlt_unlock_account_2()
 if rlt_ua_account_number == rlt_ua_input[3]:
  rlt_unlock_account_3()
 if rlt_ua_account_number == rlt_ua_input[4]:
  rlt_unlock_account_4()
 if rlt_ua_account_number == rlt_ua_input[5]:
  rlt_unlock_account_5()
 if rlt_ua_account_number == rlt_ua_input[6]:
  rlt_unlock_account_6()
 if rlt_ua_account_number not in rlt_ua_input:
  print('Must Integer Within Range '+rlt_accounts_range+'.')
 

def rlt_approve_between_accounts(fromAccount, toAccount, msgValue):
  rlt_update_accounts()
  rlt_a_0 = rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(rlt_a_0)

def rlt_approve(fromAccountNumber, toAddress, msgValue):
  rlt_update_accounts()
  rlt_unlock_account(fromAccountNumber)
  rlt_a_1 = rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(rlt_a_1)

def rlt_transfer_between_accounts(fromAccount, toAccount, msgValue):
  rlt_update_accounts()
  rlt_unlock_account(fromAccount)
  rlt_t_0 = rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(rlt_t_0)

def rlt_transfer(fromAccountNumber, toAddress, msgValue):
  rlt_update_accounts()
  rlt_unlock_account(fromAccountNumber)
  rlt_t_1 = rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(rlt_t_1)

def rlt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  rlt_update_accounts()
  rlt_unlock_account(callAccount)
  rlt_tf_0 = rlt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(rlt_tf_0)

def rlt_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  rlt_update_accounts()
  rlt_unlock_account(callAccount)
  rlt_tf_1 = rlt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(rlt_tf_1)
  


def rlt_help():
  print('Following Functions For '+rlt_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * rlt_unlock => web3.personal.unlockAccount
/ * rlt_accounts => web3.personal.listAccounts
/ * rlt_balance = web3.eth.getBalance
** rlt => web3.eth.contract(abi=rlt_abi, address=rlt_address)
** / * rlt_balanceOf => rlt.call().balanceOf

~ Function Listing Below:
~ rlt_update_accounts()
~ rlt_update_balances() \n\r -- => rlt_update_accounts()
~ rlt_list_all_accounts() \n\r -- => rlt_update_accounts()
~ rlt_account_balance(accountNumber) \n\r -- => rlt_update_balances() 
~ rlt_list_all_account_balances() \n\r -- => rlt_update_balances()
~ rlt_unlock_all_accounts() \n\r -- => rlt_unlock_account_0() \n\r -- => rlt_unlock_account_1() \n\r -- => rlt_unlock_account_2() \n\r -- => rlt_unlock_account_3() \n\r -- => rlt_unlock_account_4() \n\r -- => rlt_unlock_account_5() \n\r -- => rlt_unlock_account_6() 
~ rlt_unlock_account_0() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account0, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_1() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account1, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_2() \n\r -- => rlt_update_accounts() \n\r --/ *rlt_w_unlock(rlt_account2, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_3() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account3, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_4() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account4, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_5() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account5, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account_6() \n\r -- => rlt_update_accounts() \n\r -- / *rlt_w_unlock(rlt_account6, rlt_account0pw, rlt_unlockTime)
~ rlt_unlock_account(rlt_ua_accountNumber) \n\r -- => rlt_update_accounts() \n\r -- // rlt_unlock_account_0() \n\r -- // rlt_unlock_account_1() \n\r -- // rlt_unlock_account_2() \n\r -- // rlt_unlock_account_3() \n\r -- // rlt_unlock_account_4() \n\r -- // rlt_unlock_account_5() \n\r -- // rlt_unlock_account_6()
~ rlt_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(fromAccount) \n\r -- / ** rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rlt_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(fromAccountNumber) \n\r -- / ** rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ rlt_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(fromAccount) \n\r -- / ** rlt.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ rlt_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(fromAccountNumber) \n\r -- / ** rlt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rlt_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(callAccount) \n\r / ** rlt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ rlt_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => rlt_update_accounts() \n\r -- => rlt_unlock_account(callAccount) \n\r -- / ** rlt.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ rlt_help() <-- You Are Here. ''')