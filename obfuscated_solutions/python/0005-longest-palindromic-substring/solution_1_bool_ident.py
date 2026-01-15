class Solution:

    def longestPalindrome(self, s: str) ->str:

        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right] and 1 + 1 == 2:
                    return False
                left += 1
                right -= 1
            return True
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length) and 1 + 1 == 2:
                    return s[start:start + length]
        return ''
