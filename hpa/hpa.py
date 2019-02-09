#!/usr/bin/env python
# ...........................................................................
# hpa.py
#
# 2019-02-07 09:45
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
# 2019-01-22 12:15 kwargs passed to hpa()
# 2019-01-22 12:30 simplify code
# 2019-01-22 12:35 reciprocals "over"
# 2019-01-25 22:00 rearrange
# 2019-02-03 14:00 rename as hpa
# 2019-02-03 14:00 hpa_report
# 2019-02-03 18:00 output format changes
# 2019-02-03 18:00 recip is an option -r
# 2019-02-04 16:20 switch to argparse
# 2019-02-06 18:30 show settings using -s or -S for verbose
# 2019-02-06 18:40 remove traceback for clean help
# 2019-02-07 09:45 clarify skip squares 4, 9, 16 cubes 8, 27 etc. -s True by default
#
# ...........................................................................

import traceback
import math
import argparse
import os
import sys
# for python2:
# from fractions import gcd

# ...........................................................................
# high precision approximation
#
# return sorted list of triplets : [text of approximation, error, actual value]
# ...........................................................................
def hpa(target, **kwargs):

    global results, settings_short, settings_verbose

    results = []

    settings_short = ""
    settings_verbose = []

    ndmax   = kwargs['ndmx']
    sm      = kwargs['sm']
    cm      = kwargs['cm']
    thresh  = kwargs['thr']
    recip   = kwargs['enable_recip']

    hpa_p(target, ndmax, thresh, 1.0, "ratio")
    settings_short = "settings: nd {} sm {} cm {}".format(ndmax, sm, cm)

    settings_verbose.append("{:<35} : {}".format("numerator/denominator limit", ndmax))

    settings_verbose.append("{:<35} : {}".format("square root max", sm))

    settings_verbose.append("{:<35} : {}".format("cube root max", cm))

    if recip:
        settings_short = settings_short + " recip"
        settings_verbose.append("{:<35} : {}".format("matching reciprocals", True))

    if kwargs['enable_e']:
        hpa_pr(target, ndmax, thresh, math.e, "e", recip)
        settings_short = settings_short + " e"
        settings_verbose.append("{:<35} : {}".format("matching e", True))

    if kwargs['enable_pi']:
        hpa_pr(target, ndmax, thresh, math.pi, "Pi", recip)
        settings_short = settings_short + " pi"
        settings_verbose.append("{:<35} : {}".format("matching pi", True))

    if kwargs['enable_phi']:
        phi = (1 + 5 ** 0.5) / 2
        hpa_pr(target, ndmax, thresh, phi, "Phi", recip)
        settings_short = settings_short + " phi"
        settings_verbose.append("{:<35} : {}".format("matching phi", True))

    if kwargs['enable_tau']:
        tau = math.pi * 2.0
        hpa_pr(target, ndmax, thresh, tau, "Tau", recip)
        settings_short = settings_short + " tau"
        settings_verbose.append("{:<35} : {}".format("matching tau", True))

    for s in range (2,sm+1):
        a = math.sqrt(s)
        b = int(math.sqrt(s))
        # skip squares 4, 9, 16 etc
        if a > b:
            hpa_pr(target, ndmax, thresh, math.sqrt(s), "sqrt({})".format(s), recip)

    for s in range (2,cm+1):
        a = math.pow(s,1.0/3)
        b = int(math.pow(s,1.0/3))
        # skip cubes 8, 27 etc
        if a > b:
            hpa_pr(target, ndmax, thresh, math.pow(s,1.0/3), "cbrt({})".format(s), recip)

    results = sorted(results, key=takeSecond, reverse=False)

    return results


# ...........................................................................
# call with and without reciprocal
# ...........................................................................
def hpa_pr(tval, numdenmax, thresh, multiplier, rp, recip):

    hpa_p(tval, numdenmax, thresh, multiplier, "* " + rp)

    if recip:
        hpa_p(tval, numdenmax, thresh, 1.0/multiplier, "* recip " + rp)


# ...........................................................................
def hpa_p(tval, numdenmax, thresh, fixed, fixed_p):

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
            d = math.floor( (n * f)/ tval )
            try:
                t = ((n * f)/ d) - tval
            except:
                t = math.inf
                # for python2 : t = float("inf")
            test_ratio()

            d += 1

            t = ((n * f) / d) - tval
            test_ratio()

    except:
        traceback.print_exc()


