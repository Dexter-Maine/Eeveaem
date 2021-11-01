#python convert 3.1 Skrypt

import shlex



def map():
    print(' _____________________________ ')
    print('|         |         |         |')
    print('|         |         |         |')
    print('| Room B  = Room D  =  Room E |')
    print('|   Jeff  |  Sword  |  Alien  |')
    print('|         |         |         |')
    print('|____||___|____||___|____\____|')
    print('|         |         |         |')
    print('|         |         |         |')
    print('|  Skrypt | Skoty   |  Room F |')
    print('| Room A  = Room C  =  Chest  |')
    print('|         |         |         |')
    print('|_________|_________|_________|')



#The Room class
class Room(object):
    def __init__(self, location,objectsinRoom, containersinRooom, wallsinRoom,peopleinRoom,hasDoor,
    description,descriptionpeople,descriptiondirections):

        self.location = location
        self.objectsinRoom = objectsinRoom
        self.containersinRooom = containersinRooom
        self.wallsinRoom = wallsinRoom
        self.peopleinRoom = peopleinRoom
        self.hasDoor = hasDoor
        self.description = description
        self.descriptionpeople = descriptionpeople
        self.descriptiondirections = descriptiondirections


#Returns what will be printed about the Room you're in right meow
    def display_Room(self):
        stri = (' ')

        itemprint = []
        contprint = []
        peopprint = []

        for item in self.objectsinRoom:
            if item.islocked == True:
                pass
            else:
                if item.incontainer == True:
                    itemprint.append('A ' + item.name + ' is in the ' + item.containername + '. ')
                else:
                    itemprint.append('A ' + item.name + ' is here.')
        stritem = stri.join(itemprint)

        for cont in self.containersinRooom:
            contprint.append(cont.text)
        strcont = stri.join(contprint)

        for people in self.peopleinRoom:
            if people.state == 'alive':
                peopprint.append(' ' +  people.name + ' is here. ')
            elif people.state != 'alive':
                peopprint.append(' ' +  people.name + "'s dead body is here. ")
        strpeop = stri.join(peopprint)

        return self.description + strpeop + strcont + stritem

#The class for NPCs
class People(object):
    def __init__(self,location,name,text,description,state):
        self.location = location
        self.name = name
        self.text = text
        self.description = description
        self.state = state

#Pretty much useless
    def printText(self):
        print(self.text)


#Moves the player to another room
    def go(self,location,Decision):

        newlocation = list(self.location)


        if Decision == 'go north' or Decision == 'go n' or Decision == 'n':
            newlocation[1] += 1
            test = world.get(tuple(newlocation))
            if test == None:
                print('You cannot go there')
            else:
                if test.wallsinRoom[2] == False and (test.hasDoor == None or test.hasDoor.islocked == False
                or test.hasDoor.dir1 != 'n'):
                    Ply.location = tuple(newlocation)
                elif test.wallsinRoom[2] == True:
                    print('There is a wall here. ')
                elif test.hasDoor.islocked == True:
                    print('There is a door in the way. ')

        elif Decision == 'go south' or Decision == 'go s' or Decision == 's':
            newlocation[1] -= 1
            test = world.get(tuple(newlocation))
            if test == None:
                print('You cannot go there')
            else:
                if test.wallsinRoom[0] == False and (test.hasDoor == None or test.hasDoor.islocked == False
                or test.hasDoor.dir1 != 's'):

                    Ply.location = tuple(newlocation)
                elif test.wallsinRoom[0] == True:
                    print('There is a wall here. ')
                elif test.hasDoor.islocked == True:
                    print('There is a door in the way. ')


        elif Decision == 'go east' or Decision == 'go e' or Decision == 'e':
            newlocation[0] += 1
            test = world.get(tuple(newlocation))
            if test == None:
                print('You cannot go there')
            else:
                if test.wallsinRoom[3] == False and (test.hasDoor == None or test.hasDoor.islocked == False\
                or test.hasDoor.dir1 != 'e'):
                    Ply.location = tuple(newlocation)
                elif test.wallsinRoom[3] == True:
                    print('There is a wall here. ')
                elif test.hasDoor.islocked == True:
                    print('There is a door in the way. ')


        elif Decision == 'go west' or Decision == 'go w' or Decision == 'w':
            newlocation[0] -= 1
            test = world.get(tuple(newlocation))
            if test == None:
                print('You cannot go there')
            else:
                if test.wallsinRoom[1] == False and (test.hasDoor == None or test.hasDoor.islocked == False\
                or test.hasDoor.dir1 != 'w'):
                    Ply.location = tuple(newlocation)
                elif test.wallsinRoom[1] == True:
                    print('There is a wall here. ')
                elif test.hasDoor.islocked == True:
                    print('There is a door in the way. ')



