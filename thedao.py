#!/usr/bin/python3
import time
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
global true
global false
global thedao_account_0_a
global thedao_account_1_a
global thedao_account_2_a
global thedao_account_3_a
global thedao_account_4_a
global thedao_account_5_a
global thedao_account_6_a
global thedao_address
global thedao_abi
global thedao
global thedao_call_0
global thedao_call_1
global thedao_call_2
global thedao_call_3
global thedao_call_4
global thedao_call_5
global thedao_call_6
global thedao_call_ab
global thedao_accounts
global thedao_account_0_pw
global thedao_account_1_pw
global thedao_account_2_pw
global thedao_account_3_pw
global thedao_account_4_pw
global thedao_account_5_pw
global thedao_account_6_pw
global thedao_account_0_n
global thedao_account_1_n
global thedao_account_2_n
global thedao_account_3_n
global thedao_account_4_n
global thedao_account_5_n
global thedao_account_6_n
global thedao_account1pw
global thedao_account2pw
global thedao_account3pw
global thedao_account4pw
global thedao_account5pw
global thedao_account6pw
global thedao_last_price
global thedao_accounts_range
global thedao_tokenName
global thedao_last_ethereum_price
global thedao_unlockTime
global thedao_balance
global thedao_balanceOf
global thedao_unlock
global thedao_token_d
global _e_d
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
thedao_token_d = 1e8
_e_d = 1e18
thedao_accounts_range = '[0, 6]'
thedao_unlock = web3.personal.unlockAccount
thedao_last_ethereum_price = 370.00
thedao_last_price = 3.83
thedao_accounts = web3.personal.listAccounts # For personal accounts, Accounts Can Also Be String ('0x..') Listed.
thedao_balance = web3.eth.getBalance
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
thedao_tokenName = 'TheDao Token'
thedao_unlockTime = hex(10000) # Must be hex()
thedao_account_0_a = thedao_accounts[0]
thedao_account_1_a = thedao_accounts[1]
thedao_account_2_a = thedao_accounts[2]
thedao_account_3_a = thedao_accounts[3]
thedao_account_4_a = thedao_accounts[4]
thedao_account_5_a = '0xFBb1b73C4f0BDa4f67dcA266ce6Ef42f520fBB98'
thedao_account_6_a = thedao_accounts[6]
# Supply Unlock Passwords For Transactions Below
thedao_account_0_pw = 'GuildSkrypt2017!@#'
thedao_account_1_pw = ''
thedao_account_2_pw = 'GuildSkrypt2017!@#'
thedao_account_3_pw = ''
thedao_account_4_pw = ''
thedao_account_5_pw = ''
thedao_account_6_pw = ''
# Supply Names Below Standard Is 'Unknown'
thedao_account_0_n = 'Skotys Bittrex Account'
thedao_account_1_n = 'Jeffs Account'
thedao_account_2_n = 'Skrypts Bittrex Account'
thedao_account_3_n = 'Skotys Personal Account'
thedao_account_4_n = 'Unknown'
thedao_account_5_n = 'Watched \'Bittrex\' Account.'
thedao_account_6_n = 'Watched Account (1)'
# Contract Information Below :
thedao_address = '0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413'
thedao_abi = [{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"proposals","outputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"},{"name":"description","type":"string"},{"name":"votingDeadline","type":"uint256"},{"name":"open","type":"bool"},{"name":"proposalPassed","type":"bool"},{"name":"proposalHash","type":"bytes32"},{"name":"proposalDeposit","type":"uint256"},{"name":"newCurator","type":"bool"},{"name":"yea","type":"uint256"},{"name":"nay","type":"uint256"},{"name":"creator","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"minTokensToCreate","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"rewardAccount","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"daoCreator","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"divisor","outputs":[{"name":"divisor","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"extraBalance","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_proposalID","type":"uint256"},{"name":"_transactionData","type":"bytes"}],"name":"executeProposal","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"unblockMe","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalRewardToken","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"actualBalance","outputs":[{"name":"_actualBalance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"closingTime","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"allowedRecipients","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferWithoutReward","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"refund","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_description","type":"string"},{"name":"_transactionData","type":"bytes"},{"name":"_debatingPeriod","type":"uint256"},{"name":"_newCurator","type":"bool"}],"name":"newProposal","outputs":[{"name":"_proposalID","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"DAOpaidOut","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"minQuorumDivisor","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_newContract","type":"address"}],"name":"newContract","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_allowed","type":"bool"}],"name":"changeAllowedRecipients","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"halveMinQuorum","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"paidOut","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_proposalID","type":"uint256"},{"name":"_newCurator","type":"address"}],"name":"splitDAO","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"DAOrewardAccount","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"proposalDeposit","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"numberOfProposals","outputs":[{"name":"_numberOfProposals","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"lastTimeMinQuorumMet","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_toMembers","type":"bool"}],"name":"retrieveDAOReward","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[],"name":"receiveEther","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"isFueled","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_tokenHolder","type":"address"}],"name":"createTokenProxy","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_proposalID","type":"uint256"}],"name":"getNewDAOAddress","outputs":[{"name":"_newDAO","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_proposalID","type":"uint256"},{"name":"_supportsProposal","type":"bool"}],"name":"vote","outputs":[{"name":"_voteID","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[],"name":"getMyReward","outputs":[{"name":"_success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"rewardToken","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFromWithoutReward","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_proposalDeposit","type":"uint256"}],"name":"changeProposalDeposit","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"blocked","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"curator","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[{"name":"_proposalID","type":"uint256"},{"name":"_recipient","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_transactionData","type":"bytes"}],"name":"checkProposalCode","outputs":[{"name":"_codeChecksOut","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"privateCreation","outputs":[{"name":"","type":"address"}],"type":"function"},{"inputs":[{"name":"_curator","type":"address"},{"name":"_daoCreator","type":"address"},{"name":"_proposalDeposit","type":"uint256"},{"name":"_minTokensToCreate","type":"uint256"},{"name":"_closingTime","type":"uint256"},{"name":"_privateCreation","type":"address"}],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"FuelingToDate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"CreatedToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Refund","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"recipient","type":"address"},{"indexed":false,"name":"amount","type":"uint256"},{"indexed":false,"name":"newCurator","type":"bool"},{"indexed":false,"name":"description","type":"string"}],"name":"ProposalAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"position","type":"bool"},{"indexed":true,"name":"voter","type":"address"}],"name":"Voted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"result","type":"bool"},{"indexed":false,"name":"quorum","type":"uint256"}],"name":"ProposalTallied","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_newCurator","type":"address"}],"name":"NewCurator","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_recipient","type":"address"},{"indexed":false,"name":"_allowed","type":"bool"}],"name":"AllowedRecipientChanged","type":"event"}]
thedao = web3.eth.contract(abi=thedao_abi, address=thedao_address)
thedao_balanceOf = thedao.call().balanceOf
# End Contract Information
def thedao_update_accounts():
 global thedao_account0
 global thedao_account1
 global thedao_account2
 global thedao_account3
 global thedao_account4
 global thedao_account5
 global thedao_account6
 global thedao_account0_n
 global thedao_account1_n
 global thedao_account2_n
 global thedao_account3_n
 global thedao_account4_n
 global thedao_account5_n
 global thedao_account6_n
 global thedao_account0pw
 global thedao_account1pw
 global thedao_account2pw
 global thedao_account3pw
 global thedao_account4pw
 global thedao_account5pw
 global thedao_account6pw
 thedao_account0 = thedao_account_0_a
 thedao_account1 = thedao_account_1_a
 thedao_account2 = thedao_account_2_a
 thedao_account3 = thedao_account_3_a
 thedao_account4 = thedao_account_4_a
 thedao_account5 = thedao_account_5_a
 thedao_account6 = thedao_account_6_a
 thedao_account0_n = thedao_account_0_n
 thedao_account1_n = thedao_account_1_n
 thedao_account2_n = thedao_account_2_n
 thedao_account3_n = thedao_account_3_n
 thedao_account4_n = thedao_account_4_n
 thedao_account5_n = thedao_account_5_n
 thedao_account6_n = thedao_account_6_n
 thedao_account0pw = thedao_account_0_pw
 thedao_account1pw = thedao_account_1_pw
 thedao_account2pw = thedao_account_2_pw
 thedao_account3pw = thedao_account_3_pw
 thedao_account4pw = thedao_account_4_pw
 thedao_account5pw = thedao_account_5_pw
 thedao_account6pw = thedao_account_6_pw
 print(thedao_tokenName+' Accounts Updated.')
