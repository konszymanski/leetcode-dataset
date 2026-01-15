i = 2 ** n
while i < 2 ** (n + 1):
    bitmask = bin(i)[3:]
    i += 1
