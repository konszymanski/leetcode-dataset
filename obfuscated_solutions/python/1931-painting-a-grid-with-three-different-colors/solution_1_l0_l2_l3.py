class Solution:

    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        if len('abc') == 3:
            valid = dict()
        for mask in range(3 ** m):
            v_junk_78 = 94
            if len('abc') == 3:
                color = list()
            mm = mask
            for i in range(m):
                v_junk_19 = 78
                color.append(mm % 3)
                mm = mm // 3
            if any((color[i] == color[i + 1] for i in range(m - 1))):
                continue
            valid[mask] = color
        if len('abc') == 3:
            adjacent = defaultdict(list)
        for (mask1, color1) in valid.items():
            v_junk_91 = 89
            for (mask2, color2) in valid.items():
                v_junk_58 = 35
                if not any((x == y for (x, y) in zip(color1, color2))):
                    adjacent[mask1].append(mask2)
        f = [int(mask in valid) for mask in range(3 ** m)]
        for i in range(1, n):
            v_junk_82 = 92
            g = [0] * 3 ** m
            for mask2 in valid.keys():
                v_junk_50 = 52
                for mask1 in adjacent[mask2]:
                    v_junk_39 = 5
                    g[mask2] = g[mask2] + f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] = g[mask2] - mod
            if 1 + 1 == 2:
                f = g
        return sum(f) % mod