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
from resources.TheCoreData.C0reRoomSystem.C0reRooms import TheC0reRooms
from resources.TheCoreData.C0reUserSystem.UserObject import *
global C0RESUBPATH
global C0RESYNTAXPATH
C0RESUBPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSubSyntax.cmf'
C0RESYNTAXPATH = './resources/TheCoreData/C0reSyntaxSystem/C0reSyntax.cmf'





users = {}
Total_Users = 0
# starts C0re Server
C0re = C0reServer(input('|[USERNAME]>>: '),hashlib.sha256(input('|[USERNAME]>>: ').encode()).hexdigest())
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
        C0re.send_message(id, Eresp["E_Notice_Welcome"].title())
    for id in C0re.get_disconnected_users():

        if id not in users: continue

        for pid,pl in users.items():

            C0re.send_message(pid, Eresp["E_Notice_Quit"].format(users[id].Name))

        del(users[id])

    for id,gak,params in C0re.get_commands():
        if id not in users: continue

        if users[id].Started == False:
            users[id].Name = 'GuestWallet'+str(hex(Total_Users))
            users[id].Started = True
            for pid,pl in users.items():
                usershere = []
                if users[pid].Room == users[id].Room:
                    usershere.append(users[pid].Name)
            C0re.send_message(pid, Eresp["E_Notice_Public_Symbol"].title())
            C0re.send_message(pid, Eresp["E_Notice_Enter_Message"].format(users[id].Name))  
            rm = rooms[users[id].Room]
            C0re.send_message(id, Eresp["E_Notice_Welcome_0"].format(users[id].Name))
            C0re.send_message(id, Eresp['E_Notice_Welcome_1'].format())
            C0re.send_message(id, Eresp['E_Notice_Have_Entered'].format(users[id].Room))
            C0re.send_message(id, Eresp['E_Notice_Current_Room_Id'].format(users[id].RoomID))
            C0re.send_message(id, Eresp['E_Notice_Open_Room_Format'].format(rm["description"]))
            C0re.send_message(id, Eresp['E_Notice_Also_Here']+"%s" % ", ".join(usershere).title())
            C0re.send_message(id, Eresp['E_Notice_Visible_Exits']+"%s" % ", ".join(rm["exits"]).title())
