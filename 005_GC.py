#!/usr/bin/env python
'''
Problem Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/

'''

def GCcontent(dna):
    gc_count = dna.count('G') + dna.count('C')
    gc_fraction = float(gc_count) / len(dna)
    print(100 * gc_fraction)  

seq=''
with open('rosalind_gc.txt') as infile:
    for line in infile:
        if line.startswith('>'):
            label = line[1:]
            if seq != '':
                print(label)
                seq_list=list(seq)
                GCcontent(seq)
                seq='' 
        else:
            seq += line.strip()
            
if seq != '':
    print(label)
    dna_list=list(seq)
    GCcontent(seq)
    seq=''
