


# Giant Grass Snail
# Giant Leathered Snail
# Giant Horned Snail
# Giant Frozen Snail
# Giant Zombie Snail
# Giant Metalic Snail
# Giant NanoTech Snail

# Grass Serpent
# Leathered Serpent
# Horned Serpent
# Frozen Serpent
# Zombie Sperpent
# Metalic Serpent
# NanoTech Serpent
class Critter:
    def __init__(self, Name, MinHealth,MaxHealth, MinDefence, MaxDefence, MinAtk, MaxAtk, Inventory, Exp, Level, FireResist, ColdResist, ElectricResist, ToxinResist):
        self.Name = Name
        self.MinHealth = MinHealth
        self.MaxHealth = MaxHealth
        self.MinAtk = MinAtk
        self.MaxAtk = MaxAtk
        self.MinDefence = MinDefence
        self.MaxDefence = MaxDefence
        self.Inventory = Inventory
        self.Exp = Exp
        self.Level = Level
        self.FireResist = FireResist
        self.ColdResist = ColdResist
        self.ElectricResist = ElectricResist
        self.ToxinResist = ToxinResist


class MetalicSerpent(Character):
    def __init__(self):
        super().__init__(name="Metalic Serpent",MinAtk=1,MaxAtk=5, Level=1, FireResist=4
                         Hp=10,Defence=3,Inventory={'Drops': [], 'Parts': []},Exp=10,ElectricResist=0,ColdResist=2,ToxinResist=1)
    MaxHp = 1000
    MaxDefence = 1000
    levelUp = 20
