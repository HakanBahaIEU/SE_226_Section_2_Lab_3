import random
import string

print("Choose 10 characters (lowercase only) and assign 5 replacement options each:")
Dict = {}
set1 = {"a","b"}
set1.clear

keys = input("Enter a lowercase character: ")

Dict['key1'] = keys
for x in range(3):
    keys = input("Enter a replacement for "+Dict["key1"])
    set1.add(keys)
Dict["Rkey1"] = set1
set1.clear

keys = "aa"
while(keys[1] != None):
    keys = input("Enter a lowercase character: ")

Dict['key2'] = keys
for x in range(3):
    keys = input("Enter a replacement for "+Dict["key2"])
    set1.add(keys)
Dict["Rkey2"] = set1
set1.clear

keys = "aa"
keys = input("Enter a lowercase character: ")

Dict['key3'] = keys
for x in range(3):
    keys = input("Enter a replacement for "+Dict["key3"])
    set1.add(keys)
Dict["Rkey3"] = set1
set1.clear

keys = "aa"
keys = input("Enter a lowercase character: ")

Dict['key4'] = keys
for x in range(3):
    keys = input("Enter a replacement for "+Dict["key4"])
    set1.add(keys)
Dict["Rkey4"] = set1
set1.clear

keys = "aa"
keys = input("Enter a lowercase character: ")

Dict['key5'] = keys
for x in range(3):
    keys = input("Enter a replacement for "+Dict["key5"])
    set1.add(keys)
Dict["Rkey5"] = set1
set1.clear

lowercases = {1:Dict["key1"],2:Dict["key2"],3:Dict["key3"],4:Dict["key4"],5:Dict["key5"]
              ,10:Dict["Rkey1"],20:Dict["Rkey2"],30:Dict["Rkey3"],40:Dict["Rkey4"],50:Dict["Rkey5"]}


passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)
    strornot = 0
    for x in range (15):
        for y in range (3):
            if(passwords[x] == lowercases[y]):
                passwords[x] = lowercases[y*10](random.choice(k=3))
                strornot += 1
    if(strornot > 4):
        print( passwords+" is strong")
    else:
        print(passwords + "is weak")
