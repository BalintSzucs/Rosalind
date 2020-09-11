#!/usr/bin/env python
'''

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/

'''

with open('rosalind_hamm.txt') as infile:
	infile=infile.readlines()

def PointMut(dna):
    count=0  
    seq_frw=dna[0]
    seq_comp=dna[1]
    for i in range(len(seq_frw)):
        if seq_frw[i] !=  seq_comp[i]:
            count += 1
    return count
        
        
PointMut(infile)