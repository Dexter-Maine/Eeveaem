
from .RoomObject import Room
from .LocationMapping import LocationMap


############ GENESIS ROOMS ONLY BELOW ##################
class DeathRoom(Room):
 def __init__(self):
  self.Name = '[Death Room]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class SkryptekTavernGuestRoom(Room):
 def __init__(self):
  self.Name = '[Skryptek Tavern, Guest Room]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class SkryptekTavernHallway(Room):
 def __init__(self):
  self.Name = '[Skryptek Tavern, Hallway]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class SkryptekTavernCommonRoom(Room):
 def __init__(self):
  self.Name = '[Skryptek Tavern, Common Room]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class RentilBalinicAvenue(Room):
 def __init__(self):
  self.Name = '[Rentil, Balinic Avenue]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class SkryptekTavernBackAlley(Room):
 def __init__(self):
  self.Name = '[Skryptek Tavern, Back Alley]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])

class SkryptekTavernWindowLedge(Room):
 def __init__(self):
  self.Name = '[Skryptek Tavern, Window Ledge]'
  super().__init__(Name=self.Name,Description=LocationMap[self.Name]['Description'],ID=LocationMap[self.Name]['ID'],NPCs=list(),PlayersHere=list(),
                   HiddenPlayers=list(),CrittersAllowed=LocationMap[self.Name]['Critters Allowed'],CrittersAlive=list(),
                   CrittersDead=list(),Private=LocationMap[self.Name]['Private'],Shop=LocationMap[self.Name]['Shop'],SpecialShop=LocationMap[self.Name]['Special Shop'],
                   SpecialShopRequirements=LocationMap[self.Name]['Special Shop Requirements'],Ground=list(),HiddenExits=LocationMap[self.Name]['Hidden Exits'],
                   Exits=LocationMap[self.Name]['Exits'])
