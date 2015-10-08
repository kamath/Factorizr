import sqlite3 as lite
import sys

number = int(raw_input("Input your number: "))

con = lite.connect('primes')
primes = []
def getprime(number):
	a = 0
	while number % 2 == 0:
		a+=1
		number /= 2
		primes.append(2)
	with con:
		cur = con.cursor()
		cur.execute("select * from primes")
		rows = cur.fetchall()
		for row in rows:
			if int(row[1]) == number:
				primes.append(int(row[1]))
				break
			else:
				if number % int(row[1]) == 0:
					primes.append(int(row[1]))
					number/=int(row[1])	
					getprime(number)
					break
	return primes
print str(getprime(number)) + " are the factors of " + str(number)