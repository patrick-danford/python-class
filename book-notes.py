# coding=utf-8
#Ch 3.1
"""
Any number raised to the 0 power results in 1
"""

#notes:
"""product = 1
for count in xrange(4):
    product = product * (count + 1)
    print(product)

product2 = 1
for count in xrange(1,5):
    product = product * (count + 2)
    print product

for blamo in "Hello":
    print blamo

sum = 0
for count in xrange(2,20,2):
    sum = sum + count
    print sum

for count in xrange(10,0,-1):
    print count

range(10,1,-1)"""

# #exersises
# for count in xrange(5):
#     print count + 1
#
# print "\n"
#
# for count in xrange(1,4):
#     print count
#
# print "\n"
#
# for count in xrange(1, 6, 2):
#     print count + 1
#
# print "\n"
#
# for name in range(100):
#     name = "Patrick" + '\n'
#     print name
#
# for characters in range (1,128):
#     print chr(characters)
#
# testString = "This is a test"
# for convert in testString:
#     print ord(convert)
#
# #ch 3.2
#
# amount = 24.325
# print "Your salary is $%7f" % amount
#
# x = 1
# y = 2
# z = 3
# print "%18d" % x, y, z
#
# salaries = [100, 200, 300, 400]
#
# for numbers in salaries:
#     print "%12.2f" % numbers

#Ch 3.3

#Ch 3.5

# sum = 0
# for count in range(1,100):
#     sum += count
#     print sum

# sum = 0
# while count <= 100:
#     sum = sum + count
#     count += 1
#     print sum

# for count in range(100):
#     print count

# count = 0
# while count < 100:
#     count += 1
#     print count

# for count in range (1,101):
#     print count

# count = 0
# while count < 100:
#     count += 1
#     print count

# count = 0
# while True:
#     if count < 100:
#         count += 1
#         print count
#     else:
#         break

# for count in range(100,0,-1):
#     print count

# count = 101
# while count > 1:
#     count -= 1
#     print count

#
# for count in xrange(1, 101):
#     print count

# count = 0
# while count < 101:
#     count = count + 1
#     print count


# for count in xrange(100, 0, -1):
#     print count

# count = 101
# while count > 1:
#     count = count -1
#     print count

# n = input("Enter a number: ")
# product = 1
# for count in range(n):
#     product = product * (count + 1)
#     print product

# n = input("Enter a number: ")
# product = 1
# while product <= n + 1:
#     product = (product + 1)
#     sum = product * n
#     print sum

# m = input("Enter a number: ")
# n = input("Enter another number: ")
#
# if m >= 0 and m > n:
#     high = m
#     low = n
# else:
#     high = n
#     low = m
#
#
# diff = high - low
#
# print high, low, diff
# print "High is %d, low is %d, the difference is %d" % (high, low, diff)

# import math
#
# x = input("Enter a number: ")
# z = 1.0
# sq = math.sqrt(x)
#
# while z != sq:
#     z = (z + x / z) / 2
# print "The square root is %d" % sq

# import math
# x = input("Enter a number: ")
# start = 1.0
# tolerance = 0.0001
#
# while True:
#     start = (start + x / start) / 2
#     diff = abs(x - start ** 2)
#     if diff <= tolerance:
#         break
#
# print "Programs calculation: ", start
# print "Pythons calculation: ", math.sqrt(x)

# for count in xrange(10):
#     print count

# count = 5
# while count > 1:
#     print count
#     count -= 1

# sum = 0.0
# while True:
#     number = raw_input("Enter a number: ")
#     if number == "":
#         break
#         sum += float(number)
# import math
#
# side1 = input("What is the length of the first side?")
# side2 = input("What is the length of the second side?")
# side3 = input("What is the length of the third side?")
#
# side1sq = side1 ** 2
# side2sq = side2 ** 2
# side3sq = side3 ** 2
# twosidesq = side1sq + side2sq
#
# print side3sq,side2sq,side3sq, twosidesq
#
# if side1 == side2 and side1 == side3:
#     print "Equilateral"
# else:
#     print "Not equilateral"
#
# if twosidesq == side3sq:
#     print "Right Triangle"
# else:
#     print "Not Right Triangle"

