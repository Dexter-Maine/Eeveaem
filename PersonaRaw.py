class User:
 def __init__(self, persona):
  self.persona = persona

Profile = {
  'Audio': 'Not Active',
  'Vivian': 'Not Active',
  "name": None,
  "started": False,
  "namecheck": False,
  "public_name": '', #Public Address
  "private_name": '', #IF Private (Private-Key (Recovery))
  "speech": "say",
  "specialspeech": False,
  "move": "walk",
  "room": "[Eeveem, Starting Room]",
  "roomid": "0",
  "roomsdiscovered": [],
  "inventory": [],
  "exp": 0,
  "level": 0,
  "right_hand": [],
  "left_hand": [],
  "sitting": False,
  "standing": True,
  "laying_down": False,
  "alive": True,
  "right_hand_full": False,
  "left_hand_full": False,
  "signed_in": False,
  "wallet_set": False,
  "parity_wallet": False,
  "personal_wallet": False,
  "this balances": {
     'decimals': 1e18,
     'Crypits': 0,
     'Ethereal Tokens': 0,
     'Koinium': 0,
   },
  }