#Used to make requests
import urllib.request
import time
target = "https://etherscan.io/address/0x53d284357ec70ce289d6d64134dfac8e511c8a3d"
addition = 1
counter = 1000
total_pages = 3618502788666131106986593281521497120401173883721090761956411348172442546699
found = False
while True:
 if found == False:
  #now, with the below headers, we defined ourselves as a simpleton who is
  #still using internet explorer.
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  url = 'https://ethdir.io/'+str(counter)
  req = urllib.request.Request(url, headers = headers)
  x = urllib.request.urlopen(req)
  l = str(x.read())
  if target in l:
   saveFile = open('found.txt','w')
   saveFile.write(l)
   saveFile.close()
   counter = counter + addition
   time.sleep(0.5)
   found == True
   print('try counter '+str(counter))

  elif target not in l:
   found == False
   print('not here')
   time.sleep(0.2)
   counter = counter + addition
   print('page '+str(counter))
   print(str(total_pages - counter)+' Left')



#d09dd0b8d0bad0bed0b3d0b4d0b0d0bdd0b5d0b7d0b0d0b3d180d183d0b6d0b0d0b9d182d0b5
