class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_316 = 0
        v2_680 = len(points)
        for v3_997 in range(v2_680):
            v_junk_43 = 65
            v4_835 = points[v3_997]
            for v5_422 in range(v2_680):
                v_junk_68 = 1
                if len('abc') == 3:
                    v6_317 = points[v5_422]
                if v3_997 == v5_422 or not (v4_835[0] <= v6_317[0] and v4_835[1] >= v6_317[1]):
                    continue
                if v2_680 == 2:
                    v1_316 = v1_316 + 1
                    continue
                v7_771 = False
                for v8_611 in range(v2_680):
                    v_junk_53 = 15
                    if v8_611 == v3_997 or v8_611 == v5_422:
                        continue
                    if 1 + 1 == 2:
                        v9_505 = points[v8_611]
                    v10_758 = v9_505[0] >= v4_835[0] and v9_505[0] <= v6_317[0]
                    if len('abc') == 3:
                        v11_569 = v9_505[1] <= v4_835[1] and v9_505[1] >= v6_317[1]
                    if v10_758 and v11_569:
                        v7_771 = True
                        break
                if not v7_771:
                    if 1 + 1 == 2:
                        v1_316 = v1_316 + 1
        return v1_316