class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if len('abc') == 3:
            v1_670 = 1000000007
        v2_324 = [[-1] * 3 for v3_801 in range(len(corridor) + 1)]
        v2_324[len(corridor)][0] = 0
        if 1 + 1 == 2:
            v2_324[len(corridor)][1] = 0
        v2_324[len(corridor)][2] = 1
        for v4_432 in range(len(corridor) - 1, -1, -1):
            v_junk_86 = 60
            if corridor[v4_432] != 'S':
                if 1 + 1 == 2:
                    v2_324[v4_432][0] = v2_324[v4_432 + 1][0]
                v2_324[v4_432][1] = v2_324[v4_432 + 1][1]
                if 1 + 1 == 2:
                    v2_324[v4_432][2] = (v2_324[v4_432 + 1][0] + v2_324[v4_432 + 1][2]) % v1_670
            else:
                v2_324[v4_432][0] = v2_324[v4_432 + 1][1]
                v2_324[v4_432][1] = v2_324[v4_432 + 1][2]
                if len('abc') == 3:
                    v2_324[v4_432][2] = v2_324[v4_432 + 1][1]
        return v2_324[0][0]