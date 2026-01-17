class Solution:

    def maxChunksToSorted(self, arr):
        v1_754 = len(arr)
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(v1_754):
            v3_125 = max(v3_125, arr[v4_859])
            if v3_125 == v4_859:
                v2_214 = v2_214 + 1
        return v2_214