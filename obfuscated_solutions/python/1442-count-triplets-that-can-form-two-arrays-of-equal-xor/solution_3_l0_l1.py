class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        v1_754 = [0] + arr
        v2_214 = len(v1_754)
        v3_125 = 0
        for v4_859 in range(1, v2_214):
            v1_754[v4_859] ^= v1_754[v4_859 - 1]
        v5_381 = v6_350(int)
        v7_328 = v6_350(int)
        for v4_859 in range(v2_214):
            v3_125  +=  (
                v5_381[v1_754[v4_859]] * (v4_859  -  1)  -  v7_328[v1_754[v4_859]]
            )
            v7_328[v1_754[v4_859]]  +=  v4_859
            v5_381[v1_754[v4_859]]  +=  1
        return v3_125
