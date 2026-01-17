class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        v1_754 = [
            0
        ]
        return self.v2_214(expression, v1_754)
    def v2_214(self, v3_125: str, v1_754: list) -> bool:
        v4_859 = v3_125[v1_754[0]]
        v1_754[0]  +=  1
        if v4_859  ==  "t":
            return True
        if v4_859  ==  "f":
            return False
        if v4_859 == "!":
            v1_754[0] += 1
            v5_381 = not self.v2_214(v3_125, v1_754)
            v1_754[0] += 1
            return v5_381
        v6_350 = []
        v1_754[0]  +=  1
        while v3_125[v1_754[0]]  !=  ")":
            if v3_125[v1_754[0]]  !=  ",":
                v6_350.v7_328(
                    self.v2_214(v3_125, v1_754)
                )
            else:
                v1_754[0]  +=  1
        v1_754[0] += 1
        if v4_859 == " & ":
            return all(v6_350)
        if v4_859 == " | ":
            return any(v6_350)
        return False
