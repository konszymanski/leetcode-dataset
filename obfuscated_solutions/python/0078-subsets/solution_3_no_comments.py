nth_bit = 1 << n
for i in range(nth_bit):  
    
    bitmask = bin(i | nth_bit)[3:]