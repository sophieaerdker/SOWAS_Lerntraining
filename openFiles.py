
print "Writing..."
file = open("example.txt", 'w') #open file in write-modus
file.write("Hello World!")   # writes the string "Hello World!" into example.txt
file.close() # make sure you close your file!

file = open("example.txt", 'r') #opens file in read-only modus
print file.read(5) #reads until a number of 5 bytes is reached
print file.read() # tries to read as much as possible, starting from the last point
file.close()

print "\nAppending..."
file = open("example.txt", 'a') #appends modus
file.write("Hello there!") #appends the string to the file
file.close()

file = open("example.txt", 'r')
print file.read()
file.close()

print "\nOpen with write but write nothing:"
file = open("example.txt", 'w')
file.close()

file = open("example.txt", 'r')
print file.read()
file.close()
