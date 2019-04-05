import json
import time
import unidecode
from genderize import Genderize

with open("newout.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
fl = wat
gender_fn = "genderize_results.json"
with open("genderize_results.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr = wat
y = 1
total = len(fl)
start = time.time()
print(start)
Genderize.api_key = "746a65219f0c47a2854215064bc17db0"

for x in fl:
	#print(Genderize().get(['James', 'Eva', 'Thunder']))
	fnam = x['first_name']
	coun = x['country']
	fnam = unidecode.unidecode(fnam)
	fnam = unidecode.unidecode(fnam)
	#dataf = next((item for item in wat if item["name"] == x[0]), None)
	dataf = None
	if dataf == None:
		nam = [fnam]
		dataf = Genderize().get(nam, coun)
		dcheck = dataf[0]
		if dcheck['gender'] == None:
			dataf = Genderize().get(nam)
		dataf = dataf[0]
		if (dataf['gender']) == None:
			datao = [{'first_name': dataf['name'], 'last_name': x['last_name'], 'country': x['country'], 'gender': dataf['gender'], 'probability': None, 'count': None}]
		else:
			datao = [{'first_name': dataf['name'], 'last_name': x['last_name'], 'country': x['country'], 'gender': dataf['gender'], 'probability': dataf['probability'], 'count': dataf['count']}]
		arr = arr + datao
	elapsed = time.time() - start
	ETR = (elapsed/(y+1))*(total-(y+1))
	print(fnam + " " + str(y) + "/" + str(total) + " ETR: " + str(ETR))
	y += 1
	with open(gender_fn, mode="w", encoding='utf-8') as f:
		json.dump(arr, f, indent=4, sort_keys=True)
