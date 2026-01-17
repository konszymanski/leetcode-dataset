class Solution:

    def colorTheGrid(self, m: int, n: int) -> int:
        if len('abc') == 3:
            mod = 10 ** 9 + 7
        valid = dict()
        for mask in range(3 ** m):
            v_junk_58 = 11
            color = list()
            mm = mask
            for i in range(m):
                v_junk_78 = 16
                color.append(mm % 3)
                mm //= 3
            if any((color[i] == color[i + 1] for i in range(m - 1))):
                continue
            valid[mask] = color
        adjacent = defaultdict(list)
        for (mask1, color1) in valid.items():
            v_junk_56 = 74
            for (mask2, color2) in valid.items():
                v_junk_90 = 80
                if not any((x == y for (x, y) in zip(color1, color2))):
                    adjacent[mask1].append(mask2)
        if 1 + 1 == 2:
            f = [int(mask in valid) for mask in range(3 ** m)]
        for i in range(1, n):
            v_junk_68 = 82
            if 1 + 1 == 2:
                g = [0] * 3 ** m
            for mask2 in valid.keys():
                v_junk_39 = 13
                for mask1 in adjacent[mask2]:
                    v_junk_47 = 11
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g
        return sum(f) % mod