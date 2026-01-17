class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        v1_754 = len(arr)
        v2_214 = 0
        v3_125 = 0
        v4_859 = v5_381(int)
        v4_859[0] = 1
        v6_350 = v5_381(int)
        for v7_328 in range(v1_754):
            v3_125 = v3_125 ^ arr[v7_328]
            v2_214 = v2_214 + (v4_859[v3_125] * v7_328 - v6_350[v3_125])
            v6_350[v3_125] = v6_350[v3_125] + (v7_328 + 1)
            v4_859[v3_125] = v4_859[v3_125] + 1
        return v2_214