#Conditions To The Alive Player Below

    
# Refer to Ess.py for gak list referrences. ~Skrypt
        elif gak.lower() in C0reSub:
         par = params
         par_split = par.split(' ')
         Command = C0reSub[gak.lower()]
         if 'global' in C0reSyntax[Command]['Rooms'] or users[id].Room_id in C0reSyntax[Command]['Rooms']:
          if users[id].User_Level in C0reSyntax[Command]['Users'] or 'global' in C0reSyntax[Command]['Users']:
           # Assert Command Match Here
           if users[id].C0reTime == 0:
           ########### Start Of 'Say' Syntax #################################
            if Command == 'say':
             if TheC0reRooms[users[id].Room].Private == False and TheC0reRooms[users[id].Room].Whisper_Only == False:
              if users[id].Special_Speech == False:
               C0re.send_message(id, '{0}, \'{1}\''.format(users[id].Speech,params),users[id].Name) # Alert User
              elif users[id].Special_Speech == True:
               C0re.send_message(id, '{0} and Say, \'{1}\''.format(users[id].Speech,params),user[id].Name) # Alert User
              # go through every user in the game
              for pid,pl in users.items():
               # if they're in the same room as the user
               if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
                if users[id].Special_Speech == False:
                 C0re.send_message(pid, '{1}s, \'{2}\''.format(users[id].Speech, params),users[id].Name) # Tell Everyone In Room Except User
                elif users[id].Special_Speech == True:
                 C0re.send_message(pid, '{1} and Says, \'{2}\''.format(users[id].Speech,params),users[id].Name)
             elif TheC0reRooms[users[id].Room].Private == True or TheC0reRooms[users[id].Room].Whisper_Only == True:
              if TheC0reRooms[users[id].Room].Private == True:
               C0re.send_message(id, 'I\'m Sorry [{}] This Is A Private Area No Speaking Or Whispering Allowed.'.format(users[id].Name),'Vivian')
               for pid,pl in users.items():
                if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
                 C0re.send_message(pid, 'Tries But Fails To Speak.',users[id].Name)
              elif TheC0reRooms[users[id].Room].Whisper_Only == True:
               C0re.send_message(id, 'I\'m Sorry [{}], This Is A Whisper Only Area')
               for pid,pl in users.items():
                if users[pid].Room == users[id].Room and users[pid].Name != users[id].Name:
                 C0re.send_message(pid,'Fails To Whisper.',users[id].Name)
          ######## End Of Say Syntax ###################################################
                 
           elif users[id].C0reTime > 0:
            users[id].C0reTime += C0reTimeMap[gak.lower()] # Adds Additional C0re-Time To Prevent Server Spam
            C0re.send_message(id,'...Please Wait ({}) C0re-Time...'.format(users[id].C0reTime),'Vivian')
          elif users[id].User_Level not in C0reSyntax[Command]['Users'] and 'global' not in C0reSyntax[Command]['Users']:
           # Assert Command Level Failure
           C0re.send_message(id, '[{}] Syntax Is Not A [{}] Privlidge At This Time.'.format(Command,users[id].User_Level),'Vivian')
         elif 'global' not in C0reSyntax[Command]['Rooms'] or users[id].Room_id not in C0reSyntax[Command]['Rooms']:
          # Assert Command Room Failure
          C0re.send_message(id, '[{}] Syntax Is Not Available Within Room [{}] At This Time.'.format(Command,users[id].Room),'Vivian')
        else:
         C0re.send_message(id, '[{}] Is A Unknown Command Please \'Submit\' A Support Ticket If You Feel This Is A Mistake.')


# 'get' command (Object Initiated) Inventory active needs room objects initiated and sub-surface objects (table items etc.)
        elif gak.lower() in Ess["get"]["sets"]:
         pa = params.lower()
         pa_sub = pa.split(' ')
         user_has_item = False
         taken = False
         try:
          if pa_sub[0] == 'my' and pa_sub[1] != '':
           for i in users[id]["inventory"]:
            if i.Name == pa_sub[1].title():
             user_has_item = True
             taken = False
            elif i.Name == pa_sub[1].title()+' '+pa_sub[2].title():
             user_has_item = True
             taken = False
            if user_has_item == True and taken == False:
             if users[id]["left hand"] != [] and users[id]["right hand"] != []:
              C0re.send_message(id, "Your Hands Are Full. Maybe STOW Something And Try Again?")
             elif users[id]["right hand"] == []:
              users[id]["inventory"].remove(i)
              users[id]["right hand"].append(i)
              taken = True
              C0re.send_message(id, "You Get Your {0} From Your Inventory With Your Right Hand.".format(i.Name))
             elif users[id]["left hand"] == []:
              users[id]["inventory"].remove(i)
              users[id]["left hand"].append(i)
              taken = True
              C0re.send_message(id, "You Get Your {0} From Your Inventory With Your Left Hand.".format(i.Name))
            else:
             C0re.send_message(id, "Sorry {0}, You Do Not Have {1}.".format(users[id]["name"].title(), i.Name))
          else:
           C0re.send_message(id, 'What Are You Trying To Get?') 
         except Exception as Get_What:
          C0re.send_message(id, 'What Are You Trying To Get?')
          #elif paramTitle in wi: #needs work on this block (items need to be added to WI)
           #Evm.send_message(id, "Sorry {0}, You Cannot Get This Period.".format(users[id]["name"].title())) 
       



