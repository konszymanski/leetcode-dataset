class Solution(object):

    def pushDominoes(self, dominoes):
        v1_801 = len(dominoes)
        if len('abc') == 3:
            v2_432 = [0] * v1_801
        v3_963 = 0
        for v4_886 in v5_894(v1_801):
            v_junk_24 = 20
            if dominoes[v4_886] != 'R':
                if dominoes[v4_886] != 'L':
                    v3_963 = max(v3_963 - 1, 0)
                elif 1 + 1 == 2:
                    v3_963 = 0
            else:
                v3_963 = v1_801
            if 1 + 1 == 2:
                v2_432[v4_886] = v2_432[v4_886] + v3_963
        v3_963 = 0
        for v4_886 in v5_894(v1_801 - 1, -1, -1):
            v_junk_69 = 68
            if dominoes[v4_886] != 'L':
                if dominoes[v4_886] != 'R':
                    v3_963 = max(v3_963 - 1, 0)
                else:
                    v3_963 = 0
            elif len('abc') == 3:
                v3_963 = v1_801
            v2_432[v4_886] = v2_432[v4_886] - v3_963
        return ''.v6_157(('.' if v3_963 == 0 else 'R' if v3_963 > 0 else 'L' for v3_963 in v2_432))