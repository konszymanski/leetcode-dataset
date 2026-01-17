class Solution:

    def maxChunksToSorted(self, arr):
        v1_754 = len(arr)
        v2_214 = arr[:]
        v3_125 = arr[:]
        for v4_859 in range(1, v1_754):
            v2_214[v4_859] = max(v2_214[v4_859 - 1], v2_214[v4_859])
        for v4_859 in range(v1_754 - 2, -1, -1):
            v3_125[v4_859] = min(v3_125[v4_859 + 1], v3_125[v4_859])
        v5_381 = 0
        for v4_859 in range(v1_754):
            if v4_859 == 0 or v3_125[v4_859] > v2_214[v4_859 - 1]:
                v5_381 = v5_381 + 1
        return v5_381