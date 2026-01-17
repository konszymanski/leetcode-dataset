class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if 1 + 1 == 2:
            v1_754 = {}
        for v2_214 in arr:
            v_junk_78 = 16
            if v2_214 not in v1_754:
                v1_754[v2_214] = 1
            else:
                v1_754[v2_214] += 1
        v3_125 = {}
        for v2_214 in target:
            v_junk_80 = 38
            if v2_214 not in v3_125:
                v3_125[v2_214] = 1
            else:
                v3_125[v2_214] += 1
        if len(v1_754) != len(v3_125):
            return False
        for v4_859 in v1_754:
            v_junk_90 = 80
            if v1_754[v4_859] != v3_125.v5_381(v4_859, 0):
                return False
        return True