def thedao_update_balances():
 global thedao_call_0
 global thedao_call_1
 global thedao_call_2
 global thedao_call_3
 global thedao_call_4
 global thedao_call_5
 global thedao_call_6
 global thedao_w_call_0
 global thedao_w_call_1
 global thedao_w_call_2
 global thedao_w_call_3
 global thedao_w_call_4
 global thedao_w_call_5
 global thedao_w_call_6
 thedao_update_accounts()
 print('Updating '+thedao_tokenName+' Balances Please Wait...')
 thedao_call_0 = thedao_balanceOf(thedao_account0)
 thedao_call_1 = thedao_balanceOf(thedao_account1)
 thedao_call_2 = thedao_balanceOf(thedao_account2)
 thedao_call_3 = thedao_balanceOf(thedao_account3)
 thedao_call_4 = thedao_balanceOf(thedao_account4)
 thedao_call_5 = thedao_balanceOf(thedao_account5)
 thedao_call_6 = thedao_balanceOf(thedao_account6)
 thedao_w_call_0 = thedao_balance(thedao_account0)
 thedao_w_call_1 = thedao_balance(thedao_account1)
 thedao_w_call_2 = thedao_balance(thedao_account2)
 thedao_w_call_3 = thedao_balance(thedao_account3)
 thedao_w_call_4 = thedao_balance(thedao_account4)
 thedao_w_call_5 = thedao_balance(thedao_account5)
 thedao_w_call_6 = thedao_balance(thedao_account6)
 print(thedao_tokenName+' Balances Updated.')
