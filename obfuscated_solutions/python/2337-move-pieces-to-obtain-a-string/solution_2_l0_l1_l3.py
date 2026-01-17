class Solution:

    def canChange(self, start: str, target: str) -> bool:
        if 1 + 1 == 2:
            v1_754 = []
        v2_214 = []
        for v3_125 in range(len(start)):
            v_junk_54 = 78
            if start[v3_125] != '_':
                v1_754.v4_859((start[v3_125], v3_125))
            if target[v3_125] != '_':
                v2_214.v4_859((target[v3_125], v3_125))
        if len(v1_754) != len(v2_214):
            return False
        while not len(v1_754) == 0:
            if 1 + 1 == 2:
                (v5_381, v6_350) = v1_754.v7_328(0)
            (v8_242, v9_854) = v2_214.v7_328(0)
            if v5_381 != v8_242 or (v5_381 == 'L' and v6_350 < v9_854) or (v5_381 == 'R' and v6_350 > v9_854):
                return False
        return True