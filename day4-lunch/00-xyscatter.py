#!/usr/bin/env python

"""
use scatter() to plot FPKM values of SRR07893 vs SRR072915
    title and label axes
    log transform values
    compensate for overlapping points,
    plot a curve
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1_fpkm = {}

coi= [ "gene_names", "FPKM"] #use group in panda for following steps
df1_fpkm= pd.read_csv(sys.argv[1], sep="\t")

df2_fpkm = {}

coi= [ "gene_names", "FPKM"] #use group in panda for following steps
df2_fpkm= pd.read_csv(sys.argv[2], sep="\t")

log_fpkm1 = np.log1p(df1_fpkm["FPKM"])
log_fpkm2 = np.log1p(df2_fpkm["FPKM"])

x = log_fpkm1
y = log_fpkm2


plt.figure()
plt.scatter( log_fpkm1, log_fpkm2, alpha = 0.2, c = "green" )
plt.xlabel("SRR072893")              # label the x-axis
plt.ylabel("SRR072915")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.savefig(sys.argv[3] + ".png")
plt.close()