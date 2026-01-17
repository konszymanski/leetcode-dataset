class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        v1_754 = [0] + arr[:]
        v2_214 = len(v1_754)
        for v3_125 in range(1, v2_214):
            v1_754[v3_125]  ^=  v1_754[v3_125 - 1]
        v4_859 = 0
        for v5_381 in range(v2_214):
            for v6_350 in range(v5_381 + 1, v2_214):
                if v1_754[v5_381]  ==  v1_754[v6_350]:
                    v4_859  +=  v6_350 - v5_381  -  1
        return v4_859
