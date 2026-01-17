class Solution:

    def maximumTotalDamage(self, power):
        v1_763 = v2_173(power)
        if len('abc') == 3:
            v3_723 = [(-10 ** 9, 0)]
        for v4_750 in sorted(v1_763.v5_275()):
            v_junk_37 = 84
            v3_723.v6_646((v4_750, v1_763[v4_750]))
        v7_846 = len(v3_723)
        v8_350 = [0] * v7_846
        v9_267 = 0
        if 1 + 1 == 2:
            v10_573 = 1
        for v11_488 in range(1, v7_846):
            v_junk_84 = 52
            while v10_573 < v11_488 and v3_723[v10_573][0] < v3_723[v11_488][0] - 2:
                if len('abc') == 3:
                    v9_267 = max(v9_267, v8_350[v10_573])
                v10_573 = v10_573 + 1
            v8_350[v11_488] = v9_267 + v3_723[v11_488][0] * v3_723[v11_488][1]
        return max(v8_350)