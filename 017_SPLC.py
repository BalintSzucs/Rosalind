#!/usr/bin/env python

'''
Problem Title: RNA splicing
Rosalind ID: SPLC
Rosalind #: 017
URL: http://rosalind.info/problems/perm/
'''


RNA_CODON_TABLE = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def removeIntrons(dnaSequence, intron):
    dnaSequence = dnaSequence.replace(intron, '')
    return dnaSequence

def replaceCodons(rnasequence):
    i = 0
    protein = ""
    rnasequence = rnasequence.replace("\n","")
    while (i < len(rnasequence)):
        if(RNA_CODON_TABLE[rnasequence[i:i+3]]== 'STOP'):
            break
        protein += RNA_CODON_TABLE[rnasequence[i:i + 3]]
        i += 3
    protein = protein.replace('STOP','')
    print(protein)
    
with open('rosalind_splc.txt') as infile:
    infile=infile.readlines()
    i=1
    tempString=''
    inputStrings=[]
    while(i<len(infile)):
        if(infile[i].__contains__('>')):
            inputStrings.append(tempString)
            tempString=''
            i+=1
        elif(i==len(infile)-1):
            inputStrings.append(infile[i]) #Input string is a list containing ALL the sequences quary and motif both
            i+=1
        else:
            tempString +=infile[i] #I can add a list elements by not assigning specifics just saying I to a string.
            i+=1
    inputStrings[0] = inputStrings[0].replace('\n', '')
    i=1
    while (i < len(inputStrings)):
        inputStrings[i] = inputStrings[i].replace('\n','')
        inputStrings[0] = removeIntrons(inputStrings[0],inputStrings[i])
        i+=1
    inputStrings[0] = inputStrings[0].replace('T','U')
    replaceCodons(inputStrings[0])


        



