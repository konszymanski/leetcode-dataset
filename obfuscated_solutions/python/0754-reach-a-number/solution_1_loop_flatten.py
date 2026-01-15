class Solution(object):

    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while True:
            if not target > 0:
                break
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2
