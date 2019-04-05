import json
import unidecode

f = open("names.txt","r")
g = open("countries.txt","r")

fl = f.readlines()
narr = []
carr = []

for x in fl:
	x = x.replace("[","")
	x = x.replace("]","")
	x = x.replace("\"","")
	x = x.replace(":","")
	x = x.replace("\'","")
	x = x.replace(","," ,")
	x = x.split()
	currname = ""
	lastname = ""
	while (x != []) and (x[0] != ','):
		x[0] = unidecode.unidecode(x[0])
		if (currname != ""):
			currname += " "
		currname += x[0]
		x = x[1:]
	while (x != []):
		x[0] = unidecode.unidecode(x[0])
		if(x[0] == ','):
			x = x[1:]
		if (lastname != ""):
			lastname += " "
		if(x != []):
			lastname += x[0]
			#x = x[1:]
			x = []
	if lastname == "":
		lastname = currname
	narr += [{'last_name': currname, 'first_name': lastname, 'country': "", 'gender': ""}]

fl = g.readlines()
z = 0
for x in fl:
	x = x.split()
	x = x[0]
	narr[z]['country'] = x
	z += 1

print(narr)
	
with open("newout.json", mode="w", encoding='utf-8') as f:
		json.dump(narr, f, indent=4, sort_keys=True)
