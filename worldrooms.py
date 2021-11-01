#THIS IS THE ROOMS SECTION ALL ROOMS TO BE ALTERED/ADDED MUST BE HANDLED HERE
# New Room Object Routine
DescriptionBase = dict()
DescriptionBase['Registration Room'] = '[The Core Registration Room. You Are In A Personal Empty Starting Room. There Is A Door And There Is Also A Sign.]'
DescriptionBase['Main Chatter Room'] = "[A cozy chatter room. A Stone Based Room With A Hand Carved Wooden Floor. You See A Listings Board A Red Door With Something Written On It And A Large Sparkling Mermaid Fountain.]"
DescriptionBase['Routine Shop'] = "[The Core Trading Routine Shop. There Is A Stone Shelf, A Wired Shelf, A Oak Bench, And A Crystal Case Labeled 'S-P-E-C-I-A-L'.]"
DescriptionBase['The Mermaid\'s Fountain'] = "[Inside A Mermaid's Fountain, The Water Is A Soft Blue Green. There Is A Large Grate In The Center That Looks Ajar. ]"
DescriptionBase['Hand Traders Alley'] = "[A Crooked Makeshift Avenue Built From Aligning Pillars. The Street Like Bottom Is Paved With A Mixture Of Crushed Rock And Dirt. The Only Things Visible Among The Many Voices Are A Dangling Rope And A Crooked Sign.]"
class C0reRoom(object):
  def __init__(self,name,iden,description,exits,players,hidden,items,private,whisper,mobs,npc):
   self.Name = name
   self.Room_id = iden
   self.Description = Description
   self.Players = players
   self.HiddenPlayers = hidden
   self.Items = items
   self.Private = private
   self.Whisper_Only = whisper
   self.Mobs = mobs
   self.Npc = npc
   self.Exits = exits

TheCoreRooms = dict()
TheCoreRooms["[The Core, Registration Room]"] = C0reRoom(name="[The Core, Registration Room]",iden='0x0',description=DescriptionBase['Registration Room'],exits={ "door": "[The Core, Main Chatter Room]" },players=list(),hidden=list(),items=list(),private=True,whisper=False,mobs=list(),npc=list())
TheCoreRooms["[The Core, Main Chatter Room]"] =  C0reRoom(name="[The Core, Main Chatter Room]",iden='0x1',description=DescriptionBase["Main Chatter Room"],exits={ "red door": "[The Core, Routine Shop]", "fountain": "[The Core, In The Mermaid's Fountain]" },players=list(),hidden=list(),items=list(),private=False,whisper=False,mobs=list(),npc=list())
TheCoreRooms["[The Core, Routine Shop]"] =  C0reRoom(name="[The Core, Routine Shop]",iden='0x2',description=DescriptionBase["Routine Shop"],exits={ "red door": "[The Core, Main Chatter Room]"},players=list(),hidden=list(),items=list(),private=False,whisper=False,mobs=list(),npc=list())
TheCoreRooms["[The Core, In The Mermaid's Fountain]"] =  C0reRoom(name="[The Core, In The Mermaid's Fountain]",iden='0x3',description=DescriptionBase["The Mermaid's Fountain"],exits={"large grate": "[The Core, Hand Traders Alley]", "out": "[The Core, Main Chatter Room]"},players=list(),hidden=list(),items=list(),private=False,whisper=False,mobs=list(),npc=list())
TheCoreRooms["[The Core, Hand Traders Alley]"] = C0reRoom(name="[The Core, Hand Traders Alley]",iden='0x4',description=DescriptionBase["Hand Traders Alley"],exits={"rope": "[The Core, In The Mermaid's Fountain]"},players=list(),hidden=list(),items=list(),private=False,whisper=False,mobs=list(),npc=list())


