class Solution(object):

    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k = k + 1
            target = target - k
        return k if target % 2 == 0 else k + 1 + k % 2