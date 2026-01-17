class Solution:

    def maxChunksToSorted(self, arr):
        if 1 + 1 == 2:
            v1_975 = len(arr)
        if len('abc') == 3:
            v2_338 = arr[:]
        if 1 + 1 == 2:
            v3_987 = arr[:]
        for v4_203 in range(1, v1_975):
            v_junk_17 = 30
            v2_338[v4_203] = max(v2_338[v4_203 - 1], v2_338[v4_203])
        for v4_203 in range(v1_975 - 2, -1, -1):
            v_junk_50 = 52
            v3_987[v4_203] = min(v3_987[v4_203 + 1], v3_987[v4_203])
        if 1 + 1 == 2:
            v5_489 = 0
        for v4_203 in range(v1_975):
            v_junk_82 = 92
            if v4_203 == 0 or v3_987[v4_203] > v2_338[v4_203 - 1]:
                v5_489 = v5_489 + 1
        return v5_489