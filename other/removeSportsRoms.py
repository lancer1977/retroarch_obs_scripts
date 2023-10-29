# Python code to 
# traverse a list of directories that contain zip or other compressed files,
# if a file contains a word in the BAN list, add that to the list of delete subjects
# prompt the user to confirm,
# if yes, delete all these files.
count = 0  
matches = {} 
msg = f'Match on had {count} items'
print(msg)

import os
import re
banList = ["Mahjong","(Brazil)","(Korea)","(Beta)","(Taiwan)","(Demo)"]
#,"Olympic","Wimbledon","Carmen Sandiego","Wrestle", "Monaco", "Slap Shot", "Formula","Tennis","Hockey","Basketball", "Baseball", "Football","Soccer","Golf","Othello","NHL","MBA","MLB","NFL","Blackjack", "Bowling","Bases Loaded","Championship", "Wheel of Fortune"]
#get current working directory
inputdir = os.getcwd()

# Using readlines() 

for folder in os.listdir(inputdir):   
    try:
        for file in os.listdir(inputdir + "\\" + folder + "\\roms"):  
            for ban in banList:
                if file.find(ban) > 0:                              
                    print(file)
                    try:
                        if ban not in matches.keys():
                            matches[ban] = []         
                    except:
                        print(f"Key fail {folder}")                        
                    matches[ban].append(file)  
                    break
    #       if(file == "roms"):
        print(f"Found {folder}")
    except:
        print(f"Did not find {folder}")

#for file in [os.path.join(dp, f) for dp, dn, fn in os.walk(inputdir) for f in fn]:
   
for key in matches:
    print(f"Match on had {len(matches[key])} items.")
    for item in  matches[key]:
        print("Removing: " + key + " " + item)
        #os.remove(item)



 
#file2 = open('fielog.txt', 'w',encoding="utf8") 
#file2.writelines(L) 
#file2.close() 