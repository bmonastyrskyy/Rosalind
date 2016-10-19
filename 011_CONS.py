#!/usr/bin/python

# Problem Description

# Given: A collection of at most 10 DNA strings of equal 
# length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the 
# collection. (If several possible consensus strings exist,
# then you may return any one of them.)

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

# convert multiple sequence alignment to profile
def msa2prof(msa):
    prof = []
    for idd, seq in msa.iteritems():
	for i in xrange(0, len(seq)):
	     try:
		prof[i][seq[i]] = prof[i][seq[i]] + 1;
	     except IndexError:
		prof.append({'A':0, 'C':0, 'G':0, 'T':0})
		prof[i][seq[i]] = prof[i][seq[i]] + 1;
    return prof;

# print profile
def printProf(prof):
    for a in ['A', 'C', 'G', 'T']:
	print "%s:" % a,
	for i in xrange(0, len(prof)):
		print prof[i][a],
	print ""

# extract consensus string from profile
def prof2consStr(prof):
    result = "";
    for i in xrange(0, len(prof)):
	a = 'A'
	for key in ['A', 'C', 'G', 'T']:
	    if prof[i][key] > prof[i][a]:
		a = key
	result = result + a
    return result


if __name__ == "__main__":
    infile = ""
    try:
    	infile = sys.argv[1]
    except IndexError:
	print "USAGE:", sys.argv[0], " <MSA_FILE> "
	sys.exit(1)
    msa = parseFasta(infile);
    prof = msa2prof(msa);
    print prof2consStr(prof)
    printProf(prof)