#The Player class!
class Player(People):
    def __init__(self,location,name,text,state):
        self.location = location
        self.name = name
        self.text = text
        self.state = state


#Actually prints the description of your location
    def printlocation(self,location):
        return world.get(self.location).display_Room()

#Adds to inventory n shit
    def take(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) != 2  or tokens[1] not in objects:
            print("This doesn't exist.")
        else:
            if Ply.location == objects[tokens[1]].location:
                if objects[tokens[1]].ininv == 'no':
                    if objects[tokens[1]].islocked == False:
                        Inventory.append(objects[tokens[1]].name)
                        print('Taken')
                        objects[tokens[1]].ininv = 'yes'
                        objects[tokens[1]].incontainer = 'yes'
                        objects[tokens[1]].containername = None
                        world.get(self.location).objectsinRoom.remove(objects[tokens[1]])
                    else:
                        print("You don't see that")
                elif objects[tokens[1]].ininv == 'no':
                    print("You already have that")

            else:
                print("You don't see that")

#Removes from inventory n shit
    def drop(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) != 2 or tokens[1] not in Inventory:
            print("You don't have that")
        else:
            objects[tokens[1]].ininv = 'no'
            Inventory.remove(objects[tokens[1]].name)
            objects[tokens[1]].location = self.location
            world.get(self.location).objectsinRoom.append(objects[tokens[1]])
            print('Dropped')

#Puts something in a container.
    def put(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) != (4) or tokens[1] not in Inventory:
            print("You don't have that")
        elif tokens[2] != 'in' and tokens[2] != 'on':
            print('What?')
        elif tokens[2] == 'in':
            if tokens[3] not in containers:
                print("The thing you want that in doesn't exist")
            else:
                objects[tokens[1]].ininv = 'no'
                Inventory.remove(objects[tokens[1]].name)
                objects[tokens[1]].location = self.location
                world.get(self.location).objectsinRoom.append(objects[tokens[1]])
                objects[tokens[1]].incontainer = True
                objects[tokens[1]].containername = tokens[3]
                print('Put.')
        elif tokens[2] == 'on' and tokens[3] == 'floor':
            if tokens[1] not in Inventory:
                print("You don't have that")
            else:
                objects[tokens[1]].ininv = 'no'
                Inventory.remove(objects[tokens[1]].name)
                objects[tokens[1]].location = self.location
                world.get(self.location).objectsinRoom.append(objects[tokens[1]])
                print('Dropped')

#Opens a door or container
    def open(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) != 2 or tokens[1] not in containers:
            if tokens[1] == 'door':
                unlock(Decision)
            else:
                print("This doesn't exist.")
        else:
            containers[tokens[1]].isopen = True
            print('Opened')
            containers[tokens[1]].text = "An open " + containers[tokens[1]].name +" is here. "
            for item in itemsincontainers[containers[tokens[1]]]:
                item.islocked = False

#Closes a container
    def close(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) != 2 or tokens[1] not in containers:
            print("This doesn't exist.")
        else:
            containers[tokens[1]].isopen = False
            print('Closed')
            containers[tokens[1]].text = "A " + containers[tokens[1]].name +" is here. "
            for item in itemsincontainers[containers[tokens[1]]]:
                item.islocked = True


