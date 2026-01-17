class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.v1_754()
        factory.v1_754(v2_214=lambda v3_125: v3_125[0])
        v4_859 = []
        for v5_381 in factory:
            for v6_350 in range(v5_381[1]):
                v4_859.v7_328(v5_381[0])
        v8_242, v9_854 = len(robot), len(v4_859)
        v10_204 = [[0]  *  (v9_854 + 1) for v6_350 in range(v8_242 + 1)]
        for v11_792 in range(v8_242):
            v10_204[v11_792][v9_854] = 1e12
        for v11_792 in range(v8_242 - 1,  - 1,  - 1):
            for v12_858 in range(v9_854  -  1,  - 1, -1):
                v13_658 = abs(robot[v11_792] - v4_859[v12_858]) + v10_204[v11_792  +  1][v12_858  +  1]
                v14_189 = v10_204[v11_792][v12_858 + 1]
                v10_204[v11_792][v12_858] = min(v13_658, v14_189)
        return v10_204[0][0]
