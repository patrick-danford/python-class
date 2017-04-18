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

#
# def sum(lower, upper, margin):
#     blanks = " " * margin
#     print blanks, lower, upper
#     if lower > upper:
#         print blanks, 0
#         return 0
#     else:
#         result = lower + sum(lower + 1, upper, margin + 4)
#         print blanks, result
#         return result
#
# sum (1, 4, 0
#      )


#April 13
"""
Book to read - the pragmatic programmer, Andy Hunt


Midterm
10 problems
1 - what does the code do.  Will get code, name the function/purpose
2 - write some test cases for a function.  write a function, write some tests. empty, odd even, 
    duplicates, negative, etc.  use the assert function
3 - Find the bugs.   Will get some code, find the bugs. Go over the "what kind of bugs" link posted
    in discussion.  syntax errors, range errors, could be a logical error (no error repoted in compiler, 
    but wrong answer given
4 - Will get a function or two.  We need to refactor - make it more efficient, easier to read, etc. 
    Refactoring is making the code better, more readble, more efficient etc. 
5 - Will get snippets of code, will need to say what the output is.  Will be base python, built in functions
6 - write a function to ...
7 - write a function to ... 
8 - Design a problem.  use case, features, psudocode, descriptions.  No code required really.  Write down 
    requirements and assumptions
9 - General programming question
10 - General programming question, like why do we write functions?  or general Qs about software dev, etc

other notes for test:  dont worry about classes.  Ends at higher order functions
We don't get to use a computer!!   Up to ch 6

"""


#function that takes a function as input

# def times_2(n):
#     return n * 2
#
# def greater_than_5(n):
#     if n > 5:
#         return n
# print filter(greater_than_5, range(10))
# print(map(times_2, range(10)))

# lambda - anonymous function

