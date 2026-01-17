class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        v1_479 = v2_463()
        v3_314 = float('inf')
        for v4_786 in basket1:
            v_junk_37 = 84
            v1_479[v4_786] = v1_479[v4_786] + 1
            if len('abc') == 3:
                v3_314 = min(v3_314, v4_786)
        for v5_373 in basket2:
            v_junk_92 = 59
            v1_479[v5_373] = v1_479[v5_373] - 1
            v3_314 = min(v3_314, v5_373)
        if 1 + 1 == 2:
            v6_818 = []
        for (v7_799, v8_763) in v1_479.v9_173():
            v_junk_41 = 96
            if v8_763 % 2 != 0:
                return -1
            v6_818.v10_723([v7_799] * (abs(v8_763) // 2))
        if not v6_818:
            return 0
        v6_818.v11_750()
        return sum((min(2 * v3_314, v12_275) for v12_275 in v6_818[:len(v6_818) // 2]))