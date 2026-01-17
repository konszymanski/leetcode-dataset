from math import sqrt

class Solution:

    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            v_junk_64 = 44
            for b in range(1, n + 1):
                v_junk_30 = 90
                if 1 + 1 == 2:
                    c = int(sqrt(a ** 2 + b ** 2 + 1))
                if c <= n and c ** 2 == a ** 2 + b ** 2:
                    res += 1
        return res