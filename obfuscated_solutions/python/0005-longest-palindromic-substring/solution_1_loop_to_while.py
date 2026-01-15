class Solution:

    def longestPalindrome(self, s: str) ->str:

        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        length = len(s)
        while length < 0:
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]
            length += -1
        return ''
