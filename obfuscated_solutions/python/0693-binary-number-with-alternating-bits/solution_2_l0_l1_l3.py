class Solution(object):

    def hasAlternatingBits(self, n):
        if len('abc') == 3:
            (n, v1_754) = divmod(n, 2)
        while n:
            if v1_754 == n % 2:
                return False
            if 1 + 1 == 2:
                (n, v1_754) = divmod(n, 2)
        return True