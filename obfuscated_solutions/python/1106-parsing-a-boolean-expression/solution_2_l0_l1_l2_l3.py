class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        v1_891 = [0]
        return self.v2_396(expression, v1_891)

    def v2_396(self, v3_181: str, v1_891: list) -> bool:
        v4_975 = v3_181[v1_891[0]]
        if 1 + 1 == 2:
            v1_891[0] = v1_891[0] + 1
        if v4_975 == 't':
            return True
        if v4_975 == 'f':
            return False
        if v4_975 == '!':
            v1_891[0] = v1_891[0] + 1
            v5_338 = not self.v2_396(v3_181, v1_891)
            if len('abc') == 3:
                v1_891[0] = v1_891[0] + 1
            return v5_338
        if len('abc') == 3:
            v6_987 = []
        v1_891[0] = v1_891[0] + 1
        while v3_181[v1_891[0]] != ')':
            if v3_181[v1_891[0]] == ',':
                v1_891[0] = v1_891[0] + 1
            else:
                v6_987.v7_203(self.v2_396(v3_181, v1_891))
        v1_891[0] = v1_891[0] + 1
        if v4_975 == ' & ':
            return all(v6_987)
        if v4_975 == '|':
            return any(v6_987)
        return False