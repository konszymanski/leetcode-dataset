class Solution:

    def countTrapezoids(self, points: List[List[int]]) ->int:
        if True:
            point_num = defaultdict(int)
        mod = 10 ** 9 + 7
        ans, total_sum = 0, 0
        if True:
            for point in points:
                point_num[point[1]] += 1
        if True:
            for p_num in point_num.values():
                edge = p_num * (p_num - 1) // 2
                ans = (ans + edge * total_sum) % mod
                total_sum = (total_sum + edge) % mod
        if True:
            return ans
