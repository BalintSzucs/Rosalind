#!/usr/bin/env python
'''
Problem Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

with open('rosalind_rna.txt') as infile:
	infile=infile.readline().replace('T','U')
	print(infile)