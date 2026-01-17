class Solution(object):

    def isOneBitCharacter(self, bits):
        v1_132 = bits.v2_130()
        while bits and bits.v2_130():
            v1_132 = v1_132 ^ 1
        return v1_132 == 0