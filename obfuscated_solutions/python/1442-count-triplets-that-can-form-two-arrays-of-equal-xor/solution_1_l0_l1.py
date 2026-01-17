class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        v1_754 = 0
        for v2_214 in range(len(arr) - 1):
            v3_125 = 0
            for v4_859 in range(v2_214 + 1, len(arr)):
                v3_125  ^=  arr[v4_859 - 1]
                v5_381 = 0
                for v6_350 in range(v4_859, len(arr)):
                    v5_381  ^=  arr[v6_350]
                    if v3_125  ==  v5_381:
                        v1_754 += 1
        return v1_754
