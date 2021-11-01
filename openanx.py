#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global anx_account_0_a
global anx_account_1_a
global anx_account_2_a
global anx_account_3_a
global anx_account_4_a
global anx_account_5_a
global anx_account_6_a
global anx_address
global anx_abi
global anx
global anx_call_0
global anx_call_1
global anx_call_2
global anx_call_3
global anx_call_4
global anx_call_5
global anx_call_6
global anx_call_ab
global anx_accounts
global anx_account_0_pw
global anx_account_1_pw
global anx_account_2_pw
global anx_account_3_pw
global anx_account_4_pw
global anx_account_5_pw
global anx_account_6_pw
global anx_account_0_n
global anx_account_1_n
global anx_account_2_n
global anx_account_3_n
global anx_account_4_n
global anx_account_5_n
global anx_account_6_n
global anx_account1pw
global anx_account2pw
global anx_account3pw
global anx_account4pw
global anx_account5pw
global anx_account6pw
global anx_last_price
global anx_accounts_range
global anx_tokenName
global anx_last_ethereum_price
global anx_unlockTime
global anx_balance
global anx_balanceOf
global anx_unlock
global anx_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
anx_token_d = 1e18
_e_d = 1e18
anx_accounts_range = '[0, 6]'
anx_unlock = web3.personal.unlockAccount
anx_last_ethereum_price = 370.00
anx_last_price = 0.78
anx_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
anx_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
anx_tokenName = 'OpenANX Token'
anx_unlockTime = hex(10000) # Must be hex()
anx_account_0_a = anx_accounts[0]
anx_account_1_a = anx_accounts[1]
anx_account_2_a = anx_accounts[2]
anx_account_3_a = anx_accounts[3]
anx_account_4_a = anx_accounts[4]
anx_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
anx_account_6_a = anx_accounts[6]
# Supply Unlock Passwords For Transactions Below
anx_account_0_pw = 'GuildSkrypt2017!@#'
anx_account_1_pw = ''
anx_account_2_pw = 'GuildSkrypt2017!@#'
anx_account_3_pw = ''
anx_account_4_pw = ''
anx_account_5_pw = ''
anx_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
anx_account_0_n = 'Skotys Bittrex Account'
anx_account_1_n = 'Jeffs Account'
anx_account_2_n = 'Skrypts Bittrex Account'
anx_account_3_n = 'Skotys Personal Account'
anx_account_4_n = 'Unknown'
anx_account_5_n = 'Watched \'Bittrex\' Account.'
anx_account_6_n = 'Watched Account (1)'
# Contract Information Below :
anx_address = '0x701C244b988a513c945973dEFA05de933b23Fe1D'
anx_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKENS_TOTAL","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_tokensPerKEther","type":"uint256"}],"name":"setTokensPerKEther","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"lockedTokens","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"participant","type":"address"}],"name":"kycVerify","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOfLocked1Y","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"finalised","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"CONTRIBUTIONS_MIN","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"DECIMALS","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"START_DATE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"participant","type":"address"},{"name":"balance","type":"uint256"}],"name":"addPrecommitment","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKENS_SOFT_CAP","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"wallet","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"END_DATE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupplyLocked","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupplyLocked2Y","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"}],"name":"burnFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"TOKENS_HARD_CAP","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"DECIMALSFACTOR","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"CONTRIBUTIONS_MAX","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"LOCKED_2Y_DATE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"NAME","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finalise","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"tokensPerKEther","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"kycRequired","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOfLocked2Y","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupplyLocked1Y","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupplyUnlocked","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"tokenAddress","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferAnyERC20Token","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_wallet","type":"address"}],"name":"setWallet","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOfLocked","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"LOCKED_1Y_DATE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"participant","type":"address"}],"name":"proxyPayment","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"SYMBOL","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"inputs":[{"name":"_wallet","type":"address"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newWallet","type":"address"}],"name":"WalletUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"tokensPerKEther","type":"uint256"}],"name":"TokensPerKEtherUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"buyer","type":"address"},{"indexed":false,"name":"ethers","type":"uint256"},{"indexed":false,"name":"newEtherBalance","type":"uint256"},{"indexed":false,"name":"tokens","type":"uint256"},{"indexed":false,"name":"newTotalSupply","type":"uint256"},{"indexed":false,"name":"tokensPerKEther","type":"uint256"}],"name":"TokensBought","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"participant","type":"address"},{"indexed":false,"name":"balance","type":"uint256"}],"name":"PrecommitmentAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"participant","type":"address"}],"name":"KycVerified","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
anx = web3.eth.contract(abi=anx_abi, address=anx_address)
anx_balanceOf = anx.call().balanceOf
# End Contract Information
def anx_update_accounts():
 global anx_account0
 global anx_account1
 global anx_account2
 global anx_account3
 global anx_account4
 global anx_account5
 global anx_account6
 global anx_account0_n
 global anx_account1_n
 global anx_account2_n
 global anx_account3_n
 global anx_account4_n
 global anx_account5_n
 global anx_account6_n
 global anx_account0pw
 global anx_account1pw
 global anx_account2pw
 global anx_account3pw
 global anx_account4pw
 global anx_account5pw
 global anx_account6pw
 anx_account0 = anx_account_0_a
 anx_account1 = anx_account_1_a
 anx_account2 = anx_account_2_a
 anx_account3 = anx_account_3_a
 anx_account4 = anx_account_4_a
 anx_account5 = anx_account_5_a
 anx_account6 = anx_account_6_a
 anx_account0_n = anx_account_0_n
 anx_account1_n = anx_account_1_n
 anx_account2_n = anx_account_2_n
 anx_account3_n = anx_account_3_n
 anx_account4_n = anx_account_4_n
 anx_account5_n = anx_account_5_n
 anx_account6_n = anx_account_6_n
 anx_account0pw = anx_account_0_pw
 anx_account1pw = anx_account_1_pw
 anx_account2pw = anx_account_2_pw
 anx_account3pw = anx_account_3_pw
 anx_account4pw = anx_account_4_pw
 anx_account5pw = anx_account_5_pw
 anx_account6pw = anx_account_6_pw
 print(anx_tokenName+' Accounts Updated.')
