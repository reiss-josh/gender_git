import json

with open("genderize_results.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat

z = 0
while z < len(arr1):
	print(arr1[z])
	currname = arr1[z]['name']
	g1 = arr1[z]['gender']
	if (arr1[z]['gender'] != None):
		if (arr1[z]['probability'] < 0.8):
			arr1[z]['gender'] = None
	z += 1
print(arr1)
with open("new_genderize_results.json", mode="w", encoding='utf-8') as f:
		json.dump(arr1, f, indent=4, sort_keys=True)
