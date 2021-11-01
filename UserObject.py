from .UserObjectHealthMap import HealthMap
import random


########### BODY / RACE TYPES BELOW #####################################

class BodyPart:
 def __init__(self,Name,Description,Health,Bleeding,Scar,Tattoo,Piercing,Worn,Color,Has,Condition):
  self.Name = Name
  self.Description = Description
  self.Health = Health
  self.Bleeding = Bleeding
  self.Scar = Scar
  self.Tattoo = Tattoo
  self.Piercing = Piercing
  self.Worn = Worn
  self.Color = Color
  self.Has = Has
  self.Condition = Condition

 def _UpdateHealth(self):
  self.Condition = HealthMap[self.Health]

 def CheckHealth(self):
  if self.Has == True:
   self._UpdateHealth()
   return self.Condition
  else:
   return 'None'

class Thumb(object):
 def __init__(self):
  self.Size = random.randint(0,12)
  self.Worn = list()
  self.WornMax = 2

class Finger(object):
 def __init__(self):
  self.Size = random.randint(0,12)
  self.Worn = list()
  self.WornMax = 2  

##### Body Parts Below ######
#@Dev: Bleeding = [IsBleeding(bool),RateOfDamage(Int),PlayerAlerted(bool),BeenBleeding(float),BleedTime(float),Tended(bool),MaxBleedTime(float)]

