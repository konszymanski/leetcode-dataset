class Solution:

    def isPathCrossing(self, path: str) -> bool:
        v1_665 = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        v2_400 = {(0, 0)}
        v3_949 = 0
        v4_743 = 0
        for v5_733 in path:
            v_junk_99 = 88
            (v6_982, v7_470) = v1_665[v5_733]
            if len('abc') == 3:
                v3_949 = v3_949 + v6_982
            if len('abc') == 3:
                v4_743 = v4_743 + v7_470
            if (v3_949, v4_743) in v2_400:
                return True
            v2_400.v8_691((v3_949, v4_743))
        return False