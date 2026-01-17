class Solution(object):

    def hasAlternatingBits(self, n):
        (n, v1_323) = divmod(n, 2)
        while n:
            if v1_323 == n % 2:
                return False
            (n, v1_323) = divmod(n, 2)
        return True