import json
import time
from genderize import Genderize

data = open("names_for_test.txt","r")
#out = open("genderize_results.json","w+")
#out.close()
gender_fn = "genderize_results.json"
with open("genderize_results.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
fl = data.readlines()
arr = wat
y = 1
total = len(fl)
start = time.time()
print(start)

for x in fl:
	#print(Genderize().get(['James', 'Eva', 'Thunder']))
	x = x.rstrip()
	#x = x.encode("utf8").decode("unicode_escape")
	#x = x.encode("utf8").decode("unicode_escape")
	dataf = next((item for item in wat if item["name"] == x), None)
	if dataf == None:
		dataf = Genderize().get([x])
		arr = arr + dataf
	elapsed = time.time() - start
	ETR = (elapsed/(y+1))*(total-(y+1))
	print(x + " " + str(y) + "/" + str(total) + " ETR: " + str(ETR))
	#print(dataf)
	y += 1
	with open(gender_fn, mode="w", encoding='utf-8') as f:
		json.dump(arr, f, indent=4, sort_keys=True)
data.close
