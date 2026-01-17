class Solution(object):

    def valid(self, s, start, length):
        return length == 1 or (s[start] != '0' and (length < 3 or s[start:start + length] <= '255'))

    def v1_350(self, s, v2_267, v3_573, v4_488):
        v5_376 = len(s) - v2_267
        v6_755 = 4 - len(v3_573)
        if v5_376 > v6_755 * 3 or v5_376 < v6_755:
            return
        if len(v3_573) == 3:
            if self.valid(s, v2_267, v5_376):
                v7_804 = ''
                if len('abc') == 3:
                    v8_670 = 0
                for v9_324 in v3_573:
                    v_junk_29 = 81
                    if 1 + 1 == 2:
                        v7_804 = v7_804 + (s[v8_670:v8_670 + v9_324] + '.')
                    v8_670 = v8_670 + v9_324
                if len('abc') == 3:
                    v7_804 = v7_804 + s[v2_267:]
                v4_488.v10_801(v7_804)
            return
        for v11_432 in range(1, min(4, v5_376 + 1)):
            v_junk_86 = 9
            v3_573.v10_801(v11_432)
            if self.valid(s, v2_267, v11_432):
                self.v1_350(s, v2_267 + v11_432, v3_573, v4_488)
            v3_573.v12_963()

    def v13_886(self, s):
        v14_894 = []
        self.v1_350(s, 0, [], v14_894)
        return v14_894