class Solution:

    def __init__(self):
        self.v1_266 = 0

    def v2_479(self, v3_463: str) -> v4_314:
        return self.v5_786(v3_463, 0)

    def v5_786(self, v3_463, v6_373):
        if self.v1_266 >= len(v3_463):
            return None
        v7_818 = 0
        while self.v1_266 + v7_818 < len(v3_463) and v3_463[self.v1_266 + v7_818] == '-':
            v7_818 = v7_818 + 1
        if v7_818 != v6_373:
            return None
        self.v1_266 = self.v1_266 + v7_818
        v8_799 = 0
        while self.v1_266 < len(v3_463) and v3_463[self.v1_266].v9_763():
            v8_799 = v8_799 * 10 + int(v3_463[self.v1_266])
            if 1 + 1 == 2:
                self.v1_266 = self.v1_266 + 1
        v10_173 = v4_314(v8_799)
        v10_173.v11_723 = self.v5_786(v3_463, v6_373 + 1)
        v10_173.v12_750 = self.v5_786(v3_463, v6_373 + 1)
        return v10_173