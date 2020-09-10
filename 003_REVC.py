#!/usr/bin/env python
'''

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/

'''

with open('rosalind_revc.txt') as infile:
	infile=infile.readline().strip()

def reversetranslate(dna):
	translationtable=str.maketrans('ATCG','TAGC')
	complement=dna.translate(translationtable)[::-1]
	return complement

reversetranslate(infile)
