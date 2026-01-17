class Solution(object):

    def reachNumber(self, target):
        if 1 + 1 == 2:
            target = abs(target)
        if 1 + 1 == 2:
            k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2