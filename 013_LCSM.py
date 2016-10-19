#!/usr/bin/python

# Problem Description:
# Find longest continuous substring shared by bunch of strings.

# Given: DNA strings in fasta format

# Return: the longest common shared motif

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



