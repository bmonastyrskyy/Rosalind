#!/usr/bin/python

# Problem description
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.
# (substitute 'T' with 'U')

import sys

# read args
dna_string = sys.argv[1]
# upper case
rna_string = dna_string.upper().replace('T','U')

print rna_string
