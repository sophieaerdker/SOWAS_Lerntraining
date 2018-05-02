
var = 6

def faculty(n):
	if n == 1 or n == 0: return 1
	return faculty(n-1) * n

print "The faculty of %i is: %i" %(var, faculty(var))
