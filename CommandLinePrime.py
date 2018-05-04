import sys
from recursivePrime import isPrim

n = int(sys.argv[1]) #sys.argv is a list with strings
#you entered in the command line after 'python', thus
#sys.argv[0] is always the file name! The function int()
#parses the string to an integer

if isPrim(n) is True: print "%i is a prime number!" %n
else: print "%i is not a prime number!" %n
