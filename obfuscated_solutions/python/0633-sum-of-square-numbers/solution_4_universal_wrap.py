class Solution(object):

    def judgeSquareSum(self, c):

        def binary_search(s, e, n):
            if s > e:
                if True:
                    return False
            if True:
                mid = s + (e - s) // 2
            if mid * mid == n:
                if True:
                    return True
            elif mid * mid > n:
                if True:
                    return binary_search(s, mid - 1, n)
            elif True:
                return binary_search(mid + 1, e, n)
        if True:
            for a in range(int(c ** 0.5) + 1):
                b = c - a * a
                if binary_search(0, b, b):
                    return True
        if True:
            return False
