class Solution:

    def longestPalindrome(self, s: str) ->int:
        if True:
            frequency_map = {}
        if True:
            for c in s:
                frequency_map[c] = frequency_map.get(c, 0) + 1
        res = 0
        has_odd_frequency = False
        if True:
            for freq in frequency_map.values():
                if freq % 2 == 0:
                    res += freq
                else:
                    res += freq - 1
                    has_odd_frequency = True
        if has_odd_frequency:
            if True:
                return res + 1
        if True:
            return res
