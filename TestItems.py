
def test_me(prms):
 pa = prms.lower()
 pa_sub = pa.split(' ')
 if pa_sub[0] == 'knuckles':
  item = Knuckles()
  users[id]['inventory'].append(item)
  Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'wooden':
  if pa_sub[1] == 'knuckles':
   item = WoodenKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'aluminum':
  if pa_sub[1] == 'knuckles':
   item = AluminumKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'brass':
  if pa_sub[1] == 'knuckles':
   item = BrassKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'iron':
  if pa_sub[1] == 'knuckles':
   item = IronKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'quartz':
  if pa_sub[1] == 'knuckles':
   item = QuartzKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'steel':
  if pa_sub[1] == 'knuckles':
   item = SteelKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'titanium':
  if pa_sub[1] == 'knuckles':
   item = TitaniumKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'koinium':
  if pa_sub[1] == 'knuckles':
   item = KoiniumKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
 elif pa_sub[0] == 'nanotech':
  if pa_sub[1] == 'knuckles':
   item = NanotechKnuckles()
   users[id]['inventory'].append(item)
   Evm.send_message(id, item.Name+' Added To Inventory')