def thedao_list_all_accounts():
 thedao_update_accounts()
 print(thedao_tokenName+' '+thedao_account0_n+': '+thedao_account0)
 print(thedao_tokenName+' '+thedao_account1_n+': '+thedao_account1)
 print(thedao_tokenName+' '+thedao_account2_n+': '+thedao_account2)
 print(thedao_tokenName+' '+thedao_account3_n+': '+thedao_account3)
 print(thedao_tokenName+' '+thedao_account4_n+': '+thedao_account4)
 print(thedao_tokenName+' '+thedao_account5_n+': '+thedao_account5)
 print(thedao_tokenName+' '+thedao_account6_n+': '+thedao_account6)

def thedao_account_balance(accountNumber):
 thedao_update_balances()
 thedao_ab_account_number = accountNumber
 thedao_ab_input = [0, 1, 2, 3, 4, 5, 6]
 if thedao_ab_account_number == thedao_ab_input[0]:
  print('Calling '+thedao_account0_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account0_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_0 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_0 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[1]:
  print('Calling '+thedao_account1_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account1_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_1 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_1 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[2]:
  print('Calling '+thedao_account2_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account2_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_2 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_2 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[3]:
  print('Calling '+thedao_account3_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account3_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_3 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_3 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[4]:
  print('Calling '+thedao_account4_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account4_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_4 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_4 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[5]:
  print('Calling '+thedao_account5_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account5_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_5 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_5 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number == thedao_ab_input[6]:
  print('Calling '+thedao_account6_n+' '+thedao_tokenName+' Balance: ')
  print(thedao_account6_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_6 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_6 / thedao_token_d * thedao_last_price))
 if thedao_ab_account_number not in thedao_ab_input:
  print('Must Integer Within Range '+thedao_accounts_range+'.')

def thedao_list_all_account_balances():
 thedao_update_balances()
 print('Loading Account Data...')
 #Account 0 Data
 print('Calling Account_0 '+thedao_tokenName+' Balance: ')
 print(thedao_account0_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_0 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_0 / thedao_token_d * thedao_last_price))
 print('Calling Account_0 Ethereum Balance: ')
 print(thedao_account0_n+': Ethereum Balance '+str(thedao_w_call_0 / _e_d)+' $'+str(thedao_w_call_0 / _e_d * thedao_last_ethereum_price))
 #Account 1 Data
 print('Calling Account_1 '+thedao_tokenName+' Balance: ')
 print(thedao_account1_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_1 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_1 / thedao_token_d * thedao_last_price))
 print('Calling Account_1 Ethereum Balance: ')
 print(thedao_account1_n+': Ethereum Balance '+str(thedao_w_call_1 / _e_d)+' $'+str(thedao_w_call_1 / _e_d * thedao_last_ethereum_price))
 #Account 2 Data
 print('Calling Account_2 '+thedao_tokenName+' Balance: ')
 print(thedao_account2_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_2 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_2 / thedao_token_d * thedao_last_price))
 print('Calling Account_2 Ethereum Balance: ')
 print(thedao_account2_n+': Ethereum Balance '+str(thedao_w_call_2 / _e_d)+' $'+str(thedao_w_call_2 / _e_d * thedao_last_ethereum_price))
 #Account 3 Data
 print('Calling Account_3 '+thedao_tokenName+' Balance: ')
 print(thedao_account3_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_3 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_3 / thedao_token_d * thedao_last_price))
 print('Calling Account_3 Ethereum Balance: ')
 print(thedao_account3_n+': Ethereum Balance '+str(thedao_w_call_3 / _e_d)+' $'+str(thedao_w_call_3 / _e_d * thedao_last_ethereum_price))
 #Account 4 Data
 print('Calling Account_4 '+thedao_tokenName+' Balance: ')
 print(thedao_account4_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_4 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_4 / thedao_token_d * thedao_last_price))
 print('Calling Account_4 Ethereum Balance: ')
 print(thedao_account4_n+': Ethereum Balance '+str(thedao_w_call_4 / _e_d)+' $'+str(thedao_w_call_4 / _e_d * thedao_last_ethereum_price))
 #Account 5 Data
 print('Calling Account_5 '+thedao_tokenName+' Balance: ')
 print(thedao_account5_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_5 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_5 / thedao_token_d * thedao_last_price))
 print('Calling Account_5 Ethereum Balance: ')
 print(thedao_account5_n+': Ethereum Balance '+str(thedao_w_call_5 / _e_d)+' $'+str(thedao_w_call_5 /_e_d * thedao_last_ethereum_price))
 #Account 0 Data
 print('Calling Account_6 '+thedao_tokenName+' Balance: ')
 print(thedao_account6_n+': '+thedao_tokenName+' Balance: '+str(thedao_call_6 / thedao_token_d)+' Usd/'+thedao_tokenName+' Balance: $'+str(thedao_call_6 / thedao_token_d * thedao_last_price))
 print('Calling Account_6 Ethereum Balance: ')
 print(thedao_account6_n+': Ethereum Balance '+str(thedao_w_call_6 / _e_d)+' $'+str(thedao_w_call_6 / _e_d * thedao_last_ethereum_price))
