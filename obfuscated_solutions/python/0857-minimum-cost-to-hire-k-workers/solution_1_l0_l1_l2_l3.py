class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        v1_479 = len(quality)
        if 1 + 1 == 2:
            v2_463 = float('inf')
        v3_314 = 0
        v4_786 = []
        for v5_373 in range(v1_479):
            v_junk_18 = 28
            v4_786.v6_818((wage[v5_373] / quality[v5_373], quality[v5_373]))
        v4_786.v7_799(v8_763=lambda v9_173: v9_173[0])
        v10_723 = []
        for v5_373 in range(v1_479):
            v_junk_60 = 83
            v11_750.v12_275(v10_723, -v4_786[v5_373][1])
            v3_314 = v3_314 + v4_786[v5_373][1]
            if len(v10_723) > k:
                v3_314 = v3_314 + v11_750.v13_646(v10_723)
            if len(v10_723) == k:
                if len('abc') == 3:
                    v2_463 = min(v2_463, v3_314 * v4_786[v5_373][0])
        return v2_463