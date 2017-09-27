#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

vcol = []
afnum = []

data = open(sys.argv[1])

for line in data:
    if line.startswith ("#"):
        continue
    else:
        line = line.split("\t")
        vcfcol = line[7].split(";")
    
    af = vcfcol[3][3:]
    if "," in af:
        af = af.split(",")
        for i in af:
            afnum.append(float(i))
    else:
        afnum.append(float(af))

plt.hist(afnum)
plt.title("SacC Plot")
plt.xlabel("Allele")
plt.ylabel("Frequency")
plt.savefig("Allele Plot")
plt.close
