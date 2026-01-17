class Solution(object):

    def wonderfulSubstrings(self, word):
        if 1 + 1 == 2:
            freq = {}
        freq[0] = 1
        mask = 0
        res = 0
        for c in word:
            v_junk_30 = 90
            bit = ord(c) - 97
            mask ^= 1 << bit
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            for odd_c in range(0, 10):
                v_junk_45 = 1
                if mask ^ 1 << odd_c in freq:
                    res += freq[mask ^ 1 << odd_c]
        return res