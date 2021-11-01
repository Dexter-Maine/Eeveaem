# @Dev: Add: Pushing NoneType For Users And Rooms:
# @Dev: (Test Add Balance) Error: Output NoneTypes
########################################################
#Setting [['global']] Users For New Syntax
#[balance] Is Already Linked To: [balance]
#[balanc] Is Already Linked To: [balance]
#[balan] Is Already Linked To: [balance]
#[bala] Is Already Linked To: [balance]
#Word: [balance2] | self.Syntax[word]['Users']: [None] | self.Syntax[word]['Rooms']: [None] |

from addC0reSyntax import *
Server = C0reSyntaxUpdater()
On = True
print('Welcome To The C0re Syntax Controller v0.1.0')
print('Any Errors Please Report To Skrypt # RealmKoin@Gmail.com')
global _rooms
global _users
_rooms = []
_users = []


def _collectUsers():
 try:
  global _users
  print('Please Insert The Users You Would Like To Add To The New Syntax Or Use Done. You May Use Help For More Information.')
  _R = input('>>: ')
  _R2 = _R.split(' ')
  if _R2[0].lower() == 'done':
   print('Setting [{}] Users For New Syntax'.format(_users))
   return _users
  elif _R2[0].lower() == 'exit':
   print('Setting [{}] Users For New Syntax'.format(_users))
   return _users
  elif _R2[0].lower() == 'help':
   print('You May Insert A User Id \'ID\', (User Groupings Are Integer Valued) Or Use View,Clear or Remove For List Options You May Use Exit At Any Time.')
   _collectUsers()
  elif _R2[0].lower() == 'view':
   print('Current Users To Be Added To New Syntax: {}'.format(_users))
   _collectUsers()
  elif _R2[0].lower() == 'clear':
   print('Clearing Users: [{}]'.format(_users))
   _users = []
   print('Users: [{}] Cleared'.format(_users))
   _collectUsers()
  elif _R2[0].lower() == 'add':
   ID = _R2[1]
   if ID.lower() == 'global':
    _users = []
    _users.append('global')
    print('Current Users: [{}] Set Global For New Syntax'.format(_users))
    _collectUsers()
   elif ID != 'global':
    if 'global' not in _users:
     _users.append(ID)
     print('[{}] Added To Users, Current User Groupings Allowed For New Syntax: [{}]'.format(ID,_users))
     _collectUsers()
    elif 'global' in _users:
     print('This Syntax User Groupings Is Already Set As Global. Please Use Done/Exit Or Remove Global')
     _collectUsers()
  elif _R2[0].lower() == 'remove':
   if _R2[1].lower() in _users:
    _users.remove(_R2[1].lower())
    print('Removed [{}] From User Grouping List: [{}]'.format(_R2[1].lower(),_users))
    _collectUsers()
   elif _R2[1].lower() not in _users:
    print('[{}] Not In User Groupings. Current User Groupings List: [{}]'.format(_R2[1].lower(),_users))
    _collectUsers()
  else:
   print('Please Use One Of The Provided Syntax For Users Addition. Thank You')
   _collectUsers()
 except Exception as E:
  print('Something Has Gone Seriously Wrong With _collectUsers() External Function. Please Investigate')
  print('Error: [{}]'.format(E))


  

def _collectRooms():
 try:
  global _rooms
  print('Please Insert The Rooms You Would Like To Add To The New Syntax Or Use Done. You May Use Help For More Information.')
  _R = input('>>: ')
  _R2 = _R.split(' ')
  if _R2[0].lower() == 'done':
   print('Setting [{}] Rooms For New Syntax'.format(_rooms))
   return _rooms
  elif _R2[0].lower() == 'exit':
   print('Setting [{}] Rooms For New Syntax'.format(_rooms))
   return _rooms
  elif _R2[0].lower() == 'help':
   print('You May Insert A Room Id \'0xID\', Or Use View,Clear or Remove For List Options You May Use Exit At Any Time.')
   _collectRooms()
  elif _R2[0].lower() == 'view':
   print('Current Rooms To Be Added To New Syntax: {}'.format(_rooms))
   _collectRooms()
  elif _R2[0].lower() == 'clear':
   print('Clearing Rooms: {}'.format(_rooms))
   _rooms = []
   print('Rooms: {} Cleared'.format(_rooms))
   _collectRooms()
  elif _R2[0].lower() == 'add':
   ID = _R2[1]
   if ID.lower() == 'global':
    _rooms = []
    _rooms.append('global')
    print('Current Rooms: {} Set Global For New Syntax'.format(_rooms))
    _collectRooms()
   elif ID[:2] == '0x':
    if 'global' not in _rooms:
     _rooms.append(ID)
     print('[{}] Added To Rooms, Current Rooms Allowed For New Syntax: {}'.format(ID,_rooms))
     _collectRooms()
    elif 'global' in _rooms:
     print('This Syntax Is Already Set As Global. Please Use Done/Exit Or Remove Global')
     _collectRooms()
  elif _R2[0].lower() == 'remove':
   if _R2[1].lower() in _rooms:
    _rooms.remove(_R2[1].lower())
    print('Removed {} From Rooms List: {}'.format(_R2[1].lower(),_rooms))
    _collectRooms()
   elif _R2[1].lower() not in _rooms:
    print('{} Not In Rooms. Current Rooms List: {}'.format(_R2[1].lower(),_rooms))
    _collectRooms()
  else:
   print('Please Use One Of The Provided Syntax For Room Addition. Thank You')
   _collectRooms()
 except Exception as E:
  print('Something Has Gone Seriously Wrong With _collectRooms() External Function. Please Investigate')
  print('Error: [{}]'.format(E))

# Options Selection
def _OptionsSelector():
 global _rooms
 global _users
 print('Please Choose What To Do Or Use [Help] For A List Of Options')
 REQ = input('>>: ')
 _Req = REQ.split(' ')

 # Help
 if _Req[0].lower() == 'help':
  print('''Options Include:
   Add [Syntax] | View | Edit Users
                 Edit Rooms''')
  pass

 # View
 elif _Req[0].lower() == 'view':
  print('Please Provide A Syntax To View.')
  Syn = input('>>: ')
  _Action = Server.view_syntax(Syn)
  if _Action == True:
   pass
  else:
   print('Failure _Action: [{}]'.format(_Action))
   exit()

 # Add [Syntax]
 elif _Req[0].lower() == 'add':
  room = _collectRooms()
  user = _collectUsers()
  if len(_Req) > 1:
   _Action = Server.publish_syntax(_Req[1].lower(),_users,_rooms)
   _users = [] # Hard Reset
   _rooms = [] # Hard Reset
   if _Action == True:
    pass
   else:
    print('Failure _Action: [{}]'.format(_Action))
    exit()
  elif len(_Req) <= 1:
   print('Required Syntax: add [SYNTAX]')
   pass
########### Second Variable Listing ##################
 if len(_Req) > 1:
  # Edit Rooms 
  if _Req[0].lower()+' '+_Req[1].lower() == 'edit rooms':
   _Action = Server.edit_syntax_rooms()
   if _Action == True:
    pass
   else:
    print('Failure _Action: [{}]'.format(_Action))
    exit()

  # Edit Users
  elif _Req[0].lower()+' '+_Req[1].lower() == 'edit users':
   _Action = Server.edit_syntax_users()
   if _Action == True:
    pass
   else:
    print('Failure _Action: [{}]'.format(_Action))
    exit()
   


while On:
 _OptionsSelector()
 
  
  
 
