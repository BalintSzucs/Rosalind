#!/usr/bin/env python
'''
Problem Title: Finding a Shared Motif
Rosalind ID: LCSM
Rosalind #: 012
URL: http://rosalind.info/problems/lcsm/

'''
def long_substr(data):
    substr=''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True    

sequence=[]
seq=''  
with open('rosalind_lcsm.txt') as infile:
    for line in infile:
        if line.startswith('>'):
            if seq != '':
                sequence.append(seq)
                seq=''
        else:
            seq += line
            seq=seq.replace('\n','')
            seq=seq.replace('\r','')
    if seq != '':
        sequence.append(seq)
        seq=''


long_substr(sequence)




