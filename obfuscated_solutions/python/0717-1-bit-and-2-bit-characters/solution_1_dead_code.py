class Solution(object):

    def isOneBitCharacter(self, bits):
        i = 0
        udaxi = 32 * 2
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
