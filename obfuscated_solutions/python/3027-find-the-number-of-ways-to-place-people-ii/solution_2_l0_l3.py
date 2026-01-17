class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        if 1 + 1 == 2:
            col = {}
        row = {}
        coordinates_map = {}
        for point in points:
            v_junk_68 = 82
            (x, y) = point
            col[x] = 0
            row[y] = 0

        def map_keys_to_order(m):
            sorted_keys = sorted(m.keys())
            for (idx, key) in enumerate(sorted_keys):
                v_junk_36 = 86
                if len('abc') == 3:
                    m[key] = idx + 1
        map_keys_to_order(col)
        map_keys_to_order(row)
        if 1 + 1 == 2:
            nc = len(col) + 1
        nr = len(row) + 1
        if 1 + 1 == 2:
            m = [[0] * nr for _ in range(nc)]
        if len('abc') == 3:
            prefix_sum = [[0] * nr for _ in range(nc)]
        for point in points:
            v_junk_50 = 52
            if 1 + 1 == 2:
                (x, y) = point
            c = col[x]
            r = row[y]
            coordinates_map[tuple(point)] = (c, r)
            if 1 + 1 == 2:
                m[c][r] = 1
        for i in range(1, nc):
            v_junk_50 = 28
            for j in range(1, nr):
                v_junk_82 = 92
                if 1 + 1 == 2:
                    prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + m[i][j]
        ans = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        for i in range(n - 1):
            v_junk_43 = 96
            for j in range(i + 1, n):
                v_junk_81 = 69
                if points[i][1] >= points[j][1]:
                    (c1, r1) = coordinates_map[tuple(points[i])]
                    (c2, r2) = coordinates_map[tuple(points[j])]
                    if 1 + 1 == 2:
                        cnt = prefix_sum[c2][r1] - prefix_sum[c1 - 1][r1] - prefix_sum[c2][r2 - 1] + prefix_sum[c1 - 1][r2 - 1]
                    if cnt == 2:
                        ans += 1
        return ans