"""    
Open Test Arbatrage System USE AT YOUR OWN RISK!
MULTIPLE EXCHANGE ACCEPTANCE
ALLOWS 'USERS' TO CHOOSE THEIR OWN STRATEGY AS WELL AS TRADING COINS
PROVIDES DETAILED INFORMATION ABOUT EXCHANGES & PLATFORMS
ALLOWS USERS TO CONNECT IN A FRIENDLY ENVIRONMENT
Author: ~Skrypt~
"""

#@Dev: Finish Fixing User Pointing At Self
#@Dev: Finish Stalking / Hidden Movement, Give User Object Hidden Boolean
#@Dev: Finish Look For Room Items
#@Dev: Allow Players To Move & Guard
#@Dev: Deploy RK Token Via Testnet For Inital Circulation Event & System Deployment (CryptoTab {Infura.io, Ropsten.Io Etc.})

import sys
import os
import time
import shlex
import random
import sha3
import pickle
import hashlib
#from web3 import Web3
#from web3.providers.rpc import HTTPProvider
#from ecdsa import SigningKey, SECP256k1
#web3 = Web3(HTTPProvider('https://mainnet.infura.io/M4QNeQhVp2x0Lm0OxNvW'))
#true = True
#false = False



#from resources import *
#from resources.TheCoreData.RawData import *
from resources.PersonaData.UserObject import *
from resources.TheCoreData.CoreResponse import *
#from resources.TheCoreData.CoreSyntax import CoreSyntaxSets
from resources.worlditems import worldItems
from resources.worldnotice import worldNotice
from resources.worldLists import worldLists
from resources.useroptions import userOptions
from resources.worldBoolean import worldBoolean
# import the Environment server class
from resources.server import C0reServer
from resources.TheCoreData.CoreItems import *
from resources.TheCoreData.C0reRoomSystem.C0reRooms import *
#from resources.TheCoreData.C0reUserSystem import *
global C0RESUBPATH
global C0RESYNTAXPATH
C0RESUBPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSubSyntax.cmf'
C0RESYNTAXPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSyntax.cmf'




global Total_Users
users = {}
Total_Users = 0
# starts C0re Server
C0re = C0reServer()
INTERVAL = 0.2
C0reSub = pickle.load(open(C0RESUBPATH,'rb'))
C0reSyntax = pickle.load(open(C0RESYNTAXPATH,'rb'))
print('Starting C0re Server And Hosting Platform Please Wait A Moment')

class ServerRefresh:
 def __init__(self):
  global Total_Users
  time.sleep(0.2)
  for id in C0re.get_new_users():
