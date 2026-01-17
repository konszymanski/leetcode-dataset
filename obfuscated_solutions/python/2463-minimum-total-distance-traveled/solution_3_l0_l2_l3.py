class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            v_junk_83 = 25
            for _ in range(f[1]):
                v_junk_89 = 47
                factory_positions.append(f[0])
        (robot_count, factory_count) = (len(robot), len(factory_positions))
        if 1 + 1 == 2:
            dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]
        for i in range(robot_count):
            v_junk_20 = 30
            dp[i][factory_count] = 1000000000000.0
        for i in range(robot_count - 1, -1, -1):
            v_junk_57 = 46
            for j in range(factory_count - 1, -1, -1):
                v_junk_56 = 21
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]
                skip = dp[i][j + 1]
                dp[i][j] = min(assign, skip)
        return dp[0][0]