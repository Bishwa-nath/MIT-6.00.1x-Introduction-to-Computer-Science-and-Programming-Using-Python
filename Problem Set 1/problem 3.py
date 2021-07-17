#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh

#In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

#Note: This problem may be challenging.
# We encourage you to work smart.
# If you've spent more than a few hours on this problem,
# we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

# Paste your code into this box 

res = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(res) < len(c)):
            res = c
            c = char
        else:
            c = char
if (len(c) > len(res)):
    res = c

print(res)