# ...........................................................................
def test_ratio():

    global n, d, t, nb, db, best, results, f, fp

    if ( abs(t) < best ):
        nb = n
        db = d
        best = abs(t)
        # print("{} / {}  best {}  value {} gcd {}".format(nb, db, best, nb/db, math.gcd(nb,db)))

        # greatest common divisor used to avoid redundant ratios
        if math.gcd(nb,db) < 2: # for python2 : if gcd(nb, db) < 2:
            pretty = "({} / {})  {}".format(nb, db, fp)

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
# call hpa and report result set
# ...........................................................................
def hpa_report(target, top_n, **kwargs):

    global settings_short, settings_verbose

    # ...........................................................................
    # remember if negative
    # ...........................................................................
    if (target < 0):
        tneg = True
        tval = 0.0 - target
        sign = "-"
    else:
        tneg = False
        tval = target
        sign = " "

    results = hpa(tval, **kwargs)

    try:
        if kwargs['settings']:
            print("")
            print(" {:<35}".format(settings_short))

        if kwargs['verbose']:
            print("")
            for s in settings_verbose:
                print(" {:<35}".format(s))

        print("\n top {} best approximations to {}\n".format(top_n, target))
        print("{:<35}{:21}{:15}\n".format(" approximation","  error", "value"))

        try:
            for x in range (0, top_n):
                s = results[x]

                if (s[1] < 0):
                    errsign = "-"
                else:
                    errsign = " "

                print("{}{:<35}{}{:.15f}\t{:.15f}".format(sign, s[0], errsign, abs(s[1]), s[2]))
        except:
            pass

    except:
        traceback.print_exc()


# ...........................................................................
def main(argv):

    global timing, tval, settings_short

    settings_short = None

    try:
        # ...........................................................................
        # argparse command line argument handling
        # ...........................................................................
        parser = argparse.ArgumentParser(description='hpa : high precision approximation')

        parser.add_argument('-p', '--pi',  action='store_true', default=False, help='enable Pi matching')
        parser.add_argument('-i', '--phi', action='store_true', default=False, help='enable Phi matching')
        parser.add_argument('-b', '--tau', action='store_true', default=False, help='enable Tau matching')
        parser.add_argument('-e', '--e',   action='store_true', default=False, help='enable e matching')
        parser.add_argument('-r', '--r',   action='store_true', default=False, help='enable reciprocal matching')
        parser.add_argument('-s', '--s',   action='store_true', default=False, help='show settings')
        parser.add_argument('-S', '--S',   action='store_true', default=False, help='show verbose settings')

        parser.add_argument('-n', '--ndmx',     action='store', type=int, default=1000, help='numerator and denominator limit')
        parser.add_argument('-2', '--sqrt',     action='store', type=int, default=10,   help='square root max integer value')
        parser.add_argument('-3', '--cbrt',     action='store', type=int, default=10,   help='cube root max integer value')
        parser.add_argument('-x', '--top',      action='store', type=int, default=10,   help='number of approximations')
        parser.add_argument('-t', '--thr',      action='store', type=float, default=1e-9, help='sensitivity threshold value')
        parser.add_argument('-v', '--val',      action='store', type=float, default=None, help='value to approximate')
        parser.add_argument('value', nargs='?', action='store', type=float, default=None, help='value to approximate')

        args = parser.parse_args()

        rargs = {}
        rargs['thr']          = args.thr
        rargs['ndmx']         = args.ndmx
        rargs['sm']           = args.sqrt
        rargs['cm']           = args.cbrt
        rargs['enable_pi']    = args.pi
        rargs['enable_phi']   = args.phi
        rargs['enable_e']     = args.e
        rargs['enable_tau']   = args.tau
        rargs['enable_recip'] = args.r
        rargs['settings']     = args.s
        rargs['verbose']      = args.S

        if args.val is None:
            args.val = args.value

        # ...........................................................................
        # call hpa
        # ...........................................................................
        if args.val is None:
            args.val = math.pi

        target = args.val
        top_n = args.top

        hpa_report(target, top_n, **rargs)

    except:
        pass
#       traceback.print_exc()


# ...........................................................................

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        traceback.print_exc()

# ...........................................................................
