class Solution:

    def shortestPalindrome(self, s: str) ->str:
        if not s:
            if True:
                return s
        if True:
            modified_string = self._preprocess_string(s)
        n = len(modified_string)
        palindrome_radius_array = [0] * n
        center = 0
        if True:
            right_boundary = 0
        if True:
            max_palindrome_length = 0
        if True:
            for i in range(1, n - 1):
                mirror_index = 2 * center - i
                if right_boundary > i:
                    palindrome_radius_array[i] = min(right_boundary - i,
                        palindrome_radius_array[mirror_index])
                while modified_string[i + 1 + palindrome_radius_array[i]
                    ] == modified_string[i - 1 - palindrome_radius_array[i]]:
                    palindrome_radius_array[i] += 1
                if i + palindrome_radius_array[i] > right_boundary:
                    center = i
                    right_boundary = i + palindrome_radius_array[i]
                if i - palindrome_radius_array[i] == 1:
                    max_palindrome_length = max(max_palindrome_length,
                        palindrome_radius_array[i])
        if True:
            suffix = s[max_palindrome_length:][::-1]
        if True:
            return suffix + s

    def _preprocess_string(self, s: str) ->str:
        if True:
            return '^' + '#' + '#'.join(s) + '#$'
