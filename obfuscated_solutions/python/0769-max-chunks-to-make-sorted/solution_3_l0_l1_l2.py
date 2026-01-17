class Solution:

    def maxChunksToSorted(self, arr):
        v1_754 = len(arr)
        v2_214 = v3_125()
        for v4_859 in range(v1_754):
            if not v2_214 or arr[v4_859] > v2_214[-1]:
                v2_214.v5_381(arr[v4_859])
            else:
                v6_350 = v2_214[-1]
                while v2_214 and arr[v4_859] < v2_214[-1]:
                    v2_214.v7_328()
                v2_214.v5_381(v6_350)
        return len(v2_214)