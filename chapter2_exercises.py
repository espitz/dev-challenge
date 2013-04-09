# Name:espitz
# exercise 2.1: 
01
010
0100
01000
zip code = '02492' # zip must be a string. 01 etc are octal expressions. 
# exercise 2.2
5
x = 5
x + 1
# output is 
5
5
6
print 5
print x = 5
print x + 1
print x = 5 # yields syntaxerror 
# exercise 2.3
width = 17
height = 12.0
delimeter = '.'
width/2 # = 8, int
width/2.0 # =  8.5, float
height/3 # = 4.0, float
1 + 2 * 5 # = 11, int
delimeter * 5 # = '.....', str
# exercise 2.4
4 * (pi * 5 ** 3) # = 523.5
bookcost = 24.95
discount = 0.4
shipcost = 3 + (x - 1) * 0.75
x = 60
(x * bookcost + shipcost) * discount # = 617.7$
seconds = 1
minutes = 60 * seconds
hours = 60 * minutes
easypace = 8 + 15/seconds
tempo = 7 + 12/seconds
(6 + 52/minutes) + (easypace * 2 + tempo * 3)/minutes # = 7.5 hours