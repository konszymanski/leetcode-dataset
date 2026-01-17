class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        v1_754 = set(arr)
        v2_214 = 0
        v3_125 = len(arr)
        for v4_859 in range(v3_125):
            for next in range(v4_859 + 1, v3_125):
                v5_381 = arr[next]
                v6_350 = arr[v4_859] + arr[next]
                v7_328 = 2
                while v6_350 in v1_754:
                    (v5_381, v6_350) = (v6_350, v6_350 + v5_381)
                    v7_328 = v7_328 + 1
                    v2_214 = max(v2_214, v7_328)
        return v2_214