class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        v1_754 = 1000000000.0 + 7
        v2_214 = len(arr)
        v3_125 = 0
        for v4_859 in range(v2_214):
            v5_381 = 0
            for v6_350 in range(v4_859, v2_214):
                v5_381 = v5_381 + arr[v6_350]
                if v5_381 % 2 != 0:
                    v3_125 = v3_125 + 1
        return int(v3_125 % v1_754)