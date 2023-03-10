#!/usr/bin/python3
"""
a script markdown2html.py that takes an argument 2 strings
"""

import sys
import os

if __name__ == "__main__":

    n = len(sys.argv)
    if (n < 3):
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)

    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "a") as r:
            list_is_open = False
            or_list_is_open = False

            for line in f:
                if line.startswith("#"):
                    if list_is_open is True:
                        r.write("</ul>\n")
                        list_is_open = False
                    if or_list_is_open is True:
                        r.write("</ol>\n")
                        or_list_is_open = False
                    new_l = line.strip("# ")
                    a = new_l.rstrip('\n')
                    count_tag = line.count("#")
                    r.write(f"<h{count_tag}>{a}</h{count_tag}>\n")
                if line.startswith("-"):
                    if list_is_open is False:
                        r.write("<ul>\n")
                        list_is_open = True
                    new_l = line.strip("- ")
                    a = new_l.rstrip('\n')
                    r.write(f"<li>{a}</li>\n")
                else:
                    if list_is_open is True:
                        r.write("</ul>\n")
                        list_is_open = False
                if line.startswith("*"):
                    if or_list_is_open is False:
                        r.write("<ol>\n")
                        or_list_is_open = True
                    new_l = line.strip("* ")
                    a = new_l.rstrip('\n')
                    r.write(f"<li>{a}</li>\n")
                else:
                    if or_list_is_open is True:
                        r.write("</ol>\n")
                        or_list_is_open = False
            if or_list_is_open is True:
                r.write("</ol>\n")
            if list_is_open is True:
                r.write("</ul>\n")
                list_is_open = False
    exit(0)
