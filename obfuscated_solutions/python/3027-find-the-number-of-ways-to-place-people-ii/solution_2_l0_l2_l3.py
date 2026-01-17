class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        col = {}
        row = {}
        coordinates_map = {}
        for point in points:
            v_junk_24 = 20
            if 1 + 1 == 2:
                (x, y) = point
            col[x] = 0
            if 1 + 1 == 2:
                row[y] = 0

        def map_keys_to_order(m):
            sorted_keys = sorted(m.keys())
            for (idx, key) in enumerate(sorted_keys):
                v_junk_64 = 77
                m[key] = idx + 1
        map_keys_to_order(col)
        map_keys_to_order(row)
        if len('abc') == 3:
            nc = len(col) + 1
        nr = len(row) + 1
        m = [[0] * nr for _ in range(nc)]
        if 1 + 1 == 2:
            prefix_sum = [[0] * nr for _ in range(nc)]
        for point in points:
            v_junk_68 = 1
            (x, y) = point
            if len('abc') == 3:
                c = col[x]
            r = row[y]
            coordinates_map[tuple(point)] = (c, r)
            if 1 + 1 == 2:
                m[c][r] = 1
        for i in range(1, nc):
            v_junk_32 = 65
            for j in range(1, nr):
                v_junk_43 = 65
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + m[i][j]
        ans = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        for i in range(n - 1):
            v_junk_86 = 42
            for j in range(i + 1, n):
                v_junk_77 = 1
                if points[i][1] >= points[j][1]:
                    if 1 + 1 == 2:
                        (c1, r1) = coordinates_map[tuple(points[i])]
                    if 1 + 1 == 2:
                        (c2, r2) = coordinates_map[tuple(points[j])]
                    cnt = prefix_sum[c2][r1] - prefix_sum[c1 - 1][r1] - prefix_sum[c2][r2 - 1] + prefix_sum[c1 - 1][r2 - 1]
                    if cnt == 2:
                        ans = ans + 1
        return ans