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

# Given: Positive integers n<=100 and m<=20.

# Return: The total number of rabbit pairs that will 
# remain after n months if all rabbits live for m months 

# Author : Bohdan Monastyrskyy

import sys

# usage function
def usage():
    print "USAGE: ", sys.argv[0], " <NO_MONTHS> <LIFE_LENGTH>";
    print "<NO_MONTHS> and <LIFE_LENGTH> (in months) must be integeres";
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

# slow: function calculates finanacci series recursively
def fibonacciReccur(n,k):
    if (n == 1 or n == 2):
	return 1;
    else:
	return k*fibonacciReccur(n-2,k) + fibonacciReccur(n-1,k);

# fast: function calculates fibobacci serries in loop
def fibonacciLoop(n,k):
    if (n == 1 or n == 2):
        return 1;
    else:
	result = 1;
	previous = 1;
	for i in xrange(3, n+1):
	   tmp = result;
	   result = result + k*previous;
	   previous = tmp;
        return result;


# function fibonacci sequence when rabbits die after m months
def fibonacciMortal(n,k,m): 
    born = [];
    adult = [];
    dead = [];
    for i  in xrange(0,n):
	if (i == 0):
		born.append(1);
		adult.append(0);
        if (i >= m - 1):
                dead.append(born[i-m + 1]);
        else:
                dead.append(0);
	if (i >= 1):
		adult.append(adult[i-1] + born[i-1] - dead[i-1]);
		born.append(k*adult[i-1]);
    return (born[-1] + adult[-1])


# if run script directly
if (__name__ == "__main__"):
   (n,m) = readArgs()
   print fibonacciMortal(n,1,m)
