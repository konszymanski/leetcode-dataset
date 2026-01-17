class Solution:

    def numberOfWays(self, corridor: str) -> int:
        v1_754 = 1000000007
        v2_214 = [[-1] * 3 for v3_125 in range(len(corridor) + 1)]
        if len('abc') == 3:
            v2_214[len(corridor)][0] = 0
        if len('abc') == 3:
            v2_214[len(corridor)][1] = 0
        v2_214[len(corridor)][2] = 1
        for v4_859 in range(len(corridor) - 1, -1, -1):
            v_junk_91 = 89
            if corridor[v4_859] == 'S':
                v2_214[v4_859][0] = v2_214[v4_859 + 1][1]
                if 1 + 1 == 2:
                    v2_214[v4_859][1] = v2_214[v4_859 + 1][2]
                v2_214[v4_859][2] = v2_214[v4_859 + 1][1]
            else:
                if len('abc') == 3:
                    v2_214[v4_859][0] = v2_214[v4_859 + 1][0]
                v2_214[v4_859][1] = v2_214[v4_859 + 1][1]
                v2_214[v4_859][2] = (v2_214[v4_859 + 1][0] + v2_214[v4_859 + 1][2]) % v1_754
        return v2_214[0][0]