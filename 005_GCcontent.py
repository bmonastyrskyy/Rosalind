#!/usr/bin/python

# Problem description
# The GC-content of a DNA string is given by the percentage
# of symbols in the string that are 'C' or 'G'. For example, 
# the GC-content of "AGCTATAG" is 37.5%. Note that the 
# reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated 
# into a database. A commonly used method of string labeling 
# is called FASTA format. In this format, the string is 
# introduced by a line that begins with '>', followed by some 
# labeling information. Subsequent lines contain the string 
# itself; the first line to begin with '>' indicates the 
# label of the next string.

# In Rosalind's implementation, a string in FASTA format will
# be labeled by the ID "Rosalind_xxxx", where "xxxx" 
# denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, 
# followed by the GC-content of that string. Rosalind allows 
# for a default error of 0.001 in all decimal answers unless 
# otherwise stated; please see the note on absolute error below.

# Author : Bohdan Monastyrskyy

import sys

# reversed complementary DNA
def countGC(dna):
    return 100.0*(dna.upper().count('C') + dna.upper().count('G'))/len(dna)

def parseFasta(fastafile):
    f = open(fastafile, 'r');
    result = {} # dictionary with key - id, value -string
    curr_id = ''
    for l in f :
	l = l.strip()
	if (l.startswith('>')):
	   curr_id = l[1:]
	   result[curr_id] = ''
	else:
	   result[curr_id] += l.upper()
    f.close()
    return result

# read args
fasta_file = sys.argv[1]
# parse dnas
dnas = parseFasta(fasta_file)

maxGC = 0.0
maxID = ''
# loop over dnas
for idd, dna in dnas.iteritems():
    curGC = countGC(dna)
    if (maxGC <= curGC):
	maxGC = curGC;
	maxID = idd; 

print maxID
print maxGC

