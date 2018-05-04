
limit = 10000
Fibonacci = [0,1] #starting point
#the new element is the sum of the last to elements:
newElement = Fibonacci[-1]+Fibonacci[-2]

while(newElement < limit) :

	Fibonacci.append(newElement)
	newElement = Fibonacci[-1] + Fibonacci[-2]

print Fibonacci
