from .Locations.Genesis.GenZero import *

class World:
 def __init__(self):
  self.Room = dict()
  self.Room['0'] = DeathRoom()
  self.Room['1'] = SkryptekTavernGuestRoom()
  self.Room['2'] = SkryptekTavernHallway()
  self.Room['3'] = SkryptekTavernCommonRoom()
  self.Room['4'] = RentilBalinicAvenue()
  self.Room['5'] = SkryptekTavernGuestRoom()
  self.Room['6'] = SkryptekTavernGuestRoom()

