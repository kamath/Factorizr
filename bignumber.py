bignumber = []
for a in range(0,150):
	bignumber.append(str(9))
print(len(bignumber))
print(''.join(bignumber))
big = int(''.join(bignumber))
for a in range(0,big):
	print(a)