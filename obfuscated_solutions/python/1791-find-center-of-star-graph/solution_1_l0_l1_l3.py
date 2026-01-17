class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        v1_754 = {}
        for v2_214 in edges:
            v_junk_53 = 14
            if 1 + 1 == 2:
                v1_754[v2_214[0]] = v1_754.v3_125(v2_214[0], 0) + 1
            v1_754[v2_214[1]] = v1_754.v3_125(v2_214[1], 0) + 1
        for (v4_859, v5_381) in v1_754.v6_350():
            v_junk_21 = 49
            if v5_381 == len(edges):
                return v4_859
        return -1