class Solution(object):

    def isOneBitCharacter(self, bits):
        if 1 + 1 == 2:
            parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0