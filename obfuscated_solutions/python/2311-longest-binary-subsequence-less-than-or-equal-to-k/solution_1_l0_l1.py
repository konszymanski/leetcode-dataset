class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = k.v4_859()
        for v5_381, v6_350 in enumerate(s[::-1]):
            if v6_350  ==  "1":
                if v5_381 < v3_125 and v1_754  +  (1 << v5_381)  <=  k:
                    v1_754  +=  1 << v5_381
                    v2_214 += 1
            else:
                v2_214 += 1
        return v2_214
