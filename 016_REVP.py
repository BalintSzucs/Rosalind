#!/usr/bin/env python

'''
Problem Title: Locating Restriction Sites
Rosalind ID: REVP
Rosalind #: 016
URL: http://rosalind.info/problems/perm/
'''

def reverstranslation(s):
    translationtable=str.maketrans('ATCG','TAGC')
    complement=s.translate(translationtable)[::-1]
    return complement

result=[]
with open('rosalind_revp.txt') as infile:
	headline=infile.readline()
	dna=infile.read().strip()

for i in range(len(dna)):
    for j in range(4,13):
        if i + j > len(dna):
            continue
            
        s1=dna[i:i+j]
        s2=reverstranslation(s1)
        
        if s1 == s2:
            result.append((i+1,j))

print ("\n".join([' '.join(map(str, r)) for r in result]))