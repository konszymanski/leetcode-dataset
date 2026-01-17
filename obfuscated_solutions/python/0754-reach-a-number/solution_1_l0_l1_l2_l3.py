class Solution(object):

    def reachNumber(self, target):
        target = abs(target)
        v1_877 = 0
        while target > 0:
            v1_877 = v1_877 + 1
            target = target - v1_877
        return v1_877 if target % 2 == 0 else v1_877 + 1 + v1_877 % 2