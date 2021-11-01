
#THIS IS THE GENESIS ROOMS SECTION ALL STABLE ROOM DATA TO BE ALTERED/ADDED MUST BE HANDLED HERE
#Paths are not unique between rooms to be able to enforce locked or closed features per destination pair
# Uses PathObjects\CorePathwayObjects.py For Pathway Association (Allows Open/Closed/Locked/Keys/Guarded)
#Exit(starting room)X(ending room) = TypeOfPath()

from .PathObjects.CorePathwayObjects import *
#@ Dev: Location Exits Need To Be Handled In self.Locations [LOCATION0,LOCATION2] (for i in self: if not current room in engine)
#@ Dev: Location Exits Need self.Paths[LOCATION#] = NEW_ID (For Player & Server Update)

LocationMap = dict() # Assign The Rooms A Dataset (Dictionary)

######### Room Stencil ############
#LocationMap['[ROOM LABEL]'] = dict() # Create A Dataset For Current Room
#LocationMap['[ROOM LABEL]']['Description'] = '[Room Description Here]' # (String) Room Description Including Visible Items
#LocationMap['[ROOM LABEL]']['ID'] = 0,-0 # (Int) Room Number Is Here
#LocationMap['[ROOM LABEL]']['Critters Allowed'] = True/False # (Boolean) Are Critters Allowed Here?
#LocationMap['[ROOM LABEL]']['Private'] = True/False # (Boolean) Is This Room Private?
#LocationMap['[ROOM LABEL]']['Shop'] = True/False # (Boolean) Is There A Shop Here?
#LocationMap['[ROOM LABEL]']['Special Shop'] = True/False # (Boolean) Is There A Special Shop Here?
#LocationMap['[ROOM LABEL]']['Special Shop Requirements'] = {'Guild': 'Trader'} # (Dictionary) Special Shop Requirements?
#LocationMap['[ROOM LABEL]']['Hidden Exits'] = [VARIABLE,VARIABLE] # (List) Hidden Exit Variable List (Variables Needed For Shared Objects)
#LocationMap['[ROOM LABEL]']['Exits'] = [VARIABLE,VARIABLE] # (List) Exit Variable List (Variables Needed For Shared Objects)

###################################
##########Shared Exits Below########
Exit0x0 = GlimmeringDoor() # Death Room => Closest Spawn
Exit1x2 = IronDoor() # Skryptek Tavern Guest Room => Skryptek Tavern Hallway
Exit1x6 = RosewoodWindow() # Skryptek Tavern, Guest Room => Skryptek Tavern, Window Ledge
Exit2x3 = RosewoodStairway() # Skryptek Tavern Hallway => Skryptek Tavern Common Room
Exit3x4 = RosewoodDoor() # SKryptek Tavern Hallway => Rantil Balinic Avenue
Exit4x5 = Alley() # Rentil Balinic Avenue => Skryptek Tavern, Back Alley


######### Room [0] [Dead] ################
LocationMap['[Death Room]'] = dict()
LocationMap['[Death Room]']['Description'] = '[This Dark Chamber Is Filled With Nothing Except Moving Shadows.\n\r Every Time A Shadow Whisps Across The Forboding Walls A Shriek Or Wail Of Unknown Location Or Orgin Follows.]'
LocationMap['[Death Room]']['ID'] = '0'
LocationMap['[Death Room]']['Critters Allowed'] = []
LocationMap['[Death Room]']['Private'] = False
LocationMap['[Death Room]']['Shop'] = False
LocationMap['[Death Room]']['Special Shop'] = False
LocationMap['[Death Room]']['Special Shop Requirements'] = None
LocationMap['[Death Room]']['Hidden Exits'] = [Exit0x0]
LocationMap['[Death Room]']['Exits'] = []

