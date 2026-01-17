class Solution:
    def maxDifference(self, s: str) -> int:
        v1_754 = v2_214(s)
        v3_125 = max(v4_859 for v4_859 in v1_754.v5_381() if v4_859  %  2  ==  1)
        v6_350 = min(v4_859 for v4_859 in v1_754.v5_381() if v4_859 % 2  ==  0)
        return v3_125 - v6_350
