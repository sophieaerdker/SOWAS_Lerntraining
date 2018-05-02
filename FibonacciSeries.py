
limit = 10000
Fibonacci = [0,1]
newElement = Fibonacci[-1]+Fibonacci[-2]

while(newElement < limit) :
	
	Fibonacci.append(newElement)
	newElement = Fibonacci[-1] + Fibonacci[-2]

print Fibonacci
