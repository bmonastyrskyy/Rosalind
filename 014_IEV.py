#!/usr/bin/python

# Problem Description:
# Recall the definition of the Fibonacci numbers from 
# "Rabbits and Recurrence Relations", which followed 
# the recurrence relation Fn=Fn-1+Fn-2 and assumed that 
# each pair of rabbits reaches maturity in one month and 
# produces a single pair of offspring (one male, one female)
# each subsequent month.
# Our aim is to somehow modify this recurrence relation to 
# achieve a dynamic programming solution in the case that 
# all rabbits die out after a fixed number of months.

# Given: Six positive integers, each of which does not 
# exceed 20,000. The integers correspond to the number of 
# couples in a population possessing each genotype pairing 
# for a given factor. In order, the six given integers 
# represent the number of couples having the following genotypes:
#  1  AA-AA
#  2  AA-Aa
#  3  AA-aa
#  4  Aa-Aa
#  5  Aa-aa
#  6  aa-aa

# Return: The expected number of offspring displaying the 
# dominant phenotype in the next generation, under the assumption 
# that every couple has exactly two offspring.
 

# Author : Bohdan Monastyrskyy

import sys

# usage function
def usage():
    print "USAGE: ", sys.argv[0], " <NO1> <NO2> <NO3> <NO4> <NO5> <NO6> ";
    print "<NOi> integers: - number of pairs of i-th type";
    print "  1  AA-AA";
    print "  2  AA-Aa";
    print "  3  AA-aa";
    print "  4  Aa-Aa";
    print "  5  Aa-aa";
    print "  6  aa-aa";
    print "The program is supposed to return expected value of offsprings"; 
    print " displaying the dominant phenotype in the next generation,";
    print " under assumption that every couple has two offsprings";
    sys.exit(2)

# function reads arguments and perform checking the format   
def readArgs():
    try:
	n1 = int(sys.argv[1]);
	n2 = int(sys.argv[2]);
	n3 = int(sys.argv[3]);
        n4 = int(sys.argv[4]);
	n5 = int(sys.argv[5]);
        n6 = int(sys.argv[6]);
	return (n1,n2,n3,n4,n5,n6);
    except IndexError, ValueError:
	usage();



# if run script directly
if (__name__ == "__main__"):
   (n1,n2,n3,n4,n5,n6) = readArgs()
   print 2*(n1 + n2 + n3 + 0.75*n4 + 0.5*n5 +0.0*n6)
