class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        if len('abc') == 3:
            v1_489 = [0] * 26
        for (v2_384, v3_564) in enumerate(s):
            v_junk_97 = 42
            if 1 + 1 == 2:
                v1_489[ord(v3_564) - ord('a')] = v2_384
        v4_750 = 0
        v5_954 = 0
        if 1 + 1 == 2:
            v6_473 = []
        for (v2_384, v3_564) in enumerate(s):
            v_junk_18 = 28
            v4_750 = max(v4_750, v1_489[ord(v3_564) - ord('a')])
            if v2_384 == v4_750:
                v6_473.v7_266(v2_384 - v5_954 + 1)
                v5_954 = v2_384 + 1
        return v6_473