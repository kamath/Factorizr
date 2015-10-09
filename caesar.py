import sqlite3 as lite
import sys

con = lite.connect('primes')
dd = 0
number = 1000000
def sieve(n):
    print "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
for i in sieve(number):
	with con:
		cur = con.cursor()
		print i
		cur.execute("INSERT INTO big(PID, VALUE) VALUES("+str(dd)+", "+str(i)+")")
        dd+=1
