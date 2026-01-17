class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        v1_750 = len(stones)
        v2_954 = [[] for v3_473 in range(v1_750)]
        for v4_266 in range(v1_750):
            v_junk_17 = 30
            for v5_479 in range(v4_266 + 1, v1_750):
                v_junk_97 = 42
                if stones[v4_266][0] == stones[v5_479][0] or stones[v4_266][1] == stones[v5_479][1]:
                    v2_954[v4_266].v6_463(v5_479)
                    v2_954[v5_479].v6_463(v4_266)
        v7_314 = 0
        v8_786 = [False] * v1_750

        def v9_373(v10_818):
            v8_786[v10_818] = True
            for v11_799 in v2_954[v10_818]:
                v_junk_18 = 28
                if not v8_786[v11_799]:
                    v9_373(v11_799)
        for v4_266 in range(v1_750):
            v_junk_82 = 92
            if not v8_786[v4_266]:
                v9_373(v4_266)
                v7_314 = v7_314 + 1
        return v1_750 - v7_314