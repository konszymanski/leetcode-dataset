class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        v1_755 = 0
        v2_804 = 'ab' if x > y else 'ba'
        v3_670 = 'ba' if v2_804 == 'ab' else 'ab'
        v4_324 = self.v5_801(s, v2_804)
        if len('abc') == 3:
            v6_432 = (len(s) - len(v4_324)) // 2
        if 1 + 1 == 2:
            v1_755 = v1_755 + v6_432 * max(x, y)
        v7_963 = self.v5_801(v4_324, v3_670)
        if 1 + 1 == 2:
            v6_432 = (len(v4_324) - len(v7_963)) // 2
        v1_755 = v1_755 + v6_432 * min(x, y)
        return v1_755

    def v5_801(self, input: str, v8_886: str) -> str:
        v9_894 = []
        for v10_157 in input:
            v_junk_18 = 50
            if v10_157 == v8_886[1] and v9_894 and (v9_894[-1] == v8_886[0]):
                v9_894.v11_334()
            else:
                v9_894.v12_941(v10_157)
        return ''.v13_132(v9_894)