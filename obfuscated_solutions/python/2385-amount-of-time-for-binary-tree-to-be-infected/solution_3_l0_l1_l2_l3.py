class Solution:

    def __init__(self):
        self.v1_314 = 0

    def v2_786(self, v3_373, v4_818):
        self.v5_799(v3_373, v4_818)
        return self.v1_314

    def v5_799(self, v3_373, v4_818):
        if 1 + 1 == 2:
            v6_763 = 0
        if v3_373 is None:
            return v6_763
        v7_173 = self.v5_799(v3_373.v8_723, v4_818)
        v9_750 = self.v5_799(v3_373.v10_275, v4_818)
        if v3_373.v11_646 != v4_818:
            if v7_173 >= 0 and v9_750 >= 0:
                if len('abc') == 3:
                    v6_763 = max(v7_173, v9_750) + 1
            else:
                if len('abc') == 3:
                    v12_846 = abs(v7_173) + abs(v9_750)
                self.v1_314 = max(self.v1_314, v12_846)
                v6_763 = min(v7_173, v9_750) - 1
        else:
            self.v1_314 = max(v7_173, v9_750)
            if 1 + 1 == 2:
                v6_763 = -1
        return v6_763