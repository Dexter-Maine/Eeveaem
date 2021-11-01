"""    
Open Test Arbatrage System USE AT YOUR OWN RISK!
MULTIPLE EXCHANGE ACCEPTANCE
ALLOWS 'USERS' TO CHOOSE THEIR OWN STRATEGY AS WELL AS TRADING COINS
PROVIDES DETAILED INFORMATION ABOUT EXCHANGES & PLATFORMS
ALLOWS USERS TO CONNECT IN A FRIENDLY ENVIRONMENT
Author: ~Skrypt~
"""
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
from resources.TheCoreData.RawData import *
from resources.PersonaData.PersonaRaw import *
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
from resources.TheCoreData.C0reUserSystem.UserObject import *
global C0RESUBPATH
global C0RESYNTAXPATH
C0RESUBPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSubSyntax.cmf'
C0RESYNTAXPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSyntax.cmf'





users = {}
Total_Users = 0
# starts C0re Server
C0re = C0reServer()
INTERVAL = 0.2
C0reSub = pickle.load(open(C0RESUBPATH,'rb'))
C0reSyntax = pickle.load(open(C0RESYNTAXPATH,'rb'))
print('Starting C0re Server And Hosting Platform Please Wait A Moment')
while True:
    time.sleep(0.2)
    # 'update' must be called in the loop to keep the environment running and give
    # us up-to-date information
    
    C0re.update()
    for id in C0re.get_new_users():
# User IS DEFINED HERE FROM - [Resources.PersonaData.UserObject.py]
        users[id] = C0reGuest()
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
             usershere = []
             usershere.append(users[pid].Name)
             C0re.send_message(pid, 'A Slight Shift Within Eeveaem\'s C0re Allows Room For Another Wandering Wallet.'.title(),'Vivian')
             C0re.send_message(pid, 'Welcome [{}] To Eeveaem. The Center Of The Cryptoverse'.format(users[id].Name),'Vivian')  
            C0re.send_message(id, 'Welcome [{}] To Eeveaem. The Center Of The Cryptoverse'.format(users[id].Name),'Vivian')
            C0re.send_message(id, 'You Have Entered [{}]'.format(users[id].Room),'Vivian')
            C0re.send_message(id, '{} Current Room Identification Number.'.format(users[id].Room_id),'Vivian')
            C0re.send_message(id, '{}'.format(TheC0reRooms[users[id].Room].Description),'Vivian')
            C0re.send_message(id, 'Also Here: ['+"%s]" % ", ".join(usershere).title(),'Vivian')
            C0re.send_message(id, 'Visible Exits: ['+"%s]" % ", ".join(TheC0reRooms[users[id].Room].Exits).title(),'Vivian')
#Conditions To The Alive Player Below

    
# Refer to Ess.py for gak list referrences. ~Skrypt
        elif gak.lower() in C0reSub:
         par = params
         par_split = par.split(' ')
         Command = C0reSub[gak.lower()]
         if 'global' in C0reSyntax[Command]['Rooms'] or users[id].Room_id in C0reSyntax[Command]['Rooms']:
          if users[id].Type['id'] in C0reSyntax[Command]['Users'] or 'global' in C0reSyntax[Command]['Users']:
           # Assert Command Match Here
           if users[id].C0reTime == 0:
           ########### Start Of 'Say' Syntax #################################
            if Command == 'say':
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
          ######## End Of Say Syntax ###################################################


            if Command == 'read':
                 
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