#Talks to a NPC
    def talk(self,location,Decision):
        if Decision == 'talk skrypt' or Decision == 'talk to skrypt' or Decision == 'talk with skrypt':
            if self.location == Skrypt.location:
                if Jeff.state == 'dead':
                    if gold.ininv == 'no':
                        print('You killed Jeff! Take this is a reward.')
                        print('Gold added to Inventory')
                        Inventory.append(gold.name)
                    elif gold.ininv == 'yes':
                        print('Thanks again, man.')
                elif Skrypt.state == 'dead':
                    print('This person is dead.')

                else:
                    Skrypt.printText()
            else:
                print("This person is not here.")

        elif Decision == 'talk jeff' or Decision == 'talk to jeff' or Decision == 'talk with jeff':
            if self.location == Jeff.location:
                if Jeff.state == 'dead':
                    print('This person is dead.')
                else:
                    Jeff.printText()
            else:
                print('This person is not here')

        elif Decision == 'talk skoty' or Decision == 'talk to skoty' or Decision == 'talk with skoty':
            if self.location == Skoty.location:
                if Skoty.state == 'dead':
                    print('this person is dead')
                elif 'gold' in Inventory:
                    Drug = input('You wanna buy some drugs?')
                    if Drug == 'no':
                        print('THEN FUCK OFF')
                    elif Drug == 'yes':
                        Inventory.remove('gold')
                        Inventory.append(meth.name)
                        print('Gold removed from Inventory')
                        print('Meth added to Inventory')
                else:
                    Skoty.printText()
            else:
                print('This person is not here')


        elif Decision == 'talk alien' or Decision == 'talk to alien' or Decision == 'talk with alien':
            if self.location == Alien.location:
                if Alien.state == 'dead':
                    print('this monster is dead')
                else:
                    Alien.printText()
                    print('The alien fucking raped you')
                    print('Game over')
                    Ply.state = 'dead'
            else:
                print('This thing is not here')

#Kills a NPC
    def kill(self,location,Decision):
        tokens = shlex.split(Decision)
        if len(tokens) == 2:
            if tokens[1] in people:
                if self.location == people[tokens[1]].location:
                    killhelp(tokens[1])
                else:
                    print('This person is not here.')
            else:
                print('This person does not exist')
        elif len(tokens) == 4:
            if tokens[2] == 'with':
                if tokens[1] in people:
                    if self.location == people[tokens[1]].location:
                        killhelpwithitem(tokens[3],tokens[1])
                    else:
                        print('This person is not here.')
                else:
                    print('This person does not exist')
            else:
                print("This won't work")
        else:
            print("This doesn't work")

#The item class
class Item(object):
    def __init__(self,name,text,location,cankill,ininv,incontainer,islocked,containername):
        self.name = name
        self.text = text
        self.location = location
        self.cankill = cankill
        self.ininv = ininv
        self.incontainer = incontainer
        self.islocked = islocked
        self.containername = containername

#Container Class
class Container(object):
    def __init__(self,name,text,location,isopen,contains):
        self.name = name
        self.text = text
        self.location = location
        self.isopen = isopen
        self.contains = contains

#Door class
class Door(object):
    def __init__(self,name,text,location1,location2,dir1,dir2,islocked,needskey,key):
        self.name = name
        self.text = text
        self.location1 = location1
        self.location2 = location2
        self.dir1 = dir1
        self.dir2 = dir2
        self.islocked = islocked
        self.needskey = needskey
        self.key = key


#helps the killmethod find out, if kill works
def killhelp(victim):
    Dec = input('With what?')
    Dec2 = Dec.lower()
    if Dec2 in objects:
        if Dec2 in Inventory:
            if objects[Dec2].cankill == 'yes':
                killcons(victim)
            else:
                print("You can't kill with that!")
        else:
            print("You don't have that.")
    else:
        print("This doesn't exist.")

#helps the killmethod find out, if kill works
def killhelpwithitem(Item,victim):
    if Item in objects:
        if Item in Inventory:
            if objects[Item].cankill == 'yes':
                killcons(victim)
            else:
                print("You can't kill with that!")
        else:
            print("You don't have that.")
    else:
        print("This doesn't exist.")

#The consequences of a kill
def killcons(victim):
    genericvictims = ['skrypt','jeff','skoty']

    if victim in genericvictims:
        people[victim].state = 'dead'
        print(victim + ' died. ')
    else:
        if victim == 'myself':
            print('You killed yourself. Good job, Really. Congratulations.')
            print('Game over')
            Ply.state = 'dead'
        elif victim == 'alien':
            print('YOU CANNOT KILL A ALIEN GODDAMNIT')