# 'stow' command (Object Initiated)
        elif gak in Ess["stow"]["sets"]:
            pa = params.lower()
            if users[id]["right hand"] == [] and users[id]["left hand"] == []:
              C0re.send_message(id, "You Have Nothing To Stow In Your Hands.")
            elif users[id]["right hand"] != [] and pa == "right":
              item_to_stow = users[id]["right hand"][0]
              users[id]["right hand"].remove(item_to_stow)
              users[id]["inventory"].append(item_to_stow)
              C0re.send_message(id, "You Put Your {} From Your Right Hand In Your Inventory.".format(item_to_stow.Name))             
            elif users[id]["left hand"] != [] and pa == "left":
              item_to_stow = users[id]["left hand"][0]
              users[id]["left hand"].remove(item_to_stow)
              users[id]["inventory"].append(item_to_stow)
              C0re.send_message(id, "You Put Your {} From Your Left Hand In Your Inventory.".format(item_to_stow.Name))
            elif users[id]["right hand"] == [] and pa == "right":
              C0re.send_message(id, "You Have Nothing In Your Right Hand To Put In Your Inventory.")
            elif users[id]["left hand"] == [] and pa == "left":
              C0re.send_message(id, "You Have Nothing In Your Left Hand To Put In Your Inventory.")
            elif params == "":
              C0re.send_message(id, "Usage Is STOW RIGHT/LEFT.".format())

# 'swap' command (Object Initiated)
        elif gak in Ess["swap"]["sets"]:
            if users[id]["right hand"] == [] and users[id]["left hand"] == []:
              C0re.send_message(id, "You Have Nothing To Swap In Your Hands.")
            elif users[id]["right hand"] != [] and users[id]["left hand"] == []:
              item_to_swap = users[id]["right hand"][0]
              users[id]["right hand"].remove(item_to_swap)
              users[id]["left hand"].append(item_to_swap)
              C0re.send_message(id, "You Swap Your {} From Your Right Hand To Your Left Hand.".format(item_to_swap.Name))
            elif users[id]["right hand"] == [] and users[id]["left hand"] != []:
              item_to_swap = users[id]["left hand"][0]
              users[id]["left hand"].remove(item_to_swap)
              users[id]["right hand"].append(item_to_swap)
              C0re.send_message(id, "You Swap Your {} From Your Left Hand To Your Right Hand.".format(item_to_swap.Name))
            elif users[id]["right hand"] != [] and users[id]["left hand"] != []:
              r = users[id].Body.RightHand[0]
              l = users[id].Body.LeftHand[0]
              users[id].Body.RightHand.remove(r)
              users[id].Body.RightHand.append(l)
              users[id].Body.LeftHand.remove(l)
              users[id].Body.LeftHand.append(r)
              C0re.send_message(id, 'You carefully swap {0} and {1} between your hands.'.format(users[id].Body.LeftHand,users[id].Body.RightHand))

# 'glance' command (Object Initiated)
        elif gak.lower() in Ess["glance"]["sets"]:
            if users[id]["right hand"] == [] and users[id]["left hand"] == []:
              C0re.send_message(id, "You Glance Down At Your Empty Hands.")
            elif users[id]["right hand"] != [] and users[id]["left hand"] == []:
              C0re.send_message(id, "You Glance Down And See Nothing In Your Left Hand And {} In Your Right Hand.".format(users[id]["right hand"][0].Name))
            elif users[id]["right hand"] == [] and users[id]["left hand"] != []:
              C0re.send_message(id, "You Glance Down And See Nothing In Your Right Hand And {} In Your Left Hand.".format(users[id]["left hand"][0].Name))
            elif users[id]["right hand"] != [] and users[id]["left hand"] != []:
              C0re.send_message(id, "You Glance Down And See {0} In Your Right Hand And {1} In Your Left Hand.".format(users[id]["right hand"][0].Name, users[id]["left hand"][0].Name))
