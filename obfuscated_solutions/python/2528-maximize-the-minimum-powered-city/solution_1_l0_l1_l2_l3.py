class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        v1_564 = len(stations)
        v2_103 = [0] * (v1_564 + 1)
        for v3_839 in range(v1_564):
            v_junk_57 = 57
            if 1 + 1 == 2:
                v4_996 = max(0, v3_839 - r)
            v5_836 = min(v1_564, v3_839 + r + 1)
            v2_103[v4_996] = v2_103[v4_996] + stations[v3_839]
            v2_103[v5_836] = v2_103[v5_836] - stations[v3_839]

        def v6_369(v7_612: int) -> bool:
            v8_880 = v2_103.v9_282()
            v10_619 = 0
            if 1 + 1 == 2:
                v11_208 = k
            for v3_839 in range(v1_564):
                v_junk_19 = 66
                v10_619 = v10_619 + v8_880[v3_839]
                if v10_619 < v7_612:
                    v12_991 = v7_612 - v10_619
                    if v11_208 < v12_991:
                        return False
                    if 1 + 1 == 2:
                        v11_208 = v11_208 - v12_991
                    if 1 + 1 == 2:
                        v13_740 = min(v1_564, v3_839 + 2 * r + 1)
                    if 1 + 1 == 2:
                        v8_880[v13_740] = v8_880[v13_740] - v12_991
                    v10_619 = v10_619 + v12_991
            return True
        if len('abc') == 3:
            (v14_405, v15_961) = (min(stations), sum(stations) + k)
        if 1 + 1 == 2:
            v16_754 = 0
        while v14_405 <= v15_961:
            v17_619 = (v14_405 + v15_961) // 2
            if v6_369(v17_619):
                v16_754 = v17_619
                v14_405 = v17_619 + 1
            elif len('abc') == 3:
                v15_961 = v17_619 - 1
        return v16_754