# User IS DEFINED HERE FROM - [Resources.PersonaData.UserObject.py]
   users[id] = Guest()
   Total_Users += 1
   C0re.send_message(id, 'Welcome To The Center Of The Cryptoverse. Please Enter Any Data To Continue.'.title(),'Vivian')
  for id in C0re.get_disconnected_users():
   if id not in users: continue
   for pid,pl in users.items():
    C0re.send_message(pid, '[{}] Has Left The C0re.'.format(users[id].Name),'Vivian')
   del(users[id])
  for id,gak,params in C0re.get_commands():
   if id not in users: continue
   if users[id].Started == False:
    users[id].Name = 'GuestWallet#'+str(Total_Users)
    users[id].Started = True
    for pid,pl in users.items():
     users[pid].Body._UpdateOverallHealth()
     if users[pid].Name != users[id].Name:
      if users[pid].Alerts['New Users']:
       C0re.send_message(pid, 'A Slight Shift Within Eeveaem\'s C0re Allows Room For Another Wandering Wallet.'.title(),'Vivian')
       C0re.send_message(pid, 'Welcome [{}] To Eeveaem. The Center Of The Cryptoverse'.format(users[id].Name),'Vivian')  
    C0re.send_message(id, 'Welcome [{}] To Eeveaem. The Center Of The Cryptoverse'.format(users[id].Name),'Vivian')
    C0re.send_message(id, 'You Have Entered [{}]'.format(C0re.World.Room[users[id].RoomID].Name),'Vivian')
    C0re.send_message(id, '{} Current Room Identification Number.'.format(users[id].RoomID),'Vivian')
    C0re.send_message(id, '{}'.format(C0re.World.Room[users[id].RoomID].Description),'Vivian')
    C0re.World.Room[users[id].RoomID].PlayersHere.append(users[id].Name)
    AlsoHere = list()
    for P in C0re.World.Room[users[id].RoomID].PlayersHere:
     if P not in AlsoHere and P != users[id].Name:
      AlsoHere.append(P)
    for HP in C0re.World.Room[users[id].RoomID].HiddenPlayers:
     for pid,pl in users.items():
      if users[id].SkillTree.Skills['Survival']['Sight'].Level > users[pid].SkillTree.Skills['Survival']['Stealth'].Level:
       if HP not in AlsoHere and HP != users[id].Name:
        AlsoHere.append(HP.Name+' Who Is Trying To Stay Hidden')
    C0re.send_message(id, 'Also Here: ['+"%s]" % ", ".join(AlsoHere).title(),'Vivian')
    VisibleExits = list()
    for E in C0re.World.Room[users[id].RoomID].Exits:
     if E.Name not in VisibleExits:
      VisibleExits.append(E.Name)
    C0re.send_message(id, 'Visible Exits: ['+"%s]" % ", ".join(VisibleExits).title(),'Vivian')
   elif gak.lower() in C0reSub:
    par = params
    par_split = par.split(' ')
    Syntax = C0reSub[gak.lower()]
    if 'global' in C0reSyntax[Syntax]['Rooms'] or users[id].RoomID in C0reSyntax[Syntax]['Rooms']:
     if users[id].Type['id'] in C0reSyntax[Syntax]['Users'] or 'global' in C0reSyntax[Syntax]['Users']:
     # Assert Syntax Match Here
      if users[id].C0reTime == 0:
       ########### Start Of 'Say' Syntax #################################
       if Syntax == 'say':
        if C0re.World.Room[users[id].RoomID].Private == False:
         if users[id].SpecialSpeech == False:
          C0re.send_message(id, '{0}\'s, \'{1}\''.format(users[id].Speech.title(),par.title()),users[id].Name.title()) # Alert User
          for pid,pl in users.items():
          # If thery are in the same room as player but not the player
           if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name:
            C0re.send_message(pid, '{0}\'s, \'{1}\''.format(users[id].Speech.title(), params.title()),users[id].Name.title()) # Tell Everyone In Room Except User
         elif users[id].SpecialSpeech == True:
          C0re.send_message(id, '{0}\'s and {1}\'s, \'{2}\''.format(users[id].SpecialSpeech.title(),users[id].Speech.title(),params.title()),user[id].Name.title()) # Alert User
          # go through every user in the game
          for pid,pl in users.items():
          # if they're in the same room as the user
           if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name:
            C0re.send_message(pid, '{0}\'s and {1}\'s, \'{2}\''.format(users[id].SpecialSpeech.title(),users[id].Speech.title(),params.title()),users[id].Name.title())
        elif C0re.World.Room[users[id].RoomID].Private == True:
         C0re.send_message(id, 'I\'m Sorry {} This Is A Private Area No Speaking Or Whispering Is Allowed.'.format(users[id].Name),'Vivian')
         for pid,pl in users.items():
          if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
           C0re.send_message(pid, 'Tries But Fails To Speak.',users[id].Name.title(),'Vivian')
           
       ######## End Of Say Syntax ###################################################

       ######## Start Of Look Syntax #############################################
       elif Syntax == 'look':
        if len(par_split) == 1:
         if par_split[0] == '':
          C0re.send_message(id, '{}'.format(C0re.World.Room[users[id].RoomID].Description),'Vivian')
          AlsoHere = list()
          for P in C0re.World.Room[users[id].RoomID].PlayersHere:
           if P not in AlsoHere and P != users[id].Name:
            AlsoHere.append(P)
          for HP in C0re.World.Room[users[id].RoomID].HiddenPlayers:
           for pid,pl in users.items():
            if users[pid].Name == HP:
             if users[id].SkillTree.Skills['Survival']['Sight'].Level >= users[pid].SkillTree.Skills['Survival']['Stealth'].Level:
              if HP != users[id].Name and HP not in AlsoHere:
               AlsoHere.append(HP+' Who Is Trying To Stay Hidden')
          if AlsoHere != []:
           C0re.send_message(id, 'Also Here: ['+"%s]" % ", ".join(AlsoHere).title(),'Vivian')
          elif AlsoHere == []:
           C0re.send_message(id, 'Also Here: No One','Vivian')
          VisibleExits = list()
          for E in C0re.World.Room[users[id].RoomID].Exits:
           if E.Name not in VisibleExits:
            VisibleExits.append(E.Name)
          C0re.send_message(id, 'Visible Exits: ['+"%s]" % ", ".join(VisibleExits).title(),'Vivian')
         elif par_split[0].lower() == 'self' or par_split[0].lower() == 'me' or par_split[0] == users[id].Name:
          C0re.send_message(id,'You See Yourself.','Vivian')
          C0re.send_message(id,'{}'.format(users[id]._ProvideDescription()),'Vivian') #Test Not Finished
          for pid,pl in users.items():
           if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name or users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers and users[pid].Name != users[id].Name:
            C0re.send_message(pid,'Looks At Themself.',users[id].Name)   
        elif len(par_split) == 2:
         if par_split[0].lower() == 'at':
          if par_split[1] in C0re.World.Room[users[id].RoomID].PlayersHere:
           for pid,pl in users.items():
            if users[pid].Name == par_split[1]:
             C0re.send_message(id,'You See {}.'.format(users[pid].Name),'Vivian')
             C0re.send_message(id,users[pid].Description,'Vivian')
          elif par_split[1] in C0re.World.Room[users[id].RoomID].HiddenPlayers:
           for pid,pl in users.items():
            if par_split[1] == users[pid].Name:
             if users[id].SkillTree.Skills['Survival']['Sight'].Level > users[pid].SkillTree.Skills['Survival']['Stealth'].Level:
              C0re.send_message(id,'You See {} Who Is Trying To Stay Hidden.'.format(users[pid].Name),'Vivian')
              C0re.send_message(id,users[pid].Description,'Vivian')
             elif users[id].SkillTree.Skills['Survival']['Sight'].Level == users[pid].SkillTree.Skills['Survival']['Stealth'].Level:
              C0re.send_message(id,'You Can Barely See The Outline Of {} But Not Much More..'.format(users[pid].Name),'Vivian')
       ######## End Of Look Syntax #################################################
          
       ######## Start Of Hide Syntax ###############################################
       elif Syntax == 'hide':
        C0re.World.Room[users[id].RoomID].HiddenPlayers.append(users[id].Name) # Apply The Player To Hidden Players List
        C0re.World.Room[users[id].RoomID].PlayersHere.remove(users[id].Name) # Remove The Player From Visible Players List
        C0re.send_message(id,'You Silently Melt Into The Shadows Around You.','Vivian') # Alert The Player
        for pid,pl in users.items(): # Go Through All Users In The Game
         if users[pid].Name != users[id].Name and users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere or users[pid].Name != users[id].Name and users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers: # Check For Other Players In Room
          if users[pid].SkillTree.Skills['Survival']['Sight'].Level >= users[id].SkillTree.Skills['Survival']['Stealth'].Level: # Check If They Can See The Player Attempting To Hide
           if users[pid].Alerts['Hiding Players']:
            C0re.send_message(pid,'You Observe Silently As {} Slips Into The Shadows.'.format(users[id].Name),'Vivian') # Alerts Qualified Players
       ######## End Of Hide Syntax #################################################
           
       ######## Start Of Unhide Syntax #############################################
       elif Syntax == 'unhide':
        C0re.World.Room[users[id].RoomID].PlayersHere.append(users[id].Name) # Apply The Player To Visible Players List
        C0re.World.Room[users[id].RoomID].HiddenPlayers.remove(users[id].Name) # Remove The Player From Hidden Players List
        C0re.send_message(id,'You Silently Step Out Of The Shadows.','Vivian') # Alert The Player
        for pid,pl in users.items(): # Go Through All Users In The Game
         if users[pid].Name != users[id].Name and users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere or users[pid].Name != users[id].Name and users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers: # Check For Other Players In Room
          if users[pid].SkillTree.Skills['Survival']['Sight'].Level >= users[id].SkillTree.Skills['Survival']['Stealth'].Level: # Check If They Can See The Player Attempting To Unhide
           if users[pid].Alerts['Hiding Players']:
            C0re.send_message(pid,'You Observe Silently As {} Steps Out Of The Shadows.'.format(users[id].Name),'Vivian') # Alerts Qualified Players
       ######## End Of Unhide Syntax ###############################################
            
       ############## ADMIN CHEATERS SECTION FOR TESTING ONLY ######################
       elif Syntax == 'login':
        if par_split[0] == 'Trinity':
         users[id].Type['Number'] = '1'
         users[id].Type['id'] = 'Admin'
         C0re.send_message(id,'Admin Effect Activated','Admin System')


       elif Syntax == 'cheat':
        if par_split[0] == 'sight':
         users[id].SkillTree.Skills['Survival']['Sight'].Level += 10
         C0re.send_message(id,'You Have Successfully Cheated Asshole. New Sight Level: {}'.format(users[id].SkillTree.Skills['Survival']['Sight'].Level),'Admin System')
        elif par_split[0] == 'stealth':
         users[id].SkillTree.Skills['Survival']['Stealth'].Level += 10
         C0re.send_message(id,'You Have Successfully Cheated Asshole. New Stealth Level: {}'.format(users[id].SkillTree.Skills['Survival']['Stealth'].Level),'Admin System')
       ############ END OF ADMIN CHEATERS SECTION FOR TESTING ONLY #################
         
       ######## Start Of Point Syntax ##############################################
       elif Syntax == 'point':
        if len(par_split) == 1: # If We Have One Argument
         if par_split[0] == '': # If The Argument Is Blank
          C0re.send_message(id,'You Point At What Appears To Be Thin Air.','Vivian') # Send A Goofy Message
          for pid,pl in users.items(): # Go Through The Players In The Game
           if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name or users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers and users[pid].Name != users[id].Name:
            C0re.send_message(pid,'Points At What Appears To Be Thin Air.',users[id].Name.title()) # Tell All Other Players What Happened
         if par_split[0].lower() == 'me' or par_split[0].lower() == 'self' or par_split[0] == users[id].Name: # If Player Is Referring To Themselves
          C0re.send_message(id,'You Point At Yourself.','Vivian')
          for pid,pl in users.items():
           if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name or users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers and users[pid].Name != users[id].Name:
            C0re.send_message(pid,'Points Directly At Their Own Chest.',users[id].Name)
         elif par_split[0] in C0re.World.Room[users[id].RoomID].PlayersHere or par_split[0] in C0re.World.Room[users[id].RoomID].HiddenPlayers: # If The Argument Is A Player
          if par_split[0] in C0re.World.Room[users[id].RoomID].PlayersHere: # Check If The Player Is Visible To Everyone Else
           C0re.send_message(id,'You Point At {}'.format(par_split[0]),'Vivian') # Point At Other Player If They Exist
           for pid,pl in users.items(): # Go Through The Players In The Game
            if users[pid].Name == par_split[0]: # If Its The Player Being Pointed At
             C0re.send_message(pid,'Points At You',users[id].Name) # Tell Them
            elif users[pid].Name != par_split[0] and users[pid].Name != users[id].Name: # If Its A Bystander
             C0re.send_message(pid,'Points At {}'.format(par_split[0]),users[id].Name) # Tell Bystander
          elif par_split[0] in C0re.World.Room[users[id].RoomID].HiddenPlayers: # If The Player Is Hidden
           for pid,pl in users.items(): # Go Through The Players In The Game
            if users[pid].Name == par_split[0]: # Select Hidden Player
             if users[pid].SkillTree.Skills['Survival']['Stealth'].Level == users[id].SkillTree.Skills['Survival']['Sight'].Level: # Check Pointers Sight Vs Hidden Players Stealth (Equal)
              C0re.send_message(id,'You Point At {} But No One Seems To Take Notice.'.format(users[pid].Name),'Vivian')
              C0re.send_message(pid,'You Smile Silently As {} Fails To Ruin Your Hiding Place.'.format(users[id].Name),'Vivian')
             elif users[pid].SkillTree.Skills['Survival']['Stealth'].Level > users[id].SkillTree.Skills['Survival']['Sight'].Level: # Check Pointers Sight Vs Hidden Players Stealth (Below)
              C0re.send_message(id,'You Point At What Appears To Be Thin Air.','Vivian')
              for pid,pl in users.items():
               if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name or users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers and users[pid].Name != users[id].Name:
                C0re.send_message(pid,'Points At What Appears To Be Thin Air.',users[id].Name.title())
             elif users[pid].SkillTree.Skills['Survival']['Stealth'].Level < users[id].SkillTree.Skills['Survival']['Sight'].Level: # Check Pointers Sight Vs Hidden Players Stealth (Above)
              C0re.World.Room[users[id].RoomID].PlayersHere.append(users[pid].Name) # Add The Hidden Player To Visible List
              C0re.World.Room[users[id].RoomID].HiddenPlayers.remove(users[pid].Name) # Remove The Player From Hidden List
              C0re.send_message(id,'You Point At {} Ruining Their Hiding Place.'.format(users[pid].Name),'Vivian')
              for pid,pl in users.items():
               if users[pid].Name in C0re.World.Room[users[id].RoomID].PlayersHere and users[pid].Name != users[id].Name or users[pid].Name in C0re.World.Room[users[id].RoomID].HiddenPlayers and users[pid].Name != users[id].Name:
                if users[pid].Name == par_split[0]:
                 C0re.send_message(pid,'Pointed You Out Ruining Your Hiding Place.',users[id].Name)
                elif users[pid].Name != par_split[0]:
                 C0re.send_message(pid,'Points Out {} Ruining Their Hiding Place.'.format(par_split[0]),users[id].Name)
       ######## End Of Point Syntax ################################################
            
       ######## Start Of Health Syntax #############################################
       elif Syntax == 'health':
        if len(par_split) >= 1:
         if par_split[0] == '':
          C0re.send_message(id,'Your Body {}'.format(users[id].Body.CheckHealth()),'Vivian')
         else:
          returned = users[id].Body.CheckHealth(params)
          if returned != None:
           C0re.send_message(id,'Your {} {}'.format(params.title(),users[id].Body.CheckHealth(params)),'Vivian')
          elif returned == None:
           C0re.send_message(id,'You Don\'t Appear To Have A {}'.format(params.title()),'Vivian')
       ######## End Of Health Syntax ###################################################  
         
    
                 
      elif users[id].C0reTime > 0:
       users[id].C0reTime += C0reTimeMap[gak.lower()] # Adds Additional C0re-Time To Prevent Server Spam
       C0re.send_message(id,'...Please Wait ({}) C0re-Time...'.format(users[id].C0reTime),'Vivian')
      elif users[id].Type['id'] not in C0reSyntax[Command]['Users'] and 'global' not in C0reSyntax[Command]['Users']:
      # Assert Command Level Failure
       C0re.send_message(id, '[{}] Syntax Is Not A [{}] Privlidge At This Time.'.format(Command,users[id].Type['Name']),'Vivian')
      elif 'global' not in C0reSyntax[Command]['Rooms'] or users[id].Room_id not in C0reSyntax[Command]['Rooms']:
      # Assert Command Room Failure
       C0re.send_message(id, '[{}] Syntax Is Not Available Within Room [{}] At This Time.'.format(gak.upper(),users[id].Room),'Vivian')
   else:
    C0re.send_message(id, '[{}] Is A Unknown Command Please \'Submit\' A Support Ticket If You Feel This Is A Mistake.'.format(gak.upper()),'Vivian')
while True:
    # 'update' must be called in the loop to keep the environment running and give
    # us up-to-date information
    
 C0re.update()
#Conditions To The Alive Player Below
 ServerRefresh()

