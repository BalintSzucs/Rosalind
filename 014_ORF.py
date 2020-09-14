#!/usr/bin/env python
'''
Problem Title: Open Reading Frames
Rosalind ID: ORF
Rosalind #: 014
URL: http://rosalind.info/problems/orf/

'''
codon={"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
            "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
            "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
            "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

with open('rosalind_orf', 'r') as infile:
    infile.readline()
    dna=''
    for line in infile:
        dna+=line.strip()
    dna=list(dna)

rnareverse=[]

for i in range(len(dna)):
    ind=len(dna)-1-i
    if dna[ind]=="T":
        dna[ind]="U"
        rnareverse.append("A")
    else:
        if dna[ind] == "A":
            rnareverse.append("U")
        else:
            if dna[ind]=="C":
                rnareverse.append("G")
            else:
                rnareverse.append("C")

rna=''.join(dna)
rnareverse=''.join(rnareverse)


answer=[]
for i in range(len(rna)-2):
    if rna[i:i+3]=='AUG':
        j=i
        prot=''
        letter='AUG'
        while codon[letter]!="Stop":
            prot+=codon[letter]
            j+=3
            if j>len(rna)-3:
                break
            letter=rna[j:j+3]
        if codon[letter]=="Stop" and prot not in answer:
            answer.append(prot)

for i in range(len(rnareverse)-2):
    if rnareverse[i:i+3]=='AUG':
        j=i
        prot=''
        letter='AUG'
        while codon[letter]!="Stop":
            prot+=codon[letter]
            j+=3
            if j>len(rnareverse)-3:
                break
            letter=rnareverse[j:j+3]
        if codon[letter]=="Stop" and prot not in answer:
            answer.append(prot)

for i in answer:
    print(i)