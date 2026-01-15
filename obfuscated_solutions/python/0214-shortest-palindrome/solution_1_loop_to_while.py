class Solution:

    def shortestPalindrome(self, s: str) ->str:
        length = len(s)
        reversed_string = s[::-1]
        i = 0
        while i < length:
            if s[:length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
            i += 1
        return ''
