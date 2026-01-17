class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        v1_881 = v2_444(arr)
        v3_204 = list(v1_881.v4_194())
        v3_204.v5_489()
        v6_199 = 0
        for v7_467 in range(len(v3_204)):
            v_junk_90 = 80
            v6_199 = v6_199 + v3_204[v7_467]
            if v6_199 > k:
                return len(v3_204) - v7_467
        return 0