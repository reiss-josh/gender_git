import json

with open("genderize_results_old.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat
with open("genderize_results.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr2 = wat
arr3 = []
arr4 = []
arr5 = []

z = 0
while z < len(arr1):
	currname = arr1[z]['name']
	g1 = arr1[z]['gender']
	print(currname)
	for x in arr2:
		if x['name'] == currname:
			g2 = x['gender']
	if (g1 == g2) and (g1 == None):
		arr5 += [{'name': currname, 'gender': g1}]
	elif (g1 != g2):
		arr3 += [{'name': currname, 'gender': g1}]
		arr4 += [{'name': currname, 'gender': g2}]
		
	z += 1
	#if(arr1[z]['gender'] != arr2[z]['gender']):
	#	if ((arr1[z]['gender'] == 'unknown') and (arr2[z]['gender'] == None)):
	#		print("Both null")
	#		arr5 += [{'name': arr1[z]['name'], 'gender': arr1[z]['gender'], 'probability': arr1[z]['probability'], 'count': arr1[z]['count']}]
	#	else:
	#		print(arr1[z])
	#		print(arr2[z])
	#		print("")
	#		x = [{'name': arr1[z]['name'], 'gender': arr1[z]['gender'], 'probability': arr1[z]['probability'], 'count': arr1[z]['count']}]
	#		if(arr2[z]['gender'] == None):
	#			y = [{'name': arr2[z]['name'], 'gender': arr2[z]['gender'], 'probability': 0, 'count': 0}]
	#		else:
	#			y = [{'name': arr2[z]['name'], 'gender': arr2[z]['gender'], 'probability': arr2[z]['probability'], 'count': arr2[z]['count']}]
	#		arr3 += x
	#		arr4 += y
	z += 1
print(arr3)
print(arr4)
print(arr5)
with open("arr3.json", mode="w", encoding='utf-8') as f:
		json.dump(arr3, f, indent=4, sort_keys=True)
with open("arr4.json", mode="w", encoding='utf-8') as f:
		json.dump(arr4, f, indent=4, sort_keys=True)
with open("arr5.json", mode="w", encoding='utf-8') as f:
		json.dump(arr5, f, indent=4, sort_keys=True)
