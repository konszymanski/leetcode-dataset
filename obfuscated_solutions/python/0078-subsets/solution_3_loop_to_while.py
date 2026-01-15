nth_bit = 1 << n
i = 0
while i < nth_bit:
    bitmask = bin(i | nth_bit)[3:]
    i += 1
