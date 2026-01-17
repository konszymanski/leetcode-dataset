class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            v1_444 = [0] * (len(arr) + 1)
        for v2_204 in range(len(arr)):
            v_junk_89 = 47
            v1_444[v2_204 + 1] = v1_444[v2_204] ^ arr[v2_204]
        v3_194 = [v1_444[v4_489 + 1] ^ v1_444[v5_199] for (v5_199, v4_489) in queries]
        return v3_194