# '*say' command
        elif gak.lower() in Ess["say change"]["sets"]:
          pa = params.lower()
          poa = po["user_actions"]
          empty = ""
          if pa == empty:
             Evm.send_message(id, "Please Use *say "+"STYLE ".upper()+"For More Information On "+"STYLE".upper()+" use /*say".title())
          if pa not in poa["say_options"] and pa != empty:
            if pa not in poa["plural_options"]:
               C0re.send_message(id, "that is not an option")
          if pa in poa["say_options"]:
             C0re.send_message(id, "thank you for choosing ".title()+pa.title())
             C0re.send_message(id, "please remember to use *say in the future to alter your options".title())
             users[id]["special speech"] = False
             users[id]["speech"] = pa
          elif pa in poa["plural_options"]:
             C0re.send_message(id, "thank you for choosing ".title()+pa.title())
             C0re.send_message(id, "please remember to use *say in the future to alter your options".title())
             users[id]["special speech"] = True
             users[id]["speech"] = pa
# 'inv' command (Object Initiated)
        elif gak.lower() in Ess["inventory"]["sets"]:
            name = users[id]["name"].title()
            # send a message to user with the inventory
            if users[id]["inventory"] == []:
             C0re.send_message(id, "Sorry {0} Your Inventory Is Empty".format(name))
            else:
             inventory_list = []
             for i in users[id]["inventory"]:
              inventory_list.append(i.Name)
              real_inventory_list = '%s' % ", ".join(inventory_list)
             C0re.send_message(id, "{0} Your Inventory Consists Of:> ~>{1}<~".format(name, real_inventory_list))
# 'stand' command
        elif gak.lower() == "stand" and params == "":
            if users[id]["userdown"] == True:
             C0re.send_message(id, "You Stand Back Up.")
             users[id]["userdown"] = False
             users[id]["standing"] = True
             playershere = []
             for pid,pl in users.items():
                    # if user is in the same room and isn't the user sending the command
                if users[pid]["room"] == users[id]["room"] and pid!=id:
                        # send them a message telling them that the user searched their pockets
                 C0re.send_message(pid, "{0} Stands Up.".format(users[id]["name"].title()) )
            elif users[id]["userdown"] == False:
             C0re.send_message(id, "You Are Already Standing")

# 'say' command
        elif gak.lower() in Ess["says"]["sets"]:
            name = users[id]["name"]
            nameTitle = name.title()
            speech = users[id]["speech"]
            speechTitle = speech.title()
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
              if users[id]["special speech"] == False:
                    # send them a message telling them what the user said
               C0re.send_message(pid, nameTitle + " {0}s, \"{1}\"".format(users[id]["speech"], params))
              elif users[id]["special speech"] == True:
               C0re.send_message(pid, nameTitle+" "+speechTitle+" And Says, \"{0}\"".format(params))
# 'wave' command
        elif gak == "wave":     
            # go through every user in the game
            C0re.send_message(id,'You Wave.')
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"] and users[pid]["name"] != users[id]["name"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"%s waves" % (users[id]["name"]))

# 'snort' command
        elif gak.lower() == "snort":     
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"{0} snorts".format(users[id]["name"]))

# 'shake' command
        elif gak == "shake":
         pa = params.lower()
         pa_sub = pa.split(' ')
         try:
          if pa_sub[0] == 'fist':
           # go through every user in the game
           for pid,pl in users.items():
           # if they're in the same room as the user
            if users[pid]["room"] == users[id]["room"]:
            # send them a message telling them what the user did
             C0re.send_message(pid,"%s Shakes Thier Fist." % (users[id]["name"]))
         except Exception as e:
          if 'list index' in e:
           C0re.send_message(id, 'Shake What?')
          else:
           C0re.send_message(id, str(e))
# 'cough' command
        elif gak == "cough":     
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"%s coughs" % (users[id]["name"]))
# 'sigh' command
        elif gak == "sigh":     
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"%s sighs" % (users[id]["name"]))
# 'giggle' command
        elif gak == "giggle":     
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"%s giggles" % (users[id]["name"]))


# 'emote' command
        elif gak == "emote":
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
             if users[pid]["room"] == users[id]["room"]:
                    # send them a message telling them what the user did
              C0re.send_message(pid,"%s %s" % (users[id]["name"],params))
