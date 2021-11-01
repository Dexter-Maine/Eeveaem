from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from vweb3config import *
#web3_kovan = Web3(KeepAliveRPCProvider(host='10.0.0.11', port='8545'))
#web3_main = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
unlock_pass = 'GuildSkrypt2017!@#'
default_manual = '0x00C6a4B7133Ec7b7b68309F6057AeFEdf9Ec0836'
manual_default_pass = 'guildworx2017!'
c_list = [0, 1, 2, 3, 4, 5, 6]
k_list = ['k', 'ko', 'kov', 'kova', 'kovan', 'K', 'KO', 'KOV', 'KOVA', 'KOVAN', '--k', '-k', '--K', '-K']
m_list = ['m', 'ma', 'mai', 'main', 'M', 'MA', 'MAI', 'MAIN', '--m', '-m', '--M', '-M']
print('Venom Web3 Initiated Without Chain Selection Please Use set_chain(_choice)!')
# Main Net Setup Functions below
def set_chain(_choice):
   if _choice in c_list:
    if block_chains['current_chains_active']['active_chain_0'] == None:
     block_chains['current_chains_active']['active_chain_0'] = block_chains['block_chain_'+str(_choice)]['name']
     global web3_0
     web3_0 = block_chains['block_chain_'+str(_choice)]['web3']
     print(web3_0)
     global web3_0_send_out
     web3_0_send_out = web3_0.eth.sendTransaction
     print(web3_0_send_out)
     print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    elif block_chains['current_chains_active']['active_chain_0'] != None:
     if block_chains['current_chains_active']['active_chain_1'] == None:
      block_chains['current_chains_active']['active_chain_1'] = block_chains['block_chain_'+str(_choice)]['name']
      global web3_1
      web3_1 = block_chains['block_chain_'+str(_choice)]['web3']
      print(web3_1)
      global web3_1_send_out
      web3_1_send_out = web3_1.eth.sendTransaction
      print(web3_1_send_out)
      print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    elif block_chains['current_chains_active']['active_chain_0'] != None:
     if block_chains['current_chains_active']['active_chain_1'] != None:
      if block_chains['current_chains_active']['active_chain_2'] == None:
       block_chains['current_chains_active']['active_chain_2'] = block_chains['block_chain_'+str(_choice)]['name']
       global web3_2
       web3_2 = block_chains['block_chain_'+str(_choice)]['web3']
       print(web3_2)
       global web3_2_send_out
       web3_2_send_out = web3_2.eth.sendTransaction
       print(web3_2_send_out)
       print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    elif block_chains['current_chains_active']['active_chain_0'] != None:
     if block_chains['current_chains_active']['active_chain_1'] != None:
      if block_chains['current_chains_active']['active_chain_2'] != None:
       if block_chains['current_chains_active']['active_chain_3'] == None:
        block_chains['current_chains_active']['active_chain_3'] = block_chains['block_chain_'+str(_choice)]['name']
        global web3_3
        web3_3 = block_chains['block_chain_'+str(_choice)]['web3']
        print(web3_3)
        global web3_3_send_out
        web3_3_send_out = web3_3.eth.sendTransaction
        print(web3_3_send_out)
        print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    elif block_chains['current_chains_active']['active_chain_0'] != None:
     if block_chains['current_chains_active']['active_chain_1'] != None:
      if block_chains['current_chains_active']['active_chain_2'] != None:
       if block_chains['current_chains_active']['active_chain_3'] != None:
        if block_chains['current_chains_active']['active_chain_4'] == None:
         block_chains['current_chains_active']['active_chain_4'] = block_chains['block_chain_'+str(_choice)]['name']
         global web3_4
         web3_4 = block_chains['block_chain_'+str(_choice)]['web3']
         print(web3_4)
         global web3_4_send_out
         web3_4_send_out = web3_4.eth.sendTransaction
         print(web3_4_send_out)
         print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    elif block_chains['current_chains_active']['active_chain_0'] != None:
     if block_chains['current_chains_active']['active_chain_1'] != None:
      if block_chains['current_chains_active']['active_chain_2'] != None:
       if block_chains['current_chains_active']['active_chain_3'] != None:
        if block_chains['current_chains_active']['active_chain_4'] != None:
         if block_chains['current_chains_active']['active_chain_5'] == None:
          block_chains['current_chains_active']['active_chain_5'] = block_chains['block_chain_'+str(_choice)]['name']
          global web3_5
          web3_5 = block_chains['block_chain_'+str(_choice)]['web3']
          print(web3_5)
          global web3_5_send_out
          web3_5_send_out = web3_5.eth.sendTransaction
          print(web3_5_send_out)
          print(web3config_echos['block_chain_'+str(_choice)+'_echo'])
    else:
      print('All Chains Slots Active Please Use Chain List And Unset A Chain.')
