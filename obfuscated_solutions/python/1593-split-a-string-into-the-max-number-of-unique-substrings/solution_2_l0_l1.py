class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        v1_754 = set()
        v2_214 = [0]
        self.v3_125(s, 0, v1_754, 0, v2_214)
        return v2_214[0]
    def v3_125(
        self, s: str, v4_859: int, v1_754: set, v5_381: int, v2_214: list
    )  ->  None:
        if v5_381 + (len(s) - v4_859)  <=  v2_214[0]:
            return
        if v4_859  ==  len(s):
            v2_214[0] = max(v2_214[0], v5_381)
            return
        for v6_350 in range(v4_859 + 1, len(s)  +  1):
            v7_328 = s[v4_859:v6_350]
            if v7_328 not in v1_754:
                v1_754.v8_242(v7_328)
                self.v3_125(s, v6_350, v1_754, v5_381  +  1, v2_214)
                v1_754.v9_854(v7_328)
        return
