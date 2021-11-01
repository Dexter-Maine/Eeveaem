#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global nmr_account_0_a
global nmr_account_1_a
global nmr_account_2_a
global nmr_account_3_a
global nmr_account_4_a
global nmr_account_5_a
global nmr_account_6_a
global nmr_address
global nmr_abi
global nmr
global nmr_call_0
global nmr_call_1
global nmr_call_2
global nmr_call_3
global nmr_call_4
global nmr_call_5
global nmr_call_6
global nmr_call_ab
global nmr_accounts
global nmr_account_0_pw
global nmr_account_1_pw
global nmr_account_2_pw
global nmr_account_3_pw
global nmr_account_4_pw
global nmr_account_5_pw
global nmr_account_6_pw
global nmr_account_0_n
global nmr_account_1_n
global nmr_account_2_n
global nmr_account_3_n
global nmr_account_4_n
global nmr_account_5_n
global nmr_account_6_n
global nmr_account1pw
global nmr_account2pw
global nmr_account3pw
global nmr_account4pw
global nmr_account5pw
global nmr_account6pw
global nmr_last_price
global nmr_accounts_range
global nmr_tokenName
global nmr_last_ethereum_price
global nmr_unlockTime
global nmr_balance
global nmr_balanceOf
global nmr_unlock
global nmr_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
nmr_token_d = 1e18
_e_d = 1e18
nmr_accounts_range = '[0, 6]'
nmr_unlock = web3.personal.unlockAccount
nmr_last_ethereum_price = 370.00
nmr_last_price = 35.10
nmr_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
nmr_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
nmr_tokenName = 'Numeraire Token'
nmr_unlockTime = hex(10000) # Must be hex()
nmr_account_0_a = nmr_accounts[0]
nmr_account_1_a = nmr_accounts[1]
nmr_account_2_a = nmr_accounts[2]
nmr_account_3_a = nmr_accounts[3]
nmr_account_4_a = nmr_accounts[4]
nmr_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
nmr_account_6_a = nmr_accounts[6]
# Supply Unlock Passwords For Transactions Below
nmr_account_0_pw = 'GuildSkrypt2017!@#'
nmr_account_1_pw = ''
nmr_account_2_pw = 'GuildSkrypt2017!@#'
nmr_account_3_pw = ''
nmr_account_4_pw = ''
nmr_account_5_pw = ''
nmr_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
nmr_account_0_n = 'Skotys Bittrex Account'
nmr_account_1_n = 'Jeffs Account'
nmr_account_2_n = 'Skrypts Bittrex Account'
nmr_account_3_n = 'Skotys Personal Account'
nmr_account_4_n = 'Unknown'
nmr_account_5_n = 'Watched \'Bittrex\' Account.'
nmr_account_6_n = 'Watched Account (1)'
# Contract Information Below :
nmr_address = '0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671'
nmr_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_tournamentID","type":"uint256"}],"name":"getTournament","outputs":[{"name":"","type":"uint256"},{"name":"","type":"uint256[]"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"numerai","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"isOwner","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"}],"name":"getRound","outputs":[{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"delegateContract","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"},{"name":"_endTime","type":"uint256"},{"name":"_resolutionTime","type":"uint256"}],"name":"createRound","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_staker","type":"address"},{"name":"_tag","type":"bytes32"},{"name":"_etherValue","type":"uint256"},{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"},{"name":"_successful","type":"bool"}],"name":"releaseStake","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"emergencyStop","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_staker","type":"address"},{"name":"_value","type":"uint256"},{"name":"_tag","type":"bytes32"},{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"},{"name":"_confidence","type":"uint256"}],"name":"stakeOnBehalf","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"tournaments","outputs":[{"name":"creationTime","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"stopped","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_owners","type":"address[]"},{"name":"_required","type":"uint256"}],"name":"changeShareable","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"contractUpgradable","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"numeraiTransfer","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"release","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"},{"name":"_staker","type":"address"},{"name":"_tag","type":"bytes32"}],"name":"getStake","outputs":[{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"bool"},{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"initial_disbursement","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"},{"name":"_tag","type":"bytes32"},{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"},{"name":"_confidence","type":"uint256"}],"name":"stake","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_oldValue","type":"uint256"},{"name":"_newValue","type":"uint256"}],"name":"changeApproval","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"weekly_disbursement","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"mint","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_staker","type":"address"},{"name":"_tag","type":"bytes32"},{"name":"_tournamentID","type":"uint256"},{"name":"_roundID","type":"uint256"}],"name":"destroyStake","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"deploy_time","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"disableContractUpgradability","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_operation","type":"bytes32"}],"name":"revoke","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"stoppable","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"total_minted","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_operation","type":"bytes32"},{"name":"_owner","type":"address"}],"name":"hasConfirmed","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"ownerIndex","type":"uint256"}],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"disableStopping","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"withdraw","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"required","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_tournamentID","type":"uint256"}],"name":"createTournament","outputs":[{"name":"ok","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"}],"name":"claimTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newDelegate","type":"address"}],"name":"changeDelegate","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"supply_cap","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getMintable","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"previousDelegates","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"inputs":[{"name":"_owners","type":"address[]"},{"name":"_num_required","type":"uint256"},{"name":"_initial_disbursement","type":"uint256"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"oldAddress","type":"address"},{"indexed":false,"name":"newAddress","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"staker","type":"address"},{"indexed":false,"name":"tag","type":"bytes32"},{"indexed":false,"name":"totalAmountStaked","type":"uint256"},{"indexed":false,"name":"confidence","type":"uint256"},{"indexed":true,"name":"tournamentID","type":"uint256"},{"indexed":true,"name":"roundID","type":"uint256"}],"name":"Staked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tournamentID","type":"uint256"},{"indexed":true,"name":"roundID","type":"uint256"},{"indexed":false,"name":"endTime","type":"uint256"},{"indexed":false,"name":"resolutionTime","type":"uint256"}],"name":"RoundCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tournamentID","type":"uint256"}],"name":"TournamentCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tournamentID","type":"uint256"},{"indexed":true,"name":"roundID","type":"uint256"},{"indexed":true,"name":"stakerAddress","type":"address"},{"indexed":false,"name":"tag","type":"bytes32"}],"name":"StakeDestroyed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tournamentID","type":"uint256"},{"indexed":true,"name":"roundID","type":"uint256"},{"indexed":true,"name":"stakerAddress","type":"address"},{"indexed":false,"name":"tag","type":"bytes32"},{"indexed":false,"name":"etherReward","type":"uint256"}],"name":"StakeReleased","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"owner","type":"address"},{"indexed":false,"name":"operation","type":"bytes32"}],"name":"Confirmation","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"owner","type":"address"},{"indexed":false,"name":"operation","type":"bytes32"}],"name":"Revoke","type":"event"}]
nmr = web3.eth.contract(abi=nmr_abi, address=nmr_address)
nmr_balanceOf = nmr.call().balanceOf
# End Contract Information
def nmr_update_accounts():
 global nmr_account0
 global nmr_account1
 global nmr_account2
 global nmr_account3
 global nmr_account4
 global nmr_account5
 global nmr_account6
 global nmr_account0_n
 global nmr_account1_n
 global nmr_account2_n
 global nmr_account3_n
 global nmr_account4_n
 global nmr_account5_n
 global nmr_account6_n
 global nmr_account0pw
 global nmr_account1pw
 global nmr_account2pw
 global nmr_account3pw
 global nmr_account4pw
 global nmr_account5pw
 global nmr_account6pw
 nmr_account0 = nmr_account_0_a
 nmr_account1 = nmr_account_1_a
 nmr_account2 = nmr_account_2_a
 nmr_account3 = nmr_account_3_a
 nmr_account4 = nmr_account_4_a
 nmr_account5 = nmr_account_5_a
 nmr_account6 = nmr_account_6_a
 nmr_account0_n = nmr_account_0_n
 nmr_account1_n = nmr_account_1_n
 nmr_account2_n = nmr_account_2_n
 nmr_account3_n = nmr_account_3_n
 nmr_account4_n = nmr_account_4_n
 nmr_account5_n = nmr_account_5_n
 nmr_account6_n = nmr_account_6_n
 nmr_account0pw = nmr_account_0_pw
 nmr_account1pw = nmr_account_1_pw
 nmr_account2pw = nmr_account_2_pw
 nmr_account3pw = nmr_account_3_pw
 nmr_account4pw = nmr_account_4_pw
 nmr_account5pw = nmr_account_5_pw
 nmr_account6pw = nmr_account_6_pw
 print(nmr_tokenName+' Accounts Updated.')
