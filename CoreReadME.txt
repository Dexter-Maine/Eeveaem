The Server Is Active As Well As A 'Guest' Persona. The Server Owns The Skryptek Tavern Within The Genesis Zone.
Player Is Only Able To Speak As Of 5/25/2019 @ 12:55 AM
Ending Thoughts:
 Chat Logs Need To Be Added. Tomorrow I Would Like To Add Player Movement And Start With Items And Critter Association.
Next I Think I Should Move To Minor Skills & Stats Then To CryptoVerse Type Actions (Tickers, Exchanges, Block Explorers Etc.)
Finally Tightening Up With Banking, Shops and Transactions To Finish Base Commands. Then I Need To Not Forget To Start The Lore Of The Verse
Guilds, Magik, Crafts (items), Skills and Quests.

Don't Forget To At Least Get Movement And Basic Commands (F
ix That Stupid Log Tester) And Some Items Down Tomorrow

To Edit The Player & Wallet Objects Please Refer To resources/PersonaData/UserObject.py

The Player And Environment Commands Are Currently Held Within Engine.py / Test_Engine.py

To Add A Room First A Room Object Must Be Created Within resources/Locations
Next The Room Mapping Must Be Updated With Correct Room Information And A Pathway Object Associated (Created) (CorePathwayObjects.py)
Last Add The room to The Server World By Editing The World Object Within resources/CoreRooms.py
 Information The Room Object Holds:
  - Players
  - Hidden Players
  - Alive Critters
  - Dead Critters
  - Exit Pathway Objects