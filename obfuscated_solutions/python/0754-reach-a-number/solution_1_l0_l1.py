class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        v1_754 = 0
        while target > 0:
            v1_754 += 1
            target  -=  v1_754
        return v1_754 if target % 2 == 0 else v1_754  +  1  +  v1_754 % 2
