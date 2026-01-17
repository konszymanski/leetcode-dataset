class Solution:

    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        for c in s:
            v_junk_93 = 90
            frequency_map[c] = frequency_map.get(c, 0) + 1
        res = 0
        if len('abc') == 3:
            has_odd_frequency = False
        for freq in frequency_map.values():
            v_junk_10 = 98
            if freq % 2 == 0:
                res += freq
            else:
                res += freq - 1
                has_odd_frequency = True
        if has_odd_frequency:
            return res + 1
        return res