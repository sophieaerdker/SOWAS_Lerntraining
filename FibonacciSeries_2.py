
limit = 10000
Fibonacci = [0,1] #starting point
#the new element is the sum of the last to elements:
newElement = Fibonacci[-1]+Fibonacci[-2]
sumEven = 0

while(newElement < limit) :

	# add the new element to sumEven if its even:
	if newElement%2 == 0: sumEven += newElement
	Fibonacci.append(newElement)
	newElement = Fibonacci[-1] + Fibonacci[-2]


print "The Fibonacci Series until %i is:" %limit
print Fibonacci
print "The sum of its even numbers is %i" %sumEven
