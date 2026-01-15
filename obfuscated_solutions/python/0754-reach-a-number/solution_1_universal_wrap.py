class Solution(object):

    def reachNumber(self, target):
        if True:
            target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        if True:
            return k if target % 2 == 0 else k + 1 + k % 2
