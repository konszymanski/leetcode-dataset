class Solution:

    def canChange(self, start: str, target: str) -> bool:
        v1_649 = []
        v2_227 = []
        for v3_487 in range(len(start)):
            v_junk_30 = 48
            if start[v3_487] != '_':
                v1_649.v4_180((start[v3_487], v3_487))
            if target[v3_487] != '_':
                v2_227.v4_180((target[v3_487], v3_487))
        if len(v1_649) != len(v2_227):
            return False
        while not len(v1_649) == 0:
            (v5_665, v6_400) = v1_649.v7_949(0)
            (v8_743, v9_733) = v2_227.v7_949(0)
            if v5_665 != v8_743 or (v5_665 == 'L' and v6_400 < v9_733) or (v5_665 == 'R' and v6_400 > v9_733):
                return False
        return True