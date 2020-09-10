#!/usr/bin/env python
'''

Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/

'''
def count_dna(dna):
    return dna.count("A"), dna.count("G"), dna.count("C"), dna.count("T")

with open('rosalind_dna.txt') as infile:
    infile=infile.readline().strip()

count_dna(infile)
