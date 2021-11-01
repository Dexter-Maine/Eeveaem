#!/usr/bin/python3
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
adx_token_d = 1e4
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
adx_tokenName = 'AdEx'
adx_unlockTime = hex(10000) # Must be hex()
# Contract Information Below :
adx_address = '0x4470BB87d77b963A013DB939BE332f927f2b992e'
adx_abi = [{"constant":true,"inputs":[],"name":"PREBUY_PORTION_MAX","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"}],"name":"tokenGrantsCount","outputs":[{"name":"index","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"PRICE_STAGE_TWO","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuy3","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuy1","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"publicEndTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"grants","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"},{"name":"start","type":"uint64"},{"name":"revokable","type":"bool"},{"name":"burnsOnRevoke","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ADXSold","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuy2","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"multisigAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ALLOC_BOUNTIES","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"publicStartTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"tokenGrant","outputs":[{"name":"granter","type":"address"},{"name":"value","type":"uint256"},{"name":"vested","type":"uint256"},{"name":"start","type":"uint64"},{"name":"cliff","type":"uint64"},{"name":"vesting","type":"uint64"},{"name":"revokable","type":"bool"},{"name":"burnsOnRevoke","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"STAGE_TWO_TIME_END","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"}],"name":"lastTokenIsTransferableDate","outputs":[{"name":"date","type":"uint64"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ALLOC_WINGS","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"STAGE_ONE_TIME_END","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_wei","type":"uint256"},{"name":"_rate","type":"uint256"}],"name":"calcAmount","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ALLOC_CROWDSALE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"adexTeamAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"getPriceRate","outputs":[{"name":"o_rate","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"privateStartTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_halted","type":"bool"}],"name":"toggleHalt","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ownerAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"PRICE_STAGE_ONE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_start","type":"uint64"},{"name":"_cliff","type":"uint64"},{"name":"_vesting","type":"uint64"},{"name":"_revokable","type":"bool"},{"name":"_burnsOnRevoke","type":"bool"}],"name":"grantVestedTokens","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"drain","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"prebuyPortionTotal","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"hardcapInEth","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"ALLOC_TEAM","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"halted","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"etherRaised","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"holder","type":"address"},{"name":"time","type":"uint64"}],"name":"transferableTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuyPrice1","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuyPrice2","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"tokens","type":"uint256"},{"name":"time","type":"uint256"},{"name":"start","type":"uint256"},{"name":"cliff","type":"uint256"},{"name":"vesting","type":"uint256"}],"name":"calculateVestedTokens","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"PRICE_STAGE_THREE","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_adexTeamAddress","type":"address"},{"name":"_adexFundAddress","type":"address"}],"name":"grantVested","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_holder","type":"address"},{"name":"_grantId","type":"uint256"}],"name":"revokeTokenGrant","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"preBuyPrice3","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"PRICE_STANDARD","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"STAGE_THREE_TIME_END","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"preBuy","outputs":[],"payable":true,"type":"function"},{"inputs":[{"name":"_multisig","type":"address"},{"name":"_adexTeam","type":"address"},{"name":"_publicStartTime","type":"uint256"},{"name":"_privateStartTime","type":"uint256"},{"name":"_hardcapInEth","type":"uint256"},{"name":"_prebuy1","type":"address"},{"name":"_preBuyPrice1","type":"uint256"},{"name":"_prebuy2","type":"address"},{"name":"_preBuyPrice2","type":"uint256"},{"name":"_prebuy3","type":"address"},{"name":"_preBuyPrice3","type":"uint256"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"PreBuy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_recipient","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Buy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"grantId","type":"uint256"}],"name":"NewTokenGrant","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]
adx = web3.eth.contract(abi=adx_abi, address=adx_address)
adx_balanceOf = adx.call().balanceOf
# End Contract Information
class AdEx():
 def __init__(self):
  pass

 def adx_information(self, option):
  if option == 0:
   try:
    return adx_address
   except Exception as E:
    return 'Error returning (Adx) Address.'
  elif option == 1:
   try:
    self_balance = adx_balanceOf(adx_address)//adx_token_d
    adx_info_string = 'AdEx Self Balance: [{}].'.format(self_balance)
    return adx_info_string
   except Exception as E:
    return 'Error returning (Adx) Self Balance.'
  elif option == 2:
   try:
    return adx_abi
   except Exception as E:
    return 'Error returning (Adx) ABI information.'
  else:
   return 'Options: [0,1,2] This Is An Internal Object Error.'

 def adx_balance(self,address):
  try:
   balance_check = adx_balanceOf(address)
   return balance_check // adx_token_d
  except Exception as E:
   return 'Error With [(Adx) Balance Function Call] Please Investigate'

 def adx_approve(self,fromAddress, toAddress, msgValue):
  try:
   adx_a_1 = adx.transact({'from': fromAddress}).approve(toAddress, msgValue)
   return adx_a_1
  except Exception as E:
   return 'Error With [(Adx) Approve Function Call] Please Investigate'

 def adx_transfer(self,fromAddress, toAddress, msgValue):
  try:
   adx_t_1 = adx.transact({'from': fromAddress}).transfer(toAddress, msgValue)
   return adx_t_1
  except Exception as E:
   return 'Error With [(Adx) Transfer Function Call] Please Investigate'


 def adx_transferFrom(self,callAddress, fromAddress, toAccount, msgValue):
  try:
   adx_tf_1 = adx.transact({'from': callAddress}).transferFrom(fromAddress, toAddress, msgValue)
   return adx_tf_1
  except Exception as E:
   return 'Error With [(Adx) Transfer From Function Call] Please Investigate'
  
