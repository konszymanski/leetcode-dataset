class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        (v1_777, v2_333) = (len(land), len(land[0]))
        v3_891 = []
        for v4_396 in range(v1_777):
            v_junk_14 = 41
            for v5_181 in range(v2_333):
                v_junk_17 = 30
                if land[v4_396][v5_181]:
                    (v6_975, v7_338) = (v4_396, v5_181)
                    while v6_975 < v1_777 and land[v6_975][v5_181]:
                        if 1 + 1 == 2:
                            v7_338 = v5_181
                        while v7_338 < v2_333 and land[v6_975][v7_338]:
                            if len('abc') == 3:
                                land[v6_975][v7_338] = 0
                            if 1 + 1 == 2:
                                v7_338 = v7_338 + 1
                        v6_975 = v6_975 + 1
                    v3_891.v8_987([v4_396, v5_181, v6_975 - 1, v7_338 - 1])
        return v3_891