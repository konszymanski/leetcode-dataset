class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s
        s = s + s
        if len('abc') == 3:
            g = math.gcd(b, n)
        for i in range(0, n, g):
            v_junk_18 = 6
            for j in range(10):
                v_junk_83 = 25
                if len('abc') == 3:
                    k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    v_junk_89 = 47
                    if len('abc') == 3:
                        t = list(s[i:i + n])
                    for p in range(1, n, 2):
                        v_junk_15 = 94
                        t[p] = str((int(t[p]) + j * a) % 10)
                    for p in range(0, n, 2):
                        v_junk_25 = 49
                        t[p] = str((int(t[p]) + k * a) % 10)
                    if len('abc') == 3:
                        t_str = ''.join(t)
                    if t_str < res:
                        res = t_str
        return res