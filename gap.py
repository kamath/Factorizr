#Uses the a+2^x method to find potential primes and verifies it with the database
import sqlite3 as lite
import sys
import matplotlib
import pylab
con = lite.connect('primes')
primes = []
def getprime():
    with con:
        cur = con.cursor()
        cur.execute("select * from primes")
        rows = cur.fetchall()
        i = 0
        for a in range(0, len(rows)):
			primes.append(int(rows[a][1]) - i)
			i = int(rows[a][1])
	return primes

def showplot():
	x = getprime()
	y = []
	for a in range(0, len(x)):
		y.append(a)
	matplotlib.pyplot.scatter(x,y)
	matplotlib.pyplot.show()

showplot()