# 'touch' command
        elif gak == "touch":
            # store the user's current room
            rm = rooms[users[id]["room"]]
            # stores params and checks to see if applicable
            rx = params.lower()+users[id]["roomid"]
            if rx not in rm["objects"] and wi:
             rx = params.lower() 
             for pid,pl in users.items():
              rx = params.lower()      # if user is in the same room and isn't the user sending the command
              if users[pid]["room"] == users[id]["room"] and pid!=id:
               if rx == users[pid]["name"] and rx != users[id]["name"]:
                  C0re.send_message(id, "You Reach Out And Touch %s" % rx.title())
                  C0re.send_message(pid, "%s Reaches out and touches you." % users[id]["name"].title())
               elif rx != users[pid]["name"] or rx != users[id]["name"]:
                   C0re.send_message(id, "I Cannot Find Who You Are Referring To.")
              elif users[pid]["room"] == users[id]["room"] and rx == users[id]["name"]:
                C0re.send_message(id, "You Touch Yourself... That's A Little Creepy...")
            elif rx in rm["objects"] and wi:
              si = wi[rx]
              C0re.send_message(id, si["touchdesc"])
              for pid,pl in users.items():
                    # if user is in the same room and isn't the user sending the command
               if users[pid]["room"] == users[id]["room"] and pid!=id:
                 if rx in rm["objects"] and wi:
                   si = wi[rx]
                   C0re.send_message(pid, si["othertouchdesc"].format(users[id]["name"]))
# 'look' command
        elif gak == "look":
            # store the user's current room
            rm = rooms[users[id]["room"]]
            # stores params and checks to see if applicable
            rx = params.lower()+users[id]["roomid"]
            pa = params.lower()
            name = users[id]['name']
            if pa == name.lower():
             C0re.send_message(id, str(users[id]))
            if rx not in rm["objects"] and wi:
             rx = params.lower()  
             C0re.send_message(id, "I Cannot Find {0}".format(rx) )
            elif rx in rm["objects"] and wi:
             si = wi[rx]
             C0re.send_message(id, si["shortdesc"])
                # go through all the users in the game
            for pid,pl in users.items():
                    # if user is in the same room and isn't the user sending the command
             if users[pid]["room"] == users[id]["room"] and pid!=id:
                 if rx in rm["objects"] and wi:
                   si = wi[rx]
                        # send them a message telling them that the user searched their pockets
                   C0re.send_message(pid, si["othershortdesc"].format(users[id]["name"]) )
# 'poke' command
        elif gak == "poke":
            # store the user's current room
            rm = rooms[users[id]["room"]]
            # stores params and checks to see if applicable
            rx = params.lower()+users[id]["room id"]
            if rx not in rm["objects"] and wi:
             rx = params.lower()  
             C0re.send_message(id, "I Cannot Find {0}".format(rx) )
            elif rx in rm["objects"] and wi:
             si = wi[rx]
             C0re.send_message(id, si["pokedesc"])       
                # go through all the users in the game
            for pid,pl in users.items():
                    # if user is in the same room and isn't the user sending the command
             if users[pid]["room"] == users[id]["room"] and pid!=id:
                 if rx in rm["objects"] and wi:
                   si = wi[rx]     
                        # send them a message telling them that the user searched their pockets
                   C0re.send_message(pid, si["otherpokedesc"].format(users[id]["name"]))
# 'read' command         
        elif gak == "read":
            # store the user's current room
            rm = rooms[users[id]["room"]]
            # stores params and checks to see if applicable
            pa = params.lower()
            rx = params.lower()+users[id]["room id"]
            # Check false first.
            if rx not in rm["objects"] and wi:
             rx = params.lower()  
             C0re.send_message(id, "I Cannot Find {0}".format(rx))
            elif rx in rm["objects"] and wi:
             si = wi[rx]
             C0re.send_message(id, si["readdesc"])
