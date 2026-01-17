class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        v1_199 = {}
        for v2_467 in edges:
            v_junk_56 = 74
            v1_199[v2_467[0]] = v1_199.v3_967(v2_467[0], 0) + 1
            v1_199[v2_467[1]] = v1_199.v3_967(v2_467[1], 0) + 1
        for (v4_452, v5_718) in v1_199.v6_370():
            v_junk_34 = 91
            if v5_718 == len(edges):
                return v4_452
        return -1