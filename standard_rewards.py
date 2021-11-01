# Reward Types Include :
# ('item', 'crypits', 'koinium', 'ethereal')
# 'item' = String
# 'crypits' = Int (Ex. 23213123 ) Divides By Users, This Balances['Decimal']
# 'koinium' = Int (Ex. 23213123 ) Divides By Users, This Balances['Decimal']
# 'ethereal' = Int (Ex. 23213123 ) Divides By Users, This Balances['Decimal']
Standard_Dice_Reward_Types = {
    '[1]': 'item',
    '[2]': 'koinium',
    '[3]': 'crypits',
    '[4]': 'ethereal',
    '[5]': 'item',
    '[6]': 'crypits',
    '[7]': 'koinium',
    '[8]': 'ethereal',
    '[9]': 'item',
    '[10]': 'ethereal',
    '[11]': 'koinium',
    '[12]': 'crypits',
    '[13]': 'item',
    '[14]': 'koinium',
    '[15]': 'item',
    '[16]': 'ethereal',
    '[17]': 'item',
    '[18]': 'crypits',
    '[19]': 'ethereal',
    '[20]': 'koinium',
}

Standard_Dice_Rewards = {
    'reward_0': {
        'reward': "Yellow Rabbit",
    },
    'reward_1': {
        'reward': 100000000000000000,
    },
    'reward_2': {
        'reward': 100000000000000000,
    },
    'reward_3': {
        'reward': 100000000000000000,
    },
    'reward_4': {
        'reward': "Gold Rabbit",
    },
    'reward_5': {
        'reward': 100000000000000000,
    },
    'reward_6': {
        'reward': 100000000000000000,
    },
    'reward_7': {
        'reward': 100000000000000000,
    },
    'reward_8': {
        'reward': "Vanilla Rabbit",
    },
    'reward_9': {
        'reward': 100000000000000000,
    },
    'reward_10': {
        'reward': 100000000000000000,
    },
    'reward_11': {
        'reward': 100000000000000000,
    },
    'reward_12': {
        'reward': 'Mini Rabbit',
    },
    'reward_13': {
        'reward': 100000000000000000,
    },
    'reward_14': {
        'reward': 'Handmade Rabbit',
    },
    'reward_15': {
        'reward': 100000000000000000,
    },
    'reward_16': {
        'reward': 'Black Rabbit',
    },
    'reward_17': {
        'reward': 100000000000000000,
    },
    'reward_18': {
        'reward': 100000000000000000,
    },
    'reward_19': {
        'reward': 100000000000000000,
    },
}

Standard_Dice_Returns = {
    '[1]': {
     'public return': 'Rolled A 1!',
     'self return': 'You Rolled A 1!',
     'reward type': Standard_Dice_Reward_Types['[1]'],
     'reward': Standard_Dice_Rewards['reward_0']['reward'],
    },
    '[2]': {
     'self return': 'You Rolled A 2!',
     'reward type': Standard_Dice_Reward_Types['[2]'],
     'reward': Standard_Dice_Rewards['reward_1']['reward'],
    },
    '[3]': {
     'self return': 'You Rolled A 3!',
     'reward type': Standard_Dice_Reward_Types['[3]'],
     'reward': Standard_Dice_Rewards['reward_2']['reward'],
    },
    '[4]': {
     'self return': 'You Rolled A 4!',
     'reward type': Standard_Dice_Reward_Types['[4]'],
     'reward': Standard_Dice_Rewards['reward_3']['reward'],
    },
    '[5]': {
     'self return': 'You Rolled A 5!',
     'reward type': Standard_Dice_Reward_Types['[5]'],
     'reward': Standard_Dice_Rewards['reward_4']['reward'],
    },
    '[6]': {
     'self return': 'You Rolled A 6!',
     'reward type': Standard_Dice_Reward_Types['[6]'],
     'reward': Standard_Dice_Rewards['reward_5']['reward'],
    },
    '[7]': {
     'self return': 'You Rolled A 7!',
     'reward type': Standard_Dice_Reward_Types['[7]'],
     'reward': Standard_Dice_Rewards['reward_6']['reward'],
    },
    '[8]': {
     'self return': 'You Rolled A 8!',
     'reward type': Standard_Dice_Reward_Types['[8]'],
     'reward': Standard_Dice_Rewards['reward_7']['reward'],
    },
    '[9]': {
     'self return': 'You Rolled A 9!',
     'reward type': Standard_Dice_Reward_Types['[9]'],
     'reward': Standard_Dice_Rewards['reward_8']['reward'],
    },
    '[10]': {
     'self return': 'You Rolled A 10!',
     'reward type': Standard_Dice_Reward_Types['[10]'],
     'reward': Standard_Dice_Rewards['reward_9']['reward'],
    },
    '[11]': {
     'self return': 'You Rolled A 11!',
     'reward type': Standard_Dice_Reward_Types['[11]'],
     'reward': Standard_Dice_Rewards['reward_10']['reward'],

    },
    '[12]': {
     'self return': 'You Rolled A 12!',
     'reward type': Standard_Dice_Reward_Types['[12]'],
     'reward': Standard_Dice_Rewards['reward_11']['reward'],

    },
    '[13]': {
     'self return': 'You Rolled A 13!',
     'reward type': Standard_Dice_Reward_Types['[13]'],
     'reward': Standard_Dice_Rewards['reward_12']['reward'],

    },
    '[14]': {
     'self return': 'You Rolled A 14!',
     'reward type': Standard_Dice_Reward_Types['[14]'],
     'reward': Standard_Dice_Rewards['reward_13']['reward'],

    },
    '[15]': {
     'self return': 'You Rolled A 15!',
     'reward type': Standard_Dice_Reward_Types['[15]'],
     'reward': Standard_Dice_Rewards['reward_14']['reward'],

    },
    '[16]': {
     'self return': 'You Rolled A 16!',
     'reward type': Standard_Dice_Reward_Types['[16]'],
     'reward': Standard_Dice_Rewards['reward_15']['reward'],

    },
    '[17]': {
     'self return': 'You Rolled A 17!',
     'reward type': Standard_Dice_Reward_Types['[17]'],
     'reward': Standard_Dice_Rewards['reward_16']['reward'],

    },
    '[18]': {
     'self return': 'You Rolled A 18!',
     'reward type': Standard_Dice_Reward_Types['[18]'],
     'reward': Standard_Dice_Rewards['reward_17']['reward'],

    },
    '[19]': {
     'return': 'You Rolled A 19!',
     'reward type': Standard_Dice_Reward_Types['[19]'],
     'reward': Standard_Dice_Rewards['reward_18']['reward'],
    },
    '[20]': {
     'return': 'You Rolled A 20!',
     'reward type': Standard_Dice_Reward_Types['[20]'],
     'reward': Standard_Dice_Rewards['reward_19']['reward'],
    },
}