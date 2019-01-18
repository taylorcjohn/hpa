#!/usr/bin/env python
# ...........................................................................
# ratap.py
#
# 2019-01-18 10:00
#
# ...........................................................................
#
# 2019-01-17 15:10 ratio
# 2019-01-17 18:00 sqrt added
# 2019-01-17 18:30 top results ordered
# 2019-01-17 19:00 remove sqrt for natural squares e.g. sqrt(4), sqrt(9)
# 2019-01-17 21:00 cube root added (-3)
# 2019-01-18 10:00 enable_tau
#
# ...........................................................................

import traceback
import math
import getopt
import os
import sys
import time


# ...........................................................................
def ratap(target, numdenmax, sm, cm, thresh, enable_tau):

    global results

    results = []

    ratap_p(target, numdenmax, thresh, 1.0,      "ratio")

    ratap_p(target, numdenmax, thresh, math.pi,  "* Pi")

    if enable_tau:
        tau = math.pi * 2.0
        ratap_p(target, numdenmax, thresh, tau, "* Tau")

    ratap_p(target, numdenmax, thresh, math.e,   "* e")

    for s in range (2,sm+1):
        if (math.sqrt(s)-int(math.sqrt(s)) > 0):
            ratap_p(target, numdenmax, thresh, math.sqrt(s), "* sqrt({})".format(s))

    for s in range (2,cm+1):
        if (math.pow(s,1.0/3)-int(math.pow(s,1.0/3)) > 0):
            ratap_p(target, numdenmax, thresh, math.pow(s,1.0/3), "* cbrt({})".format(s))

    results = sorted(results, key=takeSecond, reverse=False)

    return results

# ...........................................................................
def ratap_p(target, numdenmax, thresh, fixed, fixed_p):

    global n, d, t, nb, db, best, results, f, fp

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

    global n, d, t, nb, db, best, results, f, fp

    if ( t < best ):
        nb = n
        db = d
        best = t
        # print("{} / {}  best {}  value {} gcd {}".format(nb, db, best, nb/db, math.gcd(nb,db)))

        if math.gcd(nb,db) < 2:
            pretty = "{} / {}  {}".format(nb, db, fp)

            results.append ((pretty, best, (nb * f)/ db) )


# ...........................................................................
# usage message
# ...........................................................................
def usage(argv):
    print('usage : ' + argv[0] + ' -h help -t thresh -n numdenmax -m sqrtmax -v value -x top_n -2 sqrtmax -3 cubemax ')
    os._exit(1)


# ...........................................................................
def takeSecond(elem):
    return elem[1]


# ...........................................................................
def main(argv):

    global timing

    time_start = time.time()

    thresh = 1e-9
    numdenmax = 1000
    sm = 3
    cm = 3
    target = math.pi
    top_n = 10
    enable_tau = False

    try:
        # ...........................................................................
        # getopt command line argument handling
        # ...........................................................................

        a = argv

        opts, args = getopt.getopt(a[1:], 'hb2:3:n:t:v:x:')  # @UnusedVariable

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

            elif opt in ("-b", "tau"):
                enable_tau = not enable_tau

        for arg in args:
            target = float(arg)

        results = ratap(target, numdenmax, sm, cm, thresh, enable_tau)

        print("\ntop {} best approximations to {}\n".format(top_n, target))

        print("{:<25}{:15}\t{:15}\n".format("approximation","error","value"))

        for x in range (0, top_n):
            s = results[x]
            print("{:<25}{:.15f}\t{:.15f}".format(s[0], s[1], s[2]))

    except:
        traceback.print_exc()

# ...........................................................................

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        traceback.print_exc()

# ...........................................................................