# height = input("How high did you drop the ball from?")
# bounces = input("How many times did it bounce?")
# bounce_index = 0.6
#
# for distance in range(bounces - 1):
#     height = height + (height * bounce_index)
#     print height
#
# print "The ball traveled %f distance in total" % height
#
# initial_amount = input("How many organisms did you start with?")
# amount_now = input("How many do you have now?")
# time = input("How many hours have elapsed?")
#
# diff = (amount_now - initial_amount) / time
# print "The organisms have grown at a rate of %d per hour" % diff
# rate = (amount_now - initial_amount) % initial_amount * 100
# print "That is a growth rate of %f" % rate

# import math.pi

# starting_salary = 30000
# raise_percentage = .02
# new_salary = starting_salary + (starting_salary * raise_percentage)
# payout = 10
#
#
# print "Year %-3d%12d" % (1, starting_salary)
# for raises in range(2, payout + 1):
#     new_salary = new_salary + (new_salary * raise_percentage)
#     print "Year %-3d%12d" % (raises, new_salary)

# num1 = input("Input a numnber")
# num2 = input("Input another number")
#
# if num1 < num2:
#     high = num2
#     low = num1
# else:
#     high = num1
#     low = num2
#
# remain = high % low
# print remain
#
# while remain > 0:
#     new_remain = low % remain
#     print new_remain
# name = "Patrick Danford"
# for index in range(len(name)):
#     print (index, name[index])
#
# print name[:]
#
# mylist = ["file1.txt", "file2.exe", "file3.txt", "file4.txt"]
# for sort in mylist:
#     if ".txt" in sort:
#         print sort
#
# data = "myprogram.exe"
# print data[2]
# print data[-1]
# print len(data)
# # print data[2:-8]
#
# myString = "Patrick Danford"
# for chars in range(1, len(myString) + 1):
#     print (chars, myString[-chars])

#
# inputValue = raw_input("Input a lowercase word: ")
# distance = input("Enter a number for encryption distance: ")
# code = " "
#
# for ch in inputValue:
#     ordValue = ord(ch)
#     cipherValue = ordValue + distance
#     if cipherValue < ord('z'):
#         cipherValue = ord('a') + distance - \
#                       (ord('z') - ordValue + 1)
#         code += chr(cipherValue)
#
# print code

# for element in [5, 6, 7, 8]:
#     print element
#
# print 4 in [5]

# mylist = [1,2,3,4,5]
# print mylist
#
# entry = input("Enter another number: ")
# mylist.append(entry)
# print mylist
#
# entry2 = input("Enther another number: ")
# mylist.insert(0,entry2)
# print mylist
#
# mylist.pop(1)
# print "Now removing index 1"
# print mylist

# aList = [34, 45, 67]
# target = 46
# if target in aList:
#     print aList.index(target)
# else:
#     print -1

# aList = [2,3,1,4,5,9,0]
# print aList
# aList = aList.sort()
# print aList
#
# """
# fileName = raw_input(“Enter
# the
# filename: “)
# f = open(fileName, 'r')
#
# # Input the text, convert it to numbers, and
# # add the numbers to a list
# numbers = []
# for line in f:     words = line.split()
# for word in words:         numbers.append(float(word))
# # Sort the list and print the number at its midpoint
# numbers.sort()
# midpoint = len(numbers) / 2
# print “The
# median is”,
# if len(numbers) % 2 == 1:
#     print numbers[midpoint]
# else:
#     print (numbers[midpoint] + numbers[midpoint - 1]) / 2
# """

# fileName = raw_input("Enter the filename: ")
# f = open(fileName, 'r')
#
# numbers = []
# for line in f:
#     words = line.split()
#     for word in words:
#         numbers.append(float(word))
#
# numbers.sort()
# midpoint = len(numbers) / 2
# print "The median is",
# if len(numbers) % 2 == 1:
#     print numbers[midpoint]
# else:
#     print (numbers[midpoint]) + numbers[midpoint - 1] / 2

data = [5,3,7]
print data
print data[2]
print data[-1]
print len(data)
print tuple(data)
