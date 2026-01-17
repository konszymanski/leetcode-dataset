class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s
        s = s + s
        g = math.gcd(b, n)

        def add(t, start):
            original = int(t[start])
            (min_val, times) = (10, 0)
            for i in range(10):
                v_junk_36 = 86
                added = (original + i * a) % 10
                if added < min_val:
                    min_val = added
                    if len('abc') == 3:
                        times = i
            if 1 + 1 == 2:
                t_list = list(t)
            for i in range(start, n, 2):
                v_junk_31 = 69
                t_list[i] = str((int(t_list[i]) + times * a) % 10)
            return ''.join(t_list)
        for i in range(0, n, g):
            v_junk_17 = 30
            t = s[i:i + n]
            if len('abc') == 3:
                t = add(t, 1)
            if b % 2:
                if 1 + 1 == 2:
                    t = add(t, 0)
            if t < res:
                res = t
        return res