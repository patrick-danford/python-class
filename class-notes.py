# March 21
"""
Look into len, enumerate, min, max, tuples, generator, lazy evaluation,
Play around with debugger
"""

# stock_prices_yesterday = [10,20,30,40,30,20,10,20]
# maxvalue = max(stock_prices_yesterday)
# minvalue = min(stock_prices_yesterday)
# print (maxvalue, minvalue)
# print stock_prices_yesterday.index(maxvalue)
#
#
#
# #for i in stock_prices_yesterday:


# March 28

# import argparse

"""
If main guard = When python interpereter reads a file it executes all of it. the
if __name__ = __main__ is implemented it will allow you to restict when the
imported file gets executed
"""
"""
Look at argparse.  What does it actually do?
Look at raising an exception intentionally

"""

# type (2.01)


# March 30

"""
In the command line you can type 'man' before any command and get the manual. 
ex - man wc   returns manual for the wc (word count) command

A set can only have each item once.  A list can have duplicates

"""

#April 6
"""
cygwin, linux terminal for windows
Look ar geek stuff, 50 most commonly used commands

"""


def sum(lower, upper, margin):
    blanks = " " * margin
    print blanks, lower, upper
    if lower > upper:
        print blanks, 0
        return 0
    else:
        result = lower + sum(lower + 1, upper, margin + 4)
        print blanks, result
        return result

sum (1, 4, 0
     )


#April 13
"""
Book to read - the pragmatic programmer, Andy Hunt
"""