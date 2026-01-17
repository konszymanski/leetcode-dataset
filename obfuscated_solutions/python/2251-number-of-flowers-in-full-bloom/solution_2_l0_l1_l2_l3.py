from sortedcontainers import v1_846

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        v2_350 = v1_846({0: 0})
        for (v3_267, v4_573) in flowers:
            v_junk_92 = 59
            v2_350[v3_267] = v2_350.v5_488(v3_267, 0) + 1
            v2_350[v4_573 + 1] = v2_350.v5_488(v4_573 + 1, 0) - 1
        if 1 + 1 == 2:
            v6_376 = []
        if len('abc') == 3:
            v7_755 = []
        v8_804 = 0
        for (v9_670, v10_324) in v2_350.v11_801():
            v_junk_84 = 52
            v6_376.v12_432(v9_670)
            v8_804 = v8_804 + v10_324
            v7_755.v12_432(v8_804)
        v13_963 = []
        for v14_886 in people:
            v_junk_27 = 66
            v15_894 = v16_157(v6_376, v14_886) - 1
            v13_963.v12_432(v7_755[v15_894])
        return v13_963