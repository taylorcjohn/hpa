#!/usr/bin/env python
# ...........................................................................
# ratap.py
#
# 2019-01-17 21:00
#
# ...........................................................................
#
# 2019-01-17 15:10 ratio
# 2019-01-17 18:00 sqrt added
# 2019-01-17 18:30 top results ordered
# 2019-01-17 19:00 remove sqrt for natural squares e.g. sqrt(4), sqrt(9)
# 2019-01-17 21:00 cube root added (-3)
#
# ...........................................................................

import traceback
import math
import getopt
import os
import sys
import time


# ...........................................................................
def ratap(target, numdenmax, sm, cm, thresh):

    global res
    res = []
    ratap_p(target, numdenmax, thresh, 1.0,      "ratio")
    ratap_p(target, numdenmax, thresh, math.pi,  "* Pi")
    ratap_p(target, numdenmax, thresh, math.tau, "* Tau")
    ratap_p(target, numdenmax, thresh, math.e,   "* e")
    for s in range (2,sm+1):
        if (math.sqrt(s)-int(math.sqrt(s)) > 0):
            ratap_p(target, numdenmax, thresh, math.sqrt(s), "* sqrt({})".format(s))

    for s in range (2,cm+1):
        if (math.pow(s,1.0/3)-int(math.pow(s,1.0/3)) > 0):
            ratap_p(target, numdenmax, thresh, math.pow(s,1.0/3), "* cbrt({})".format(s))

    so = sorted(res, key=takeSecond, reverse=False)

    return so

# ...........................................................................
def ratap_p(target, numdenmax, thresh, fixed, fixed_p):

    global n, d, t, nb, db, best, res, f, fp

    best = 1e6
    f = fixed
    fp = fixed_p
    n = 0
    d = 0
    t = 0.0
    nb = 0.0
    db = 0.0

    try:
        while (max(n,d) < numdenmax) & (best > thresh):
            n += 1
            d = math.floor( (n * f)/ target )
            try:
                t = ( (n * f)/ d ) - target
            except:
                t = math.inf
            test()
            d += 1
            t = target - ( (n * f)/ d )
            test()

    except:
        traceback.print_exc()


# ...........................................................................
def test():

    global n, d, t, nb, db, best, res, f, fp

    if ( t < best ):
        nb = n
        db = d
        best = t
        # print("{} / {}  best {}  value {} gcd {}".format(nb, db, best, nb/db, math.gcd(nb,db)))

        if math.gcd(nb,db) < 2:
            pretty = "{} / {}  {}".format(nb, db, fp)

            res.append ((pretty, best, (nb * f)/ db) )


# ...........................................................................
# usage message
# ...........................................................................
def usage(argv):
    print('usage : ' + argv[0] + ' -h help -t thresh -n numdenmax -m sqrtmax -v value -x top_n')
    os._exit(1)


# ...........................................................................
def takeSecond(elem):
    return elem[1]


# ...........................................................................
def main(argv):

    global timing

    time_start = time.time()

    thresh = 1e-9
    numdenmax = 10000
    sm = 3
    cm = 3
    target = math.pi
    top_n = 10

    try:
        # ...........................................................................
        # getopt command line argument handling
        # ...........................................................................

        a = argv

        opts, args = getopt.getopt(a[1:], 'h2:3:n:t:v:x:')  # @UnusedVariable

        for opt, arg in opts:
            if opt == '-h':
                usage( argv )

            elif opt in ("-t", "thresh"):
                thresh = float(arg)

            elif opt in ("-n", "numdenmax"):
                numdenmax = int(arg)

            elif opt in ("-2", "sqrtmax"):
                sm = int(arg)

            elif opt in ("-3", "cubemax"):
                cm = int(arg)

            elif opt in ("-v", "value"):
                target = float(arg)

            elif opt in ("-x", "top"):
                top_n = int(arg)

        for arg in args:
            target = float(arg)

    except:
        traceback.print_exc()

    res = ratap(target, numdenmax, sm, cm, thresh)

    print("\ntop {} best approximations to {}\n".format(top_n, target))

    for x in range (0, top_n):
        s = res[x]
        print("{:<25}{:.15f}\t{:.15f}".format(s[0], s[1], s[2]))

# ...........................................................................

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        traceback.print_exc()

# ...........................................................................
