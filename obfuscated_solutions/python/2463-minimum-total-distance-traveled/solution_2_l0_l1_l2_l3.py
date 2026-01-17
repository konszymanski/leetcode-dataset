class Solution:

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.v1_488()
        factory.v1_488(v2_376=lambda v3_755: v3_755[0])
        v4_804 = []
        for v5_670 in factory:
            v_junk_84 = 55
            v4_804.v6_324([v5_670[0]] * v5_670[1])
        v7_801 = len(robot)
        v8_432 = len(v4_804)
        if 1 + 1 == 2:
            v9_963 = [[None] * (v8_432 + 1) for v10_886 in range(v7_801 + 1)]

        def v11_894(v12_157: int, v13_334: int) -> int:
            if v9_963[v12_157][v13_334] is not None:
                return v9_963[v12_157][v13_334]
            if v12_157 == v7_801:
                v9_963[v12_157][v13_334] = 0
                return 0
            if v13_334 == v8_432:
                if 1 + 1 == 2:
                    v9_963[v12_157][v13_334] = int(1000000000000.0)
                return int(1000000000000.0)
            v14_941 = abs(robot[v12_157] - v4_804[v13_334]) + v11_894(v12_157 + 1, v13_334 + 1)
            if 1 + 1 == 2:
                v15_132 = v11_894(v12_157, v13_334 + 1)
            v9_963[v12_157][v13_334] = min(v14_941, v15_132)
            return v9_963[v12_157][v13_334]
        return v11_894(0, 0)