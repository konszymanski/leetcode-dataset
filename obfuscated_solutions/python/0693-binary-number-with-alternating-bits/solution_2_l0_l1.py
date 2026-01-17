class Solution(object):
    def hasAlternatingBits(self, n):
        n, v1_754 = divmod(n, 2)
        while n:
            if v1_754 == n  %  2: return False
            n, v1_754 = divmod(n, 2)
        return True
