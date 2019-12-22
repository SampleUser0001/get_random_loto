import random
import sys

values = []
while len(values) < int(sys.argv[1]):
	tmp = random.randint(1,int(sys.argv[2]))
	if tmp in values:
		pass
	else:
		values.append(tmp)
print(values)