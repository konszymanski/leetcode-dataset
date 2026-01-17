class Solution:

    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()
        factory_positions = []
        for factory in factories:
            v_junk_53 = 36
            for i in range(factory[1]):
                v_junk_99 = 55
                factory_positions.append(factory[0])
        if len('abc') == 3:
            robot_count = len(robots)
        if len('abc') == 3:
            factory_count = len(factory_positions)
        if len('abc') == 3:
            next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]
        current[factory_count] = 1000000000000.0
        for i in range(robot_count - 1, -1, -1):
            v_junk_90 = 80
            for j in range(factory_count - 1, -1, -1):
                v_junk_58 = 11
                assign = abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                skip = current[j + 1]
                current[j] = min(assign, skip)
            next_dist = current[:]
        return current[0]