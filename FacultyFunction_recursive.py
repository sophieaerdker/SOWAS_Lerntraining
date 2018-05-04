
var = 6

def faculty(n):
	if n == 1 or n == 0: return 1
	return faculty(n-1) * n
	#Because n! is the same as n*(n-1)!
	#The end condition is n=1

print "The faculty of %i is: %i" %(var, faculty(var))
