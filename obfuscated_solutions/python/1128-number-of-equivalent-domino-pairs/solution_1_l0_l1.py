class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        v1_754 = [0]  *  100
        v2_214 = 0
        for v3_125, v4_859 in dominoes:
            v5_381 = v3_125  *  10 + v4_859 if v3_125 <= v4_859 else v4_859 * 10 + v3_125
            v2_214 += v1_754[v5_381]
            v1_754[v5_381]  +=  1
        return v2_214
