import json
import time

from urllib.request import urlopen

f = open("outfile.txt","r")
g = open("firstcountry2.txt","w+")

fl = f.readlines()
carr = 0

for x in fl:
	x = x.replace("[","")
	x = x.replace("]","")
	x = x.replace("\'","")
	x = x.replace(":","")
	x = x.replace("\'","")
	x = x.replace(",","")
	x = x.split()
	print(x)
	carr = x

i = 0
while i < len(x)-1:
	p = x[i]+" "+x[i+1]+"\n"
	g.write(p)
	i = i + 2

f.close
g.close
