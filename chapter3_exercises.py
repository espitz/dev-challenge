# Exercises for chapter 3:

# Name: espitz
#exercise 3.1 
print_lyrics ()
#Traceback (most recent call last):
  #File "<pyshell#0>", line 1, in <module>
    #print_lyrics ()
#NameError: name 'print_lyrics' is not defined
#exercise 3.2
def repeat_lyrics ():
	print_lyrics ()
	print_lyrics ()

def print_lyrics ():
	print "I'm a lumberjack and I'm okay"
	print "I sleep all night and I work all"
#SyntaxError: invalid syntax  # highlights def print_lyrics
# exercise 3.3
>>> def right_justify (part1, part2):
	justify = part1 + part2
	print (justify)


>>> part1 = ' '*70
>>> part2 = 's'
>>> right_justify (part1, part2)
#exercise 3.4
>>> def do_twice (f, z):
	f(z)
	f(z)

	
>>> def print_twice (z):
	print (z)
	print (z)

	
>>> do_twice (print_twice, 'spam')
>>> do_four(print_twice, 'spam')