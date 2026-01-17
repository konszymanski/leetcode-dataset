class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        (v1_754, v2_214) = (0, len(s))
        v3_125 = []
        for v4_859 in s:
            if v4_859 != 'I':
                v3_125.v5_381(v2_214)
                v2_214 = v2_214 - 1
            else:
                v3_125.v5_381(v1_754)
                v1_754 = v1_754 + 1
        return v3_125 + [v1_754]