"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

foo_txt = open('foo.txt', 'r')

def foo_read():
 for line in foo_txt:
  print(line, end='')

print(foo_read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

bar_txt = open('bar.txt', 'r+')

bar_txt.write('The marathon continues, Stay ten toes down, It\'s not on you, it\'s in you.')

print(bar_txt.read())