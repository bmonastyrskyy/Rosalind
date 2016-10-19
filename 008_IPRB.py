#!/usr/bin/python

# Description of the Problem
# Given: Three positive integers k, m, and n, representing
# a population containing k+m+n organisms: k individuals 
# are homozygous dominant for a factor, m are heterozygous, 
# and n are homozygous recessive.

# Return: The probability that two randomly selected mating 
# organisms will produce an individual possessing a dominant 
# allele (and thus displaying the dominant phenotype). 
# Assume that any two organisms can mate.

# Author: Bohdan Monastyrskyy

import sys

# number of combinations k of n
def c(k,n):
    if (k > n or k < 0 or n < 0):
	raise ValueError("Bad parameters of function c(k,n): k =", k , "n = ", n)
    if (n == 0 or n == 1):
	return 1;
    result =  1.0;
    for i in xrange(0,k):
	result = result * (n - i) / (i + 1);
    return result;  

def probDominant(k, m, n):
    return (1.0 - (c(2,n) + c(2,m)*0.25 +c(1,m)*c(1,n)*0.5)/(c(2,k+m+n)));

def usage():
    print ""
    print "USAGE: ", sys.argv[0], "k m n"
    print "The script calculates the probability of getting dominant allele "
    print "in an offspring from randamly selected parents from the pool: k , m , n"
    print "k - number of individuals which are homozygous dominant for a factor,"
    print "m are heterozygous, and n are homozygous recessive"
    print ""
    sys.exit(1)

if __name__ == "__main__":
   try:
      k, m, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
   except IndexError, ValueError:
      usage()
   print probDominant(k, m, n)

