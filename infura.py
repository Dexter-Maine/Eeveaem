#!/usr/bin/python

# pip install web3
#1st from web3 import Web3, KeepAliveRPCProvider, IPCProvider # For Parity Ethereum Node
import time
from web3 import Web3
from web3.providers.rpc import HTTPProvider # For Infura Ethereum Node
# Note that you should create only one RPCProvider per
# process, as it recycles underlying TCP/IP network connections between
# your process and Ethereum node
# Hosting Parity (Homestead) via windows 10 - Python 3.6
web3 = Web3(HTTPProvider('https://kovan.infura.io/0NYe3mNSlgDgjd3gMzHI'))
#1st web3 = Web3(KeepAliveRPCProvider(host='10.0.0.11', port='8545')) # The RPC Connection
quarterBack = "0xB2Cf4aDb16C976D55FEF1f0aDc5C53e4Cd868eb2" #quarterBack Address
rk3d = '0x001F50d401BdB0188E02d53AD77a415f0cA30693' #rk3d Address
receiver = '0xb24cB989523524b12D7D590A323C798955C55Ef8' #receiver Address
dump_account = '0x00697D86c8C5449AC3e8F22bA13F6e3086660a33' #Dump Address
pass_phrase = 'GuildSkrypt' # Universal Passphrase
one_eth = 1000000000000000000 # 1.0 Eth in Wei
#list_accounts = web3.personal.listAccounts # Displays personal accounts
global max_receiver_count # Global Declaration For Function
global to_receiver_tx_count # Global Declaration For Function
global to_dump_tx_count # Global Declaration For Function
max_receiver_count = 5 # Max Transactions Out To Receiver
to_receiver_tx_count = 0 # Check For Max ^^
to_dump_tx_count = 0 # Check For Dump Sends (No Data Display Of Yet)
global rk3d_balance # Global Declaration For Function
global receiver_balance # Global Declaration For Function
global dump_balance # Global Declaration For Function
rk3d_balance = web3.eth.getBalance(rk3d) # Variable For Web3 Balance (Rk3d) Via Parity
receiver_balance = web3.eth.getBalance(receiver) # Variable For Web3 Balance (receiver) Via Parity
dump_balance = web3.eth.getBalance(dump_account) # Variable For Web3 Balance (dump_account)(One-Eyed-Al) Via Parity

### Display Printout ###

print('Functions Are As Follows:')
print('list_accounts [Lists All Accounts Within Connected RPC]')
print('quarterBack [Lists quarterBack Address]')
print('rk3d [Lists RK3D Address], receiver [Lists receiver Address]')
print('pass_phrase [Lists Universal Pass-Phrase], one_eth [1.0 Eth Equiv In Wei]')
print('trasact(toAddress, fromAddress, ethValue, passwordPhrase) [Sends Transaction Using From Address Phrase]')
print('getBalance(address) [Displays Address Balance]')
global test # Test Squishy, Don't Fuck With Me
test = False # ^^ Likewise
#print('Test = '+str(test))  << Squishy
### Simple Function Setup ###
class Sf: # < (SkryptFunction Class)
 def transact(toAddress, fromAddress, ethValue, passwordPhrase): # Transact Function
  t = web3.personal.signAndSendTransaction({'to': toAddress, 'from': fromAddress, 'value': hex(ethValue)}, passwordPhrase)
  print(t) # Print Transaction Tx.ID
 def getBalance(address): # Get Balance Function
  b = web3.eth.getBalance(address) # Variable For Web3 Balance (address param)
  print(b) # Print Balance
 def checkTest(): # Squishy
  global test # Squishy
  if test == False: # Squishy
   print('False')  # Squishy
  elif test == True: # Squishy
   print('True') # Squishy
 def updateBalances(): # Update Balances Function For While True Statement.
  global rk3d_balance # Global Declaration For Function
  global receiver_balance # Global Declaration For Function
  global dump_balance # Global Declaration For Function
  rk3d_balance = web3.eth.getBalance(rk3d) # Variable For Web3 Balance (rk3d)
  receiver_balance = web3.eth.getBalance(receiver) # Variable For Web3 Balance (receiver)
  dump_balance = web3.eth.getBalance(dump_account) # Variable For Web3 Balance (dump_account)

while True: # While True Statement.
 print('Updating balance information') # Shows Us We Are Updating.
 time.sleep(0.2) # Pauses CPU For 2 Milliseconds
 Sf.updateBalances() # Calls Update Function
 if to_receiver_tx_count <= max_receiver_count: # Checks To Make Sure We Haven't Reached Our Max
  to_receiver_tx_count += 1 # Adds One To Counter To Check Against
  if rk3d_balance > 0: # Checks To Make Sure Balance Is Over 0
   print('Attemping to send 0.01 Eth To Receiver Account') # Tells Us What We Are Doing (Sending Eth)
   Sf.transact(receiver, rk3d, 100000000000000000, pass_phrase) # Calls Skrypt Function To Transact (rk3d>receiver).
 if receiver_balance > 0: # Check To See If Receiver Balance Is Over 0
  to_dump_tx_count += 1 # Add one to dump sends (not accounted for at the moment)
  print('balance received') # Flag Balance Has Been Received
  print('Attemping to dump receiver account.') # Flag Dumping
  Sf.transact(dump_account, receiver, receiver_balance, pass_phrase) # Skrypt Function To Transact (receiver>dump_account)
  print(dump_balance) # Tell Us Dump Balance.
 
