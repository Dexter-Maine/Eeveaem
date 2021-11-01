# Author: Skrypt
# Language: Python3
# Platform: The C0re

# C0re Syntax Build
# Adds And Profiles Syntax Usage For The C0re Platform
# Will Allow Users To Break Down Syntax As Well As Labeling C0re User => Privlidges
# Syntax Database Is A Binary Unit Dictionary Setup Like The Example Below:


# Algorithm:
 # Pull Old C0reSubSyntax Via Pickle
 # Check WORD Against C0reSubSyntax
  # Pull C0reSyntax
  # For Each New State Of WORD From Full To len(WORD) Is Equal To 3:
   # Create New C0reSyntax And C0reSubSyntax Data
 # Update Old C0reSyntax And Old C0reSubSyntax With New
 # Pickle And Dump C0reSyntax And C0reSubSyntax

###### New Syntax Addition Format Below ######
############## Create New C0reSubSyntax #######
# C0reSubSyntax = dict()
# C0reSubSyntax[SUB_WORD] = WORD
############## Create New C0reSyntax ##########
# C0reSyntax = dict() # Sets A Empty Dictionary
# C0reSyntax['List'] = list() # Sets A Empty Check List For Known Words
# C0reSyntax['List'].append(WORD) ## Adds Word To Known List
# C0reSyntax[WORD] = dict() # Creates Slot For WORD
# C0reSyntax[WORD]['Users'] = [*#,*#] # Creates Users List (Num Based Within Users Object)
# C0reSyntax[WORD]['Rooms'] = [*ROOM,*ROOM] # Creates Room Privlidge Allowacation For Assigning Room Usage