#Prints your inventory
def inv():
    stri = ', '
    print('You have ' + stri.join(Inventory))

#also opens stuff
#why is this not in the player class?
def unlock(Decision):
    tokens = shlex.split(Decision)
    otherlocation = list(Ply.location)
    if len(tokens) != 2 or tokens[1] != 'door' or Ply.location not in Doorslocations:
        if tokens[1] in containers:
            Ply.open(Ply.location,Decision)
        else:
            print("This does not exist, brother. ")
    else:
        if Doorsdirection[Ply.location] == 'n':
            otherlocation[1] += 1
            Doorslocations.get(Ply.location).islocked = False
            print('unlocked')

        elif Doorsdirection[Ply.location] == 'e':
            otherlocation[0] += 1
            Doorslocations.get(Ply.location).islocked = False
            print('unlocked')

        elif Doorsdirection[Ply.location] == 's':
            otherlocation[1] -= 1
            Doorslocations.get(Ply.location).islocked = False
            print('unlocked')

        elif Doorsdirection[Ply.location] == 'w':
            otherlocation[0] -= 1
            Doorslocations.get(Ply.location).islocked = False
            print('unlocked')


#Examines an item.
def exam(Decision):
    tokens = shlex.split(Decision)
    if len(tokens) != 2 or tokens[0] != 'exam' or tokens[1] not in objects:
        print("This doesn't exist")
    else:
        if Ply.location == objects[tokens[1]].location or tokens[1] in Inventory:
            print(objects[tokens[1]].text)
        else:
            print("You don't see this")

#This doesn't work for some reason
def dodrugs():
    if 'meth' in Inventory:
        print('YOU ARE HIGH')
        Inventory.remove('meth')
        meth.ininv = 'no'
    else:
        print("You don't have that")

#This is supposed to check at the end of turn, if something is supposed to happen
def script():
    pass

#prints the help thingy
def helpp():
    print("You can use the following commands:")
    print("go (north,south,west,east)")
    print("talk (person)")
    print("kill (person) with (item)")
    print("take (item)")
    print("drop (item)")
    print("open (door or container)")
    print("inventory")
    print("examine (item)")
    print("quit")


Inventory = []


sword = Item('sword','This is a sword',(2,2,1),'yes','no',False,False,None)
pistol = Item('pistol','This is a pistol',(3,1,1),'yes','no',True,True,'chest')
gold = Item('gold','This is gold',(1,1,1),'no','no',False,False,None)
meth = Item('meth','THIS IS SOME REALLY NICE BLUE METH',(1,2,1),'no','no',False,False,None)

objects = {
'sword': sword,
'gold': gold,
'meth': meth,
'pistol': pistol
}

objectsinroomA = []
objectsinroomB = []
objectsinroomC = [sword]
objectsinroomD = []
objectsinroomE = []
objectsinroomF = [pistol]



chest = Container('Chest','A chest is here. ',(3,1,1),False,None)

containers = {
'chest': chest

}

itemsinchest = [pistol]

itemsincontainers = {
chest: itemsinchest

}

containersinRoomA = []
containersinRoomB = []
containersinRoomC = []
containersinRoomD = []
containersinRoomE = []
containersinRoomF = [chest]



Door1 = Door('Door','This is a door. ',(3,1,1),(3,2,1),'n','s',True,False,None)

Doorslocations = {
(3,1,1): Door1,
(3,2,1): Door1

}


Doorsdirection = {
(3,1,1): Door1.dir1,
(3,2,1): Door1.dir2

}



Ply = Player((1,1,1),'Player','','alive')
Skrypt = People((1,1,1),'Skrypt',"Hi, I'm Skrypt. Dude, can you do me favor? Kill Jeff.",'This is Skrypt','alive')
Jeff = People((1,2,1),'Jeff',"Don't kill me! ",'This is Jeff','alive')
Skoty = People((2,1,1),'Skoty','Piss off, bitch.','This is Skoty','alive')
Alien = People((3,2,1),'Bad-Ass Alien','Probe, Probes for everyone!','THIS IS A FUCKING ALIEN','alive')


