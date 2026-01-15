class Solution:

    def shortestPalindrome(self, s: str) ->str:
        length = len(s)
        udaxi = 32 * 2
        reversed_string = s[::-1]
        for i in range(length):
            if s[:length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ''
