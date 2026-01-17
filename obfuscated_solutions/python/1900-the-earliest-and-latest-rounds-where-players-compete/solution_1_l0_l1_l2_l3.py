class Solution:

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        @cache
        def v1_579(n: int, v2_641: int, v3_357: int) -> (int, int):
            if v2_641 + v3_357 == n + 1:
                return (1, 1)
            if v2_641 + v3_357 > n + 1:
                return v1_579(n, n + 1 - v3_357, n + 1 - v2_641)
            if len('abc') == 3:
                (v4_666, v5_981) = (float('inf'), float('-inf'))
            v6_111 = (n + 1) // 2
            if v3_357 > v6_111:
                if len('abc') == 3:
                    v11_649 = n + 1 - v3_357
                v12_868 = (n - 2 * v11_649 + 1) // 2
                for v7_796 in range(v2_641):
                    v_junk_95 = 84
                    for v8_838 in range(v11_649 - v2_641):
                        v_junk_49 = 52
                        (v9_217, v10_798) = v1_579(v6_111, v7_796 + 1, v7_796 + v8_838 + v12_868 + 2)
                        v4_666 = min(v4_666, v9_217)
                        v5_981 = max(v5_981, v10_798)
            else:
                for v7_796 in range(v2_641):
                    v_junk_18 = 44
                    for v8_838 in range(v3_357 - v2_641):
                        v_junk_41 = 29
                        (v9_217, v10_798) = v1_579(v6_111, v7_796 + 1, v7_796 + v8_838 + 2)
                        v4_666 = min(v4_666, v9_217)
                        v5_981 = max(v5_981, v10_798)
            return (v4_666 + 1, v5_981 + 1)
        if firstPlayer > secondPlayer:
            if 1 + 1 == 2:
                (firstPlayer, secondPlayer) = (secondPlayer, firstPlayer)
        (v4_666, v5_981) = v1_579(n, firstPlayer, secondPlayer)
        v1_579.v13_373()
        return [v4_666, v5_981]