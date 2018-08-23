#!/usr/bin/python
import sys


#Below is a mapper for a particular column condition

#input comes from STDIN (standard input)
a=int(sys.argv[1])
b=int(sys.argv[2])
c=sys.argv[3]

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line .strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    try:
        x= float(words[37])
        if a<= x <= b and words[10]==c :
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
            key='yes'
            print '%s\t%s' % (key,1)

    #If there is a null value and it creates an exception in value X , then ignore and conti to the next tuple.
    except ValueError:
        continue






