#!/usr/bin/env python3

import sys

for line in sys.stdin:
    tconst, _, _, category, _, _ = line.strip().split('\t')

    if tconst == "tconst":
        continue

    if category in ["actor", "actress", "self"]:
        print(tconst, 1, sep='\t')
    else:
        print(tconst, 0, sep='\t')
