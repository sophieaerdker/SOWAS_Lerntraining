
var = 5
faculty = 1

for index in range(1,var+1):
# range(1, var+1) creates list with step 1, the last element is var
	faculty *= index

print "The faculty of %i is: %i" %(var,faculty)
