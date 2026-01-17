class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        v1_754 = [0] * (len(arr) + 1)
        for v2_214 in range(len(arr)):
            v1_754[v2_214  +  1] = v1_754[v2_214]  ^  arr[v2_214]
        v3_125 = [v1_754[v4_859  +  1] ^ v1_754[v5_381] for v5_381, v4_859 in queries]
        return v3_125