def thedao_unlock_all_accounts():
  thedao_unlock_account_0()
  thedao_unlock_account_1()
  thedao_unlock_account_2()
  thedao_unlock_account_3()
  thedao_unlock_account_4()
  thedao_unlock_account_5()
  thedao_unlock_account_6()


def thedao_unlock_account_0():
  global thedao_account0pw
  global thedao_account0
  global thedao_account0_n
  thedao_update_accounts()
  thedao_u_a_0 = thedao_w_unlock(thedao_account0, thedao_account0pw, thedao_unlockTime)
  if thedao_u_a_0 == False:
    if thedao_account0pw == '':
     thedao_account0pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account0_n+' Passphrase Denied: '+thedao_account0pw_r)
    elif thedao_account0pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+thedao_account0_n+' Passphrase Denied: '+thedao_account0pw)
  if thedao_u_a_0 == True:
   print(thedao_account0_n+' Unlocked')

def thedao_unlock_account_1():
  global thedao_account1pw
  global thedao_account1
  global thedao_account1_n
  thedao_update_accounts()
  thedao_u_a_1 = thedao_unlock(thedao_account1, thedao_account1pw, thedao_unlockTime)
  if thedao_u_a_1 == False:
    if thedao_account1pw == '':
     thedao_account1pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account1_n+' Passphrase Denied: '+thedao_account1pw_r)
    elif thedao_account1pw == 'UnAssigned (Blank String (\'\')':
     print('Unlock Failure With Account '+thedao_account1_n+' Passphrase Denied: '+thedao_account1pw)
  if thedao_u_a_1 == True:
   print(thedao_account1_n+' Unlocked')

def thedao_unlock_account_2():
  global thedao_account2pw
  global thedao_account2
  global thedao_account2_n
  thedao_update_accounts()
  thedao_u_a_2 = thedao_unlock(thedao_account2, thedao_account2pw, thedao_unlockTime)
  if thedao_u_a_2 == False:
    if thedao_account2pw == '':
     thedao_account2pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account2_n+' Passphrase Denied: '+thedao_account2pw_r)
    elif thedao_account2pw != '':
     print('Unlock Failure With Account '+thedao_account2_n+' Passphrase Denied: '+thedao_account2pw)
  if thedao_u_a_2 == True:
   print(thedao_account2_n+' Unlocked')

