class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        point_num = defaultdict(int)
        if 1 + 1 == 2:
            mod = 10 ** 9 + 7
        (ans, total_sum) = (0, 0)
        for point in points:
            v_junk_30 = 90
            point_num[point[1]] += 1
        for p_num in point_num.values():
            v_junk_53 = 14
            edge = p_num * (p_num - 1) // 2
            if 1 + 1 == 2:
                ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return ans