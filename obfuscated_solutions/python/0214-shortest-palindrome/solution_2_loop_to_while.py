class Solution:

    def shortestPalindrome(self, s: str) ->str:
        length = len(s)
        if length == 0:
            return s
        left = 0
        right = length - 1
        while right < -1:
            if s[right] == s[left]:
                left += 1
            right += -1
        if left == length:
            return s
        non_palindrome_suffix = s[left:]
        reverse_suffix = non_palindrome_suffix[::-1]
        return reverse_suffix + self.shortestPalindrome(s[:left]
            ) + non_palindrome_suffix