# 'area' command
        elif gak == "area":
            # store the user's current room
            rm = rooms[users[id].Room]
            # send the user back the description of their current room
            usershere = []
            # go through every user in the game
            for pid,pl in users.items():
                # if they're in the same room as the user
                if users[pid].Room == users[id].Room:
                    # add their name to the list
                    usershere.append(users[pid].Name)
            # send user a message containing the list of users in the room
            C0re.send_message(id, Eresp['E_Notice_Current_Location'].format(users[id].Room))
            C0re.send_message(id, Eresp['E_Notice_Current_Room_Id'].format(users[id].RoomID))
            C0re.send_message(id, Eresp['E_Notice_Open_Room_Format'].format(rm["description"]))
            C0re.send_message(id, Eresp['E_Notice_Also_Here']+"%s" % ", ".join(usershere).title())
            C0re.send_message(id, Eresp['E_Notice_Visible_Exits']+"%s" % ", ".join(rm["exits"]).title())
# 'go' command
        elif gak == "go":
            name = users[id]["name"]
            nameTitle = name.title()
            move = users[id]["move"]
            # store the exit name
            ex = params
            ext = ex.title()
            # store the user's current room & newly added id
            rm = rooms[users[id]["room"]]
            # if the specified exit is found in the room's exits list)
            if ex in rm["exits"]:
                # go through all the users in the game
                for pid,pl in users.items():
                    # if user is in the same room and isn't the user sending the command
                    if users[pid]["room"] == users[id]["room"] and pid!=id:
                        # send them a message telling them that the user left the room
                        C0re.send_message(pid,nameTitle+" "+move+"ed Away via: "+ext.format())
                # update the user's current room to the one the exit leads to and update ID
                users[id]["room"] = rm["exits"][ex]
                rm = rooms[users[id]["room"]]
                users[id]["room id"] = rm["room id"]
                current = worldRooms[users[id]["room"]]
                # go through all the users in the game
                for pid,pl in users.items():
                    # if user is in the same (new) room and isn't the user sending the command
                    if users[pid]["room"] == users[id]["room"] and pid!=id:
                        # send them a message telling them that the user entered the room
                        C0re.send_message(pid,nameTitle+" "+move+"'s into the area from the "+ext.format())
                #build usershere
                usershere = []
                # go through every user in the game
                for pid,pl in users.items():
                # if they're in the same room as the user
                 if users[pid]["room"] == users[id]["room"]:
                    # add their name to the list
                  usershere.append(users[pid]["name"])
                # send the user a message telling them where they are now
                roomti = users[id]["room"]
                roomtitle = roomti.title()
                C0re.send_message(id,nameTitle+" "+move+"ed"+" :"+roomtitle.format())
                C0re.send_message(id, Eresp['E_Notice_Have_Entered'].format(users[id]["room"]))
                C0re.send_message(id, Eresp['E_Notice_Current_Room_Id'].format(users[id]["room id"]))
                C0re.send_message(id, Eresp['E_Notice_Open_Room_Format'].format(rm["description"]))
                C0re.send_message(id, Eresp['E_Notice_Also_Here']+"%s" % ", ".join(usershere).title())
                C0re.send_message(id, Eresp['E_Notice_Visible_Exits']+"%s" % ", ".join(rm["exits"]).title())
            # the specified exit wasn't found in the current room
            else:
                # send back an 'unknown exit' message
                Evm.send_message(id, "Unknown exit '%s'" % ex)
        # 'exit' command
        elif gak in Ess["exit"]["sets"]:
            dummy = users[id]["name"]
            # send message to user that socket is being exited
            C0re.send_message(id, Vresp['Viv_Exit_Response_0'].format(users[id]['name']))
            C0re.send_message(id, Vresp['Viv_Exit_Response_1'])
            del(users[id])
            for pid,pl in users.items():
             C0re.send_message(pid,Eresp['E_Notice_Quit'].format(dummy.title()))

        # some other, bullshit command
        else:
            gak = gak.upper()
            # send back an 'unknown command' message
            C0re.send_message(id, "I'm Sorry {0} {1} Is A Unknown/Broken Syntax. If You Feel This Might Be A Error Please CONTACT The Devs For Support.".format(users[id].Name,gak))
