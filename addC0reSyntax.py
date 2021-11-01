import pickle
global FILE_A
global FILE_B
global _room
global _user
_room = []
_user = []
FILE_A = False
FILE_B = False

def _collectRoom(syntax):
 try:
  global _room
  print('Please Insert The Rooms You Would Like To Add To The New Syntax [{}] Or Use Done. You May Use Help For More Information.'.format(syntax))
  _R = input('>>: ')
  _R2 = _R.split(' ')
  if _R2[0].lower() == 'done':
   print('Setting [{}] Rooms For New Syntax'.format(_room))
   return _room
  elif _R2[0].lower() == 'exit':
   print('Setting [{}] Rooms For New Syntax'.format(_room))
   return _room
  elif _R2[0].lower() == 'help':
   print('You May Insert A Room Id \'0xID\', Or Use View,Clear or Remove For List Options You May Use Exit At Any Time.')
   _collectRoom(syntax)
  elif _R2[0].lower() == 'view':
   print('Current Rooms To Be Added To New Syntax: {}'.format(_room))
   _collectRoom(syntax)
  elif _R2[0].lower() == 'clear':
   print('Clearing Rooms: {}'.format(_room))
   _room = []
   print('Rooms: {} Cleared'.format(_room))
   _collectRoom(syntax)
  elif _R2[0].lower() == 'add':
   ID = _R2[1]
   if ID.lower() == 'global':
    _room = []
    _room.append('global')
    print('Current Rooms: {} Set Global For New Syntax'.format(_room))
    _collectRoom(syntax)
   elif ID[:2] == '0x':
    if 'global' not in _room:
     _rooms.append(ID)
     print('[{}] Added To Rooms, Current Rooms Allowed For New Syntax: {}'.format(ID,_room))
     _collectRoom(syntax)
    elif 'global' in _room:
     print('This Syntax Is Already Set As Global. Please Use Done/Exit Or Remove Global')
     _collectRoom(syntax)
  elif _R2[0].lower() == 'remove':
   if _R2[1].lower() in _room:
    _room.remove(_R2[1].lower())
    print('Removed {} From Rooms List: {}'.format(_R2[1].lower(),_room))
    _collectRoom(syntax)
   elif _R2[1].lower() not in _room:
    print('{} Not In Rooms. Current Rooms List: {}'.format(_R2[1].lower(),_room))
    _collectRoom(syntax)
  else:
   print('Please Use One Of The Provided Syntax For Room Addition. Thank You')
   _collectRoom(syntax)
 except Exception as E:
  print('Something Has Gone Seriously Wrong With _collectRooms() External Function. Please Investigate')
  print('Error: [{}]'.format(E))


def _collectUser(syntax):
 try:
  global _user
  print('Please Insert The Users You Would Like To Add To The New Syntax [{}] Or Use Done. You May Use Help For More Information.'.format(syntax))
  _R = input('>>: ')
  _R2 = _R.split(' ')
  if _R2[0].lower() == 'done':
   print('Setting [{}] Users For New Syntax'.format(_user))
   return _user
  elif _R2[0].lower() == 'exit':
   print('Setting [{}] Users For New Syntax'.format(_user))
   return _user
  elif _R2[0].lower() == 'help':
   print('You May Insert A User Id \'ID\', (User Groupings Are Integer Valued) Or Use View,Clear or Remove For List Options You May Use Exit At Any Time.')
   _collectUser(syntax)
  elif _R2[0].lower() == 'view':
   print('Current Users To Be Added To New Syntax: {}'.format(_user))
   _collectUser(syntax)
  elif _R2[0].lower() == 'clear':
   print('Clearing Users: [{}]'.format(_user))
   _user = []
   print('Users: [{}] Cleared'.format(_user))
   _collectUser(syntax)
  elif _R2[0].lower() == 'add':
   ID = _R2[1]
   if ID.lower() == 'global':
    _user = []
    _user.append('global')
    print('Current Users: [{}] Set Global For New Syntax'.format(_user))
    _collectUser(syntax)
   elif ID != 'global':
    if 'global' not in _user:
     _user.append(ID)
     print('[{}] Added To Users, Current User Groupings Allowed For New Syntax: [{}]'.format(ID,_user))
     _collectUsers(syntax)
    elif 'global' in _user:
     print('This Syntax User Groupings Is Already Set As Global. Please Use Done/Exit Or Remove Global')
     _collectUser(syntax)
  elif _R2[0].lower() == 'remove':
   if _R2[1].lower() in _user:
    _users.remove(_R2[1].lower())
    print('Removed [{}] From User Grouping List: [{}]'.format(_R2[1].lower(),_user))
    _collectUser(syntax)
   elif _R2[1].lower() not in _user:
    print('[{}] Not In User Groupings. Current User Groupings List: [{}]'.format(_R2[1].lower(),_user))
    _collectUser(syntax)
  else:
   print('Please Use One Of The Provided Syntax For Users Addition. Thank You')
   _collectUser(syntax)
 except Exception as E:
  print('Something Has Gone Seriously Wrong With _collectUsers() External Function. Please Investigate')
  print('Error: [{}]'.format(E))


