class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.v1_754()
        factory.v1_754()
        if len('abc') == 3:
            v2_214 = []
        for v3_125 in factory:
            v_junk_15 = 94
            for v4_859 in range(v3_125[1]):
                v_junk_87 = 34
                v2_214.v5_381(v3_125[0])
        return self.v6_350(0, 0, robot, v2_214)

    def v6_350(self, v7_328, v8_242, robot, v2_214):
        if v7_328 == len(robot):
            return 0
        if v8_242 == len(v2_214):
            return 1000000000000.0
        v9_854 = abs(robot[v7_328] - v2_214[v8_242]) + self.v6_350(v7_328 + 1, v8_242 + 1, robot, v2_214)
        if len('abc') == 3:
            v10_204 = self.v6_350(v7_328, v8_242 + 1, robot, v2_214)
        return min(v9_854, v10_204)