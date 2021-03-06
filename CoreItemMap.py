import random
############ Plate ################################
ItemMap = dict()
ItemMap['Plate'] = dict()
ItemMap['Plate']['MinWeight'] = 0
ItemMap['Plate']['Color'] = ['blue','green','pink','purple','red','orange','black','yellow','brown','emerald','ruby','tangerine','opal','rhinestone']
ItemMap['Plate']['FrontDescription'] = 'a {} plate'
ItemMap['Plate']['SkillTree'] = ['light thrown']
ItemMap['Plate']['BackDescription'] = 'back of a {} plate that has something written on it.'
ItemMap['Plate']['MaxWeight'] = 3
ItemMap['Plate']['MaterialType'] = ['clay','stone','aluminum']
ItemMap['Plate']['ItemType'] = ['Food', 'Thrown']
ItemMap['Plate']['Storage'] = [True,[]]
ItemMap['Plate']['Emotes'] = dict()
ItemMap['Plate']['Emotes']['read'] = '[Eeveaem 2018]'
ItemMap['Plate']['Level'] = 0
ItemMap['Plate']['MinAtk'] = 0
ItemMap['Plate']['MinDurability'] = 1
ItemMap['Plate']['MaxAtk'] = 3
ItemMap['Plate']['MinSocketCount'] = 0
ItemMap['Plate']['MaxSocketCount'] = 2
ItemMap['Plate']['SocketList'] = []
ItemMap['Plate']['MaxDurability'] = 100
ItemMap['Plate']['MinDefence'] = 0
ItemMap['Plate']['MaxDefence'] = 0
ItemMap['Plate']['Worn'] = False
ItemMap['Plate']['Range'] = 3
ItemMap['Plate']['MinBonusExp'] = 0
ItemMap['Plate']['MaxBonusExp'] = 3
ItemMap['Plate']['MinFireAtk'] = 0
ItemMap['Plate']['MaxFireAtk'] = 3
ItemMap['Plate']['MinElectricAtk'] = 0
ItemMap['Plate']['MaxElectricAtk'] = 3
ItemMap['Plate']['MinColdAtk'] = 0
ItemMap['Plate']['MaxColdAtk'] = 3
ItemMap['Plate']['MinToxinAtk'] = 0
ItemMap['Plate']['MaxToxinAtk'] = 3
ItemMap['Plate']['ToxinType'] = ['poison','sleep','paralyze']
ItemMap['Plate']['Tainted'] = [True,False]
ItemMap['Plate']['Turned'] = [True,False]
ItemMap['Plate']['Magical'] = [True,False]
ItemMap['Plate']['MagicAttributes'] = [{'strength': random.randint(0,5), 'intelligence': random.randint(0,5),'wisdom': random.randint(0,5),
                                        'charisma': random.randint(0,5),'emotion': random.randint(0,5)}]
ItemMap['Plate']['Fixed'] = False

############## Wooden Wall #######################
ItemMap['Wooden Wall'] = dict()
ItemMap['Wooden Wall']['MinWeight'] = 0
ItemMap['Wooden Wall']['Color'] = ['blue','green','pink','purple','red','orange','black','yellow','brown','emerald','ruby','tangerine','opal','rhinestone']
ItemMap['Wooden Wall']['FrontDescription'] = 'A {} Painted Wooden Wall.'
ItemMap['Wooden Wall']['SkillTree'] = ['climbing']
ItemMap['Wooden Wall']['BackDescription'] = 'There Is No Way To See Behind The {} Painted Wooden Wall.'
ItemMap['Wooden Wall']['MaxWeight'] = 3
ItemMap['Wooden Wall']['MaterialType'] = ['clay','stone','aluminum']
ItemMap['Wooden Wall']['ItemType'] = ['Food', 'Thrown']
ItemMap['Wooden Wall']['Storage'] = [True,[]]
ItemMap['Wooden Wall']['Emotes'] = dict()
ItemMap['Wooden Wall']['Emotes']['read'] = ['There Is Nothing To Read On The Wooden Wall.','Fails To Read Anything On The Wooden Wall.']
ItemMap['Wooden Wall']['Level'] = 2500
ItemMap['Wooden Wall']['MinAtk'] = 0
ItemMap['Wooden Wall']['MinDurability'] = 1000000000000000000000000000000
ItemMap['Wooden Wall']['MaxAtk'] = 0
ItemMap['Wooden Wall']['MinSocketCount'] = 0
ItemMap['Wooden Wall']['MaxSocketCount'] = 10
ItemMap['Wooden Wall']['SocketList'] = []
ItemMap['Wooden Wall']['MaxDurability'] = 1000000000000000000000000000000
ItemMap['Wooden Wall']['MinDefence'] = 0
ItemMap['Wooden Wall']['MaxDefence'] = 0
ItemMap['Wooden Wall']['Worn'] = False
ItemMap['Wooden Wall']['Range'] = 0
ItemMap['Wooden Wall']['MinBonusExp'] = 0
ItemMap['Wooden Wall']['MaxBonusExp'] = 0
ItemMap['Wooden Wall']['MinFireAtk'] = 0
ItemMap['Wooden Wall']['MaxFireAtk'] = 0
ItemMap['Wooden Wall']['MinElectricAtk'] = 0
ItemMap['Wooden Wall']['MaxElectricAtk'] = 0
ItemMap['Wooden Wall']['MinColdAtk'] = 0
ItemMap['Wooden Wall']['MaxColdAtk'] = 0
ItemMap['Wooden Wall']['MinToxinAtk'] = 0
ItemMap['Wooden Wall']['MaxToxinAtk'] = 0
ItemMap['Wooden Wall']['ToxinType'] = ['poison','sleep','paralyze']
ItemMap['Wooden Wall']['Tainted'] = [True,False]
ItemMap['Wooden Wall']['Turned'] = [True,False]
ItemMap['Wooden Wall']['Magical'] = [True,False]
ItemMap['Wooden Wall']['MagicAttributes'] = [{'strength': random.randint(0,5), 'intelligence': random.randint(0,5),'wisdom': random.randint(0,5),
                                        'charisma': random.randint(0,5),'emotion': random.randint(0,5)}]
ItemMap['Plate']['Fixed'] = False
