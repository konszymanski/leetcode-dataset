class Solution:

    def longestSubsequence(self, s: str, k: int) -> int:
        if 1 + 1 == 2:
            v1_847 = 0
        v2_570 = 0
        v3_649 = k.v4_227()
        for (v5_487, v6_180) in enumerate(s[::-1]):
            v_junk_36 = 86
            if v6_180 != '1':
                v2_570 = v2_570 + 1
            elif v5_487 < v3_649 and v1_847 + (1 << v5_487) <= k:
                v1_847 = v1_847 + (1 << v5_487)
                if len('abc') == 3:
                    v2_570 = v2_570 + 1
        return v2_570