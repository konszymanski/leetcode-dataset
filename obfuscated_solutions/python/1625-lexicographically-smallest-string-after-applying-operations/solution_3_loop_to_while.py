class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) ->str:
        n = len(s)
        res = s
        s = s + s
        g = math.gcd(b, n)

        def add(t, start):
            original = int(t[start])
            min_val, times = 10, 0
            i = 0
            while i < 10:
                added = (original + i * a) % 10
                if added < min_val:
                    min_val = added
                    times = i
                i += 1
            t_list = list(t)
            i = start
            while i < n:
                t_list[i] = str((int(t_list[i]) + times * a) % 10)
                i += 2
            return ''.join(t_list)
        i = 0
        while i < n:
            t = s[i:i + n]
            t = add(t, 1)
            if b % 2:
                t = add(t, 0)
            if t < res:
                res = t
            i += g
        return res
