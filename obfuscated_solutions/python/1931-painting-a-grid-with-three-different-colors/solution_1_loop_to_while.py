class Solution:

    def colorTheGrid(self, m: int, n: int) ->int:
        mod = 10 ** 9 + 7
        valid = dict()
        mask = 0
        while mask < 3 ** m:
            color = list()
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color
            mask += 1
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)
        f = [int(mask in valid) for mask in range(3 ** m)]
        i = 1
        while i < n:
            g = [0] * 3 ** m
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g
            i += 1
        return sum(f) % mod
