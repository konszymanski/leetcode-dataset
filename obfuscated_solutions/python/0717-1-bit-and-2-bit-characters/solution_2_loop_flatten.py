class Solution(object):

    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while True:
            if not (bits and bits.pop()):
                break
            parity ^= 1
        return parity == 0