def chain_list():
    if block_chains['current_chains_active']['active_chain_0'] != None:
     print('Active Slot 0 : '+block_chains['current_chains_active']['active_chain_0'])
    elif block_chains['current_chains_active']['active_chain_1'] != None:
     print('Active Slot 1 : '+block_chains['current_chains_active']['active_chain_1'])
    elif block_chains['current_chains_active']['active_chain_2'] != None:
     print('Active Slot 2 : '+block_chains['current_chains_active']['active_chain_2'])
    elif block_chains['current_chains_active']['active_chain_3'] != None:
     print('Active Slot 3 : '+block_chains['current_chains_active']['active_chain_3'])
    elif block_chains['current_chains_active']['active_chain_4'] != None:
     print('Active Slot 4 : '+block_chains['current_chains_active']['active_chain_4'])
    elif block_chains['current_chains_active']['active_chain_5'] != None:
     print('Active Slot 5 : '+block_chains['current_chains_active']['active_chain_5'])
    else:
     print('All Chain Slots Are Empty.')
def check_accounts(_chain):
    set_chain(_chain)
    print(web3_0.eth.accounts)

def set_default_main():
   default_unlock = web3_main.personal.unlockAccount(web3_main.personal.listAccounts[3], unlock_pass, hex(10000000))
   default_set = web3_main.eth.defaultAccount = web3_main.personal.listAccounts[3]
   print(default_unlock, default_set, web3_main.eth.defaultAccount)
   balance = web3_main.eth.getBalance(web3_main.eth.defaultAccount)
   print('Current Balance Of Defalut Account: '+str(balance / 1e18))

def set_manual_default_main():
   default_unlock = web3_main.personal.unlockAccount(default_manual, manual_default_pass, hex(10000000))
   default_set = web3_main.eth.defaultAccount = default_manual
   print(default_unlock, default_set, web3_main.eth.defaultAccount)
   balance = web3_main.eth.getBalance(web3_main.eth.defaultAccount)
   print('Current Balance Of Defalut Account: '+str(balance / 1e18))

def send_from_default_main():
  set_default_main_main()
 #try:
  default_unlock = web3_main.personal.unlockAccount(web3_main.personal.listAccounts[3], unlock_pass, hex(10000000))
  transaction = main_send_out({'to': web3_main.personal.listAccounts[9], 'from': web3_main.eth.defaultAccount, 'value': hex(10000000000000000)})
  print(transaction)
 #except ValueError:
  print('Something Has Gone Wrong.')

# Kovan Net Setup Function Below

def set_default_kovan():
   default_unlock = web3_kovan.personal.unlockAccount(web3_kovan.personal.listAccounts[3], unlock_pass, hex(10000000))
   default_set = web3_kovan.eth.defaultAccount = web3_kovan.personal.listAccounts[3]
   print(default_unlock, default_set, web3_kovan.eth.defaultAccount)
   balance = web3_kovan.eth.getBalance(web3_kovan.eth.defaultAccount)
   print('Current Balance Of Defalut Account: '+str(balance / 1e18))

def set_manual_default_kovan():
   default_unlock = web3_kovan.personal.unlockAccount(default_manual, manual_default_pass, hex(10000000))
   default_set = web3_kovan.eth.defaultAccount = default_manual
   print(default_unlock, default_set, web3_kovan.eth.defaultAccount)
   balance = web3_kovan.eth.getBalance(web3_kovan.eth.defaultAccount)
   print('Current Balance Of Defalut Account: '+str(balance / 1e18))

def send_from_default_kovan():
  set_default_kovan()
 #try:
  default_unlock = web3_kovan.personal.unlockAccount(web3_kovan.personal.listAccounts[3], unlock_pass, hex(10000000))
  transaction = kovan_send_out({'to': web3_kovan.personal.listAccounts[9], 'from': web3_kovan.eth.defaultAccount, 'value': hex(10000000000000000)})
  print(transaction)
 #except ValueError:
  print('Something Has Gone Wrong.')