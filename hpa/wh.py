#!/usr/bin/env python
# ...........................................................................
# wh.py
#
# 2019-02-09 12:00
#
# ...........................................................................
#
# 2019-02-09 12:00 wh: who, why, where etc, - all questions
#
# ...........................................................................

import math
import argparse
import sys
import traceback
import os


# ...........................................................................
def main(argv):
    try:

        # print("\ngetcwd :{0}".format(os.getcwd()))
        print('')
        # files_path = [os.path.abspath(x) for x in os.listdir()]
        for x in sorted(os.environ):
            print("{0}\t{1}".format(x, os.environ.get(x)))

        # print("{0}".format(sys.version_info))
        # print("default encoding {0}".format(sys.getdefaultencoding()))        # print("maximu# m Unicode code point {0}".format(hex(sys.maxunicode)))

    except:
        pass
        traceback.print_exc()


# ...........................................................................

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        traceback.print_exc()

# ...........................................................................
