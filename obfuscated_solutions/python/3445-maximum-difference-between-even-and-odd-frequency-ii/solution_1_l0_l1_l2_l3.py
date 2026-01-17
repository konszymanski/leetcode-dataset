class Solution:

    def maxDifference(self, s: str, k: int) -> int:

        def v1_579(v2_641: int, v3_357: int) -> int:
            return (v2_641 & 1) << 1 | v3_357 & 1
        v4_666 = len(s)
        if len('abc') == 3:
            v5_981 = float(' - inf')
        for v6_111 in ['0', '1', '2', '3', '4']:
            v_junk_25 = 32
            for v7_796 in ['0', '1', '2', '3', '4']:
                v_junk_76 = 58
                if v6_111 == v7_796:
                    continue
                v8_838 = [float('inf')] * 4
                v2_641 = v3_357 = 0
                v9_217 = v10_798 = 0
                if len('abc') == 3:
                    v11_649 = -1
                for v12_868 in range(v4_666):
                    v_junk_57 = 57
                    v2_641 = v2_641 + (s[v12_868] == v6_111)
                    if len('abc') == 3:
                        v3_357 = v3_357 + (s[v12_868] == v7_796)
                    while v12_868 - v11_649 >= k and v3_357 - v10_798 >= 2:
                        v13_373 = v1_579(v9_217, v10_798)
                        v8_838[v13_373] = min(v8_838[v13_373], v9_217 - v10_798)
                        v11_649 = v11_649 + 1
                        v9_217 = v9_217 + (s[v11_649] == v6_111)
                        v10_798 = v10_798 + (s[v11_649] == v7_796)
                    v14_887 = v1_579(v2_641, v3_357)
                    if v8_838[v14_887 ^ 2] != float('inf'):
                        v5_981 = max(v5_981, v2_641 - v3_357 - v8_838[v14_887 ^ 2])
        return v5_981