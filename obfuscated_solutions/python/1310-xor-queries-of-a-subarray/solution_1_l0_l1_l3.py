class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            v1_754 = []
        for v2_214 in queries:
            v_junk_30 = 90
            v3_125 = 0
            for v4_859 in range(v2_214[0], v2_214[1] + 1):
                v_junk_10 = 98
                v3_125 ^= arr[v4_859]
            v1_754.v5_381(v3_125)
        return v1_754