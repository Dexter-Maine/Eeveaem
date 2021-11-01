class Room(object):
 def __init__(self,Name,Description,ID,NPCs,PlayersHere,HiddenPlayers,CrittersAllowed,CrittersAlive,CrittersDead,
              Private,Shop,SpecialShop,SpecialShopRequirements,Ground,HiddenExits,Exits):
  self.Name = Name
  self.Description = Description
  self.ID = ID
  self.NPCs = NPCs
  self.PlayersHere = PlayersHere
  self.HiddenPlayers = HiddenPlayers
  self.CrittersAllowed = CrittersAllowed
  self.CrittersAlive = CrittersAlive
  self.CrittersDead = CrittersDead
  self.Private = Private
  self.Shop = Shop
  self.SpecialShop = SpecialShop
  self.SpecialShopRequirements = SpecialShopRequirements
  self.Ground = Ground
  self.HiddenExits = HiddenExits
  self.Exits = Exits
