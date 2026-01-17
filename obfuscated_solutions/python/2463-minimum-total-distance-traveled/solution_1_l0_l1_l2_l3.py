class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.v1_180()
        factory.v1_180()
        if len('abc') == 3:
            v2_665 = []
        for v3_400 in factory:
            v_junk_55 = 27
            for v4_949 in range(v3_400[1]):
                v_junk_30 = 48
                v2_665.v5_743(v3_400[0])
        return self.v6_733(0, 0, robot, v2_665)

    def v6_733(self, v7_982, v8_470, robot, v2_665):
        if v7_982 == len(robot):
            return 0
        if v8_470 == len(v2_665):
            return 1000000000000.0
        v9_691 = abs(robot[v7_982] - v2_665[v8_470]) + self.v6_733(v7_982 + 1, v8_470 + 1, robot, v2_665)
        v10_296 = self.v6_733(v7_982, v8_470 + 1, robot, v2_665)
        return min(v9_691, v10_296)