def nmr_update_balances():
 global nmr_call_0
 global nmr_call_1
 global nmr_call_2
 global nmr_call_3
 global nmr_call_4
 global nmr_call_5
 global nmr_call_6
 global nmr_w_call_0
 global nmr_w_call_1
 global nmr_w_call_2
 global nmr_w_call_3
 global nmr_w_call_4
 global nmr_w_call_5
 global nmr_w_call_6
 nmr_update_accounts()
 print('Updating '+nmr_tokenName+' Balances Please Wait...')
 nmr_call_0 = nmr_balanceOf(nmr_account0)
 nmr_call_1 = nmr_balanceOf(nmr_account1)
 nmr_call_2 = nmr_balanceOf(nmr_account2)
 nmr_call_3 = nmr_balanceOf(nmr_account3)
 nmr_call_4 = nmr_balanceOf(nmr_account4)
 nmr_call_5 = nmr_balanceOf(nmr_account5)
 nmr_call_6 = nmr_balanceOf(nmr_account6)
 nmr_w_call_0 = nmr_balance(nmr_account0)
 nmr_w_call_1 = nmr_balance(nmr_account1)
 nmr_w_call_2 = nmr_balance(nmr_account2)
 nmr_w_call_3 = nmr_balance(nmr_account3)
 nmr_w_call_4 = nmr_balance(nmr_account4)
 nmr_w_call_5 = nmr_balance(nmr_account5)
 nmr_w_call_6 = nmr_balance(nmr_account6)
 print(nmr_tokenName+' Balances Updated.')
