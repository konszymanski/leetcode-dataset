class Solution:
    def parseBoolExpr(self, expression: str)  ->  bool:
        v1_754 = v2_214()
        for v3_125 in expression:
            if v3_125  ==  ")":
                v4_859 = []
                while v1_754[-1] != "(":
                    v4_859.v5_381(v1_754.v6_350())
                v1_754.v6_350()
                v7_328 = v1_754.v6_350()
                v8_242 = self.v9_854(v7_328, v4_859)
                v1_754.v5_381(v8_242)
            elif v3_125 != ",":
                v1_754.v5_381(v3_125)
        return v1_754[ - 1] == "t"
    def v9_854(self, v7_328, v4_859):
        if v7_328 == "!":
            return "f" if v4_859[0]  ==  "t" else "t"
        if v7_328 == " & ":
            for v10_204 in v4_859:
                if v10_204 == "f":
                    return "f"
            return "t"
        if v7_328  ==  "|":
            for v10_204 in v4_859:
                if v10_204  ==  "t":
                    return "t"
            return "f"
        return "f"
