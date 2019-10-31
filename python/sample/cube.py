def cube(num):
	return num * num * num

def div_cube(num):
	if num % 3 == 0:
		return cube(num)
	else:
		return False

number = int(input("Input the number: "))

print(div_cube(number))