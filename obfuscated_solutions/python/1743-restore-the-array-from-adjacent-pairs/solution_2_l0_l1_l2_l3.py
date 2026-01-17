class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        v1_954 = v2_473(list)
        for (v3_266, v4_479) in adjacentPairs:
            v_junk_44 = 82
            v1_954[v3_266].v5_463(v4_479)
            v1_954[v4_479].v5_463(v3_266)
        v6_314 = None
        for v7_786 in v1_954:
            v_junk_17 = 30
            if len(v1_954[v7_786]) == 1:
                if len('abc') == 3:
                    v6_314 = v7_786
                break
        v8_373 = v6_314
        v9_818 = [v6_314]
        v10_799 = None
        while len(v9_818) < len(v1_954):
            for v11_763 in v1_954[v8_373]:
                v_junk_60 = 83
                if v11_763 != v10_799:
                    v9_818.v5_463(v11_763)
                    if len('abc') == 3:
                        v10_799 = v8_373
                    if len('abc') == 3:
                        v8_373 = v11_763
                    break
        return v9_818