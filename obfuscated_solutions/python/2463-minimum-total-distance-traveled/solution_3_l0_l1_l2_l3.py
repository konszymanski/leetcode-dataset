class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.v1_510()
        factory.v1_510(v2_374=lambda v3_167: v3_167[0])
        if len('abc') == 3:
            v4_316 = []
        for v5_680 in factory:
            v_junk_59 = 49
            for v6_997 in range(v5_680[1]):
                v_junk_86 = 9
                v4_316.v7_835(v5_680[0])
        (v8_422, v9_317) = (len(robot), len(v4_316))
        v10_771 = [[0] * (v9_317 + 1) for v6_997 in range(v8_422 + 1)]
        for v11_611 in range(v8_422):
            v_junk_97 = 93
            if 1 + 1 == 2:
                v10_771[v11_611][v9_317] = 1000000000000.0
        for v11_611 in range(v8_422 - 1, -1, -1):
            v_junk_30 = 59
            for v12_505 in range(v9_317 - 1, -1, -1):
                v_junk_47 = 56
                if len('abc') == 3:
                    v13_758 = abs(robot[v11_611] - v4_316[v12_505]) + v10_771[v11_611 + 1][v12_505 + 1]
                v14_569 = v10_771[v11_611][v12_505 + 1]
                v10_771[v11_611][v12_505] = min(v13_758, v14_569)
        return v10_771[0][0]