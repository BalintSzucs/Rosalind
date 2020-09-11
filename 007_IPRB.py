#!/usr/bin/env python
'''
Problem Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/

'''

def firstLaw(k,m,n):
   N = float(k+m+n)
   return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))

with open('rosalind_iprb.txt') as infile:
    for line in infile:
        line=line.split()

firstLaw(int(line[0]), int(line[1]), int(line[2]))    