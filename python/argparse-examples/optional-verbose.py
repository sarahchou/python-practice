import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
"""This program deomnstrates the use of optional arguments"""
if args.verbose:
    print "verbosity turned on"
