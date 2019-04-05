import json

f = open("names.txt","r")
g = open("countries.txt","r")

fl = f.readlines()
narr = []
carr = []

for x in fl:
	x = x.split()
	x = x[1:]
	n = str(x[:1])
	n = n.replace("[","")
	n = n.replace("]","")
	n = n.replace("\"","")
	n = n.replace(":","")
	n = n.replace("\'","")
	n = n.replace(",","")
	narr += [n]

fl = g.readlines()
for x in fl:
	x = x.split()
	carr += x

farr = []
i = len(narr)
i -= 1
while i >= 0:
	farr += [[narr[i], carr[i]]]
	i -= 1
	
h = open("outfile.txt", "w+")
h.write(str(farr))
h.close()
