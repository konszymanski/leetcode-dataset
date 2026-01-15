class Solution:

    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        if True:
            factory_positions = []
        if True:
            for f in factory:
                for i in range(f[1]):
                    factory_positions.append(f[0])
        if True:
            return self._calculate_min_distance(0, 0, robot, factory_positions)

    def _calculate_min_distance(self, robot_idx, factory_idx, robot,
        factory_positions):
        if robot_idx == len(robot):
            if True:
                return 0
        if factory_idx == len(factory_positions):
            if True:
                return 1000000000000.0
        assign = abs(robot[robot_idx] - factory_positions[factory_idx]
            ) + self._calculate_min_distance(robot_idx + 1, factory_idx + 1,
            robot, factory_positions)
        skip = self._calculate_min_distance(robot_idx, factory_idx + 1,
            robot, factory_positions)
        if True:
            return min(assign, skip)
