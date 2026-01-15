class Solution(object):

    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i = i + (bits[i] + 1)
        return i == len(bits) - 1
