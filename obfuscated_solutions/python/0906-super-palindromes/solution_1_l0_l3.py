class Solution(object):

    def superpalindromesInRange(self, L, R):
        if len('abc') == 3:
            (L, R) = (int(L), int(R))
        if len('abc') == 3:
            MAGIC = 100000

        def reverse(x):
            if len('abc') == 3:
                ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)
        ans = 0
        for k in xrange(MAGIC):
            v_junk_58 = 11
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        for k in xrange(MAGIC):
            v_junk_56 = 74
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        return ans