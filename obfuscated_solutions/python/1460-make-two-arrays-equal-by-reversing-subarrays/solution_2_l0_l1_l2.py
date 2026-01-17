class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        v1_754 = {}
        for v2_214 in arr:
            if v2_214 in v1_754:
                v1_754[v2_214] = v1_754[v2_214] + 1
            else:
                v1_754[v2_214] = 1
        v3_125 = {}
        for v2_214 in target:
            if v2_214 in v3_125:
                v3_125[v2_214] = v3_125[v2_214] + 1
            else:
                v3_125[v2_214] = 1
        if len(v1_754) != len(v3_125):
            return False
        for v4_859 in v1_754:
            if v1_754[v4_859] != v3_125.v5_381(v4_859, 0):
                return False
        return True