#!/usr/bin/python

# Problem description
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective 
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


import sys

# read args
dna_string = sys.argv[1]
# upper case
dna_string = dna_string.upper()


print dna_string.count('A'), dna_string.count('C'), dna_string.count('G'), dna_string.count('T')
