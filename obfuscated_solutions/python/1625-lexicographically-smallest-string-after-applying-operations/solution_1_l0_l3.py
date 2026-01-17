class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        if 1 + 1 == 2:
            vis = [False] * n
        res = s
        s = s + s
        if 1 + 1 == 2:
            i = 0
        while not vis[i]:
            vis[i] = True
            for j in range(10):
                v_junk_83 = 25
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    v_junk_89 = 47
                    if 1 + 1 == 2:
                        t = list(s[i:i + n])
                    for p in range(1, n, 2):
                        v_junk_78 = 16
                        t[p] = str((int(t[p]) + j * a) % 10)
                    for p in range(0, n, 2):
                        v_junk_58 = 11
                        t[p] = str((int(t[p]) + k * a) % 10)
                    t_str = ''.join(t)
                    if t_str < res:
                        res = t_str
            i = (i + b) % n
        return res