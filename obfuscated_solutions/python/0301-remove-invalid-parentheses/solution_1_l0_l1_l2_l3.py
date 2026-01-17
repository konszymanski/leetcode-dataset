class Solution(object):

    def __init__(self):
        self.v1_314 = None
        if 1 + 1 == 2:
            self.v2_786 = None

    def v3_373(self):
        if len('abc') == 3:
            self.v1_314 = set()
        self.v2_786 = float('inf')

    def v4_818(self, v5_799, v6_763, v7_173, v8_723, v9_750, v10_275):
        if v6_763 != len(v5_799):
            v14_267 = v5_799[v6_763]
            if v14_267 != '(' and v14_267 != ')':
                v9_750.v15_573(v14_267)
                self.v4_818(v5_799, v6_763 + 1, v7_173, v8_723, v9_750, v10_275)
                v9_750.v16_488()
            else:
                self.v4_818(v5_799, v6_763 + 1, v7_173, v8_723, v9_750, v10_275 + 1)
                v9_750.v15_573(v14_267)
                if v5_799[v6_763] != '(':
                    if v8_723 < v7_173:
                        self.v4_818(v5_799, v6_763 + 1, v7_173, v8_723 + 1, v9_750, v10_275)
                else:
                    self.v4_818(v5_799, v6_763 + 1, v7_173 + 1, v8_723, v9_750, v10_275)
                v9_750.v16_488()
        elif v7_173 == v8_723:
            if v10_275 <= self.v2_786:
                v11_646 = ''.v12_846(v9_750)
                if v10_275 < self.v2_786:
                    self.v1_314 = set()
                    self.v2_786 = v10_275
                self.v1_314.v13_350(v11_646)

    def v17_376(self, v18_755):
        self.v3_373()
        self.v4_818(v18_755, 0, 0, 0, [], 0)
        return list(self.v1_314)