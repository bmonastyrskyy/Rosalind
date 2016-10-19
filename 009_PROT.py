#!/usr/bin/python

# Description of the Problem

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

# Author: Bohdan Monastyrskyy

import sys

RNA2PROT = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
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

if __name__ == "__main__":
   try:
	rna = sys.argv[1].upper()
	result = ""
	for i in xrange(0, len(rna), 3):
	    try:
		if (RNA2PROT[rna[i:i+3]] == 'STOP'):
		   break;
		result = result + RNA2PROT[rna[i:i+3]]
	    except IndexError:
		print "IndexError exception";
	    except KeyError:
		print rna[i:i+3], " is not a coddon"
	print result
   except IndexError, NameError:
	print "IndexError raised"
