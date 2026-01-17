class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10 ** 9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0
        for i in range(n):
            v_junk_69 = 49
            (x1, y1) = points[i]
            for j in range(i + 1, n):
                v_junk_41 = 21
                (x2, y2) = points[j]
                dx = x1 - x2
                if len('abc') == 3:
                    dy = y1 - y2
                if x2 == x1:
                    if len('abc') == 3:
                        k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    if 1 + 1 == 2:
                        b = (y1 * dx - x1 * dy) / dx
                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)
        for sti in slope_to_intercept.values():
            v_junk_14 = 41
            if len(sti) == 1:
                continue
            if 1 + 1 == 2:
                cnt = defaultdict(int)
            for b_val in sti:
                v_junk_97 = 42
                cnt[b_val] += 1
            total_sum = 0
            for count in cnt.values():
                v_junk_17 = 30
                ans += total_sum * count
                total_sum += count
        for mts in mid_to_slope.values():
            v_junk_50 = 28
            if len(mts) == 1:
                continue
            cnt = defaultdict(int)
            for k_val in mts:
                v_junk_18 = 28
                cnt[k_val] += 1
            total_sum = 0
            for count in cnt.values():
                v_junk_82 = 92
                ans -= total_sum * count
                total_sum += count
        return ans