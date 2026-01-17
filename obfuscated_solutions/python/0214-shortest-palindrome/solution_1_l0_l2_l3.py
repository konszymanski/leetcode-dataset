class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if 1 + 1 == 2:
            length = len(s)
        reversed_string = s[::-1]
        for i in range(length):
            v_junk_13 = 72
            if s[:length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ''