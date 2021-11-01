global _users
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
