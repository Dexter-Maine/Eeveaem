#!/usr/bin/python3
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
# Global Declarations 
# Internal Variable Setup (Leave Alone Unless You Understand What They Do.)
true = True
false = False
adt_token_d = 1e8
# User Choice Variables (You May Change These Pretty Easily Without Fucking Anything Up.)
adt_tokenName = 'adToken'
adt_unlockTime = hex(10000) # Must be hex()
# Contract Information Below :
adt_address = '0xd0d6d6c5fe4a677d343cc433536bb717bae167dd'
adt_abi = [{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"},{"constant":false,"type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
adt = web3.eth.contract(abi=adt_abi, address=adt_address)
adt_balanceOf = adt.call().balanceOf
# End Contract Information
class AdToken():
 def __init__(self):
  pass

 def adt_information(self, option):
  if option == 0:
   try:
    return adt_address
   except Exception as E:
    return 'Error returning (Adt) Address.'
  elif option == 1:
   try:
    self_balance = adt_balanceOf(adt_address)//adt_token_d
    adt_info_string = 'AdToken Self Balance: [{}].'.format(self_balance)
    return adt_info_string
   except Exception as E:
    return 'Error returning (Adt) Self Balance.'
  elif option == 2:
   try:
    return adt_abi
   except Exception as E:
    return 'Error returning (Adt) ABI information.'
  else:
   return 'Options: [0,1,2] This Is An Internal Object Error.'

 def adt_balance(self, address):
  try:
   balance_check = adt_balanceOf(address)
   return balance_check // adt_token_d
  except Exception as E:
   return 'Error With [(Adt) Balance Function Call] Please Investigate.'

 def adt_approve(self, fromAddress, toAddress, msgValue):
  try:
   adt_a_1 = adt.transact({'from': fromAddress}).approve(toAddress, msgValue)
   return adt_a_1
  except Exception as E:
   return 'Error With [(Adt) Approve Function Call] Please Investigate.'


 def adt_transfer(fromAddress, toAddress, msgValue):
  try:
   adt_t_1 = adt.transact({'from': fromAddress}).transfer(toAddress, msgValue)
   return adt_t_1
  except Exception as E:
   return 'Error With [(Adt) Transfer Function Call] Please Investigate.'


 def adt_transferFrom(callAddress, fromAddress, toAddress, msgValue):
  try:
   adt_tf_1 = adt.transact({'from': callAddress}).transferFrom(fromAddress, toAddress, msgValue)
   return adt_tf_1
  except Exception as E:
   return 'Error With [(Adt) Transfer From Function Call] Please Investigate.'
  

