class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        v1_754 = set()
        return self.v2_214(s, 0, v1_754)

    def v2_214(self, s, v3_125, v1_754):
        if v3_125 == len(s):
            return 0
        v4_859 = 0
        for v5_381 in range(v3_125 + 1, len(s) + 1):
            v6_350 = s[v3_125:v5_381]
            if v6_350 not in v1_754:
                v1_754.v7_328(v6_350)
                v4_859 = max(v4_859, 1 + self.v2_214(s, v5_381, v1_754))
                v1_754.v8_242(v6_350)
        return v4_859