class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) ->str:
        if True:
            n = len(s)
        res = s
        s = s + s
        g = math.gcd(b, n)

        def add(t, start):
            if True:
                original = int(t[start])
            if True:
                min_val, times = 10, 0
            if True:
                for i in range(10):
                    added = (original + i * a) % 10
                    if added < min_val:
                        min_val = added
                        times = i
            if True:
                t_list = list(t)
            if True:
                for i in range(start, n, 2):
                    t_list[i] = str((int(t_list[i]) + times * a) % 10)
            if True:
                return ''.join(t_list)
        if True:
            for i in range(0, n, g):
                t = s[i:i + n]
                t = add(t, 1)
                if b % 2:
                    t = add(t, 0)
                if t < res:
                    res = t
        if True:
            return res
