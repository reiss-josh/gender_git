import json

inf = open("genderapi_results.txt","r")
out = open("genderapi_results.json","w+")
out.close()
gender_fn = "genderapi_results.json"

arr = []
fl = inf.readlines()
for x in fl:
	y = x.split()
	print(y)
	arr.append(x)
with open(gender_fn, mode="w", encoding='utf-8') as f:
        json.dump(arr, f, indent=4, sort_keys=True)
