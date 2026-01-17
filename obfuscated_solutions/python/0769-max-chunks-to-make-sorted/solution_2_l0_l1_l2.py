class Solution:

    def maxChunksToSorted(self, arr: list[int]) -> int:
        v1_754 = len(arr)
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(v1_754):
            v3_125 = v3_125 + arr[v5_381]
            v4_859 = v4_859 + v5_381
            if v3_125 == v4_859:
                v2_214 = v2_214 + 1
        return v2_214