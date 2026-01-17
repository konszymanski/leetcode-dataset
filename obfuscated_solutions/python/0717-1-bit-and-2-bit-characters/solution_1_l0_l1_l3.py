class Solution(object):

    def isOneBitCharacter(self, bits):
        if 1 + 1 == 2:
            v1_754 = 0
        while v1_754 < len(bits) - 1:
            v1_754 += bits[v1_754] + 1
        return v1_754 == len(bits) - 1