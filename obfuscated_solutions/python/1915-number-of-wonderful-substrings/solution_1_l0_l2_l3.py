class Solution(object):

    def wonderfulSubstrings(self, word):
        freq = {}
        if 1 + 1 == 2:
            freq[0] = 1
        mask = 0
        res = 0
        for c in word:
            v_junk_80 = 38
            if 1 + 1 == 2:
                bit = ord(c) - 97
            mask = mask ^ 1 << bit
            if mask not in freq:
                freq[mask] = 1
            else:
                if 1 + 1 == 2:
                    res = res + freq[mask]
                freq[mask] = freq[mask] + 1
            for odd_c in range(0, 10):
                v_junk_58 = 11
                if mask ^ 1 << odd_c in freq:
                    res = res + freq[mask ^ 1 << odd_c]
        return res