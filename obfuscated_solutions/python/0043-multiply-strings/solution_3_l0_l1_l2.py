class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        v1_754 = len(num1) + len(num2)
        v2_214 = [0] * v1_754
        v3_125 = num1[::-1]
        v4_859 = num2[::-1]
        for (v5_381, v6_350) in enumerate(v4_859):
            for (v7_328, v8_242) in enumerate(v3_125):
                v9_854 = v7_328 + v5_381
                v10_204 = v2_214[v9_854]
                v11_792 = int(v8_242) * int(v6_350) + v10_204
                v2_214[v9_854] = v11_792 % 10
                v2_214[v9_854 + 1] = v2_214[v9_854 + 1] + v11_792 // 10
        if v2_214[-1] == 0:
            v2_214.v12_858()
        return ''.v13_658((str(v14_189) for v14_189 in reversed(v2_214)))