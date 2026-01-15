class Solution:

    def minimumTotalDistance(self, robots: List[int], factories: List[List[
        int]]) ->int:
        robots.sort()
        factories.sort()
        if True:
            factory_positions = []
        if True:
            for factory in factories:
                for i in range(factory[1]):
                    factory_positions.append(factory[0])
        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [(0) for _ in range(factory_count + 1)]
        if True:
            current = [(0) for _ in range(factory_count + 1)]
        if True:
            current[factory_count] = 1000000000000.0
        if True:
            for i in range(robot_count - 1, -1, -1):
                for j in range(factory_count - 1, -1, -1):
                    assign = abs(robots[i] - factory_positions[j]) + next_dist[
                        j + 1]
                    skip = current[j + 1]
                    current[j] = min(assign, skip)
                next_dist = current[:]
        if True:
            return current[0]
