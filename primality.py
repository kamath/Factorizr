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
        for row in rows:
            while int(row[1])+2**a<1000:
                for x in rows:
                    if int(row[1])+2**a == int(x[1]):
                        if int(row[1])+2**a not in primes:
                            primes.append(int(row[1])+2**a)
                            print int(row[1])+2**a
                a+=1
            a = 1
        return sorted(primes)
print getprime()
