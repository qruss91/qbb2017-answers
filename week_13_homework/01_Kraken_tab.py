#!/usr/bin/env python

"""

Release the Kraken

"""

import sys

tax={}

for line in open(sys.argv[1]):
    if line.strip().split("\t")[1] not in tax:
        tax[line.strip().split("\t")[1]]=1
    else:
        tax[line.strip().split("\t")[1]]+=1
for t in tax:
    print str(tax[t]) + "\t" + "\t".join(t.split(";"))
#krakdict = {}
#for line in krakdict:
#    if line not in krakdict:
#        krakdict[line] = 1
#    else:
#        krakdict[line] += 1


#grep ">" bin.1.fa | head
#grep NODE_25_length_13321 ../KRAKEN/assembly.kraken