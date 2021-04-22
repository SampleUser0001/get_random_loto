import random
import sys

# 返したいリストのサイズ
list_length = int(sys.argv[1])

# 1～random_sizeの間の整数値を生成する
random_size = int(sys.argv[2])

# 取得した値を詰める
values = []

for i in range(0, random_size // 10):
    values.append(random.randint(1+i*10, (i+1)*10) )

print(values)

# 端数のサイズを取得
remainder = random_size % 10
# 端数の10の位
ten = random_size // 10

# print(remainder)
# print("random_size:{}, ten:{}, min:{}, max{}".format(random_size, ten, min,max))

if remainder >= random.randint(1, 10):
	min = ten*10
	max = random_size
	values.append(random.randint(min, max))

print(values)

while len(values) < int(list_length):
	tmp = random.randint(1,random_size)
	if tmp in values:
		pass
	else:
		values.append(tmp)
print(values)