#!/usr/bin/python

'''
Problem Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/

'''
with open('rosalind_subs.txt') as infile:
    infile=infile.read().split()
    for i in range(len(infile[0])):
        if infile[0][i:].startswith(infile[1]):
            print(i+1)
        
        