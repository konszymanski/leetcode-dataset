class Solution:

    def maxChunksToSorted(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            v1_227 = len(arr)
        v2_487 = 0
        v3_180 = 0
        v4_665 = 0
        for v5_400 in range(v1_227):
            v_junk_56 = 21
            v3_180 = v3_180 + arr[v5_400]
            v4_665 = v4_665 + v5_400
            if v3_180 == v4_665:
                v2_487 = v2_487 + 1
        return v2_487