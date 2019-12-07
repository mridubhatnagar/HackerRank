def beautifulDays(x):

	reverse_num = 0
	L=[]

	while(x > 0):
		quotient, remainder = divmod(x, 10)
		print("no, quotient, remainder  ", x, quotient, remainder)
		x = quotient
		reverse_num = int(reverse_num*10) + int(remainder)
		print("reverse num ", reverse_num)

		print("************************************************************")
		print(x, reverse_num)



		#value = abs(x-reverse_num)/k
		#print(value)
        
		#if not isinstance(value, float):
		#	L.append(value)

	#print(len(L))
	result = len(L)

	return result

y = int(input())
x = beautifulDays(y)