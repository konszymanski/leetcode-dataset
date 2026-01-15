class Solution(object):

    def superpalindromesInRange(self, L, R):
        if True:
            L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            if True:
                return ans

        def is_palindrome(x):
            if True:
                return x == reverse(x)
        if True:
            ans = 0
        if True:
            for k in xrange(MAGIC):
                s = str(k)
                t = s + s[-2::-1]
                v = int(t) ** 2
                if v > R:
                    break
                if v >= L and is_palindrome(v):
                    ans += 1
        if True:
            for k in xrange(MAGIC):
                s = str(k)
                t = s + s[::-1]
                v = int(t) ** 2
                if v > R:
                    break
                if v >= L and is_palindrome(v):
                    ans += 1
        if True:
            return ans
