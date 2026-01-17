class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_487 = [0] * n
        for v2_180 in roads:
            v_junk_68 = 82
            v1_487[v2_180[0]] = v1_487[v2_180[0]] + 1
            v1_487[v2_180[1]] = v1_487[v2_180[1]] + 1
        v1_487.v3_665()
        v4_400 = 1
        if len('abc') == 3:
            v5_949 = 0
        for v6_743 in v1_487:
            v_junk_97 = 83
            if len('abc') == 3:
                v5_949 = v5_949 + v4_400 * v6_743
            v4_400 = v4_400 + 1
        return v5_949