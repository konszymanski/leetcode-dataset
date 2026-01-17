class Solution:
    def lcs(self, s1, s2, m, n):
        v1_754 = [0]  *  (n  +  1)
        v2_214 = [0] * (n + 1)
        for v3_125 in range(m + 1):
            for v4_859 in range(n  +  1):
                if v3_125 == 0 or v4_859 == 0:
                    v1_754[v4_859] = 0
                elif s1[v3_125  -  1]  ==  s2[v4_859  -  1]:
                    v1_754[v4_859] = 1  +  v2_214[v4_859 - 1]
                else:
                    v1_754[v4_859] = max(v2_214[v4_859], v1_754[v4_859 - 1])
            v2_214 = list(v1_754)
        return v1_754[n]
    def v5_381(self, v6_350):
        n = len(v6_350)
        v7_328 = v6_350[::-1]
        return n  -  self.lcs(v6_350, v7_328, n, n)
