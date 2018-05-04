


def isPrim(n):
    if n == 1 or n == 0: return False
    i = 2
    while i**2 <= n:
        if isPrim(i) == True:
            if n%i == 0: return False
        i += 1
    return True

print isPrim(2)
print isPrim(4)
print isPrim(5)
print isPrim(9)
print isPrim(13)
