
def isPrim(n):
    if n == 1 or n == 0: return False # end condition
    i = 2
    while i**2 <= n:
        #check if i is prime, if its True
        #test wether n can be divides by it:
        if isPrim(i) == True:
            if n%i == 0: return False
        i += 1
    return True
