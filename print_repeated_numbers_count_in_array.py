array=[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
print(array)
print("")
list=[]
for a in array:
	count=0
	for b in array:
		if a==b:
			count+=1
	if a not in list:
		list.append(a)
		if count>1:
			print(str(a)+ "-" +str(count))

print("")
print("Press enter to exit the program")
input()
