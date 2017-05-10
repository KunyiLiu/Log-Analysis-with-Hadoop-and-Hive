#!/usr/bin/env python

import re as re
import sys

for line in sys.stdin:
    m=re.search(r'(^.*) - - \[(.*)\] "(\S+|[^" ]*)([^H]*)([^"]*)" ([\d-]+) ([\d-]+$)',line)
    word=m.groups()[5]
    print '%s - %s' % (word, 1)
