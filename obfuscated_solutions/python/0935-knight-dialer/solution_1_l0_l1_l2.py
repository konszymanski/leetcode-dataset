class Solution:

    def knightDialer(self, n: int) -> int:

        @cache
        def v1_754(v2_214, v3_125):
            if v2_214 == 0:
                return 1
            v4_859 = 0
            for v5_381 in v6_350[v3_125]:
                v4_859 = (v4_859 + v1_754(v2_214 - 1, v5_381)) % v7_328
            return v4_859
        v6_350 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        v4_859 = 0
        v7_328 = 10 ** 9 + 7
        for v3_125 in range(10):
            v4_859 = (v4_859 + v1_754(n - 1, v3_125)) % v7_328
        return v4_859