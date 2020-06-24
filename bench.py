# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s07.html
# python -O bench.py

import time
import os

def timeo(fun, n=10):
    start = time.clock(  )
    for i in range(n): fun(  )
    stend = time.clock(  )
    thetime = stend-start
    return fun.__name__, thetime

def linecount_wc(  ):
    return int(os.popen('wc -l nuc').read().split(  )[0])

def linecount_1(  ):
    return len(open('nuc').readlines(  ))

def linecount_2(  ):
    count = 0
    for line in open('nuc').xreadlines(  ): count += 1
    return count

def linecount_3(  ):
    count = 0
    thefile = open('nuc')
    while 1:
        buffer = thefile.read(65536)
        if not buffer: break
        count += buffer.count('\n')
    return count

for f in linecount_wc, linecount_1, linecount_2, linecount_3:
    print f.__name__, f(  )

for f in linecount_1, linecount_2, linecount_3:
    print "%s: %.2f"%timeo(f)
