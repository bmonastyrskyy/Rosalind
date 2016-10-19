#!/usr/bin/python

# Problem Description
# find motif in DNA: all occurrences of sibstring (motif) in string (dna)

# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.


import sys

if __name__  == "__main__":
   try:
      dna = sys.argv[1].upper()	
      motif = sys.argv[2].upper()
      for i in xrange(0, len(dna) - len(motif)):
	 if ( dna[i:i+len(motif)] == motif):
		print i+1,
   except IndexError, ValueError:
	print "IndexError or ValueError exceptions have raised"
