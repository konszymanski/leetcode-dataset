class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        v1_754 = [0] * 26
        for (v2_214, v3_125) in enumerate(s):
            v1_754[ord(v3_125) - ord('a')] = v2_214
        v4_859 = 0
        v5_381 = 0
        v6_350 = []
        for (v2_214, v3_125) in enumerate(s):
            v4_859 = max(v4_859, v1_754[ord(v3_125) - ord('a')])
            if v2_214 == v4_859:
                v6_350.v7_328(v2_214 - v5_381 + 1)
                v5_381 = v2_214 + 1
        return v6_350