def anx_update_balances():
 global anx_call_0
 global anx_call_1
 global anx_call_2
 global anx_call_3
 global anx_call_4
 global anx_call_5
 global anx_call_6
 global anx_w_call_0
 global anx_w_call_1
 global anx_w_call_2
 global anx_w_call_3
 global anx_w_call_4
 global anx_w_call_5
 global anx_w_call_6
 anx_update_accounts()
 print('Updating '+anx_tokenName+' Balances Please Wait...')
 anx_call_0 = anx_balanceOf(anx_account0)
 anx_call_1 = anx_balanceOf(anx_account1)
 anx_call_2 = anx_balanceOf(anx_account2)
 anx_call_3 = anx_balanceOf(anx_account3)
 anx_call_4 = anx_balanceOf(anx_account4)
 anx_call_5 = anx_balanceOf(anx_account5)
 anx_call_6 = anx_balanceOf(anx_account6)
 anx_w_call_0 = anx_balance(anx_account0)
 anx_w_call_1 = anx_balance(anx_account1)
 anx_w_call_2 = anx_balance(anx_account2)
 anx_w_call_3 = anx_balance(anx_account3)
 anx_w_call_4 = anx_balance(anx_account4)
 anx_w_call_5 = anx_balance(anx_account5)
 anx_w_call_6 = anx_balance(anx_account6)
 print(anx_tokenName+' Balances Updated.')
def anx_list_all_accounts():
 anx_update_accounts()
 print(anx_tokenName+' '+anx_account0_n+': '+anx_account0)
 print(anx_tokenName+' '+anx_account1_n+': '+anx_account1)
 print(anx_tokenName+' '+anx_account2_n+': '+anx_account2)
 print(anx_tokenName+' '+anx_account3_n+': '+anx_account3)
 print(anx_tokenName+' '+anx_account4_n+': '+anx_account4)
 print(anx_tokenName+' '+anx_account5_n+': '+anx_account5)
 print(anx_tokenName+' '+anx_account6_n+': '+anx_account6)

