class Solution(object):

    def judgeSquareSum(self, c):

        def binary_search(s, e, n):
            if s > e:
                return False
            mid = s + (e - s) // 2
            if mid * mid != n:
                if mid * mid <= n:
                    return binary_search(mid + 1, e, n)
                else:
                    return binary_search(s, mid - 1, n)
            else:
                return True
        for a in range(int(c ** 0.5) + 1):
            b = c - a * a
            if binary_search(0, b, b):
                return True
        return False