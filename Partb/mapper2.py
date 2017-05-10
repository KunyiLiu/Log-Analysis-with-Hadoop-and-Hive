#!/usr/bin/env python

import re as re
import sys

for line in sys.stdin:
    m=re.search(r'(^.*) - - \[(.*)\] "(\S+|[^" ]*)([^H]*)([^"]*)" ([\d-]+) ([\d-]+$)',line)
    byte=m.groups()[6]
    month=(m.groups()[1]).split('/')[1]
    byte=byte.strip()
    month=month.strip()
    if month == 'Jul' and byte != '-':
        print '%s\t%s' % (month, byte)