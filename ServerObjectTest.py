

class Say:
 def __init__(self):
  pass
 def _Action(self):
  if TheC0reRooms[users[id].Room].Private == False and TheC0reRooms[users[id].Room].Whisper_Only == False:
   if users[id].Special_Speech == False:
    C0re.send_message(id, '{0}\'s, \'{1}\''.format(users[id].Speech.title(),params.title()),users[id].Name.title()) # Alert User
   elif users[id].Special_Speech == True:
    C0re.send_message(id, '{0}\'s and {1}\'s, \'{2}\''.format(users[id].SpecialSpeech.title(),users[id].Speech.title(),params.title()),user[id].Name.title()) # Alert User
   # go through every user in the game
   for pid,pl in users.items():
    # if they're in the same room as the user
    if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
     if users[id].Special_Speech == False:
      C0re.send_message(pid, '{0}\'s, \'{1}\''.format(users[id].Speech.title(), params.title()),users[id].Name.title()) # Tell Everyone In Room Except User
     elif users[id].Special_Speech == True:
      C0re.send_message(pid, '{0}\'s and {1}\'s, \'{2}\''.format(users[id].SpecialSpeech.title(),users[id].Speech.title(),params.title()),users[id].Name.title())
  elif TheC0reRooms[users[id].Room].Private == True or TheC0reRooms[users[id].Room].Whisper_Only == True:
   if TheC0reRooms[users[id].Room].Private == True:
    C0re.send_message(id, 'I\'m Sorry {} This Is A Private Area No Speaking Or Whispering Is Allowed.'.format(users[id].Name),'Vivian')
    for pid,pl in users.items():
     if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
      C0re.send_message(pid, 'Tries But Fails To Speak.',users[id].Name.title())
     elif TheC0reRooms[users[id].Room].Whisper_Only == True:
      C0re.send_message(id, 'I\'m Sorry {}, This Is A Whisper Only Area'.format(users[id].Name.title()),'Vivian')
      for pid,pl in users.items():
       if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
        C0re.send_message(pid,'Fails To Whisper.',users[id].Name.title())
