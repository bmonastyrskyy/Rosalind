#!/usr/bin/python

# Problem description:
# For a collection of strings and a positive integer k, 
# the overlap graph for the strings is a directed graph 
# Ok in which each string is represented by a node, and 
# string s is connected to string t with a directed edge 
# when there is a length k suffix of s that matches a 
# length k prefix of t, as long as s<>t; we demand s<>t
# to prevent directed loops in the overlap graph 
# (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format 
# having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. You 
# may return edges in any order.

# Author: Bohdan Monastyrskyy

import sys

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


# method compares k-tail of str1 with k-prefix of str2
# if they are the same return true
def ismated(str1, str2, k=3):
    suffix = str1[-k:]
    prefix = str2[0:k]
    if (suffix == prefix):
	return True;
    else:
	return False;


if __name__ == "__main__":
    try:
	infile = sys.argv[1];
	dnas = parseFasta(infile)
	for idd1 in sorted(dnas.iterkeys()):
	    for idd2 in sorted(dnas.iterkeys()):
		if (not idd2 == idd1):
		    if (ismated(dnas[idd1], dnas[idd2])):
			print idd1, idd2
    except IndexError:
	print "USAGE:", sys.argv[0], "<FASTA_FILE>"
	sys.exit(1)


