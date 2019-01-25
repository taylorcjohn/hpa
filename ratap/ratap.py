#!/usr/bin/env python
# ...........................................................................
# ratap.py
#
# 2019-01-22 12:35
#
# ...........................................................................
#
# 2019-01-17 15:10 ratio
# 2019-01-17 18:00 sqrt added
# 2019-01-17 18:30 top results ordered
# 2019-01-17 19:00 remove sqrt for natural squares e.g. sqrt(4), sqrt(9)
# 2019-01-17 21:00 cube root added (-3)
# 2019-01-18 10:00 enable_tau
# 2019-01-18 12:00 tau calculated to avoid 3.7 requirement
# 2019-01-18 12:10 enable_phi
# 2019-01-18 12:30 enable_e
# 2019-01-18 17:30 sign fixes
# 2019-01-22 11:00 add enable_pi for consistency (default=True)
# 2019-01-22 12:15 kwargs passed to ratap()
# 2019-01-22 12:30 simplify code
# 2019-01-22 12:35 reciprocals "over"
#
# ...........................................................................

import traceback
import math
import getopt
import argparse
import os
import sys
import time
# for python2:
# from fractions import gcd

# ...........................................................................
def ratap(target, **kwargs):

    global results

    results = []

    numdenmax   = kwargs['numdenmax']
    sm          = kwargs['sm']
    cm          = kwargs['cm']
    thresh      = kwargs['thresh']

    ratap_p(target, numdenmax, thresh, 1.0, "ratio")

    if kwargs['enable_pi']:
        ratap_p(target, numdenmax, thresh, math.pi, "* Pi")
        ratap_p(target, numdenmax, thresh, 1.0/math.pi, "over Pi")

    if kwargs['enable_tau']:
        tau = math.pi * 2.0
        ratap_p(target, numdenmax, thresh, tau, "* Tau")
        ratap_p(target, numdenmax, thresh, 1.0/tau, "over Tau")

    if kwargs['enable_e']:
        ratap_p(target, numdenmax, thresh, math.e, "* e")
        ratap_p(target, numdenmax, thresh, 1.0/math.e, "over e")

    if kwargs['enable_phi']:
        phi = (1 + 5 ** 0.5) / 2
        ratap_p(target, numdenmax, thresh, phi, "* Phi")
        ratap_p(target, numdenmax, thresh, 1.0/phi, "over Phi")

    for s in range (2,sm+1):
        if (math.sqrt(s)-int(math.sqrt(s)) > 0):
            ratap_p(target, numdenmax, thresh, math.sqrt(s), "* sqrt({})".format(s))

    for s in range (2,cm+1):
        if (math.pow(s,1.0/3)-int(math.pow(s,1.0/3)) > 0):
            ratap_p(target, numdenmax, thresh, math.pow(s,1.0/3), "* cbrt({})".format(s))

    results = sorted(results, key=takeSecond, reverse=False)

    return results

# ...........................................................................
def ratap_p(tval, numdenmax, thresh, fixed, fixed_p):

    global n, d, t, nb, db, best, results, f, fp, tneg

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
            d = math.floor( (n * f)/ tval )
            try:
                t = ((n * f)/ d) - tval
            except:
                t = math.inf
                # for python2 : t = float("inf")
            test()

            d += 1

            t = ((n * f) / d) - tval
            test()

    except:
        traceback.print_exc()


# ...........................................................................
def test():

    global n, d, t, nb, db, best, results, f, fp

    if ( abs(t) < best ):
        nb = n
        db = d
        best = abs(t)
        # print("{} / {}  best {}  value {} gcd {}".format(nb, db, best, nb/db, math.gcd(nb,db)))

        # greatest common divisor used to avoid redundant ratios
        if math.gcd(nb,db) < 2: # for python2 : if gcd(nb, db) < 2:
            pretty = "{} / {}  {}".format(nb, db, fp)

            try:
                results.append ((pretty, t, (nb * f)/ db) )
            except:
                pass


# ...........................................................................
# usage message
# ...........................................................................
def usage(argv):
    print('usage : ' + argv[0] + ' -h help -t thresh -n numdenmax -m sqrtmax -v value -x top_n -2 sqrtmax -3 cubemax ')
    os._exit(1)


# ...........................................................................
def takeSecond(elem):
    return abs(elem[1])


# ...........................................................................
def main(argv):

    global timing, tval, tneg

    time_start = time.time()

    target = math.pi
    thresh = 1e-9
    numdenmax = 1000
    sm = 10
    cm = 10
    top_n = 10
    enable_e = True
    enable_pi = True
    enable_tau = False
    enable_phi = False
    rargs = {}

    try:
        # ...........................................................................
        # getopt command line argument handling
        # ...........................................................................

        a = argv

        opts, args = getopt.getopt(a[1:], 'hbeip2:3:n:t:v:x:')  # @UnusedVariable

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
`
            elif opt in ("-e", "exp"):
                enable_e = not enable_e

            elif opt in ("-b", "tau"):
                enable_tau = not enable_tau

            elif opt in ("-p", "pi"):
                enable_pi = not enable_pi

            elif opt in ("-i", "phi"):
                enable_phi = not enable_phi

        for arg in args:
            target = float(arg)

        # ...........................................................................
        # remember if negative
        # ...........................................................................

        if (target < 0):
            tneg = True
            tval = 0.0 - target
        else:
            tneg = False
            tval = target

        rargs ['thresh']     = thresh
        rargs ['numdenmax']  = numdenmax
        rargs ['sm']         = sm
        rargs ['cm']         = cm
        rargs ['enable_pi']  = enable_pi
        rargs ['enable_phi'] = enable_phi
        rargs ['enable_e']   = enable_e
        rargs ['enable_tau'] = enable_tau

        results = ratap(tval, **rargs)

        print("\ntop {} best approximations to {}\n".format(top_n, target))

        print("{:<25}{:23}{:15}\n".format(" approximation","  error", "value"))

        try:
            if tneg:
                sign = "-"
            else:
                sign = " "

            for x in range (0, top_n):
                s = results[x]

                if (s[1] < 0):
                    errsign = "-"
                else:
                    errsign = " "

                print("{}{:<25}{}{:.15f}\t{:.15f}".format(sign, s[0], errsign, abs(s[1]), s[2]))
        except:
            pass

        time_end = time.time()

#        if args.time:
#            print("{0:0.2f} seconds".format(time_end - time_start))

    except:
        traceback.print_exc()

# ...........................................................................

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        traceback.print_exc()

# ...........................................................................
