# Python3
# Author: Skrypt
# User Login Module
import os
import time
users = dict()
signed_in = dict()



def add_user(storage):
    global title_counter
    user = input('> Create Username: ')
    password = input('> Create Password: ')
    if user in storage:
        print('> That user already exists ')
        title_counter = 0
        time.sleep(2.0)
        os.system('cls') # From os import.
        return False
    else:
        print('> '+str(user)+' Created ')
        storage[user] = password
        signed_in[user] = True
        title_counter = 0
        time.sleep(2.0)
        os.system('cls') # From os import.
        return True

def sign_in(tried_user):
    global title_counter
    global user
    if tried_user in users:
        print('> Please Provide Password.')
        password = input('> Password: ')
        if password == users[tried_user]:
         print('> Password Accepted.')
         user = tried_user
         signed_in[user] = True
         title_counter = 0
         return True
    if tried_user not in users:
        print('> User Not Found Please Create User.')
        title_counter = 0
        time.sleep(2.0)
        os.system('cls') # From os import.
        return False

def print_users():
    global title_counter
    print('> Users: ')
    userNames = {}
    userNames.update(users)
    user_List = sorted(userNames.keys())
    print(user_List)
    title_counter = 0
    time.sleep(2.0)
    os.system('cls') # From os import.
    return True

#while True:
#    if title_counter <= 0:
#     print('> Hello '+str(user)+' Please Decide What To Do. ')
#     title_counter = 1
#    if signed_in[user] == False:
#     print('> You May Sign In or Make Account. ')
#     query = input('> What Would You Like To Do? ')
#     if query.lower() in help_list:
#      helpMe()
#     if query.lower() in add_list:
#      add_user(users)
#     if query.lower() in print_list:
#      print_users()
#     if query.lower() in sign_in_list:
#      user_to_use = input('> Which User Do You Want To Sign In As? ')
#      sign_in(user_to_use)
#    elif printable <= 0 and signed_in[user] == True:
#     print('> Thank You For Signing In '+str(user))
#     printable += 1