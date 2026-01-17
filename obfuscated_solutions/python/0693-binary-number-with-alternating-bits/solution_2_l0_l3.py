class Solution(object):

    def hasAlternatingBits(self, n):
        if 1 + 1 == 2:
            (n, cur) = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False
            (n, cur) = divmod(n, 2)
        return True