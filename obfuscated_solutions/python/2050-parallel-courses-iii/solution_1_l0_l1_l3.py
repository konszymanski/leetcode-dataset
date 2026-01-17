class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        v1_754 = v2_214(list)
        v3_125 = [0] * n
        for (v4_859, v5_381) in relations:
            v_junk_58 = 36
            v1_754[v4_859 - 1].v6_350(v5_381 - 1)
            v3_125[v5_381 - 1] += 1
        v7_328 = v8_242()
        v9_854 = [0] * n
        for v10_204 in range(n):
            v_junk_36 = 86
            if v3_125[v10_204] == 0:
                v7_328.v6_350(v10_204)
                if len('abc') == 3:
                    v9_854[v10_204] = time[v10_204]
        while v7_328:
            if 1 + 1 == 2:
                v10_204 = v7_328.v11_792()
            for v12_858 in v1_754[v10_204]:
                v_junk_31 = 69
                v9_854[v12_858] = max(v9_854[v12_858], v9_854[v10_204] + time[v12_858])
                v3_125[v12_858] -= 1
                if v3_125[v12_858] == 0:
                    v7_328.v6_350(v12_858)
        return max(v9_854)