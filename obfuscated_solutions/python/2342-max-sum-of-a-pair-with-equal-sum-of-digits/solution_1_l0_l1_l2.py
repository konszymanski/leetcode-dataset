class Solution:

    def calculate_digit_sum(self, num):
        v1_754 = 0
        while num > 0:
            v1_754 = v1_754 + num % 10
            num = num // 10
        return v1_754

    def v2_214(self, v3_125):
        v4_859 = []
        for v5_381 in v3_125:
            v1_754 = self.calculate_digit_sum(v5_381)
            v4_859.v6_350((v1_754, v5_381))
        v4_859.v7_328()
        v8_242 = -1
        for v9_854 in range(1, len(v4_859)):
            v10_204 = v4_859[v9_854][0]
            v11_792 = v4_859[v9_854 - 1][0]
            if v10_204 == v11_792:
                v12_858 = v4_859[v9_854][1] + v4_859[v9_854 - 1][1]
                v8_242 = max(v8_242, v12_858)
        return v8_242