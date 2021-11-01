if players[id]["name"] == None:
na = charCreation["name"]["notallowed"]
         if len(gak) >= 9:
            mud.send_message(id, "Only 3-9 Letter Names Supported")
            mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
            continue
         if len(gak) <= 2:
            mud.send_message(id, "Only 3-9 Letter Names Supported")
            mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
            continue
         if len(gak) == 3:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            if gak[0] not in na:
             players[id]["name"] = gak
             continue
             
             
         elif len(gak) == 4:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            else:
             players[id]["name"] = gak
         elif len(gak) == 5:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            elif gak[4] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
            else:
             players[id]["name"] = gak
         elif len(gak) == 6:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[4] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[5] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            else:
             players[id]["name"] = gak
         elif len(gak) == 7:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[4] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[5] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[6] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            else:
             players[id]["name"] = gak
         elif len(gak) == 8:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[4] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[5] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[6] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[7] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            else:
             players[id]["name"] = gak
         elif len(gak) == 9:
            if gak[0] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[1] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[2] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[3] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[4] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[5] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[6] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[7] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            elif gak[8] in na:
             mud.send_message(id, "Use Only 'a-z' or 'A-Z' Characters For Name.")
             mud.send_message(id, "You Can Thank The God Sitsuji Later For This.")
             players[id]["name"] = None
             continue
            else:
             players[id]["name"] = gak