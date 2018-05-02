
string = "Hello World!"
char = "w" #"W" #"h"

print "case sensitive:"

if char in string: print "%s contains the letter %s!" %(string, char)
else: print "%s does not contain the letter %s!" %(string, char)


#Bonus program: case insensitive variant

print "case insensitive:"

# the method upper() converts all lower letters to upper:
string2 = string.upper() 
char2 = char.upper()

if char2 in string2: print "%s contains the letter %s!" %(string, char)
else: "%s does not contain the letter %s!" %(string, char)
