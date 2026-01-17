class Solution:
    v1_754 = 0
    v2_214 = 1
    v3_125 = 2
    v4_859 = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        v5_381 = [[self.v1_754] * n for v6_350 in range(m)]
        for (v7_328, v8_242) in guards:
            v5_381[v7_328][v8_242] = self.v3_125
        for (v7_328, v8_242) in walls:
            v5_381[v7_328][v8_242] = self.v4_859

        def v9_854(v7_328, v8_242, v10_204):
            if v5_381[v7_328][v8_242] == self.v3_125:
                return True
            if v5_381[v7_328][v8_242] == self.v4_859:
                return False
            if v10_204:
                v5_381[v7_328][v8_242] = self.v2_214
            return v10_204
        for v7_328 in range(m):
            v10_204 = v5_381[v7_328][0] == self.v3_125
            for v8_242 in range(1, n):
                v10_204 = v9_854(v7_328, v8_242, v10_204)
            v10_204 = v5_381[v7_328][n - 1] == self.v3_125
            for v8_242 in range(n - 2, -1, -1):
                v10_204 = v9_854(v7_328, v8_242, v10_204)
        for v8_242 in range(n):
            v10_204 = v5_381[0][v8_242] == self.v3_125
            for v7_328 in range(1, m):
                v10_204 = v9_854(v7_328, v8_242, v10_204)
            v10_204 = v5_381[m - 1][v8_242] == self.v3_125
            for v7_328 in range(m - 2, -1, -1):
                v10_204 = v9_854(v7_328, v8_242, v10_204)
        v11_792 = 0
        for v7_328 in range(m):
            for v8_242 in range(n):
                if v5_381[v7_328][v8_242] == self.v1_754:
                    v11_792 = v11_792 + 1
        return v11_792