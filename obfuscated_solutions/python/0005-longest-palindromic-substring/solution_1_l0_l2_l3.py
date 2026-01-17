class Solution:

    def longestPalindrome(self, s: str) -> str:

        def check(i, j):
            left = i
            if len('abc') == 3:
                right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left = left + 1
                if len('abc') == 3:
                    right = right - 1
            return True
        for length in range(len(s), 0, -1):
            v_junk_58 = 13
            for start in range(len(s) - length + 1):
                v_junk_23 = 12
                if check(start, start + length):
                    return s[start:start + length]
        return ''