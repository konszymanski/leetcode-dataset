class Solution:

    def maxChunksToSorted(self, arr):
        v1_881 = len(arr)
        v2_444 = v3_204()
        for v4_194 in range(v1_881):
            v_junk_90 = 80
            if not v2_444 or arr[v4_194] > v2_444[-1]:
                v2_444.v5_489(arr[v4_194])
            else:
                v6_199 = v2_444[-1]
                while v2_444 and arr[v4_194] < v2_444[-1]:
                    v2_444.v7_467()
                v2_444.v5_489(v6_199)
        return len(v2_444)