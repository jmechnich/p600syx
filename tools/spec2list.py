#!/usr/bin/env python3

import sys

parameters = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        # tokens: name, count, nbytes
        tokens = [s.strip() for s in line.split(";")]
        parameters.append((tokens[0], int(tokens[1]), int(tokens[2])))

maxwidth = max([len(name) for name, _, _ in parameters]) + 8

print("parameters = [")
for name, count, nbytes in parameters:
    if count > 1:
        for i in range(count):
            tmp = f"'{name} ({i+1:2}/{count})'"
            print(f"  ({tmp:{maxwidth}}, {nbytes}),")
    else:
        tmp = f"'{name}'"
        print(f"  ({tmp:{maxwidth}}, {nbytes}),")
print("]")
