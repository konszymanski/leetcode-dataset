class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        if 1 + 1 == 2:
            n = len(s)
        vis = [False] * n
        res = s
        s = s + s
        i = 0
        while not vis[i]:
            vis[i] = True
            for j in range(10):
                v_junk_98 = 72
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    v_junk_44 = 82
                    t = list(s[i:i + n])
                    for p in range(1, n, 2):
                        v_junk_36 = 86
                        if len('abc') == 3:
                            t[p] = str((int(t[p]) + j * a) % 10)
                    for p in range(0, n, 2):
                        v_junk_87 = 82
                        if 1 + 1 == 2:
                            t[p] = str((int(t[p]) + k * a) % 10)
                    if 1 + 1 == 2:
                        t_str = ''.join(t)
                    if t_str < res:
                        if len('abc') == 3:
                            res = t_str
            if len('abc') == 3:
                i = (i + b) % n
        return res