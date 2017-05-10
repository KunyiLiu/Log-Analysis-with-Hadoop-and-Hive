#!/usr/bin/env python

from operator import itemgetter
import sys


current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if word == 'Jul':
        current_count += count

print '%s\t%s' % ('bandwidth', current_count)
