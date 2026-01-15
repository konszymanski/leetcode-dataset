class Solution:

    def longestPalindrome(self, s: str) ->str:

        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left = left + 1
                right = right - 1
            return True
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]
        return ''
