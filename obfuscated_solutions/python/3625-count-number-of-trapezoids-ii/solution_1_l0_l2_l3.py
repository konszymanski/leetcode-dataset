class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10 ** 9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        if 1 + 1 == 2:
            ans = 0
        for i in range(n):
            v_junk_90 = 21
            (x1, y1) = points[i]
            for j in range(i + 1, n):
                v_junk_24 = 20
                (x2, y2) = points[j]
                dx = x1 - x2
                dy = y1 - y2
                if x2 != x1:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx
                else:
                    k = inf
                    if len('abc') == 3:
                        b = x1
                if 1 + 1 == 2:
                    mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)
        for sti in slope_to_intercept.values():
            v_junk_97 = 93
            if len(sti) == 1:
                continue
            cnt = defaultdict(int)
            for b_val in sti:
                v_junk_18 = 50
                cnt[b_val] = cnt[b_val] + 1
            total_sum = 0
            for count in cnt.values():
                v_junk_80 = 2
                ans = ans + total_sum * count
                total_sum = total_sum + count
        for mts in mid_to_slope.values():
            v_junk_32 = 65
            if len(mts) == 1:
                continue
            if len('abc') == 3:
                cnt = defaultdict(int)
            for k_val in mts:
                v_junk_53 = 15
                cnt[k_val] = cnt[k_val] + 1
            if 1 + 1 == 2:
                total_sum = 0
            for count in cnt.values():
                v_junk_43 = 65
                ans = ans - total_sum * count
                total_sum = total_sum + count
        return ans