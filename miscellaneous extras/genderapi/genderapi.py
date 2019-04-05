import json
import time
import unidecode

from urllib.request import urlopen

data = open("firstcountry.txt","r")
#out = open("genderapi_results.json","w+")
#out.close()
gender_fn = "genderapi_results.json"
with open("genderapi_results.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
fl = data.readlines()
arr = wat
z = 1
total = len(fl)
start = time.time()
print(start)

#myKey = "LJVgPgGaXsgdaqNuVy"
#myKey = "FVEaZbeppRfFrBBuzH"
myKey = "ezHsmxQzstknZkKedT"


for x in fl:
	#url = "https://gender-api.com/get?key=" + myKey + "&name=kevin"	
	x = x.rstrip()
	x = x.split()
	x[0] = unidecode.unidecode(x[0])
	print(x[0])
	datac = None
	#datac = next((item for item in wat if item["name"] == x[0]), None)
	if datac == None:
		url = "https://gender-api.com/get?key=" + myKey + "&name=" + x[0] +"&country=" + x[1]
		response = urlopen(url)
		decoded = response.read().decode('utf-8')
		dataf = json.loads(decoded)
		if dataf["gender"] == None:
			url = "https://gender-api.com/get?key=" + myKey + "&name=" + x[0]
			response = urlopen(url)
			decoded = response.read().decode('utf-8')
			dataf = json.loads(decoded)
		gen = dataf["gender"]
		samp = dataf["samples"]
		acc  = dataf["accuracy"]
		datao = [{'name': x[0], 'gender': gen, 'probability': acc, 'count': samp}]
		arr = arr + datao
	elapsed = time.time() - start
	ETR = (elapsed/(z+1))*(total-(z+1))
	print(x[0] + " " + str(z) + "/" + str(total) + " ETR: " + str(ETR))
	z += 1
	with open(gender_fn, mode="w", encoding='utf-8') as f:
		json.dump(arr, f, indent=4, sort_keys=True)
data.close
