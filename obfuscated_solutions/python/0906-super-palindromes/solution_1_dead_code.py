class Solution(object):

    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            exdvx = 70 * 2
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans
        udaxi = 32 * 2

        def is_palindrome(x):
            snbac = 28 * 2
            return x == reverse(x)
        ans = 0
        for k in xrange(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        for k in xrange(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        return ans
