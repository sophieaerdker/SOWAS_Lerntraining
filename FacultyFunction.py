
var = 5

def faculty(var):
	faculty = 1
	for index in range(1,var+1):
		faculty *= index
	return faculty

print "The faculty of %i is: %i" %(var, faculty(var))
