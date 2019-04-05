f = open("file.json","r")
g = open("outfile.txt", "w+")

fl = f.readlines()
for x in fl:
	x = x.split()
	x = x[1:]
	x = x[:1]
	x = str(x)
	x = x.replace("[","")
	x = x.replace("]","")
	x = x.replace("\"","")
	x = x.replace(":","")
	x = x.replace("\'","")
	print(x)
	g.write(x)
	g.write("\n")

f.close()
g.close()
