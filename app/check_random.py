import random
import sys

search = True
count_values={}
for i in range(10000000):
	tmp = int(random.randint(0,99))
	if tmp == 99:
		search = False
	else:
		if tmp in count_values:
			count_values[tmp] = count_values[tmp]+1
		else:
			count_values[tmp] = 1

for key in count_values.keys():
	print(key , count_values[key] , sep=" : ")
