class Solution(object):

    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        udaxi = 32 * 2
        while bits and bits.pop():
            parity ^= 1
        return parity == 0