def anx_account_balance(accountNumber):
 anx_update_balances()
 anx_ab_account_number = accountNumber
 anx_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if anx_ab_account_number == anx_ab_input[0]:
  print('Calling '+anx_account0_n+' '+anx_tokenName+' Balance: ')
  print(anx_account0_n+': '+anx_tokenName+' Balance: '+str(anx_call_0 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_0 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[1]:
  print('Calling '+anx_account1_n+' '+anx_tokenName+' Balance: ')
  print(anx_account1_n+': '+anx_tokenName+' Balance: '+str(anx_call_1 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_1 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[2]:
  print('Calling '+anx_account2_n+' '+anx_tokenName+' Balance: ')
  print(anx_account2_n+': '+anx_tokenName+' Balance: '+str(anx_call_2 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_2 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[3]:
  print('Calling '+anx_account3_n+' '+anx_tokenName+' Balance: ')
  print(anx_account3_n+': '+anx_tokenName+' Balance: '+str(anx_call_3 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_3 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[4]:
  print('Calling '+anx_account4_n+' '+anx_tokenName+' Balance: ')
  print(anx_account4_n+': '+anx_tokenName+' Balance: '+str(anx_call_4 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_4 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[5]:
  print('Calling '+anx_account5_n+' '+anx_tokenName+' Balance: ')
  print(anx_account5_n+': '+anx_tokenName+' Balance: '+str(anx_call_5 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_5 / anx_token_d * anx_last_price))
 if anx_ab_account_number == anx_ab_input[6]:
  print('Calling '+anx_account6_n+' '+anx_tokenName+' Balance: ')
  print(anx_account6_n+': '+anx_tokenName+' Balance: '+str(anx_call_6 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_6 / anx_token_d * anx_last_price))
 if anx_ab_account_number not in anx_ab_input:
  print('Must Integer Within Range '+anx_accounts_range+'.')

def anx_list_all_account_balances():
 anx_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+anx_tokenName+' Balance: ')
 print(anx_account0_n+': '+anx_tokenName+' Balance: '+str(anx_call_0 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_0 / anx_token_d * anx_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(anx_account0_n+': Ethereum Balance '+str(anx_w_call_0 / _e_d)+' $'+str(anx_w_call_0 / _e_d * anx_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+anx_tokenName+' Balance: ')
 print(anx_account1_n+': '+anx_tokenName+' Balance: '+str(anx_call_1 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_1 / anx_token_d * anx_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(anx_account1_n+': Ethereum Balance '+str(anx_w_call_1 / _e_d)+' $'+str(anx_w_call_1 / _e_d * anx_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+anx_tokenName+' Balance: ')
 print(anx_account2_n+': '+anx_tokenName+' Balance: '+str(anx_call_2 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_2 / anx_token_d * anx_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(anx_account2_n+': Ethereum Balance '+str(anx_w_call_2 / _e_d)+' $'+str(anx_w_call_2 / _e_d * anx_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+anx_tokenName+' Balance: ')
 print(anx_account3_n+': '+anx_tokenName+' Balance: '+str(anx_call_3 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_3 / anx_token_d * anx_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(anx_account3_n+': Ethereum Balance '+str(anx_w_call_3 / _e_d)+' $'+str(anx_w_call_3 / _e_d * anx_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+anx_tokenName+' Balance: ')
 print(anx_account4_n+': '+anx_tokenName+' Balance: '+str(anx_call_4 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_4 / anx_token_d * anx_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(anx_account4_n+': Ethereum Balance '+str(anx_w_call_4 / _e_d)+' $'+str(anx_w_call_4 / _e_d * anx_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+anx_tokenName+' Balance: ')
 print(anx_account5_n+': '+anx_tokenName+' Balance: '+str(anx_call_5 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_5 / anx_token_d * anx_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(anx_account5_n+': Ethereum Balance '+str(anx_w_call_5 / _e_d)+' $'+str(anx_w_call_5 /_e_d * anx_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+anx_tokenName+' Balance: ')
 print(anx_account6_n+': '+anx_tokenName+' Balance: '+str(anx_call_6 / anx_token_d)+' Usd/'+anx_tokenName+' Balance: $'+str(anx_call_6 / anx_token_d * anx_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(anx_account6_n+': Ethereum Balance '+str(anx_w_call_6 / _e_d)+' $'+str(anx_w_call_6 / _e_d * anx_last_ethereum_price))
def anx_unlock_all_accounts():
  anx_unlock_account_0()
  anx_unlock_account_1()
  anx_unlock_account_2()
  anx_unlock_account_3()
  anx_unlock_account_4()
  anx_unlock_account_5()
  anx_unlock_account_6()


def anx_unlock_account_0():
  global anx_account0pw
  global anx_account0
  global anx_account0_n
  anx_update_accounts()
  anx_u_a_0 = anx_w_unlock(anx_account0, anx_account0pw, anx_unlockTime)
  if anx_u_a_0 == False:
    if anx_account0pw == '':
     anx_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account0_n+' Passphrase Denied: '+anx_account0pw_r)
    elif anx_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+anx_account0_n+' Passphrase Denied: '+anx_account0pw)
  if anx_u_a_0 == True:
   print(anx_account0_n+' Unlocked')

def anx_unlock_account_1():
  global anx_account1pw
  global anx_account1
  global anx_account1_n
  anx_update_accounts()
  anx_u_a_1 = anx_unlock(anx_account1, anx_account1pw, anx_unlockTime)
  if anx_u_a_1 == False:
    if anx_account1pw == '':
     anx_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account1_n+' Passphrase Denied: '+anx_account1pw_r)
    elif anx_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+anx_account1_n+' Passphrase Denied: '+anx_account1pw)
  if anx_u_a_1 == True:
   print(anx_account1_n+' Unlocked')

def anx_unlock_account_2():
  global anx_account2pw
  global anx_account2
  global anx_account2_n
  anx_update_accounts()
  anx_u_a_2 = anx_unlock(anx_account2, anx_account2pw, anx_unlockTime)
  if anx_u_a_2 == False:
    if anx_account2pw == '':
     anx_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account2_n+' Passphrase Denied: '+anx_account2pw_r)
    elif anx_account2pw != '':
     print('Unlock Failure With Account '+anx_account2_n+' Passphrase Denied: '+anx_account2pw)
  if anx_u_a_2 == True:
   print(anx_account2_n+' Unlocked')

def anx_unlock_account_3():
  global anx_account3pw
  global anx_account3
  global anx_account3_n
  anx_update_accounts()
  anx_u_a_3 = anx_unlock(anx_account3, anx_account3pw, anx_unlockTime)
  if anx_u_a_3 == False:
    if anx_account3pw == '':
     anx_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account3_n+' Passphrase Denied: '+anx_account3pw_r)
    elif anx_account3pw != '':
     print('Unlock Failure With Account '+anx_account3_n+' Passphrase Denied: '+anx_account3pw)
  if anx_u_a_3 == True:
   print(anx_account3_n+' Unlocked')

def anx_unlock_account_4():
  global anx_account4pw
  global anx_account4
  global anx_account4_n
  anx_update_accounts()
  anx_u_a_4 = anx_unlock(anx_account4, anx_account4pw, anx_unlockTime)
  if anx_u_a_4 == False:
    if anx_account4pw == '':
     anx_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account4_n+' Passphrase Denied: '+anx_account4pw_r)
    elif anx_account4pw != '':
     print('Unlock Failure With Account '+anx_account4_n+' Passphrase Denied: '+anx_account4pw)
  if anx_u_a_4 == True:
   print(anx_account4_n+' Unlocked')

def anx_unlock_account_5():
  global anx_account5pw
  global anx_account5
  global anx_account5_n
  anx_update_accounts()
  anx_u_a_5 = anx_unlock(anx_account5, anx_account5pw, anx_unlockTime)
  if anx_u_a_5 == False:
    if anx_account5pw == '':
     anx_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account5_n+' Passphrase Denied: '+anx_account5pw_r)
    elif anx_account5pw != '':
     print('Unlock Failure With Account '+anx_account5_n+' Passphrase Denied: '+anx_account5pw)
  if anx_u_a_5 == True:
   print(anx_account5_n+' Unlocked')

def anx_unlock_account_6():
  global anx_account6pw
  global anx_account6
  global anx_account6_n
  anx_update_accounts()
  anx_u_a_6 = anx_unlock(anx_account6, anx_account6pw, anx_unlockTime)
  if anx_u_a_6 == False:
    if anx_account6pw == '':
     anx_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+anx_account6_n+' Passphrase Denied: '+anx_account6pw_r)
    elif anx_account6pw != '':
     print('Unlock Failure With Account '+anx_account6_n+' Passphrase Denied: '+anx_account6pw)
  if anx_u_a_6 == True:
   print(anx_account6_n+' Unlocked')

def anx_unlock_account(anx_ua_accountNumber):
 anx_update_accounts()
 anx_ua_account_number = anx_ua_accountNumber
 anx_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if anx_ua_account_number == anx_ua_input[0]:
  anx_unlock_account_0()
 if anx_ua_account_number == anx_ua_input[1]:
  anx_unlock_account_1()
 if anx_ua_account_number == anx_ua_input[2]:
  anx_unlock_account_2()
 if anx_ua_account_number == anx_ua_input[3]:
  anx_unlock_account_3()
 if anx_ua_account_number == anx_ua_input[4]:
  anx_unlock_account_4()
 if anx_ua_account_number == anx_ua_input[5]:
  anx_unlock_account_5()
 if anx_ua_account_number == anx_ua_input[6]:
  anx_unlock_account_6()
 if anx_ua_account_number not in anx_ua_input:
  print('Must Integer Within Range '+anx_accounts_range+'.')
 

def anx_approve_between_accounts(fromAccount, toAccount, msgValue):
  anx_update_accounts()
  anx_a_0 = anx.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(anx_a_0)

def anx_approve(fromAccountNumber, toAddress, msgValue):
  anx_update_accounts()
  anx_unlock_account(fromAccountNumber)
  anx_a_1 = anx.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(anx_a_1)

def anx_transfer_between_accounts(fromAccount, toAccount, msgValue):
  anx_update_accounts()
  anx_unlock_account(fromAccount)
  anx_t_0 = anx.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(anx_t_0)

def anx_transfer(fromAccountNumber, toAddress, msgValue):
  anx_update_accounts()
  anx_unlock_account(fromAccountNumber)
  anx_t_1 = anx.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(anx_t_1)

def anx_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  anx_update_accounts()
  anx_unlock_account(callAccount)
  anx_tf_0 = anx.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(anx_tf_0)

def anx_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  anx_update_accounts()
  anx_unlock_account(callAccount)
  anx_tf_1 = anx.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(anx_tf_1)
  


def anx_help():
  print('Following Functions For '+anx_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * anx_unlock => web3.personal.unlockAccount
/ * anx_accounts => web3.personal.listAccounts
/ * anx_balance = web3.eth.getBalance
** anx => web3.eth.contract(abi=anx_abi, address=anx_address)
** / * anx_balanceOf => anx.call().balanceOf

~ Function Listing Below:
~ anx_update_accounts()
~ anx_update_balances() \n\r -- => anx_update_accounts()
~ anx_list_all_accounts() \n\r -- => anx_update_accounts()
~ anx_account_balance(accountNumber) \n\r -- => anx_update_balances() 
~ anx_list_all_account_balances() \n\r -- => anx_update_balances()
~ anx_unlock_all_accounts() \n\r -- => anx_unlock_account_0() \n\r -- => anx_unlock_account_1() \n\r -- => anx_unlock_account_2() \n\r -- => anx_unlock_account_3() \n\r -- => anx_unlock_account_4() \n\r -- => anx_unlock_account_5() \n\r -- => anx_unlock_account_6() 
~ anx_unlock_account_0() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account0, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_1() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account1, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_2() \n\r -- => anx_update_accounts() \n\r --/ *anx_w_unlock(anx_account2, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_3() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account3, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_4() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account4, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_5() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account5, anx_account0pw, anx_unlockTime)
~ anx_unlock_account_6() \n\r -- => anx_update_accounts() \n\r -- / *anx_w_unlock(anx_account6, anx_account0pw, anx_unlockTime)
~ anx_unlock_account(anx_ua_accountNumber) \n\r -- => anx_update_accounts() \n\r -- // anx_unlock_account_0() \n\r -- // anx_unlock_account_1() \n\r -- // anx_unlock_account_2() \n\r -- // anx_unlock_account_3() \n\r -- // anx_unlock_account_4() \n\r -- // anx_unlock_account_5() \n\r -- // anx_unlock_account_6()
~ anx_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(fromAccount) \n\r -- / ** anx.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ anx_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(fromAccountNumber) \n\r -- / ** anx.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ anx_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(fromAccount) \n\r -- / ** anx.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ anx_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(fromAccountNumber) \n\r -- / ** anx.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ anx_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(callAccount) \n\r / ** anx.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ anx_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => anx_update_accounts() \n\r -- => anx_unlock_account(callAccount) \n\r -- / ** anx.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ anx_help() <-- You Are Here. ''')