######### Room [1] [Skryptek Tavern, Guest Room] ################
LocationMap['[Skryptek Tavern, Guest Room]'] = dict()
LocationMap['[Skryptek Tavern, Guest Room]']['Description'] = '[A cozy tavern room. The room seems to have been quickly crafted with a bed a cracked wooden chair next to a makeshift vanity atopped with a crooked mirror. You also see a sign.]'
LocationMap['[Skryptek Tavern, Guest Room]']['ID'] = '1'
LocationMap['[Skryptek Tavern, Guest Room]']['Critters Allowed'] = []
LocationMap['[Skryptek Tavern, Guest Room]']['Private'] = False
LocationMap['[Skryptek Tavern, Guest Room]']['Shop'] = False
LocationMap['[Skryptek Tavern, Guest Room]']['Special Shop'] = False
LocationMap['[Skryptek Tavern, Guest Room]']['Special Shop Requirements'] = None
LocationMap['[Skryptek Tavern, Guest Room]']['Hidden Exits'] = []
LocationMap['[Skryptek Tavern, Guest Room]']['Exits'] = [Exit1x2,Exit1x6]
######### Room [2] [Skryptek Tavern, Hallway] ################
LocationMap['[Skryptek Tavern, Hallway]'] = dict()
LocationMap['[Skryptek Tavern, Hallway]']['Description'] = '[Outside a tavern room in a dimly lit hallway. The only thing visible besides the stairs is a poorly replicated painting of a flying hog.]'
LocationMap['[Skryptek Tavern, Hallway]']['ID'] = '2'
LocationMap['[Skryptek Tavern, Hallway]']['Critters Allowed'] = []
LocationMap['[Skryptek Tavern, Hallway]']['Private'] = False
LocationMap['[Skryptek Tavern, Hallway]']['Shop'] = False
LocationMap['[Skryptek Tavern, Hallway]']['Special Shop'] = False
LocationMap['[Skryptek Tavern, Hallway]']['Special Shop Requirements'] = None
LocationMap['[Skryptek Tavern, Hallway]']['Hidden Exits'] = []
LocationMap['[Skryptek Tavern, Hallway]']['Exits'] = [Exit1x2,Exit2x3]
######### Room [3] [Skryptek Tavern, Common Room] ################
LocationMap['[Skryptek Tavern, Common Room]'] = dict()
LocationMap['[Skryptek Tavern, Common Room]']['Description'] = '[A large common room filled with laughter, noises, smells, and involintary tastes that can\'t quite be described. You also see a red table, a blue table, a green table, and a cracked stool sitting next to the handmade R\'ati skin menu.]'
LocationMap['[Skryptek Tavern, Common Room]']['ID'] = '3'
LocationMap['[Skryptek Tavern, Common Room]']['Critters Allowed'] = []
LocationMap['[Skryptek Tavern, Common Room]']['Private'] = False
LocationMap['[Skryptek Tavern, Common Room]']['Shop'] = False
LocationMap['[Skryptek Tavern, Common Room]']['Special Shop'] = False
LocationMap['[Skryptek Tavern, Common Room]']['Special Shop Requirements'] = None
LocationMap['[Skryptek Tavern, Common Room]']['Hidden Exits'] = []
LocationMap['[Skryptek Tavern, Common Room]']['Exits'] = [Exit2x3,Exit3x4]
######### Room [4] [Rentil, Balinic Avenue] ################
LocationMap['[Rentil, Balinic Avenue]'] = dict()
LocationMap['[Rentil, Balinic Avenue]']['Description'] = '[A crooked makeshift avenue built from aligning shops where the street is paved with a mixture of crushed rock and dirt. You also see a sign attached to a makeshift building that swings in the breeze.]'
LocationMap['[Rentil, Balinic Avenue]']['ID'] = '4'
LocationMap['[Rentil, Balinic Avenue]']['Critters Allowed'] = []
LocationMap['[Rentil, Balinic Avenue]']['Private'] = False
LocationMap['[Rentil, Balinic Avenue]']['Shop'] = False
LocationMap['[Rentil, Balinic Avenue]']['Special Shop'] = False
LocationMap['[Rentil, Balinic Avenue]']['Special Shop Requirements'] = None
LocationMap['[Rentil, Balinic Avenue]']['Hidden Exits'] = []
LocationMap['[Rentil, Balinic Avenue]']['Exits'] = [Exit3x4,Exit4x5]
######### Room [5] [Back Alley, Skryptek Tavern] ################
LocationMap['[Skryptek Tavern, Back Alley]'] = dict()
LocationMap['[Skryptek Tavern, Back Alley]']['Description'] = '[A dark and omnious alley. Something scurries in the darkness making even the coldest hearts stop to listen. You can only see a thin rope and a small opening.]'
LocationMap['[Skryptek Tavern, Back Alley]']['ID'] = '5'
LocationMap['[Skryptek Tavern, Back Alley]']['Critters Allowed'] = []
LocationMap['[Skryptek Tavern, Back Alley]']['Private'] = False
LocationMap['[Skryptek Tavern, Back Alley]']['Shop'] = False
LocationMap['[Skryptek Tavern, Back Alley]']['Special Shop'] = False
LocationMap['[Skryptek Tavern, Back Alley]']['Special Shop Requirements'] = None
LocationMap['[Skryptek Tavern, Back Alley]']['Hidden Exits'] = []
LocationMap['[Skryptek Tavern, Back Alley]']['Exits'] = [Exit4x5]
######### Room [6] [Skryptek Tavern, Window Ledge] ################
LocationMap['[Skryptek Tavern, Window Ledge]'] = dict()
LocationMap['[Skryptek Tavern, Window Ledge]']['Description'] = '[Outside the guest room of Skryptek Tavern on a window\'s ledge. The wood appears sturdy and sound. You can only see a thin rope and Window.]'
LocationMap['[Skryptek Tavern, Window Ledge]']['ID'] = '6'
LocationMap['[Skryptek Tavern, Window Ledge]']['Critters Allowed'] = []
LocationMap['[Skryptek Tavern, Window Ledge]']['Private'] = False
LocationMap['[Skryptek Tavern, Window Ledge]']['Shop'] = False
LocationMap['[Skryptek Tavern, Window Ledge]']['Special Shop'] = False
LocationMap['[Skryptek Tavern, Window Ledge]']['Special Shop Requirements'] = None
LocationMap['[Skryptek Tavern, Window Ledge]']['Hidden Exits'] = []
LocationMap['[Skryptek Tavern, Window Ledge]']['Exits'] = [Exit1x6]

