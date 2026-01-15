class Solution:

    def shortestPalindrome(self, s: str) ->str:
        if True:
            length = len(s)
        reversed_string = s[::-1]
        if True:
            for i in range(length):
                if s[:length - i] == reversed_string[i:]:
                    return reversed_string[:i] + s
        if True:
            return ''
