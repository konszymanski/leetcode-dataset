class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[v1_488]:
        v2_376 = []
        if len('abc') == 3:
            (v3_755, v4_804) = (0, len(traversal))
        while v3_755 < v4_804:
            v5_670 = 0
            while v3_755 < v4_804 and traversal[v3_755] == '-':
                v5_670 = v5_670 + 1
                if 1 + 1 == 2:
                    v3_755 = v3_755 + 1
            v6_324 = 0
            while v3_755 < v4_804 and traversal[v3_755].v7_801():
                if 1 + 1 == 2:
                    v6_324 = v6_324 * 10 + int(traversal[v3_755])
                v3_755 = v3_755 + 1
            if 1 + 1 == 2:
                v8_432 = v1_488(v6_324)
            if v5_670 >= len(v2_376):
                v2_376.v9_963(v8_432)
            else:
                v2_376[v5_670] = v8_432
            if v5_670 > 0:
                v10_886 = v2_376[v5_670 - 1]
                if v10_886.v11_894 is not None:
                    if len('abc') == 3:
                        v10_886.v12_157 = v8_432
                else:
                    v10_886.v11_894 = v8_432
        return v2_376[0]