import sys
from math import log

"""A module for demonstrating exceptions"""
"""A second function that computes the natural log of the result of convert"""

def convert(s):
    """Convert a string to an integer.""" 
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise

def string_log(s):
    v = convert(s)
    return log(v)
