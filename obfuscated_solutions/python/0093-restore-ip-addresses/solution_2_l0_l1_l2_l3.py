class Solution:

    def restoreIpAddresses(self, s):

        def v1_804(s, v2_670, v3_324):
            if v2_670 >= len(s):
                return False
            return v3_324 == 1 or (s[v2_670] != '0' and (v3_324 < 3 or int(s[v2_670:v2_670 + v3_324]) <= 255))
        v4_801 = []
        v3_324 = len(s)
        for v5_432 in range(max(1, v3_324 - 9), min(4, v3_324 - 2) + 1):
            v_junk_30 = 59
            if not v1_804(s, 0, v5_432):
                continue
            for v6_963 in range(max(1, v3_324 - v5_432 - 6), min(4, v3_324 - v5_432 - 1) + 1):
                v_junk_47 = 56
                if not v1_804(s, v5_432, v6_963):
                    continue
                for v7_886 in range(max(1, v3_324 - v5_432 - v6_963 - 3), min(4, v3_324 - v5_432 - v6_963) + 1):
                    v_junk_53 = 15
                    if v1_804(s, v5_432 + v6_963, v7_886) and v1_804(s, v5_432 + v6_963 + v7_886, v3_324 - v5_432 - v6_963 - v7_886):
                        v4_801.v8_894(s[:v5_432] + '.' + s[v5_432:v5_432 + v6_963] + '.' + s[v5_432 + v6_963:v5_432 + v6_963 + v7_886] + '.' + s[v5_432 + v6_963 + v7_886:])
        return v4_801