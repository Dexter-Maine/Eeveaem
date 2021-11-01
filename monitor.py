#!/usr/bin/python3
# Vivian Ethereum Address Monitor System Example.
import time
import os
from vweb3 import *

balance = web3.eth.getBalance
transactions = web3.eth.getTransactionCount
counter = 0
Menu = True
Monitor = False
address = ''

def _balance(address):
 bal = balance(address)
 return bal

def _transactionCount(address):
 tranCount = transactions(address)
 return tranCount

def _setAddress():
 global address
 global Menu
 global Monitor
 print('Please Input The Address You Are Watching.')
 address = input('>>: ')
 if len(address) != 42:
  print('You Need To Use A Proper Ethereum Address Please.')
  _setAddress()
 for i in address:
  if i not in Allowed_Address_Characters:
   print('[{}] Is Not Allowed Within A Ethereum Address.'.format(i))
 print('Watching [{}] For Transactions And Balance Difference.'.format(address))
 try:
  AddressMap = pickle.load(open('AddressMap.vnm','rb'))
  if address not in AddressMap:
   AddressMap[address] = dict()
   AddressMap[address]['Checks'] = 0
   AddressMap[address]['Previous Balance'] = _balance(address)
   AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
   pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
   Menu = False
   Monitor = True
  else:
   AddressMap[address]['Checks'] += 1
   if _balance(address) != AddressMap[address]['Previous Balance']:
    AddressMap[address]['Previous Balance'] = _balance(address)
   if _transactionCount(address) != AddressMap[address]['Previous Transaction Count']:
    AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
   pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
   Menu = False
 except Exception as File_Needed:
  AddressMap[address] = dict()
  AddressMap[address]['Checks'] = 0
  AddressMap[address]['Previous Balance'] = _balance(address)
  AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
  pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
  Menu = False
  Monitor = True
 
while Menu:
  print('Welcome To The Eeveaem Address Auto Monitoring System.')
  _setAddress()

while Monitor:
 time.sleep(INTERVAL)
 print('Watching [{}] For Transactions And Balance Difference.'.format(address))
 try:
  AddressMap = pickle.load(open('AddressMap.vnm','rb'))
  if address not in AddressMap:
   AddressMap[address] = dict()
   AddressMap[address]['Checks'] = 0
   AddressMap[address]['Previous Balance'] = _balance(address)
   AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
   pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
   Menu = False
   Monitor = True
  else:
   AddressMap[address]['Checks'] += 1
   if _balance(address) != AddressMap[address]['Previous Balance']:
    AddressMap[address]['Previous Balance'] = _balance(address)
   if _transactionCount(address) != AddressMap[address]['Previous Transaction Count']:
    AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
   pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
   Menu = False
 except Exception as File_Needed:
  AddressMap[address] = dict()
  AddressMap[address]['Checks'] = 0
  AddressMap[address]['Previous Balance'] = _balance(address)
  AddressMap[address]['Previous Transaction Count'] = _transactionCount(address)
  pickle.dump(AddressMap,open('AddressMap.vnm','wb'))
  Menu = False
  Monitor = True


