#!/usr/bin/python

# Problem description:
# Given two strings s and t of equal length, the Hamming distance 
# between s and t, denoted dH(s,t), is the number of corresponding 
# symbols that differ in s and t.

# Given: Two DNA strings s and t of equal length

# Return: The Hamming distance dH(s,t)

# Author: Bohdan Monastyrskyy

import sys

def parseFile(infile):
    f = open(infile, 'r');
    result = [];
    # parse two lines
    i = 0
    for l in f :
	if (i > 1):
           break;
        l = l.strip()
	result.append(l);
	i += 1
    f.close()
    return result


def humming(dna1, dna2):
    if (not len(dna1) == len(dna2)):
	print "Lengths of dna's differ !!!"
	return -1.0;
    result = 0
    for i in xrange(0, len(dna1)):
	if (not dna1[i] == dna2[i]):
	   result += 1
    return result;


if (__name__ == "__main__"):
    try:
	infile = sys.argv[1]
	dnas = parseFile(infile)
	print humming(dnas[0], dnas[1])
    except IndexError:
	print "IndexError occurred"
    except IOError:
	print "IOError occurred"
    
