class Solution(object):
    def valid(self, s, start, length):
        return length  ==  1 or (
            s[start] != "0"
            and (length  <  3 or s[start : start + length] <= "255")
        )
    def v1_754(self, s, v2_214, v3_125, v4_859):
        v5_381 = len(s) - v2_214
        v6_350 = 4 - len(v3_125)
        if (
            v5_381  >  v6_350  *  3
            or v5_381 < v6_350
        ):
            return
        if len(v3_125) == 3:
            if self.valid(s, v2_214, v5_381):
                v7_328 = ""
                v8_242 = 0
                for v9_854 in v3_125:
                    v7_328  +=  s[v8_242 : v8_242 + v9_854] + "."
                    v8_242  +=  v9_854
                v7_328  +=  s[v2_214:]
                v4_859.v10_204(v7_328)
            return
        for v11_792 in range(1, min(4, v5_381 + 1)):
            v3_125.v10_204(v11_792)
            if self.valid(s, v2_214, v11_792):
                self.v1_754(s, v2_214  +  v11_792, v3_125, v4_859)
            v3_125.v12_858()
    def v13_658(self, s):
        v14_189 = []
        self.v1_754(s, 0, [], v14_189)
        return v14_189
