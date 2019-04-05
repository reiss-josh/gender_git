import json
import unidecode

f = open("names.txt","r")
g = open("genders_old.txt","r")

fl = f.readlines()
gl = g.readlines()
narr = {}

z = 0
for x in fl:
	x = x.replace("[","")
	x = x.replace("]","")
	x = x.replace("\"","")
	x = x.replace(":","")
	x = x.replace("\'","")
	x = x.rstrip('\n')
	x = unidecode.unidecode(x)
	y = gl[z].rstrip('\n')
	narr [x] = y
	z += 1

#print(narr)
	
with open("verified_gender_mapping.json", mode="w", encoding='utf-8') as f:
		json.dump(narr, f, indent=4, sort_keys=True)
