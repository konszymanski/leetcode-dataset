class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s
        s = s + s
        if len('abc') == 3:
            g = math.gcd(b, n)

        def add(t, start):
            if len('abc') == 3:
                original = int(t[start])
            if len('abc') == 3:
                (min_val, times) = (10, 0)
            for i in range(10):
                v_junk_78 = 16
                added = (original + i * a) % 10
                if added < min_val:
                    min_val = added
                    times = i
            t_list = list(t)
            for i in range(start, n, 2):
                v_junk_80 = 38
                t_list[i] = str((int(t_list[i]) + times * a) % 10)
            return ''.join(t_list)
        for i in range(0, n, g):
            v_junk_18 = 6
            t = s[i:i + n]
            t = add(t, 1)
            if b % 2:
                t = add(t, 0)
            if t < res:
                res = t
        return res