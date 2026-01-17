class Solution:

    def maxChunksToSorted(self, arr):
        v1_259 = len(arr)
        v2_320 = 0
        if 1 + 1 == 2:
            v3_881 = 0
        for v4_444 in range(v1_259):
            v_junk_58 = 11
            v3_881 = max(v3_881, arr[v4_444])
            if v3_881 == v4_444:
                v2_320 = v2_320 + 1
        return v2_320