def _checkFiles(file=''):
 global FILE_A
 global FILE_B
 SYNTAX_PATH = './C0reSyntax.cmf'
 SUB_PATH = './C0reSubSyntax.cmf'
 
 if file.lower() == 'sub' or file.lower() == 'all' and FILE_A == False:
  try:
   oldC0re = pickle.load(open(SUB_PATH,'rb'))
   print('Old C0re Sub File Opened')
   FILE_A = True
   _checkFiles(file)
  except Exception as E:
   print('New C0re Sub File Needed')
   oldC0re = dict()
   oldC0re['List'] = list()
   pickle.dump(oldC0re,open(SUB_PATH,'wb'))
   _checkFiles(file)
 if file.lower() == 'main' or file.lower() == 'all' and FILE_B == False:
  try:
   oldC0re = pickle.load(open(SYNTAX_PATH,'rb'))
   print('Old C0re Syntax File Opened')
   FILE_B = True
   _checkFiles(file)
  except Exception as E:
   print('New C0re Syntax File Needed')
   oldC0re = dict()
   oldC0re['List'] = list()
   pickle.dump(oldC0re,open(SYNTAX_PATH,'wb'))
   _checkFiles(file)
 if FILE_A == True and FILE_B == True:
  return True




class C0reSyntaxUpdater(object): 
 def __init__(self):
  self.SYNTAX_PATH = './C0reSyntax.cmf'
  self.SUB_PATH = './C0reSubSyntax.cmf'
  self.FileCheck = _checkFiles('all')
  self.Syntax = pickle.load(open(self.SYNTAX_PATH,'rb'))
  self.Sub = pickle.load(open(self.SUB_PATH,'rb'))
 
 def _pullSub(self):
  if self.FileCheck == True:
   try:
    self.Sub = pickle.load(open(self.SUB_PATH,'rb'))
    return self.Sub
   except Exception as E:
    print('Something Has Gone Wrong With Internal Sub Extraction!')
    print('Please Contact Skrypt With Following Error: [{}]'.format(E))
    exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)
  elif self.FileCheck == False:
   print('Something Has Gone Wrong With Internal File Check! Need To Exit Program')
   exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)
  else:
   print('Something Has Seriously Fucked Up With Internal File Check! Haha Causing A Exit() Check It Out Meatball!')
   print('_pullSub(self) issue.')
   print('self.FileCheck: [{}]'.format(self.FileCheck))
   exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)

 def _pullSyntax(self):
  if self.FileCheck == True:
   try:
    self.Syntax = pickle.load(open(self.SYNTAX_PATH,'rb'))
    return self.Syntax
   except Exception as E:
    print('Something Has Gone Wrong With Internal Syntax Extraction!')
    print('Please Contact Skrypt With Following Error: [{}]'.format(E))
    exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)
  elif self.FileCheck == False:
   print('Something Has Gone Wrong With Internal File Check! Need To Exit Program')
   exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)
  else:
   print('Something Has Seriously Fucked Up With Internal File Check! Haha Causing A Exit() Check It Out Meatball!')
   print('_pullSyntax(self) issue.')
   exit() # Must Pull Internal Exit Even With Controller ( There Is A Serious Problem With Main Extraction Protocol)
   
 def _publishSub(self,word):
  self.Length = len(word) # Stores A Internal Length Factor
  self.Counter = 1 # Stores A Internal Counter
  if word not in self.Sub:
   try:
    self.Sub[word] = word # Attaches Our Word To Our Substitute Binary File
    while self.Length > 4: # Checks Internal Length Factor For Above (6)
     new_word = word[:-int(self.Counter)]
     if new_word not in self.Sub: # Checks To Make Sure There Is No Path Collisions
      self.Sub[new_word] = word # Creates A Link Between Substitutes And Actual Syntax Map
      print('Added Substitute: [{}] For Syntax: [{}]'.format(new_word,self.Sub[new_word]))
      self.Counter += 1 # Updates Our Counter
      self.Length -= 1 # Updates Our Length Factor
      if self.Length <= 4:
       break
     elif new_word in self.Sub:
      print('[{}] Is Already Linked To: [{}]'.format(new_word,self.Sub[new_word])) # Alerts User We Have Blocked A Collision
      self.Counter += 1
      self.Length -= 1
    pickle.dump(self.Sub,open(self.SUB_PATH,'wb')) # Dumps Our Substitute File.
    return True # Tells Our Publish_Syntax Function Everything Has Gone As Expected
   except Exception as E:
    print('There Was An Error Trying To Update Substitue cmf Please Investigate')
    print('Error: [{}]'.format(E))
    return False # Internal False (Controller Assisted Had To Arrange Exit() => False)
  elif word in self.Sub:
   print('[{}] Already Known In Substitute Memory'.format(word)) # Alerts User There Is Nothing To Be Done
   return True # Tells Our Publish_Syntax Function Everything Has Gone As Expected.
   
    
 def publish_syntax(self,word,users=list(),rooms=list()):
  '''
   Requires:
    word = String
    users = Listed Numbers (Refer To User Object Privlidges Mapping)
    rooms = Global Declaration And/Or Listed Room ids (Refer To C0re Rooms For Mapping)
  '''
  try:
   self.Sub = self._pullSub() # Sets Substitute Attribute
   self.Syntax = self._pullSyntax() # Sets Syntax Attribute
   if word not in self.Syntax: # Checks word Against Syntax Attribute
    subbed = self._publishSub(word) # Creates A Substitute Collection For word
    if subbed: # If Substitute Collection Creation Was Successful
     self.Syntax[word] = dict() # Create New Slot For word Within Syntax Dictionary
     self.Syntax['List'].append(word) # Add word To Syntax List
     self.Syntax[word]['Users'] = users # Add Base users Availablity To word
     self.Syntax[word]['Rooms'] = rooms # Add Base rooms Availablity To word
     pickle.dump(self.Syntax,open(self.SYNTAX_PATH,'wb')) # Dump Binary Representation Of self.Syntax
     print('Word: [{}] | self.Syntax[word][\'Users\']: [{}] | self.Syntax[word][\'Rooms\']: [{}] |'.format(word,self.Syntax[word]['Users'],self.Syntax[word]['Rooms']))
     return True # Tells Contoller To move Forward
    else: # If Substitue Collection Has Failed Without Throwing An Exception
     print('Something Has Gone Wrong Subbed (Publish_Syntax()) Has Returned False Please Investigate.') # Tell User They Are Fucked
     return False # Tells Contoller To move Forward
   elif word in self.Syntax: # If word (Syntax) Already Within Our Syntax List
    print('[{}] Is Already Noted Within Our Syntax List Please Use View And Alteration Methods.'.format(word)) # Tell Us This Is The Case
    return True # Tells Contoller To move Forward
  except Exception as E: # Catch Any Exceptions
   print('Something Has Gone Amuck With publish_syntax() Please Investigate With The Below Error.') # Tell Us About Exception
   print('Error: [{}]'.format(E)) # Print The Actual Exception
   return False # Tells Contoller To move Forward

 def _editRooms(self,edit):
  global _room
  self.Sub = self._pullSub()
  self.Syntax = self._pullSyntax()
  try:
   print('Current Available Rooms: {} For Syntax [{}]'.format(self.Syntax[self.Sub[edit]]['Rooms'],edit))
   _room = self.Syntax[self.Sub[edit]]['Rooms'] # Hard Set
   room_to = _collectRoom(edit)
   self.Syntax[self.Sub[edit]]['Rooms'] = _room
   pickle.dump(self.Syntax,open(self.SYNTAX_PATH,'wb'))
   return True # Tells Controller To Move Forward
  except Exception as E:
   print('Something Has Gone Wrong With Internal Function _editRooms(self,edit) Please Investigate')
   print('Error: [{}]'.format(E))
   return False # Tells Contoller To move Forward

 def _editUsers(self,edit):
  global _user
  self.Sub = self._pullSub()
  self.Syntax = self._pullSyntax()
  try:
   print('Current Available Users: {} For Syntax [{}]'.format(self.Syntax[self.Sub[edit]]['Users'],edit))
   _user = self.Syntax[self.Sub[edit]]['Users']
   users_to = _collectUser(edit)
   self.Syntax[self.Sub[edit]]['Users'] = _user
   pickle.dump(self.Syntax,open(self.SYNTAX_PATH,'wb'))
  except Exception as E:
   print('Something Has Gone Wrong With Internal Function _editUsers(self,edit) Please Investigate')
   print('Error: [{}]'.format(E))
   return False # Tells Contoller To move Forward
     
 def edit_syntax_rooms(self):
  self.Sub = pickle.load(open(self.SUB_PATH,'rb'))
  self.Syntax = pickle.load(open(self.SYNTAX_PATH,'rb'))
  try:
   print('Please Provide A Syntax To Edit The Rooms For')
   edit = input('>>: ')
   if edit in self.Sub:
    print('[{}] Available To Be Edited'.format(edit))
    self._editRooms(self.Sub[edit])
    return True # Tells Contoller To move Forward
   else:
    print('Syntax Does Not Exist')
    self.edit_syntax_rooms()
    return True # Tells Contoller To move Forward
  except Exception as e:
   print('Something Has Gone Wrong With Main Function edit_syntax_rooms(self) Please Investigate')
   print('Error: [{}]'.format(e))
   return False # Tells Contoller To move Forward

 def edit_syntax_users(self):
  self.Sub = pickle.load(open(self.SUB_PATH,'rb'))
  self.Syntax = pickle.load(open(self.SYNTAX_PATH,'rb'))
  try:
   print('Please Provide A Syntax To Edit To User Privlidges For')
   edit = input('>>: ')
   if edit in self.Sub:
    print('[{}] Available To Be Edited'.format(edit))
    self._editUsers(self.Sub[edit])
    return True # Tells Contoller To move Forward
   else:
    print('Syntax Does Not Exist')
    self.edit_syntax_users()
    return True # Tells Contoller To move Forward
  except Exception as e:
   print('Something Has Gone Wrong With Main Function edit_syntax_rooms(self) Please Investigate')
   print('Error: [{}]'.format(e))
   return False # Tells Contoller To move Forward

 def view_syntax(self,word):
  self.Sub = self._pullSub()
  self.Syntax = self._pullSyntax()
  if word in self.Sub:
   base = self.Syntax[self.Sub[word]]
   print('''
   Statistics On Word: [{0}]
    {0} Users Group Id List: {1}
    {0} Available Rooms List: {2}
'''.format(word,self.Syntax[self.Sub[word]]['Users'],self.Syntax[self.Sub[word]]['Rooms']))
   return True # Tells Contoller To move Forward
  elif word not in self.Sub:
   print('Syntax [{}] Is Unknown You May Program Usage With The publish_syntax() Function'.format(word))
   return True # Tells Contoller To move Forward
     
     
