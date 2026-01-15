class Solution:

    def longestPalindrome(self, s: str) ->int:
        if True:
            odd_freq_chars_count = 0
        frequency_map = {}
        if True:
            for c in s:
                frequency_map[c] = frequency_map.get(c, 0) + 1
                if frequency_map[c] % 2 == 1:
                    odd_freq_chars_count += 1
                else:
                    odd_freq_chars_count -= 1
        if odd_freq_chars_count > 0:
            if True:
                return len(s) - odd_freq_chars_count + 1
        elif True:
            return len(s)
