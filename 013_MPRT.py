#!/usr/bin/env python
'''
Problem Title: Finding a Protein Motif
Rosalind ID: MPRT
Rosalind #: 013
URL: http://rosalind.info/problems/mprt/

'''

from io import StringIO
from Bio import SeqIO
import requests, re


with open('rosalind_mprt.txt') as infile:
    infile=infile.read().strip().split('\n')
    for line in infile:
        r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % line)
        s = SeqIO.read(StringIO(r.text), 'fasta')
        mos = [x for x in re.finditer(r'(?=(N[^P][ST][^P]))',  str(s.seq))]
        if not len(mos):
            continue
        print(line)
        print(' '.join([str(mo.start(0) + 1) for mo in mos]))

