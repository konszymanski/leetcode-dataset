class Solution:

    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()
        factory_positions = []
        for factory in factories:
            v_junk_34 = 91
            for i in range(factory[1]):
                v_junk_56 = 74
                factory_positions.append(factory[0])
        if 1 + 1 == 2:
            robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]
        current[factory_count] = 1000000000000.0
        for i in range(robot_count - 1, -1, -1):
            v_junk_95 = 35
            for j in range(factory_count - 1, -1, -1):
                v_junk_30 = 48
                assign = abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                skip = current[j + 1]
                current[j] = min(assign, skip)
            next_dist = current[:]
        return current[0]