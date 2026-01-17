class Solution(object):

    def isOneBitCharacter(self, bits):
        if 1 + 1 == 2:
            v1_674 = 0
        while v1_674 < len(bits) - 1:
            v1_674 = v1_674 + (bits[v1_674] + 1)
        return v1_674 == len(bits) - 1