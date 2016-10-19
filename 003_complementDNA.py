#!/usr/bin/python

# Problem description
# reverse complementery of DNA
# Given: A DNA string s having length at most 1000 nt.
# Return: The reverse complementery string of s.
# (substitute 'T' <-> 'A', 'C' <-> 'G' )

import sys

# reversed complementary DNA
def rvrsComplDNA(dna):
    if len(dna) == 1:
	if (dna == 'C'):
	   return 'G'
        if (dna == 'G'):
	   return 'C'
	if (dna == 'A'):
	   return 'T'
	if (dna == 'T'):
	   return 'A'

    return rvrsComplDNA(dna[1:]) + rvrsComplDNA(dna[0])

# read args
dna_string = sys.argv[1]
# use function rvrsComplDNA
compl_dna = rvrsComplDNA(dna_string.upper())

print compl_dna 
