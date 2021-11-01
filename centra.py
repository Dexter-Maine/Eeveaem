#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global ctr_account_0_a
global ctr_account_1_a
global ctr_account_2_a
global ctr_account_3_a
global ctr_account_4_a
global ctr_account_5_a
global ctr_account_6_a
global ctr_address
global ctr_abi
global ctr
global ctr_call_0
global ctr_call_1
global ctr_call_2
global ctr_call_3
global ctr_call_4
global ctr_call_5
global ctr_call_6
global ctr_call_ab
global ctr_accounts
global ctr_account_0_pw
global ctr_account_1_pw
global ctr_account_2_pw
global ctr_account_3_pw
global ctr_account_4_pw
global ctr_account_5_pw
global ctr_account_6_pw
global ctr_account_0_n
global ctr_account_1_n
global ctr_account_2_n
global ctr_account_3_n
global ctr_account_4_n
global ctr_account_5_n
global ctr_account_6_n
global ctr_account1pw
global ctr_account2pw
global ctr_account3pw
global ctr_account4pw
global ctr_account5pw
global ctr_account6pw
global ctr_last_price
global ctr_accounts_range
global ctr_tokenName
global ctr_last_ethereum_price
global ctr_unlockTime
global ctr_balance
global ctr_balanceOf
global ctr_unlock
global ctr_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
ctr_token_d = 1e18
_e_d = 1e18
ctr_accounts_range = '[0, 6]'
ctr_unlock = web3.personal.unlockAccount
ctr_last_ethereum_price = 370.00
ctr_last_price = 0.97
ctr_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
ctr_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
ctr_tokenName = 'Centra Token'
ctr_unlockTime = hex(10000) # Must be hex()
ctr_account_0_a = ctr_accounts[0]
ctr_account_1_a = ctr_accounts[1]
ctr_account_2_a = ctr_accounts[2]
ctr_account_3_a = ctr_accounts[3]
ctr_account_4_a = ctr_accounts[4]
ctr_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
ctr_account_6_a = ctr_accounts[6]
# Supply Unlock Passwords For Transactions Below
ctr_account_0_pw = 'GuildSkrypt2017!@#'
ctr_account_1_pw = ''
ctr_account_2_pw = 'GuildSkrypt2017!@#'
ctr_account_3_pw = ''
ctr_account_4_pw = ''
ctr_account_5_pw = ''
ctr_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
ctr_account_0_n = 'Skotys Bittrex Account'
ctr_account_1_n = 'Jeffs Account'
ctr_account_2_n = 'Skrypts Bittrex Account'
ctr_account_3_n = 'Skotys Personal Account'
ctr_account_4_n = 'Unknown'
ctr_account_5_n = 'Watched \'Bittrex\' Account.'
ctr_account_6_n = 'Watched Account (1)'
# Contract Information Below :
ctr_address = '0x96A65609a7B84E8842732DEB08f56C3E21aC6f8a'
ctr_abi = [{"constant":true,"inputs":[],"name":"card_blue_first","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"cards_gold","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"totalSupply","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_black_first","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ico_finish","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ownerSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_start_minamount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"withdraw","outputs":[{"name":"result","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_gold_minamount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_black_minamount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_gold_first","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"tokens_buy","outputs":[{"name":"","type":"bool"}],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"cards_black_total","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"cards_titanium_total","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ico_start","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"token_price","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_titanium_first","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"maxValue","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minValue","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"cards_start","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_titanium_minamount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minValuePre","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"cards_titanium","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"cards_blue","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"cards_black","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"cards_start_total","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"cards_black_check","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"cards_blue_total","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_start_first","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"maxTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"cards_gold_total","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"card_blue_minamount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
ctr = web3.eth.contract(abi=ctr_abi, address=ctr_address)
ctr_balanceOf = ctr.call().balanceOf
# End Contract Information
def ctr_update_accounts():
 global ctr_account0
 global ctr_account1
 global ctr_account2
 global ctr_account3
 global ctr_account4
 global ctr_account5
 global ctr_account6
 global ctr_account0_n
 global ctr_account1_n
 global ctr_account2_n
 global ctr_account3_n
 global ctr_account4_n
 global ctr_account5_n
 global ctr_account6_n
 global ctr_account0pw
 global ctr_account1pw
 global ctr_account2pw
 global ctr_account3pw
 global ctr_account4pw
 global ctr_account5pw
 global ctr_account6pw
 ctr_account0 = ctr_account_0_a
 ctr_account1 = ctr_account_1_a
 ctr_account2 = ctr_account_2_a
 ctr_account3 = ctr_account_3_a
 ctr_account4 = ctr_account_4_a
 ctr_account5 = ctr_account_5_a
 ctr_account6 = ctr_account_6_a
 ctr_account0_n = ctr_account_0_n
 ctr_account1_n = ctr_account_1_n
 ctr_account2_n = ctr_account_2_n
 ctr_account3_n = ctr_account_3_n
 ctr_account4_n = ctr_account_4_n
 ctr_account5_n = ctr_account_5_n
 ctr_account6_n = ctr_account_6_n
 ctr_account0pw = ctr_account_0_pw
 ctr_account1pw = ctr_account_1_pw
 ctr_account2pw = ctr_account_2_pw
 ctr_account3pw = ctr_account_3_pw
 ctr_account4pw = ctr_account_4_pw
 ctr_account5pw = ctr_account_5_pw
 ctr_account6pw = ctr_account_6_pw
 print(ctr_tokenName+' Accounts Updated.')
def ctr_update_balances():
 global ctr_call_0
 global ctr_call_1
 global ctr_call_2
 global ctr_call_3
 global ctr_call_4
 global ctr_call_5
 global ctr_call_6
 global ctr_w_call_0
 global ctr_w_call_1
 global ctr_w_call_2
 global ctr_w_call_3
 global ctr_w_call_4
 global ctr_w_call_5
 global ctr_w_call_6
 ctr_update_accounts()
 print('Updating '+ctr_tokenName+' Balances Please Wait...')
 ctr_call_0 = ctr_balanceOf(ctr_account0)
 ctr_call_1 = ctr_balanceOf(ctr_account1)
 ctr_call_2 = ctr_balanceOf(ctr_account2)
 ctr_call_3 = ctr_balanceOf(ctr_account3)
 ctr_call_4 = ctr_balanceOf(ctr_account4)
 ctr_call_5 = ctr_balanceOf(ctr_account5)
 ctr_call_6 = ctr_balanceOf(ctr_account6)
 ctr_w_call_0 = ctr_balance(ctr_account0)
 ctr_w_call_1 = ctr_balance(ctr_account1)
 ctr_w_call_2 = ctr_balance(ctr_account2)
 ctr_w_call_3 = ctr_balance(ctr_account3)
 ctr_w_call_4 = ctr_balance(ctr_account4)
 ctr_w_call_5 = ctr_balance(ctr_account5)
 ctr_w_call_6 = ctr_balance(ctr_account6)
 print(ctr_tokenName+' Balances Updated.')
def ctr_list_all_accounts():
 ctr_update_accounts()
 print(ctr_tokenName+' '+ctr_account0_n+': '+ctr_account0)
 print(ctr_tokenName+' '+ctr_account1_n+': '+ctr_account1)
 print(ctr_tokenName+' '+ctr_account2_n+': '+ctr_account2)
 print(ctr_tokenName+' '+ctr_account3_n+': '+ctr_account3)
 print(ctr_tokenName+' '+ctr_account4_n+': '+ctr_account4)
 print(ctr_tokenName+' '+ctr_account5_n+': '+ctr_account5)
 print(ctr_tokenName+' '+ctr_account6_n+': '+ctr_account6)

def ctr_account_balance(accountNumber):
 ctr_update_balances()
 ctr_ab_account_number = accountNumber
 ctr_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if ctr_ab_account_number == ctr_ab_input[0]:
  print('Calling '+ctr_account0_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account0_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_0 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_0 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[1]:
  print('Calling '+ctr_account1_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account1_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_1 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_1 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[2]:
  print('Calling '+ctr_account2_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account2_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_2 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_2 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[3]:
  print('Calling '+ctr_account3_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account3_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_3 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_3 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[4]:
  print('Calling '+ctr_account4_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account4_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_4 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_4 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[5]:
  print('Calling '+ctr_account5_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account5_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_5 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_5 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number == ctr_ab_input[6]:
  print('Calling '+ctr_account6_n+' '+ctr_tokenName+' Balance: ')
  print(ctr_account6_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_6 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_6 / ctr_token_d * ctr_last_price))
 if ctr_ab_account_number not in ctr_ab_input:
  print('Must Integer Within Range '+ctr_accounts_range+'.')

def ctr_list_all_account_balances():
 ctr_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+ctr_tokenName+' Balance: ')
 print(ctr_account0_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_0 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_0 / ctr_token_d * ctr_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(ctr_account0_n+': Ethereum Balance '+str(ctr_w_call_0 / _e_d)+' $'+str(ctr_w_call_0 / _e_d * ctr_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+ctr_tokenName+' Balance: ')
 print(ctr_account1_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_1 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_1 / ctr_token_d * ctr_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(ctr_account1_n+': Ethereum Balance '+str(ctr_w_call_1 / _e_d)+' $'+str(ctr_w_call_1 / _e_d * ctr_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+ctr_tokenName+' Balance: ')
 print(ctr_account2_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_2 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_2 / ctr_token_d * ctr_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(ctr_account2_n+': Ethereum Balance '+str(ctr_w_call_2 / _e_d)+' $'+str(ctr_w_call_2 / _e_d * ctr_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+ctr_tokenName+' Balance: ')
 print(ctr_account3_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_3 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_3 / ctr_token_d * ctr_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(ctr_account3_n+': Ethereum Balance '+str(ctr_w_call_3 / _e_d)+' $'+str(ctr_w_call_3 / _e_d * ctr_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+ctr_tokenName+' Balance: ')
 print(ctr_account4_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_4 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_4 / ctr_token_d * ctr_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(ctr_account4_n+': Ethereum Balance '+str(ctr_w_call_4 / _e_d)+' $'+str(ctr_w_call_4 / _e_d * ctr_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+ctr_tokenName+' Balance: ')
 print(ctr_account5_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_5 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_5 / ctr_token_d * ctr_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(ctr_account5_n+': Ethereum Balance '+str(ctr_w_call_5 / _e_d)+' $'+str(ctr_w_call_5 /_e_d * ctr_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+ctr_tokenName+' Balance: ')
 print(ctr_account6_n+': '+ctr_tokenName+' Balance: '+str(ctr_call_6 / ctr_token_d)+' Usd/'+ctr_tokenName+' Balance: $'+str(ctr_call_6 / ctr_token_d * ctr_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(ctr_account6_n+': Ethereum Balance '+str(ctr_w_call_6 / _e_d)+' $'+str(ctr_w_call_6 / _e_d * ctr_last_ethereum_price))
def ctr_unlock_all_accounts():
  ctr_unlock_account_0()
  ctr_unlock_account_1()
  ctr_unlock_account_2()
  ctr_unlock_account_3()
  ctr_unlock_account_4()
  ctr_unlock_account_5()
  ctr_unlock_account_6()


def ctr_unlock_account_0():
  global ctr_account0pw
  global ctr_account0
  global ctr_account0_n
  ctr_update_accounts()
  ctr_u_a_0 = ctr_w_unlock(ctr_account0, ctr_account0pw, ctr_unlockTime)
  if ctr_u_a_0 == False:
    if ctr_account0pw == '':
     ctr_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account0_n+' Passphrase Denied: '+ctr_account0pw_r)
    elif ctr_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ctr_account0_n+' Passphrase Denied: '+ctr_account0pw)
  if ctr_u_a_0 == True:
   print(ctr_account0_n+' Unlocked')

def ctr_unlock_account_1():
  global ctr_account1pw
  global ctr_account1
  global ctr_account1_n
  ctr_update_accounts()
  ctr_u_a_1 = ctr_unlock(ctr_account1, ctr_account1pw, ctr_unlockTime)
  if ctr_u_a_1 == False:
    if ctr_account1pw == '':
     ctr_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account1_n+' Passphrase Denied: '+ctr_account1pw_r)
    elif ctr_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+ctr_account1_n+' Passphrase Denied: '+ctr_account1pw)
  if ctr_u_a_1 == True:
   print(ctr_account1_n+' Unlocked')

def ctr_unlock_account_2():
  global ctr_account2pw
  global ctr_account2
  global ctr_account2_n
  ctr_update_accounts()
  ctr_u_a_2 = ctr_unlock(ctr_account2, ctr_account2pw, ctr_unlockTime)
  if ctr_u_a_2 == False:
    if ctr_account2pw == '':
     ctr_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account2_n+' Passphrase Denied: '+ctr_account2pw_r)
    elif ctr_account2pw != '':
     print('Unlock Failure With Account '+ctr_account2_n+' Passphrase Denied: '+ctr_account2pw)
  if ctr_u_a_2 == True:
   print(ctr_account2_n+' Unlocked')

def ctr_unlock_account_3():
  global ctr_account3pw
  global ctr_account3
  global ctr_account3_n
  ctr_update_accounts()
  ctr_u_a_3 = ctr_unlock(ctr_account3, ctr_account3pw, ctr_unlockTime)
  if ctr_u_a_3 == False:
    if ctr_account3pw == '':
     ctr_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account3_n+' Passphrase Denied: '+ctr_account3pw_r)
    elif ctr_account3pw != '':
     print('Unlock Failure With Account '+ctr_account3_n+' Passphrase Denied: '+ctr_account3pw)
  if ctr_u_a_3 == True:
   print(ctr_account3_n+' Unlocked')

def ctr_unlock_account_4():
  global ctr_account4pw
  global ctr_account4
  global ctr_account4_n
  ctr_update_accounts()
  ctr_u_a_4 = ctr_unlock(ctr_account4, ctr_account4pw, ctr_unlockTime)
  if ctr_u_a_4 == False:
    if ctr_account4pw == '':
     ctr_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account4_n+' Passphrase Denied: '+ctr_account4pw_r)
    elif ctr_account4pw != '':
     print('Unlock Failure With Account '+ctr_account4_n+' Passphrase Denied: '+ctr_account4pw)
  if ctr_u_a_4 == True:
   print(ctr_account4_n+' Unlocked')

def ctr_unlock_account_5():
  global ctr_account5pw
  global ctr_account5
  global ctr_account5_n
  ctr_update_accounts()
  ctr_u_a_5 = ctr_unlock(ctr_account5, ctr_account5pw, ctr_unlockTime)
  if ctr_u_a_5 == False:
    if ctr_account5pw == '':
     ctr_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account5_n+' Passphrase Denied: '+ctr_account5pw_r)
    elif ctr_account5pw != '':
     print('Unlock Failure With Account '+ctr_account5_n+' Passphrase Denied: '+ctr_account5pw)
  if ctr_u_a_5 == True:
   print(ctr_account5_n+' Unlocked')

def ctr_unlock_account_6():
  global ctr_account6pw
  global ctr_account6
  global ctr_account6_n
  ctr_update_accounts()
  ctr_u_a_6 = ctr_unlock(ctr_account6, ctr_account6pw, ctr_unlockTime)
  if ctr_u_a_6 == False:
    if ctr_account6pw == '':
     ctr_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+ctr_account6_n+' Passphrase Denied: '+ctr_account6pw_r)
    elif ctr_account6pw != '':
     print('Unlock Failure With Account '+ctr_account6_n+' Passphrase Denied: '+ctr_account6pw)
  if ctr_u_a_6 == True:
   print(ctr_account6_n+' Unlocked')

def ctr_unlock_account(ctr_ua_accountNumber):
 ctr_update_accounts()
 ctr_ua_account_number = ctr_ua_accountNumber
 ctr_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if ctr_ua_account_number == ctr_ua_input[0]:
  ctr_unlock_account_0()
 if ctr_ua_account_number == ctr_ua_input[1]:
  ctr_unlock_account_1()
 if ctr_ua_account_number == ctr_ua_input[2]:
  ctr_unlock_account_2()
 if ctr_ua_account_number == ctr_ua_input[3]:
  ctr_unlock_account_3()
 if ctr_ua_account_number == ctr_ua_input[4]:
  ctr_unlock_account_4()
 if ctr_ua_account_number == ctr_ua_input[5]:
  ctr_unlock_account_5()
 if ctr_ua_account_number == ctr_ua_input[6]:
  ctr_unlock_account_6()
 if ctr_ua_account_number not in ctr_ua_input:
  print('Must Integer Within Range '+ctr_accounts_range+'.')
 

def ctr_approve_between_accounts(fromAccount, toAccount, msgValue):
  ctr_update_accounts()
  ctr_a_0 = ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(ctr_a_0)

def ctr_approve(fromAccountNumber, toAddress, msgValue):
  ctr_update_accounts()
  ctr_unlock_account(fromAccountNumber)
  ctr_a_1 = ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(ctr_a_1)

def ctr_transfer_between_accounts(fromAccount, toAccount, msgValue):
  ctr_update_accounts()
  ctr_unlock_account(fromAccount)
  ctr_t_0 = ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(ctr_t_0)

def ctr_transfer(fromAccountNumber, toAddress, msgValue):
  ctr_update_accounts()
  ctr_unlock_account(fromAccountNumber)
  ctr_t_1 = ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(ctr_t_1)

def ctr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  ctr_update_accounts()
  ctr_unlock_account(callAccount)
  ctr_tf_0 = ctr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(ctr_tf_0)

def ctr_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  ctr_update_accounts()
  ctr_unlock_account(callAccount)
  ctr_tf_1 = ctr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(ctr_tf_1)
  


def ctr_help():
  print('Following Functions For '+ctr_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * ctr_unlock => web3.personal.unlockAccount
/ * ctr_accounts => web3.personal.listAccounts
/ * ctr_balance = web3.eth.getBalance
** ctr => web3.eth.contract(abi=ctr_abi, address=ctr_address)
** / * ctr_balanceOf => ctr.call().balanceOf

~ Function Listing Below:
~ ctr_update_accounts()
~ ctr_update_balances() \n\r -- => ctr_update_accounts()
~ ctr_list_all_accounts() \n\r -- => ctr_update_accounts()
~ ctr_account_balance(accountNumber) \n\r -- => ctr_update_balances() 
~ ctr_list_all_account_balances() \n\r -- => ctr_update_balances()
~ ctr_unlock_all_accounts() \n\r -- => ctr_unlock_account_0() \n\r -- => ctr_unlock_account_1() \n\r -- => ctr_unlock_account_2() \n\r -- => ctr_unlock_account_3() \n\r -- => ctr_unlock_account_4() \n\r -- => ctr_unlock_account_5() \n\r -- => ctr_unlock_account_6() 
~ ctr_unlock_account_0() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account0, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_1() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account1, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_2() \n\r -- => ctr_update_accounts() \n\r --/ *ctr_w_unlock(ctr_account2, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_3() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account3, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_4() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account4, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_5() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account5, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account_6() \n\r -- => ctr_update_accounts() \n\r -- / *ctr_w_unlock(ctr_account6, ctr_account0pw, ctr_unlockTime)
~ ctr_unlock_account(ctr_ua_accountNumber) \n\r -- => ctr_update_accounts() \n\r -- // ctr_unlock_account_0() \n\r -- // ctr_unlock_account_1() \n\r -- // ctr_unlock_account_2() \n\r -- // ctr_unlock_account_3() \n\r -- // ctr_unlock_account_4() \n\r -- // ctr_unlock_account_5() \n\r -- // ctr_unlock_account_6()
~ ctr_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(fromAccount) \n\r -- / ** ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ctr_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(fromAccountNumber) \n\r -- / ** ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ ctr_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(fromAccount) \n\r -- / ** ctr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ ctr_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(fromAccountNumber) \n\r -- / ** ctr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ctr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(callAccount) \n\r / ** ctr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ ctr_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => ctr_update_accounts() \n\r -- => ctr_unlock_account(callAccount) \n\r -- / ** ctr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ ctr_help() <-- You Are Here. ''')