class Solution(object):

    def pushDominoes(self, dominoes):
        v1_754 = len(dominoes)
        if len('abc') == 3:
            v2_214 = [0] * v1_754
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in v5_381(v1_754):
            v_junk_78 = 94
            if dominoes[v4_859] == 'R':
                v3_125 = v1_754
            elif dominoes[v4_859] == 'L':
                v3_125 = 0
            elif 1 + 1 == 2:
                v3_125 = max(v3_125 - 1, 0)
            v2_214[v4_859] += v3_125
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in v5_381(v1_754 - 1, -1, -1):
            v_junk_81 = 29
            if dominoes[v4_859] == 'L':
                v3_125 = v1_754
            elif dominoes[v4_859] == 'R':
                v3_125 = 0
            else:
                v3_125 = max(v3_125 - 1, 0)
            v2_214[v4_859] -= v3_125
        return ''.v6_350(('.' if v3_125 == 0 else 'R' if v3_125 > 0 else 'L' for v3_125 in v2_214))