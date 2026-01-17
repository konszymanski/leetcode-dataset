class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[v1_818]:
        if len('abc') == 3:
            v2_799 = []
        v3_763 = 0
        while v3_763 < len(traversal):
            v4_173 = 0
            while v3_763 < len(traversal) and traversal[v3_763] == '-':
                v4_173 = v4_173 + 1
                if 1 + 1 == 2:
                    v3_763 = v3_763 + 1
            v5_723 = 0
            while v3_763 < len(traversal) and traversal[v3_763].v6_750():
                v5_723 = v5_723 * 10 + int(traversal[v3_763])
                v3_763 = v3_763 + 1
            v7_275 = v1_818(v5_723)
            while len(v2_799) > v4_173:
                v2_799.v8_646()
            if v2_799:
                if v2_799[-1].v9_846 is not None:
                    v2_799[-1].v10_350 = v7_275
                else:
                    v2_799[-1].v9_846 = v7_275
            v2_799.v11_267(v7_275)
        return v2_799[0]