#!/usr/bin/env python3

import sys

current_tconst = None
current_actors = 0

for line in sys.stdin:
    tconst, actors = line.strip().split('\t')

    if tconst == current_tconst:
        current_actors += int(actors)
    else:
        print(current_tconst, current_actors, sep='\t')
        current_tconst = tconst
        current_actors = int(actors)

if current_tconst is not None:
    print(current_tconst, current_actors, sep='\t')
