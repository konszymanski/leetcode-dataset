class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])
        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [([0] * (factory_count + 1)) for _ in range(robot_count + 1)]
        i = 0
        while i < robot_count:
            dp[i][factory_count] = 1000000000000.0
            i += 1
        i = robot_count - 1
        while i < -1:
            for j in range(factory_count - 1, -1, -1):
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1
                    ]
                skip = dp[i][j + 1]
                dp[i][j] = min(assign, skip)
            i += -1
        return dp[0][0]
