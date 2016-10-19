#!/usr/bin/python

# Problem Description:
# When finding the n-th term of a sequence defined 
# by a recurrence relation, we can simply use the 
# recurrence relation to generate terms for progressively 
# larger values of n. This problem introduces us to the 
# computational technique of dynamic programming, which 
# successively builds up solutions by using the answers 
# to smaller cases.

# Given: Positive integers n<=40 and k<=5.

# Return: The total number of rabbit pairs that will be 
# present after n months if we begin with 1 pair and in 
# each generation, every pair of reproduction-age rabbits 
# produces a litter of k rabbit pairs (instead of only 1 pair).

# Author : Bohdan Monastyrskyy

import sys

# usage function
def usage():
    print "USAGE: ", sys.argv[0], " <NO_MONTHS> <NO_OFSPRINGS>";
    print "<NO_MONTHS> and <NO_OFFSPRINGS> must be integeres";
    sys.exit(2)

# function reads arguments and perform checking the format   
def readArgs():
    try:
	# number of months
	n = int(sys.argv[1]);
	# number of rabbit pairs in a litter
	k = int(sys.argv[2]);
	return (n,k);
    except IndexError, ValueError:
	usage();

def fibonacci(n,k):
    if (n == 1 or n == 2):
	return 1;
    else:
	return k*fibonacci(n-2,k) + fibonacci(n-1,k);


# if run scritp directly
if (__name__ == "__main__"):
   (n,k) = readArgs()
   print "Number of rabbits pairs with reproductivity rate", k, "after", n, "months is :"
   print  fibonacci(n,k);
