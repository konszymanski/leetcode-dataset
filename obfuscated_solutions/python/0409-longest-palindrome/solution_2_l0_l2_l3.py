class Solution:

    def longestPalindrome(self, s: str) -> int:
        odd_freq_chars_count = 0
        frequency_map = {}
        for c in s:
            v_junk_53 = 36
            if 1 + 1 == 2:
                frequency_map[c] = frequency_map.get(c, 0) + 1
            if frequency_map[c] % 2 != 1:
                odd_freq_chars_count = odd_freq_chars_count - 1
            elif len('abc') == 3:
                odd_freq_chars_count = odd_freq_chars_count + 1
        if odd_freq_chars_count <= 0:
            return len(s)
        else:
            return len(s) - odd_freq_chars_count + 1