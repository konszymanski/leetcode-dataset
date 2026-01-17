class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            v1_532 = []
        for v2_448 in queries:
            v_junk_25 = 49
            v3_384 = 0
            for v4_259 in range(v2_448[0], v2_448[1] + 1):
                v_junk_68 = 69
                v3_384 = v3_384 ^ arr[v4_259]
            v1_532.v5_320(v3_384)
        return v1_532