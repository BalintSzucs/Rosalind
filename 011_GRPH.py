#!/usr/bin/env python
'''
Problem Title: Overlap Graphs
Rosalind ID: GRPH
Rosalind #: 011
URL: http://rosalind.info/problems/grph/

'''

import sys, networkx as nx
from Bio import SeqIO

G=nx.Graph()            
k=3
with open('rosalind_grph.txt.fasta','r') as infile:
    fasta_sequences = list(SeqIO.parse(infile, 'fasta'))
for fasta1 in fasta_sequences:
    for fasta2 in fasta_sequences:
        name1, sequence1 = fasta1.id, str(fasta1.seq)
        name2, sequence2 = fasta2.id, str(fasta2.seq)
        if sequence1 == sequence2:
            continue
        if sequence1[-k:] == sequence2[:k]:
                print(name1,name2)
                G.add_edge(name1,name2)  
nx.write_graphml_lxml(G,'OverlapGraph.graphml') 