
try:
 print('Attempting To Import [binascii] Module.')
 import binascii
except Exception as bad_binascii_mod:
 print('Error Importing [binascii] Module. Instructing Program To Exit.')
 print('Error: [{}]'.format(bad_binascii_mod))
 exit()

try:
 print('Attempting To Import [sha3] Module.')
 import sha3
except Exception as bad_sha3_mod:
 print('Error Importing [sha3] Module. Instructing Program To Exit.')
 print('Error: [{}]'.format(bad_sha3_mod))
 exit()

try:
 print('Attempting To Import [sha3] Module.')
 import hashlib
except Exception as bad_hashlib_mod:
 print('Error Importing [hashlib] Module. Instructing Program To Exit.')
 print('Error: [{}]'.format(bad_hashlib_mod))
 exit()

try:
 print('From [ecdsa] Attempting To Import [SigningKey, SECP256k1] Methods.')
 from ecdsa import SigningKey, SECP256k1
except Exception as bad_ecdsa_mod:
 print('Error Importing [SigningKey, SECP256k1] Methods From [ecdsa] Module. Instructing Program To Exit.')
 print('Error: [{}]'.format(bad_ecdsa_mod))
 exit()
############# WALLETS BELOW ##################################
              
class Wallet:
 def __init__(self, Name, Owner, Address,PrivateKey, Balance, ServerBalance, TxHistory, TxCount):
   self.Name = Name
   self.Owner = Owner
   self.Address = Address
   self.PrivateKey = PrivateKey
   self.Balance = Balance
   self.ServerBalance = ServerBalance
   self.TxHistory = TxHistory
   self.TxCount = TxCount

 def add_eth_address(self, privateKey):
  private_key = binascii.unhexlify(privateKey)
  keccak = sha3.keccak_256()
  keccak.update(SigningKey.from_string(private_key, curve=SECP256k1).get_verifying_key().to_string())
  address = "0x{0}".format(keccak.hexdigest()[24:])
  self.Address = address
  self.PrivateKey = privateKey
  return address

 def add_owner(self):
  if self.Address != '':
   self.Owner = Name
   return True
  else:
   return False

 def update_serverBalance(self,op,value):
  if op == '-':
   self.ServerBalance -= value
   return True
  elif op == '+':
   self.ServerBalance += value
   return True
  else:
   return False
  
class EthereumWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Ethereum',Owner='',Address='',PrivateKey='',Balance=0,ServerBalance=0,TxHistory=dict(),TxCount=0)
class KoiniumWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Koinium',Owner='',Address='',PrivateKey='',Balance=0,ServerBalance=0,TxHistory=dict(),TxCount=0)
class KrypitsWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Krypits',Owner='',Address='',PrivateKey='',Balance=0,ServerBalance=0,TxHistory=dict(),TxCount=0)
class EthrealTokenWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Ethreal Token',Owner='',Address='',PrivateKey='',Balance=0,ServerBalance=0,TxHistory=dict(),TxCount=0)


############# USER CLASSES / TYPES BELOW ##########################
# Type [0]: 'Guest'
class User:
 def __init__(self, Name, Type, Level,Health,MaxHealth,Magik,MaxMagik,Notes,Wallets,Inventory,
              MaxInventory,Guild,Alive,Started,specialspeech,vocal,specialvocal,
              Room,RoomID,DeathAlert,C0reTime,UserID):
  self.Name = Name
  self.Type = Type
  self.Level = Level
  self.Health = Health
  self.MaxHealth = MaxHealth
  self.Magik = Magik
  self.MaxMagik = MaxMagik
  self.UserID = UserID
  self.Notes = Notes
  self.Wallets = Wallets
  self.Inventory = Inventory
  self.MaxInventory = MaxInventory
  self.Guild = Guild
  self.Alive = Alive
  self.Started = Started
  self.Special_Speech = specialspeech
  self.SpecialSpeech = specialvocal
  self.Speech = vocal
  self.Room = Room
  self.Room_id = RoomID
  self.DeathAlert = DeathAlert
  self.C0reTime = C0reTime

class C0reGuest(User):
 def __init__(self):
  super().__init__(Name=None,Type=dict(),Level=1,Health=100,MaxHealth=100,Magik=100,MaxMagik=100,UserID=None,Notes=dict(),Wallets=dict(),Inventory=[],MaxInventory=0,Guild=None,
                   Alive=True,Started=False,specialspeech = False, vocal='say',specialvocal='bark',
                   Room='[The Core, Registration Room]',
                   RoomID=1,DeathAlert=False,C0reTime=0.0)
  self.Type['Name'] = 'Guest'
  self.Type['id'] = 0
  self.Wallets['EthereumWallet'] = EthereumWallet()
  self.Wallets['KoiniumWallet'] = KoiniumWallet()
  self.Wallets['KrypitsWallet'] = KrypitsWallet()
  self.Wallets['EthrealWallet'] = EthrealTokenWallet()
