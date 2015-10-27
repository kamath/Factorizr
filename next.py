a = 0
primes = [2,3,5,7]
while a < 20:
	for i in primes:
		if a % i == 0:
			print a
			a+=1
		if i == len(primes):
			primes.append(a)
			a+=1
	a+=1
print primes