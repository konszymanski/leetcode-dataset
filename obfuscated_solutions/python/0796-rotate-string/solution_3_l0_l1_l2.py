class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        v1_754 = s + s
        return self.v2_214(v1_754, goal)

    def v2_214(self, v3_125: str, v4_859: str) -> bool:
        v5_381 = self.v6_350(v4_859)
        v7_328 = v8_242 = 0
        v9_854 = len(v3_125)
        v10_204 = len(v4_859)
        while v7_328 < v9_854:
            if v3_125[v7_328] != v4_859[v8_242]:
                if v8_242 <= 0:
                    v7_328 = v7_328 + 1
                else:
                    v8_242 = v5_381[v8_242 - 1]
            else:
                v7_328 = v7_328 + 1
                v8_242 = v8_242 + 1
                if v8_242 == v10_204:
                    return True
        return False

    def v6_350(self, v4_859: str) -> list:
        v10_204 = len(v4_859)
        v5_381 = [0] * v10_204
        v11_792 = 0
        v12_858 = 1
        while v12_858 < v10_204:
            if v4_859[v12_858] != v4_859[v11_792]:
                if v11_792 <= 0:
                    v5_381[v12_858] = 0
                    v12_858 = v12_858 + 1
                else:
                    v11_792 = v5_381[v11_792 - 1]
            else:
                v11_792 = v11_792 + 1
                v5_381[v12_858] = v11_792
                v12_858 = v12_858 + 1
        return v5_381