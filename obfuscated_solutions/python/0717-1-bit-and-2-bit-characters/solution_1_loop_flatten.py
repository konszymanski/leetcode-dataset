class Solution(object):

    def isOneBitCharacter(self, bits):
        i = 0
        while True:
            if not i < len(bits) - 1:
                break
            i += bits[i] + 1
        return i == len(bits) - 1
