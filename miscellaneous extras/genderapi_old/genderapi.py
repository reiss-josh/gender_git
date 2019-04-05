import json
import time

from urllib.request import urlopen

data = open("names_for_test.txt","r")
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

myKey = "FVEaZbeppRfFrBBuzH"


for x in fl:
	#url = "https://gender-api.com/get?key=" + myKey + "&name=kevin"
	x = x.rstrip()
	datac = next((item for item in wat if item["name"] == x), None)
	if datac == None:
		url = "https://gender-api.com/get?key=" + myKey + "&name=" + x
		response = urlopen(url)
		decoded = response.read().decode('utf-8')
		dataf = json.loads(decoded)
		y = dataf["gender"]
		datao = [{'name': x, 'gender': y, 'probability': 0, 'count': 0}]
		arr = arr + datao
	elapsed = time.time() - start
	ETR = (elapsed/(z+1))*(total-(z+1))
	print(x + " " + str(z) + "/" + str(total) + " ETR: " + str(ETR))
	z += 1
	with open(gender_fn, mode="w", encoding='utf-8') as f:
		json.dump(arr, f, indent=4, sort_keys=True)
data.close
