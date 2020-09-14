#!/usr/bin/env python
'''
Problem Title: Consensus and Profile
Rosalind ID: CONS
Rosalind #: 010
URL: http://rosalind.info/problems/cons/

'''

from Bio import SeqIO
import numpy


sequences = []                             
with open('rosalind_cons.txt') as infile:
    for record in SeqIO.parse(infile, 'fasta'):  
        sequence = []                         
        for nt in record.seq:                 
            sequence.extend(nt)              
        sequences.append(sequence)            
file.close() 

profile = [[0]*len(sequences)]*4                                                  
profile = numpy.zeros((4, len(sequences[0])), dtype=numpy.int)
for i,line in enumerate(sequences):                           
    for j, nt in enumerate(line):                            
        if nt == 'A':                                       
            profile[0][j] += 1                             
        elif nt == 'C':                                     
            profile[1][j] += 1                             
        elif nt == 'G':                                     
            profile[2][j] += 1                             
        elif nt == 'T':                                     
            profile[3][j] += 1  
            
consensus = ''                                                  
for A,C,G,T in zip(profile[0],profile[1],profile[2],profile[3]):
    if A >= C and A >= G and A >= T:                           
        consensus += 'A'                                      
    elif C >= A and C >= G and C >= T:                         
        consensus += 'C'                                      
    elif G >= A and G >= C and G >= T:                         
          consensus += 'G'                                      
    elif T >= A and T >= C and T >= G:                         
        consensus += 'T'  

print(consensus)                                   
print('A: ' + ' '.join(str(e) for e in profile[0]))
print('C: ' + ' '.join(str(e) for e in profile[1]))
print('G: ' + ' '.join(str(e) for e in profile[2]))
print('T: ' + ' '.join(str(e) for e in profile[3]))