#Uses sieve of Eratosthenes to compile list of primes and add them to the database
import sqlite3 as lite
import sys

con = lite.connect('primes')
dd = 0
number = 9999999
def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
for i in sieve(number):
	with con:
	   cur = con.cursor()
	   print(i)
	   cur.execute("INSERT INTO primes(PID, VALUE) VALUES("+str(dd)+", "+str(i)+")");dd+=1
