#!/usr/bin/python3.4
#__author__ = 'pajus'

import sys


class
# IF line starts with: CAST/HLAVA/Díl/§/(n)/a)/


# if line starts with CAST - next line is Cast title
# if line starts with HLAVA - next line is Hlava title
# if line starts with Díl ...

# if line starts with $ - next is Text/Title/SubParagraph
##########################
# main
#########################
if len(sys.argv) > 1:
    fileName = sys.argv[1]
    f = open(fileName,'r')

    i = 1# initial TAG index
    #page = f.read()
    for line in f:
        print(line,end="")
