class Solution(object):

    def hasAlternatingBits(self, n):
        n, cur = divmod(n, 2)
        while True:
            if not n:
                break
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True
