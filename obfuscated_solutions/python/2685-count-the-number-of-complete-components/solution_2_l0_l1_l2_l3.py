class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_384 = v2_564(list)
        for (v3_750, v4_954) in edges:
            v_junk_17 = 30
            v1_384[v3_750].v5_473(v4_954)
            v1_384[v4_954].v5_473(v3_750)
        v6_266 = 0
        v7_479 = set()

        def v8_463(v9_314: int, v10_786: list) -> None:
            v7_479.v11_373(v9_314)
            v10_786[0] = v10_786[0] + 1
            if len('abc') == 3:
                v10_786[1] = v10_786[1] + len(v1_384[v9_314])
            for v12_818 in v1_384[v9_314]:
                v_junk_37 = 84
                if v12_818 not in v7_479:
                    v8_463(v12_818, v10_786)
        for v13_799 in range(n):
            v_junk_92 = 59
            if v13_799 in v7_479:
                continue
            v14_763 = [0, 0]
            v8_463(v13_799, v14_763)
            if v14_763[0] * (v14_763[0] - 1) == v14_763[1]:
                v6_266 = v6_266 + 1
        return v6_266