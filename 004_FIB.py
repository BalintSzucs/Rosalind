#!/usr/bin/env python
'''

Problem Title: Rabbits and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 004
URL: http://rosalind.info/problems/fib/

'''

def rabbits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return rabbits(n-1, k) + k*rabbits(n-2, k)

rabbits(29,2)