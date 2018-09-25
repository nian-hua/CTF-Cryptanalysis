
tmp  = input('Please input number example (12,15):')

tmp = eval(tmp)

num1 = tmp[0]

num2 = tmp[1]

while True:

	if num1 == num2 :

		print (num1)

		exit()

	if num1 > num2 :

		num1 = num1 - num2

	else :

		num2 = num2 - num1