def thedao_unlock_account_3():
  global thedao_account3pw
  global thedao_account3
  global thedao_account3_n
  thedao_update_accounts()
  thedao_u_a_3 = thedao_unlock(thedao_account3, thedao_account3pw, thedao_unlockTime)
  if thedao_u_a_3 == False:
    if thedao_account3pw == '':
     thedao_account3pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account3_n+' Passphrase Denied: '+thedao_account3pw_r)
    elif thedao_account3pw != '':
     print('Unlock Failure With Account '+thedao_account3_n+' Passphrase Denied: '+thedao_account3pw)
  if thedao_u_a_3 == True:
   print(thedao_account3_n+' Unlocked')

def thedao_unlock_account_4():
  global thedao_account4pw
  global thedao_account4
  global thedao_account4_n
  thedao_update_accounts()
  thedao_u_a_4 = thedao_unlock(thedao_account4, thedao_account4pw, thedao_unlockTime)
  if thedao_u_a_4 == False:
    if thedao_account4pw == '':
     thedao_account4pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account4_n+' Passphrase Denied: '+thedao_account4pw_r)
    elif thedao_account4pw != '':
     print('Unlock Failure With Account '+thedao_account4_n+' Passphrase Denied: '+thedao_account4pw)
  if thedao_u_a_4 == True:
   print(thedao_account4_n+' Unlocked')

def thedao_unlock_account_5():
  global thedao_account5pw
  global thedao_account5
  global thedao_account5_n
  thedao_update_accounts()
  thedao_u_a_5 = thedao_unlock(thedao_account5, thedao_account5pw, thedao_unlockTime)
  if thedao_u_a_5 == False:
    if thedao_account5pw == '':
     thedao_account5pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account5_n+' Passphrase Denied: '+thedao_account5pw_r)
    elif thedao_account5pw != '':
     print('Unlock Failure With Account '+thedao_account5_n+' Passphrase Denied: '+thedao_account5pw)
  if thedao_u_a_5 == True:
   print(thedao_account5_n+' Unlocked')

def thedao_unlock_account_6():
  global thedao_account6pw
  global thedao_account6
  global thedao_account6_n
  thedao_update_accounts()
  thedao_u_a_6 = thedao_unlock(thedao_account6, thedao_account6pw, thedao_unlockTime)
  if thedao_u_a_6 == False:
    if thedao_account6pw == '':
     thedao_account6pw_r = 'UnAssigned (Blank String (\'\')'
     print('Unlock Failure With Account '+thedao_account6_n+' Passphrase Denied: '+thedao_account6pw_r)
    elif thedao_account6pw != '':
     print('Unlock Failure With Account '+thedao_account6_n+' Passphrase Denied: '+thedao_account6pw)
  if thedao_u_a_6 == True:
   print(thedao_account6_n+' Unlocked')

def thedao_unlock_account(thedao_ua_accountNumber):
 thedao_update_accounts()
 thedao_ua_account_number = thedao_ua_accountNumber
 thedao_ua_input = [0, 1, 2, 3, 4, 5, 6]
 if thedao_ua_account_number == thedao_ua_input[0]:
  thedao_unlock_account_0()
 if thedao_ua_account_number == thedao_ua_input[1]:
  thedao_unlock_account_1()
 if thedao_ua_account_number == thedao_ua_input[2]:
  thedao_unlock_account_2()
 if thedao_ua_account_number == thedao_ua_input[3]:
  thedao_unlock_account_3()
 if thedao_ua_account_number == thedao_ua_input[4]:
  thedao_unlock_account_4()
 if thedao_ua_account_number == thedao_ua_input[5]:
  thedao_unlock_account_5()
 if thedao_ua_account_number == thedao_ua_input[6]:
  thedao_unlock_account_6()
 if thedao_ua_account_number not in thedao_ua_input:
  print('Must Integer Within Range '+thedao_accounts_range+'.')
 

def thedao_approve_between_accounts(fromAccount, toAccount, msgValue):
  thedao_update_accounts()
  thedao_a_0 = thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(web3.personal.listAccounts[toAccount], msgValue)
  print(thedao_a_0)

def thedao_approve(fromAccountNumber, toAddress, msgValue):
  thedao_update_accounts()
  thedao_unlock_account(fromAccountNumber)
  thedao_a_1 = thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
  print(thedao_a_1)

