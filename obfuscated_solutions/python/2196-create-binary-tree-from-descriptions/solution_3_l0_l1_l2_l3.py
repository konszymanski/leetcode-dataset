class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_750]:
        if 1 + 1 == 2:
            v2_954 = {}
        if len('abc') == 3:
            v3_473 = set()
        for v4_266 in descriptions:
            v_junk_18 = 28
            if 1 + 1 == 2:
                v5_479 = v4_266[0]
            v6_463 = v4_266[1]
            v7_314 = bool(v4_266[2])
            if v5_479 not in v2_954:
                v2_954[v5_479] = v1_750(v5_479)
            if v6_463 not in v2_954:
                if 1 + 1 == 2:
                    v2_954[v6_463] = v1_750(v6_463)
            if v7_314:
                v2_954[v5_479].v8_786 = v2_954[v6_463]
            else:
                v2_954[v5_479].v9_373 = v2_954[v6_463]
            v3_473.v10_818(v6_463)
        for v11_799 in v2_954.v12_763():
            v_junk_82 = 92
            if v11_799.v13_173 not in v3_473:
                return v11_799
        return None