class Skin(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Skin',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 0
class Skull(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Skull',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.WornMax = 1
class Nose(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Nose',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Eye(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Eye',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Cheek(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Cheek',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Chin(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Chin',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Mouth(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Mouth',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Open = False
  self.Held = []
  self.HeldMax = 1
  self.WornMax = 1
class Lip(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Lip',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Eyebrow(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Eyebrow',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 0

#### HAIR NEEDS SEPARATE CONDITION MODEL FOR MALE / FEMALE / STYLES
class Hair(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Hair',Health=None,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = 'Straight'
  self.WornMax = 100
class Neck(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Neck',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Chest(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Chest',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Back(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Back',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Stomach(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Stomach',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
  self.Held = []
  self.HeldMax = 3
class Waist(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Waist',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 2
class Hamstring(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Hamstring',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Knee(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Knee',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Shin(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Shin',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1

class Ankle(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Ankle',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1

  
class Foot(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Foot',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 6
class Shoulder(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Shoulder',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Bicep(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Bicep',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Elbow(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Elbow',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Forearm(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Forearm',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Wrist(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Wrist',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.WornMax = 1
class Hand(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Hand',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Held = []
  self.HeldMax = 1
  self.WornMax = 1
  self.Thumb = Thumb()
  self.Index = Finger()
  self.Middle = Finger()
  self.Ring = Finger()
  self.Pinky = Finger()
  
class Horn(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Horn',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Damage = 1
  self.WornMax = 1
class Wing(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Wing',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Damage = 1
  self.WornMax = 100
class Fang(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Fang',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Damage = 1
  self.WornMax = 1
class Tail(BodyPart):
 def __init__(self,n):
  super().__init__(Name=n,Description='Tail',Health=100,Bleeding=[False,0,False,0.0,60.0,False,60.0],
                   Scar=dict(),Tattoo=dict(),Piercing=list(),Worn=list(),Color=None,Has=True,Condition='')
  self.Condition = HealthMap[self.Health]
  self.Held = []
  self.HeldMax = 1
  self.Damage = 1
  self.WornMax = 2



class Body:
 def __init__(self,Race,Gender,Skin,Skull,Nose,RightEye,LeftEye,RightCheek,LeftCheek,Chin,Mouth,TopLip,BottomLip,
              RightEyebrow,LeftEyebrow,Hair,Neck,Chest,RightFang,
              Back,Stomach,Waist,RightHamstring,LeftHamstring,RightKnee,LeftKnee,RightShin,LeftShin,
              LeftAnkle,RightAnkle,RightFoot,LeftFoot,RightShoulder,LeftShoulder,LeftFang,
              RightBicep,LeftBicep,RightElbow,LeftElbow,RightForearm,LeftForearm,RightWrist,LeftWrist,
              RightHand,Tail,LeftWing,RightWing,LeftHorn,RightHorn,
              LeftHand):
  self.Race = Race
  self.Gender = Gender
  self.Skull = Skull
  self.Nose = Nose
  self.Skin = Skin
  self.RightEye = RightEye
  self.LeftEye = LeftEye
  self.RightCheek = RightCheek
  self.LeftCheek = LeftCheek
  self.Chin = Chin
  self.Mouth = Mouth
  self.TopLip = TopLip
  self.BottomLip = BottomLip
  self.RightEyebrow = RightEyebrow
  self.LeftEyebrow = LeftEyebrow
  self.Hair = Hair
  self.Neck = Neck
  self.Chest = Chest
  self.Back = Back
  self.Stomach = Stomach
  self.Waist = Waist
  self.RightHamstring = RightHamstring
  self.LeftHamstring = LeftHamstring
  self.RightKnee = RightKnee
  self.LeftKnee = LeftKnee
  self.RightShin = RightShin
  self.LeftShin = LeftShin
  self.RightAnkle = RightAnkle
  self.LeftAnkle = LeftAnkle
  self.RightFoot = RightFoot
  self.LeftFoot = LeftFoot
  self.RightShoulder = RightShoulder
  self.LeftShoulder = LeftShoulder
  self.RightBicep = RightBicep
  self.LeftBicep = LeftBicep
  self.RightElbow = RightElbow
  self.LeftElbow = LeftElbow
  self.RightForearm = RightForearm
  self.LeftForearm = LeftForearm
  self.RightWrist = RightWrist
  self.LeftWrist = LeftWrist
  self.RightHand = RightHand
  self.LeftHand = LeftHand
  self.Tail = Tail
  self.LeftWing = LeftWing
  self.RightWing = RightWing
  self.LeftHorn = LeftHorn
  self.RightHorn = RightHorn
  self.LeftFang = LeftFang
  self.RightFang = RightFang
  self.BodyPart = dict()
  self.BodyPart['List'] = [self.Skin,self.Skull,self.Nose,self.RightEye,self.LeftEye,self.RightCheek,self.LeftCheek,self.Chin,self.Mouth,self.TopLip,self.BottomLip,self.RightEyebrow,
                       self.LeftEyebrow,self.Hair,self.RightKnee,self.LeftKnee,self.RightShin,self.LeftShin,self.LeftAnkle,self.RightAnkle,self.RightFoot,self.LeftFoot,self.Neck,self.Chest,self.Back,self.Stomach,
                       self.Waist,self.RightHamstring,self.LeftHamstring,self.RightShoulder,self.LeftShoulder,self.LeftForearm,self.RightForearm,self.RightBicep,self.LeftBicep,
                       self.RightElbow,self.LeftElbow,self.RightWrist,self.LeftWrist,self.RightHand,self.LeftHand,self.Tail,self.LeftWing,self.RightWing,self.LeftHorn,self.RightHorn,
                       self.LeftFang,self.RightFang]
  self.BodyPart['Head'] = [self.Skull,self.Nose,self.RightEye,self.LeftEye,self.RightCheek,self.LeftCheek,self.Chin,self.Mouth,self.TopLip,self.BottomLip,self.RightEyebrow,self.LeftEyebrow]
  self.BodyPart['Neck'] = [self.Neck]
  self.BodyPart['Torso'] = [self.Chest,self.Back,self.Stomach,self.Waist]
  self.BodyPart['Left Arm'] = [self.LeftShoulder,self.RightBicep,self.LeftElbow,self.LeftForearm,self.LeftWrist,self.LeftHand]
  self.BodyPart['Right Arm'] = [self.RightShoulder,self.RightBicep,self.RightElbow,self.RightForearm,self.RightWrist,self.RightHand]
  
  self.ConditionPoints = 100
  self.OverAllCondition = HealthMap[self.ConditionPoints]

 def _UpdateOverallHealth(self):
  self.MockConditionPoints = 0
  self.HealthCounter = 0
  for Part in self.BodyPart['List']:
   if Part.Has == True:
    Part._UpdateHealth()
    if Part.Health != None:
     self.MockConditionPoints += Part.Health
     self.HealthCounter += 1
  self.ConditionPoints = self.MockConditionPoints // self.HealthCounter
  self.OverAllCondition = HealthMap[self.ConditionPoints]

class Human(Body):
 def __init__(self):
  super().__init__(Race='Human',Gender='Unknown',Skin=Skin('Skin'),Skull=Skull('Skull'),Nose=Nose('Nose'),RightEye=Eye('Right Eye'),LeftEye=Eye('Left Eye'),RightCheek=Cheek('Right Cheek'),LeftCheek=Cheek('Left Cheek'),
                   Chin=Chin('Chin'),Mouth=Mouth('Mouth'),TopLip=Lip('Top Lip'),BottomLip=Lip('Bottom Lip'),RightEyebrow=Eyebrow('Right Eyebrow'),LeftEyebrow=Eyebrow('Left Eyebrow'),Hair=Hair('Hair'),
                   Neck=Neck('Neck'),Chest=Chest('Chest'),Back=Back('Back'),Stomach=Stomach('Stomach'),Waist=Waist('Waist'),RightHamstring=Hamstring('Right Hamstring'),LeftHamstring=Hamstring('Left Hamstring'),
                   RightKnee=Knee('Right Knee'),LeftKnee=Knee('Left Knee'),RightShin=Shin('Right Shin'),LeftShin=Shin('Left Shin'),LeftAnkle=Ankle('Left Ankle'),RightAnkle=Ankle('Right Ankle'),RightFoot=Foot('Right Foot'),LeftFoot=Foot('Left Foot'),RightShoulder=Shoulder('Right Shoulder'),
                   LeftShoulder=Shoulder('Left Shoulder'),RightBicep=Bicep('Right Bicep'),LeftBicep=Bicep('Left Bicep'),RightElbow=Elbow('Right Elbow'),LeftElbow=Elbow('Left Elbow'),RightForearm=Forearm('Right Forearm'),
                   LeftForearm=Forearm('Left Forearm'),RightWrist=Wrist('Right Wrist'),LeftWrist=Wrist('Left Wrist'),RightHand=Hand('Right Hand'),LeftHand=Hand('Left Hand'),Tail=Tail('Tail'),LeftWing=Wing('Wing'),RightWing=Wing('Right Wing'),
                   LeftHorn=Horn('Left Horn'),RightHorn=Horn('Right Horn'),LeftFang=Fang('Left Fang'),RightFang=Fang('Right Fang'))
  
  self.MainHealth = 100
  self.Tail.Has = False
  self.LeftWing.Has = False
  self.RightWing.Has = False
  self.LeftFang.Has = False
  self.RightFang.Has = False
  self.LeftHorn.Has = False
  self.RightHorn.Has = False

 def CheckHealth(self,args='overall'):
  if args.title() == 'Overall':
   self._UpdateOverallHealth()
   return self.OverAllCondition
  elif args.title() in self.BodyPart:
   self.MockConditionPoints0 = 0
   self.HealthCounter0 = 0
   for Part in self.BodyPart[args.title()]:
    if Part.Has == True:
     Part._UpdateHealth()
     if Part.Health != None:
      self.MockConditionPoints0 += Part.Health
      self.HealthCounter0 += 1
   return HealthMap[self.MockConditionPoints0 // self.HealthCounter0]
  else:
   for Part in self.BodyPart['List']:
    if Part.Name == args.title():
     Part._UpdateHealth()
     return Part.Condition

  
################# SKILLS BELOW #########################################
class Skill:
 def __init__(self, Name,Level,Exp,Cap):
  self.Name = Name
  self.Level = Level
  self.Exp = Exp
  self.Cap = Cap
############## Athletic Skills #######################################
class Athletics(Skill):
 def __init__(self):
    super().__init__(Name='Athletics',Level=0,Exp=0,Cap=None)
class Climbing(Skill):
 def __init__(self):
    super().__init__(Name='Climbing',Level=0,Exp=0,Cap=None)
class Swimming(Skill):
 def __init__(self):
    super().__init__(Name='Swimming',Level=0,Exp=0,Cap=None)
class Wandering(Skill):
 def __init__(self):
    super().__init__(Name='Wandering',Level=0,Exp=0,Cap=None)

############## Offensive Combat Skills #######################################
class MeleeCombat(Skill):
 def __init__(self):
    super().__init__(Name='Melee Combat',Level=0,Exp=0,Cap=None)
class MissileCombat(Skill):
 def __init__(self):
    super().__init__(Name='Missile Combat',Level=0,Exp=0,Cap=None)
class Brawling(Skill):
 def __init__(self):
    super().__init__(Name='Brawling',Level=0,Exp=0,Cap=None)
class HeavyThrown(Skill):
 def __init__(self):
    super().__init__(Name='Heavy Thrown',Level=0,Exp=0,Cap=None)
class LightThrown(Skill):
 def __init__(self):
    super().__init__(Name='Light Thrown',Level=0,Exp=0,Cap=None)
class Knives(Skill):
 def __init__(self):
    super().__init__(Name='Knives',Level=0,Exp=0,Cap=None)
class Staves(Skill):
 def __init__(self):
    super().__init__(Name='Staves',Level=0,Exp=0,Cap=None)
class Bows(Skill):
 def __init__(self):
    super().__init__(Name='Bows',Level=0,Exp=0,Cap=None)
class Crossbows(Skill):
 def __init__(self):
    super().__init__(Name='Crossbows',Level=0,Exp=0,Cap=None)
class Slings(Skill):
 def __init__(self):
    super().__init__(Name='Slings',Level=0,Exp=0,Cap=None)

############## Offensive Combat Skills #######################################
class Shields(Skill):
 def __init__(self):
    super().__init__(Name='Shields',Level=0,Exp=0,Cap=None)
class LeatherArmor(Skill):
 def __init__(self):
    super().__init__(Name='Leather Armor',Level=0,Exp=0,Cap=None)
class PaperArmor(Skill):
 def __init__(self):
    super().__init__(Name='Paper Armor',Level=0,Exp=0,Cap=None)
class BoneArmor(Skill):
 def __init__(self):
    super().__init__(Name='Bone Armor',Level=0,Exp=0,Cap=None)
class ChainArmor(Skill):
 def __init__(self):
    super().__init__(Name='Chain Armor',Level=0,Exp=0,Cap=None)
class Evasion(Skill):
 def __init__(self):
    super().__init__(Name='Evasion',Level=0,Exp=0,Cap=None)
class ParryAbility(Skill):
 def __init__(self):
    super().__init__(Name='Parry Ability',Level=0,Exp=0,Cap=None)

############## Survival Skills #######################################
class Stealth(Skill):
 def __init__(self):
    super().__init__(Name='Stealth',Level=0,Exp=0,Cap=None)
class Sight(Skill):
 def __init__(self):
    super().__init__(Name='Sight',Level=0,Exp=0,Cap=None)
class Hearing(Skill):
 def __init__(self):
    super().__init__(Name='Hearing',Level=0,Exp=0,Cap=None)
class AnimalLore(Skill):
 def __init__(self):
    super().__init__(Name='Animal Lore',Level=0,Exp=0,Cap=None)
class Thievery(Skill):
 def __init__(self):
    super().__init__(Name='Thievery',Level=0,Exp=0,Cap=None)
class Locksmithing(Skill):
 def __init__(self):
    super().__init__(Name='Locksmithing',Level=0,Exp=0,Cap=None)
class Foraging(Skill):
 def __init__(self):
    super().__init__(Name='Foraging',Level=0,Exp=0,Cap=None)
class MetalWorking(Skill):
 def __init__(self):
    super().__init__(Name='Metal Working',Level=0,Exp=0,Cap=None)
class Carpentry(Skill):
 def __init__(self):
    super().__init__(Name='Carpentry',Level=0,Exp=0,Cap=None)

class SkillTree:
 def __init__(self,Name):
  self.Name = Name

class NormalSkillTree(SkillTree):
 def __init__(self,Name='Normal'):
  self.Skills = dict()
  self.Skills['Survival'] = dict()
  self.Skills['Survival']['Sight'] = Sight()
  self.Skills['Survival']['Stealth'] = Stealth()

############# WALLETS BELOW ##################################
              
class Wallet:
 def __init__(self, Name, Address,PrivateKey, Balance, TxHistory, TxCount):
   self.Name = Name
   self.Address = Address
   self.PrivateKey = PrivateKey
   self.Balance = Balance
   self.TxHistory = TxHistory
   self.TxCount = TxCount

class BitcoinWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Bitcoin',Address='',PrivateKey='',Balance=0,TxHistory=dict(),TxCount=0)

class EthereumWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Ethereum',Address='',PrivateKey='',Balance=0,TxHistory=dict(),TxCount=0)
class KoiniumWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Koinium',Address='',PrivateKey='',Balance=0,TxHistory=dict(),TxCount=0)
class KrypitsWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Krypits',Address='',PrivateKey='',Balance=0,TxHistory=dict(),TxCount=0)
class EthrealTokenWallet(Wallet):
 def __init__(self):
  super().__init__(Name='Ethreal Token',Address='',PrivateKey='',Balance=0,TxHistory=dict(),TxCount=0)



############# USER CLASSES / TYPES BELOW ##########################
class User:
 def __init__(self, Name,Body,Type,Speech,SpecialSpeech,C0reTime,SkillTree,Notes,Wallets,Inventory,Guild,Alive,Started,Room,RoomID,DeathAlert,RealmTime,Locked,UserID):
  self.Name = Name
  self.UserID = UserID
  self.Body = Body
  self.Type = Type
  self.Speech = Speech
  self.SpecialSpeech = SpecialSpeech
  self.C0reTime = C0reTime
  self.SkillTree = SkillTree
  self.Notes = Notes
  self.Wallets = Wallets
  self.Inventory = Inventory
  self.Guild = Guild
  self.Alive = Alive
  self.Started = Started
  self.Room = Room
  self.RoomID = RoomID
  self.DeathAlert = DeathAlert
  self.RealmTime = RealmTime
  self.Locked = Locked
  self.Alerts = dict()
  self.Alerts['List'] = ['New Users','Hiding Players','Realm Deaths','Invasion Warnings','Market Tickers']
  self.Alerts['New Users'] = True
  self.Alerts['Hiding Players'] = True
  self.Alerts['Realm Deaths'] = True
  self.Alerts['Invasion Warnings'] = True
  self.Alerts['Market Tickers'] = True


class Guest(User):
 def __init__(self):
  super().__init__(Name=None,Body=Human(),Type=dict(),Speech='Say',SpecialSpeech=False,C0reTime=0,SkillTree=NormalSkillTree(),UserID=None,
                      Notes=dict(),Wallets=dict(),Inventory=[],Guild='Commoner',
                      Alive=True,Started=False,Room='[Skryptic Tavern, Guest Room]',
                      RoomID='1',DeathAlert=False,RealmTime=0.0,Locked=False)
  self.Type['Number'] = '3'
  self.Type['id'] = 'Guest'
  self.Wallets['BitcoinWallet'] = BitcoinWallet()
  self.Wallets['EthereumWallet'] = EthereumWallet()
  self.Wallets['KoiniumWallet'] = KoiniumWallet()
  self.Wallets['KrypitsWallet'] = KrypitsWallet()
  self.Wallets['EthrealWallet'] = EthrealTokenWallet()
  self.Description = {'Name': self.Name,'Type': self.Type['id'],'Guild':self.Guild,'Gender':self.Body.Gender,'Race': self.Body.Race}

 def _ProvideDescription(self):
  return '''{0} {1} {2} {3}. {0}, Is A {4} Of The CryptoVerse.
They Are Wearing'''.format(self.Name,self.Body.Gender,self.Guild,self.Body.Race,self.Type['id'])
