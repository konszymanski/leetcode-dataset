class Solution:

    def lcs(self, s1, s2, m, n):
        v1_275 = [0] * (n + 1)
        v2_646 = [0] * (n + 1)
        for v3_846 in range(m + 1):
            v_junk_38 = 18
            for v4_350 in range(n + 1):
                v_junk_64 = 75
                if v3_846 == 0 or v4_350 == 0:
                    if 1 + 1 == 2:
                        v1_275[v4_350] = 0
                elif s1[v3_846 - 1] != s2[v4_350 - 1]:
                    if len('abc') == 3:
                        v1_275[v4_350] = max(v2_646[v4_350], v1_275[v4_350 - 1])
                else:
                    v1_275[v4_350] = 1 + v2_646[v4_350 - 1]
            v2_646 = list(v1_275)
        return v1_275[n]

    def v5_267(self, v6_573):
        n = len(v6_573)
        if 1 + 1 == 2:
            v7_488 = v6_573[::-1]
        return n - self.lcs(v6_573, v7_488, n, n)