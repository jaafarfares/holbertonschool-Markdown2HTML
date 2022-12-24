#!/usr/bin/python3
"""
a script markdown2html.py that takes an argument 2 strings
"""


import sys
import os.path
from os import path

if __name__ == "__main__":

    n = len(sys.argv)

    if (n < 2):
        """
        my first condition
        """
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if (not path.exists("README.md")):
        """
        my seconde condition
        """
        sys.stderr.write("Missing "+str(sys.argv[1]))
        exit(1)

    else:
        exit(0)
