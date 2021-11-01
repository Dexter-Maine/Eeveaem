from .Pathway import CorePathway

#@Dev: Don't Forget To Contract Some Passages So They
#@Dev: Must Be Called To Unlock / Lock


class GlimmeringDoor(CorePathway):
 def __init__(self):
  self.Name = 'Glimmering Door'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass
    
class IronDoor(CorePathway):
 def __init__(self):
  self.Name = 'Iron Door'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass


class RosewoodWindow(CorePathway):
 def __init__(self):
  self.Name = 'Rosewood Window'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass

class RosewoodStairway(CorePathway):
 def __init__(self):
  self.Name = 'Rosewood Stairway'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass

class RosewoodDoor(CorePathway):
 def __init__(self):
  self.Name = 'Rosewood Door'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass

class Alley(CorePathway):
 def __init__(self):
  self.Name = 'Alley'
  super().__init__(Name=self.Name,Open=False,Locked=True,Skill=1000,Key=None)

 def Open(self):
  self.Open = True

 def Close(self):
  self.Open = False

 def Lock(self):
  self.Locked = True

 def Unlock(self):
  self.Locked = False

 def Create_Key(self):
  pass

 def Label_Self(self):
  pass