def nmr_list_all_accounts():
 nmr_update_accounts()
 print(nmr_tokenName+' '+nmr_account0_n+': '+nmr_account0)
 print(nmr_tokenName+' '+nmr_account1_n+': '+nmr_account1)
 print(nmr_tokenName+' '+nmr_account2_n+': '+nmr_account2)
 print(nmr_tokenName+' '+nmr_account3_n+': '+nmr_account3)
 print(nmr_tokenName+' '+nmr_account4_n+': '+nmr_account4)
 print(nmr_tokenName+' '+nmr_account5_n+': '+nmr_account5)
 print(nmr_tokenName+' '+nmr_account6_n+': '+nmr_account6)

def nmr_account_balance(accountNumber):
 nmr_update_balances()
 nmr_ab_account_number = accountNumber
 nmr_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if nmr_ab_account_number == nmr_ab_input[0]:
  print('Calling '+nmr_account0_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account0_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_0 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_0 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[1]:
  print('Calling '+nmr_account1_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account1_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_1 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_1 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[2]:
  print('Calling '+nmr_account2_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account2_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_2 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_2 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[3]:
  print('Calling '+nmr_account3_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account3_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_3 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_3 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[4]:
  print('Calling '+nmr_account4_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account4_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_4 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_4 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[5]:
  print('Calling '+nmr_account5_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account5_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_5 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_5 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number == nmr_ab_input[6]:
  print('Calling '+nmr_account6_n+' '+nmr_tokenName+' Balance: ')
  print(nmr_account6_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_6 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_6 / nmr_token_d * nmr_last_price))
 if nmr_ab_account_number not in nmr_ab_input:
  print('Must Integer Within Range '+nmr_accounts_range+'.')

def nmr_list_all_account_balances():
 nmr_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+nmr_tokenName+' Balance: ')
 print(nmr_account0_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_0 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_0 / nmr_token_d * nmr_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(nmr_account0_n+': Ethereum Balance '+str(nmr_w_call_0 / _e_d)+' $'+str(nmr_w_call_0 / _e_d * nmr_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+nmr_tokenName+' Balance: ')
 print(nmr_account1_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_1 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_1 / nmr_token_d * nmr_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(nmr_account1_n+': Ethereum Balance '+str(nmr_w_call_1 / _e_d)+' $'+str(nmr_w_call_1 / _e_d * nmr_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+nmr_tokenName+' Balance: ')
 print(nmr_account2_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_2 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_2 / nmr_token_d * nmr_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(nmr_account2_n+': Ethereum Balance '+str(nmr_w_call_2 / _e_d)+' $'+str(nmr_w_call_2 / _e_d * nmr_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+nmr_tokenName+' Balance: ')
 print(nmr_account3_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_3 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_3 / nmr_token_d * nmr_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(nmr_account3_n+': Ethereum Balance '+str(nmr_w_call_3 / _e_d)+' $'+str(nmr_w_call_3 / _e_d * nmr_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+nmr_tokenName+' Balance: ')
 print(nmr_account4_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_4 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_4 / nmr_token_d * nmr_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(nmr_account4_n+': Ethereum Balance '+str(nmr_w_call_4 / _e_d)+' $'+str(nmr_w_call_4 / _e_d * nmr_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+nmr_tokenName+' Balance: ')
 print(nmr_account5_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_5 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_5 / nmr_token_d * nmr_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(nmr_account5_n+': Ethereum Balance '+str(nmr_w_call_5 / _e_d)+' $'+str(nmr_w_call_5 /_e_d * nmr_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+nmr_tokenName+' Balance: ')
 print(nmr_account6_n+': '+nmr_tokenName+' Balance: '+str(nmr_call_6 / nmr_token_d)+' Usd/'+nmr_tokenName+' Balance: $'+str(nmr_call_6 / nmr_token_d * nmr_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(nmr_account6_n+': Ethereum Balance '+str(nmr_w_call_6 / _e_d)+' $'+str(nmr_w_call_6 / _e_d * nmr_last_ethereum_price))
def nmr_unlock_all_accounts():
  nmr_unlock_account_0()
  nmr_unlock_account_1()
  nmr_unlock_account_2()
  nmr_unlock_account_3()
  nmr_unlock_account_4()
  nmr_unlock_account_5()
  nmr_unlock_account_6()


def nmr_unlock_account_0():
  global nmr_account0pw
  global nmr_account0
  global nmr_account0_n
  nmr_update_accounts()
  nmr_u_a_0 = nmr_w_unlock(nmr_account0, nmr_account0pw, nmr_unlockTime)
  if nmr_u_a_0 == False:
    if nmr_account0pw == '':
     nmr_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account0_n+' Passphrase Denied: '+nmr_account0pw_r)
    elif nmr_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+nmr_account0_n+' Passphrase Denied: '+nmr_account0pw)
  if nmr_u_a_0 == True:
   print(nmr_account0_n+' Unlocked')

def nmr_unlock_account_1():
  global nmr_account1pw
  global nmr_account1
  global nmr_account1_n
  nmr_update_accounts()
  nmr_u_a_1 = nmr_unlock(nmr_account1, nmr_account1pw, nmr_unlockTime)
  if nmr_u_a_1 == False:
    if nmr_account1pw == '':
     nmr_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account1_n+' Passphrase Denied: '+nmr_account1pw_r)
    elif nmr_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+nmr_account1_n+' Passphrase Denied: '+nmr_account1pw)
  if nmr_u_a_1 == True:
   print(nmr_account1_n+' Unlocked')

def nmr_unlock_account_2():
  global nmr_account2pw
  global nmr_account2
  global nmr_account2_n
  nmr_update_accounts()
  nmr_u_a_2 = nmr_unlock(nmr_account2, nmr_account2pw, nmr_unlockTime)
  if nmr_u_a_2 == False:
    if nmr_account2pw == '':
     nmr_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account2_n+' Passphrase Denied: '+nmr_account2pw_r)
    elif nmr_account2pw != '':
     print('Unlock Failure With Account '+nmr_account2_n+' Passphrase Denied: '+nmr_account2pw)
  if nmr_u_a_2 == True:
   print(nmr_account2_n+' Unlocked')

def nmr_unlock_account_3():
  global nmr_account3pw
  global nmr_account3
  global nmr_account3_n
  nmr_update_accounts()
  nmr_u_a_3 = nmr_unlock(nmr_account3, nmr_account3pw, nmr_unlockTime)
  if nmr_u_a_3 == False:
    if nmr_account3pw == '':
     nmr_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account3_n+' Passphrase Denied: '+nmr_account3pw_r)
    elif nmr_account3pw != '':
     print('Unlock Failure With Account '+nmr_account3_n+' Passphrase Denied: '+nmr_account3pw)
  if nmr_u_a_3 == True:
   print(nmr_account3_n+' Unlocked')

def nmr_unlock_account_4():
  global nmr_account4pw
  global nmr_account4
  global nmr_account4_n
  nmr_update_accounts()
  nmr_u_a_4 = nmr_unlock(nmr_account4, nmr_account4pw, nmr_unlockTime)
  if nmr_u_a_4 == False:
    if nmr_account4pw == '':
     nmr_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account4_n+' Passphrase Denied: '+nmr_account4pw_r)
    elif nmr_account4pw != '':
     print('Unlock Failure With Account '+nmr_account4_n+' Passphrase Denied: '+nmr_account4pw)
  if nmr_u_a_4 == True:
   print(nmr_account4_n+' Unlocked')

def nmr_unlock_account_5():
  global nmr_account5pw
  global nmr_account5
  global nmr_account5_n
  nmr_update_accounts()
  nmr_u_a_5 = nmr_unlock(nmr_account5, nmr_account5pw, nmr_unlockTime)
  if nmr_u_a_5 == False:
    if nmr_account5pw == '':
     nmr_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account5_n+' Passphrase Denied: '+nmr_account5pw_r)
    elif nmr_account5pw != '':
     print('Unlock Failure With Account '+nmr_account5_n+' Passphrase Denied: '+nmr_account5pw)
  if nmr_u_a_5 == True:
   print(nmr_account5_n+' Unlocked')

def nmr_unlock_account_6():
  global nmr_account6pw
  global nmr_account6
  global nmr_account6_n
  nmr_update_accounts()
  nmr_u_a_6 = nmr_unlock(nmr_account6, nmr_account6pw, nmr_unlockTime)
  if nmr_u_a_6 == False:
    if nmr_account6pw == '':
     nmr_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+nmr_account6_n+' Passphrase Denied: '+nmr_account6pw_r)
    elif nmr_account6pw != '':
     print('Unlock Failure With Account '+nmr_account6_n+' Passphrase Denied: '+nmr_account6pw)
  if nmr_u_a_6 == True:
   print(nmr_account6_n+' Unlocked')

def nmr_unlock_account(nmr_ua_accountNumber):
 nmr_update_accounts()
 nmr_ua_account_number = nmr_ua_accountNumber
 nmr_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if nmr_ua_account_number == nmr_ua_input[0]:
  nmr_unlock_account_0()
 if nmr_ua_account_number == nmr_ua_input[1]:
  nmr_unlock_account_1()
 if nmr_ua_account_number == nmr_ua_input[2]:
  nmr_unlock_account_2()
 if nmr_ua_account_number == nmr_ua_input[3]:
  nmr_unlock_account_3()
 if nmr_ua_account_number == nmr_ua_input[4]:
  nmr_unlock_account_4()
 if nmr_ua_account_number == nmr_ua_input[5]:
  nmr_unlock_account_5()
 if nmr_ua_account_number == nmr_ua_input[6]:
  nmr_unlock_account_6()
 if nmr_ua_account_number not in nmr_ua_input:
  print('Must Integer Within Range '+nmr_accounts_range+'.')
 

def nmr_approve_between_accounts(fromAccount, toAccount, msgValue):
  nmr_update_accounts()
  nmr_a_0 = nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(nmr_a_0)

def nmr_approve(fromAccountNumber, toAddress, msgValue):
  nmr_update_accounts()
  nmr_unlock_account(fromAccountNumber)
  nmr_a_1 = nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(nmr_a_1)

def nmr_transfer_between_accounts(fromAccount, toAccount, msgValue):
  nmr_update_accounts()
  nmr_unlock_account(fromAccount)
  nmr_t_0 = nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(nmr_t_0)

def nmr_transfer(fromAccountNumber, toAddress, msgValue):
  nmr_update_accounts()
  nmr_unlock_account(fromAccountNumber)
  nmr_t_1 = nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(nmr_t_1)

def nmr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  nmr_update_accounts()
  nmr_unlock_account(callAccount)
  nmr_tf_0 = nmr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(nmr_tf_0)

def nmr_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  nmr_update_accounts()
  nmr_unlock_account(callAccount)
  nmr_tf_1 = nmr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(nmr_tf_1)
  


def nmr_help():
  print('Following Functions For '+nmr_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * nmr_unlock => web3.personal.unlockAccount
/ * nmr_accounts => web3.personal.listAccounts
/ * nmr_balance = web3.eth.getBalance
** nmr => web3.eth.contract(abi=nmr_abi, address=nmr_address)
** / * nmr_balanceOf => nmr.call().balanceOf

~ Function Listing Below:
~ nmr_update_accounts()
~ nmr_update_balances() \n\r -- => nmr_update_accounts()
~ nmr_list_all_accounts() \n\r -- => nmr_update_accounts()
~ nmr_account_balance(accountNumber) \n\r -- => nmr_update_balances() 
~ nmr_list_all_account_balances() \n\r -- => nmr_update_balances()
~ nmr_unlock_all_accounts() \n\r -- => nmr_unlock_account_0() \n\r -- => nmr_unlock_account_1() \n\r -- => nmr_unlock_account_2() \n\r -- => nmr_unlock_account_3() \n\r -- => nmr_unlock_account_4() \n\r -- => nmr_unlock_account_5() \n\r -- => nmr_unlock_account_6() 
~ nmr_unlock_account_0() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account0, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_1() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account1, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_2() \n\r -- => nmr_update_accounts() \n\r --/ *nmr_w_unlock(nmr_account2, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_3() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account3, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_4() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account4, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_5() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account5, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account_6() \n\r -- => nmr_update_accounts() \n\r -- / *nmr_w_unlock(nmr_account6, nmr_account0pw, nmr_unlockTime)
~ nmr_unlock_account(nmr_ua_accountNumber) \n\r -- => nmr_update_accounts() \n\r -- // nmr_unlock_account_0() \n\r -- // nmr_unlock_account_1() \n\r -- // nmr_unlock_account_2() \n\r -- // nmr_unlock_account_3() \n\r -- // nmr_unlock_account_4() \n\r -- // nmr_unlock_account_5() \n\r -- // nmr_unlock_account_6()
~ nmr_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(fromAccount) \n\r -- / ** nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ nmr_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(fromAccountNumber) \n\r -- / ** nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ nmr_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(fromAccount) \n\r -- / ** nmr.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ nmr_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(fromAccountNumber) \n\r -- / ** nmr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ nmr_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(callAccount) \n\r / ** nmr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ nmr_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => nmr_update_accounts() \n\r -- => nmr_unlock_account(callAccount) \n\r -- / ** nmr.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ nmr_help() <-- You Are Here. ''')