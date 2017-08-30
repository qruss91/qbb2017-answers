#!/usr/bin/env python

"""
match kmers in a fasta file
"""

import sys
import fasta
#length of sequence being examined

kmer_position = {}

target = open(sys.argv[1])


kmer_length = -int(sys.argv[-1])

kmer_target = {}

for ident, sequence in fasta.FASTAReader( target ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - kmer_length ):
        kmer_sequence = sequence[i:i+kmer_length]
        if kmer_sequence not in kmer_target:
             kmer_target[kmer_sequence] = [ident]
             kmer_target[kmer_sequence].append(i)
        else:
            kmer_target[kmer_sequence].append(i)

query = open(sys.argv[2])

ident, sequence = fasta.FASTAReader( query ).next()
    
for i in range( 0, len(sequence) - kmer_length ):
    sequence = sequence.upper()
    query_kmer = sequence[i:i+kmer_length]
    if query_kmer in kmer_target:
        value = kmer_target[query_kmer]
        for p in range(len(value)-1):
            print value [0], value [p+1], i, query_kmer

