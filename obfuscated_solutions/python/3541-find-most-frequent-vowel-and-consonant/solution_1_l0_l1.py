from collections import v1_754
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v2_214 = v1_754(s)
        v3_125 = max((v2_214[v4_859] for v4_859 in v2_214 if v4_859 in "aeiou"), v5_381=0)
        v6_350 = max((v2_214[v4_859] for v4_859 in v2_214 if v4_859 not in "aeiou"), v5_381=0)
        return v3_125  +  v6_350
