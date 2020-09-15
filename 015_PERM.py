#!/usr/bin/env python

'''
Problem Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 015
URL: http://rosalind.info/problems/perm/
'''

from itertools import permutations

def permGene(s): 
    info = int(s.read())
             
    count = 0  
    number = list(permutations(range(1,info + 1)))
    
    for i in number:
        count+=1
    print(count)

    for i in number:
        print(' '.join(map(str,i)))

with open('rosalind_perm.txt') as infile:
	permGene(infile)
  
    





