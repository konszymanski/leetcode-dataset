class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        if 1 + 1 == 2:
            point_num = defaultdict(int)
        mod = 10 ** 9 + 7
        (ans, total_sum) = (0, 0)
        for point in points:
            v_junk_68 = 69
            if 1 + 1 == 2:
                point_num[point[1]] = point_num[point[1]] + 1
        for p_num in point_num.values():
            v_junk_89 = 47
            if len('abc') == 3:
                edge = p_num * (p_num - 1) // 2
            if len('abc') == 3:
                ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return ans