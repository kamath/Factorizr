#Uses the a+2^x method to find potential primes and verifies it with the database
import sqlite3 as lite
import sys
con = lite.connect('primes')
primes = []
def getprime():
    with con:
        cur = con.cursor()
        cur.execute("select * from primes")
        rows = cur.fetchall()
        a = 1
        while 1+2**a<1000:
            print 1+2**a
            a+=1
        return sorted(primes)
print getprime()
