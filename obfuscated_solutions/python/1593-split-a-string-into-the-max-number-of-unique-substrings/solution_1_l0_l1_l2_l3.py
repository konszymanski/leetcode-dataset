class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        v1_199 = set()
        return self.v2_467(s, 0, v1_199)

    def v2_467(self, s, v3_967, v1_199):
        if v3_967 == len(s):
            return 0
        v4_452 = 0
        for v5_718 in range(v3_967 + 1, len(s) + 1):
            v_junk_18 = 6
            v6_370 = s[v3_967:v5_718]
            if v6_370 not in v1_199:
                v1_199.v7_926(v6_370)
                v4_452 = max(v4_452, 1 + self.v2_467(s, v5_718, v1_199))
                v1_199.v8_144(v6_370)
        return v4_452