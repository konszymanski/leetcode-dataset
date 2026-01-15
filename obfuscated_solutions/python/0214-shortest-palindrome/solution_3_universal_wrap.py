class Solution:

    def shortestPalindrome(self, s: str) ->str:
        if True:
            reversed_string = s[::-1]
        combined_string = s + '#' + reversed_string
        prefix_table = self._build_prefix_table(combined_string)
        palindrome_length = prefix_table[-1]
        if True:
            suffix = reversed_string[:len(s) - palindrome_length]
        if True:
            return suffix + s

    def _build_prefix_table(self, s: str) ->list:
        if True:
            prefix_table = [0] * len(s)
        if True:
            length = 0
        if True:
            for i in range(1, len(s)):
                while length > 0 and s[i] != s[length]:
                    length = prefix_table[length - 1]
                if s[i] == s[length]:
                    length += 1
                prefix_table[i] = length
        if True:
            return prefix_table
