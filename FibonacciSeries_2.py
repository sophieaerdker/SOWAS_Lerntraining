
limit = 10000
Fibonacci = [0,1]
newElement = Fibonacci[-1]+Fibonacci[-2]
sumEven = 0

while(newElement < limit) :
	
	if newElement%2 == 0: sumEven += newElement
	Fibonacci.append(newElement)
	newElement = Fibonacci[-1] + Fibonacci[-2]
	

print "The Fibonacci Series until %i is:" %limit
print Fibonacci
print "The sum of its even numbers is %i" %sumEven


