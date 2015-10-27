#Uses the a+2^x method to find potential primes and verifies it with the database
import sqlite3 as lite
import sys
import matplotlib
import pylab
import numpy as np
from scipy.optimize import curve_fit

con = lite.connect('primes')
x = []
y = []
with con:
    cur = con.cursor()
    cur.execute("select * from primes")
    rows = cur.fetchall()
    for a in rows:
    	x.append(int(a[1]))
    	y.append(int(a[0]))
print x
m,b = np.polyfit(x, y, 1)
pylab.ylim([0,x[len(x)-1]])
pylab.xlim([0,y[len(x)-1]])
b = eval("2*x")
lines = []
lines.append(97.0/24.0)
lines.append(997.0/167.0)
lines.append(9973.0/1228.0)
lines.append(99991.0/9591.0)
lines.append(999983.0/78497.0)
lines.append(9999991.0/664578.0)
for a in lines:
	matplotlib.pyplot.plot([0,664578], [0,664578*a], label='Line '+str(a))
	print a
matplotlib.pyplot.plot(y,x)
matplotlib.pyplot.show()