def thedao_transfer_between_accounts(fromAccount, toAccount, msgValue):
  thedao_update_accounts()
  thedao_unlock_account(fromAccount)
  thedao_t_0 = thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
  print(thedao_t_0)

def thedao_transfer(fromAccountNumber, toAddress, msgValue):
  thedao_update_accounts()
  thedao_unlock_account(fromAccountNumber)
  thedao_t_1 = thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(toAddress, msgValue)
  print(thedao_t_1)

def thedao_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue):
  thedao_update_accounts()
  thedao_unlock_account(callAccount)
  thedao_tf_0 = thedao.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], web3.personal.listAccounts[toAccount], msgValue)
  print(thedao_tf_0)

def thedao_transferFrom(callAccount, fromAccount, toAccount, msgValue):
  thedao_update_accounts()
  thedao_unlock_account(callAccount)
  thedao_tf_1 = thedao.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
  print(thedao_tf_1)
  


def thedao_help():
  print('Following Functions For '+thedao_tokenName+' Are As Follows:')
  print(''' 
@ Tag Listing Below:
~ (Function Name)
-- (Next line same subject)
/ * (variable assigned main function)
** (variable assigned contract call/transaction)
// (if condition is met)
=> (function calls in order)
/ * thedao_unlock => web3.personal.unlockAccount
/ * thedao_accounts => web3.personal.listAccounts
/ * thedao_balance = web3.eth.getBalance
** thedao => web3.eth.contract(abi=thedao_abi, address=thedao_address)
** / * thedao_balanceOf => thedao.call().balanceOf

~ Function Listing Below:
~ thedao_update_accounts()
~ thedao_update_balances() \n\r -- => thedao_update_accounts()
~ thedao_list_all_accounts() \n\r -- => thedao_update_accounts()
~ thedao_account_balance(accountNumber) \n\r -- => thedao_update_balances() 
~ thedao_list_all_account_balances() \n\r -- => thedao_update_balances()
~ thedao_unlock_all_accounts() \n\r -- => thedao_unlock_account_0() \n\r -- => thedao_unlock_account_1() \n\r -- => thedao_unlock_account_2() \n\r -- => thedao_unlock_account_3() \n\r -- => thedao_unlock_account_4() \n\r -- => thedao_unlock_account_5() \n\r -- => thedao_unlock_account_6() 
~ thedao_unlock_account_0() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account0, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_1() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account1, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_2() \n\r -- => thedao_update_accounts() \n\r --/ *thedao_w_unlock(thedao_account2, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_3() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account3, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_4() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account4, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_5() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account5, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account_6() \n\r -- => thedao_update_accounts() \n\r -- / *thedao_w_unlock(thedao_account6, thedao_account0pw, thedao_unlockTime)
~ thedao_unlock_account(thedao_ua_accountNumber) \n\r -- => thedao_update_accounts() \n\r -- // thedao_unlock_account_0() \n\r -- // thedao_unlock_account_1() \n\r -- // thedao_unlock_account_2() \n\r -- // thedao_unlock_account_3() \n\r -- // thedao_unlock_account_4() \n\r -- // thedao_unlock_account_5() \n\r -- // thedao_unlock_account_6()
~ thedao_approve_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(fromAccount) \n\r -- / ** thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ thedao_approve(fromAccountNumber, toAddress, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(fromAccountNumber) \n\r -- / ** thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).approve(toAddress, msgValue)
~ thedao_transfer_between_accounts(fromAccount, toAccount, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(fromAccount) \n\r -- / ** thedao.transact({'from': web3.personal.listAccounts[fromAccount]}).transfer(web3.personal.listAccounts[toAccount], msgValue)
~ thedao_transfer(fromAccountNumber, toAddress, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(fromAccountNumber) \n\r -- / ** thedao.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ thedao_transferFrom_between_accounts(callAccount, fromAccount, toAccount, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(callAccount) \n\r / ** thedao.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], \n\r -- web3.personal.listAccounts[toAccount], msgValue)
~ thedao_transferFrom(callAccount, fromAccount, toAccount, msgValue) \n\r -- => thedao_update_accounts() \n\r -- => thedao_unlock_account(callAccount) \n\r -- / ** thedao.transact({'from': web3.personal.listAccounts[callAccount]}).transferFrom(web3.personal.listAccounts[fromAccount], toAddress, msgValue)
~ thedao_help() <-- You Are Here. ''')