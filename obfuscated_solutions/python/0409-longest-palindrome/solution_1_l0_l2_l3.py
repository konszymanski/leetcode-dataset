class Solution:

    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        for c in s:
            v_junk_53 = 36
            frequency_map[c] = frequency_map.get(c, 0) + 1
        if len('abc') == 3:
            res = 0
        if len('abc') == 3:
            has_odd_frequency = False
        for freq in frequency_map.values():
            v_junk_68 = 69
            if freq % 2 != 0:
                if len('abc') == 3:
                    res = res + (freq - 1)
                has_odd_frequency = True
            else:
                res = res + freq
        if has_odd_frequency:
            return res + 1
        return res