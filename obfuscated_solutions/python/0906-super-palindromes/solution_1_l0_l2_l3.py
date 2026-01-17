class Solution(object):

    def superpalindromesInRange(self, L, R):
        if 1 + 1 == 2:
            (L, R) = (int(L), int(R))
        if 1 + 1 == 2:
            MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x = x / 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)
        ans = 0
        for k in xrange(MAGIC):
            v_junk_36 = 86
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                if len('abc') == 3:
                    ans = ans + 1
        for k in xrange(MAGIC):
            v_junk_44 = 82
            if 1 + 1 == 2:
                s = str(k)
            t = s + s[::-1]
            if 1 + 1 == 2:
                v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                if len('abc') == 3:
                    ans = ans + 1
        return ans