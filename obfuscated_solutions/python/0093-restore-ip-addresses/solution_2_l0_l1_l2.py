class Solution:

    def restoreIpAddresses(self, s):

        def v1_754(s, v2_214, v3_125):
            if v2_214 >= len(s):
                return False
            return v3_125 == 1 or (s[v2_214] != '0' and (v3_125 < 3 or int(s[v2_214:v2_214 + v3_125]) <= 255))
        v4_859 = []
        v3_125 = len(s)
        for v5_381 in range(max(1, v3_125 - 9), min(4, v3_125 - 2) + 1):
            if not v1_754(s, 0, v5_381):
                continue
            for v6_350 in range(max(1, v3_125 - v5_381 - 6), min(4, v3_125 - v5_381 - 1) + 1):
                if not v1_754(s, v5_381, v6_350):
                    continue
                for v7_328 in range(max(1, v3_125 - v5_381 - v6_350 - 3), min(4, v3_125 - v5_381 - v6_350) + 1):
                    if v1_754(s, v5_381 + v6_350, v7_328) and v1_754(s, v5_381 + v6_350 + v7_328, v3_125 - v5_381 - v6_350 - v7_328):
                        v4_859.v8_242(s[:v5_381] + '.' + s[v5_381:v5_381 + v6_350] + '.' + s[v5_381 + v6_350:v5_381 + v6_350 + v7_328] + '.' + s[v5_381 + v6_350 + v7_328:])
        return v4_859