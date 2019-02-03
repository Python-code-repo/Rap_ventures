salary = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}

def salar(salary):
	add=0
	for x in salary.values():
		add=add+x
	print(salary)
	print("")
	print(add)
salar(salary)

print("")
print("Press enter to exit the program")
input()
