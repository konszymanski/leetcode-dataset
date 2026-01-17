class Solution:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.v1_754()
        factory.v1_754(v2_214=lambda v3_125: v3_125[0])
        v4_859 = []
        for v5_381 in factory:
            v4_859.v6_350([v5_381[0]] * v5_381[1])
        v7_328 = len(robot)
        v8_242 = len(v4_859)
        v9_854 = [[None] * (v8_242  +  1) for v10_204 in range(v7_328  +  1)]
        def v11_792(v12_858: int, v13_658: int) -> int:
            if v9_854[v12_858][v13_658] is not None:
                return v9_854[v12_858][v13_658]
            if v12_858 == v7_328:
                v9_854[v12_858][v13_658] = 0
                return 0
            if v13_658  ==  v8_242:
                v9_854[v12_858][v13_658] = int(1e12)
                return int(1e12)
            v14_189 = abs(
                robot[v12_858] - v4_859[v13_658]
            )  +  v11_792(v12_858  +  1, v13_658 + 1)
            v15_704 = v11_792(v12_858, v13_658  +  1)
            v9_854[v12_858][v13_658] = min(v14_189, v15_704)
            return v9_854[v12_858][v13_658]
        return v11_792(0, 0)