people = {
'skrypt': Skrypt,
'jeff': Jeff,
'skoty': Skoty,
'alien' : Alien,
'myself': Ply,
}


peopleinRoomA = [Skrypt]
peopleinRoomB = [Jeff]
peopleinRoomC = []
peopleinRoomD = [Skoty]
peopleinRoomE = [Alien]
peopleinRoomF = []




#               North,East,South,West,   Northlo,Eastlo,Southlo,Westlo
wallsinRoomA = [False,False,False,False, False,False,False,False]
wallsinRoomB = [False,False,False,False, False,False,False,False]
wallsinRoomC = [False,False,False,False, False,False,False,False]
wallsinRoomD = [False,False,False,False, False,False,False,False]
wallsinRoomE = [False,False,False,False,  False,False,Door1.islocked,False]
wallsinRoomF = [False,False,False,False,  Door1.islocked,False,False,False]


RoomA = Room((1,1,1),objectsinroomA,containersinRoomA,wallsinRoomA,peopleinRoomA,None,\
'You are in Room A.','',' You see a hallway to the north and to the east.')
RoomB = Room((1,2,1),objectsinroomB,containersinRoomB,wallsinRoomB,peopleinRoomB,None,\
'You are in Room B.','',' You see a hallway to the south and to the east.')
RoomC = Room((2,2,1),objectsinroomC,containersinRoomC,wallsinRoomC,peopleinRoomC,None,\
'You are in Room C.','',' You see a hallway to the west, to the east and to the south.')
RoomD = Room((2,1,1),objectsinroomD,containersinRoomD,wallsinRoomD,peopleinRoomD,None,\
'You are in Room D.','',' You see a hallway to the north and to the west.')
RoomE = Room((3,2,1),objectsinroomE,containersinRoomE,wallsinRoomE,peopleinRoomE,Door1,\
'You are in Room E. A door leading north is here. ',' ',' You see a hallway to the west and south.')
RoomF = Room((3,1,1),objectsinroomF,containersinRoomF,wallsinRoomF,peopleinRoomF,Door1,\
'You are in Room F. A door leading south is here.','',' You see a hallway to the west and north.')

world = {
(1,1,1):RoomA,
(1,2,1):RoomB,
(2,2,1):RoomC,
(2,1,1):RoomD,
(3,2,1):RoomE,
(3,1,1):RoomF
}






emptyline = '\n'

#The turn
def main():
    print("Welcome to my Text Adventure!")
    print("Use the 'help' command for help!")
    while Ply.state == 'alive':
        print(Ply.printlocation(Ply.location))
        Decisionst = input('>')
        Decisionstr = Decisionst.lower()
        lst = shlex.split(Decisionstr)
        if lst[0] == 'go' or lst[0] in 'nwse':
            Ply.go(Ply.location,Decisionstr)
        elif lst[0] == 'take' or lst[0] == 'get':
            Ply.take(Ply.location, Decisionstr)
        elif lst[0] == 'drop':
            Ply.drop(Ply.location,Decisionstr)
        elif lst[0] == 'quit':
            break
        elif lst[0] == 'talk':
            Ply.talk(Ply.location, Decisionstr)
        elif lst[0] == 'kill':
            Ply.kill(Ply.location,Decisionstr)
        elif lst[0] == 'die':
            killcons('myself')
        elif lst[0] == 'inventory' or lst[0] == 'inv' or lst[0] == 'i':
            inv()
        elif lst[0] == 'help':
            helpp()
        elif lst[0] == 'look':
            Ply.printlocation(Ply.location)
        elif lst[0] == 'open':
            Ply.open(Ply.location,Decisionstr)
        elif lst[0] == 'close':
            Ply.close(Ply.location,Decisionstr)
        elif lst[0] == 'put':
            Ply.put(Ply.location,Decisionstr)
        elif lst[0] == 'unlock':
            unlock(Decisionstr)
        elif lst[0] == 'examine' or 'exam':
            exam(Decisionstr)
        elif Decisionstr == 'do drugs' or 'do meth':
            dodrugs()
        script()

map()
main()
