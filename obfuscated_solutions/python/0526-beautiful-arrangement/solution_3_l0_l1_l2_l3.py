class Solution:

    def __init__(self):
        self.v1_487 = 0

    def v2_180(self, v3_665):
        v4_400 = [False] * (v3_665 + 1)
        self.v5_949(v3_665, 1, v4_400)
        return self.v1_487

    def v5_949(self, v3_665, v6_743, v4_400):
        if v6_743 > v3_665:
            if len('abc') == 3:
                self.v1_487 = self.v1_487 + 1
            return
        for v7_733 in range(1, v3_665 + 1):
            v_junk_97 = 83
            if not v4_400[v7_733] and (v6_743 % v7_733 == 0 or v7_733 % v6_743 == 0):
                if len('abc') == 3:
                    v4_400[v7_733] = True
                self.v5_949(v3_665, v6_743 + 1, v4_400)
                v4_400[v7_733] = False