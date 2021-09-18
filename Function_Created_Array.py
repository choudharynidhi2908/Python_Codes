
import numpy as np
import pandas as pd

def sum_of_digits(arr):
	array2 = []
	output = []
	for i in range(0,len(arr)):
		a = np.sum(arr[i])
		result = 0
		print(a)
		while(a>0):
			rem = a%10
			result = rem + result
			a = int(a/10)
		array2.append(result)
	print('New array with digit sum ',array2)


	for i in  range(len(array2)):
		print('i value', i)
		for j in range(i+1,len(array2)):
			print('j value', j)
			if array2[i]==array2[j]:
				value = arr[i] + arr[j]
				output.append(value)
			else:
				output.append(-1)
	print(max(output))				
array1 = [51,71,17,42,111]
sum_of_digits(array1)