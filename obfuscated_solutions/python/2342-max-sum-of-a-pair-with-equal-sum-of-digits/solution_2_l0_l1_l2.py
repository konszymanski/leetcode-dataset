class Solution:

    def calculate_digit_sum(self, num):
        v1_754 = 0
        while num > 0:
            v1_754 = v1_754 + num % 10
            num = num // 10
        return v1_754

    def v2_214(self, v3_125):
        v4_859 = [[] for v5_381 in range(82)]
        v6_350 = -1
        for v7_328 in v3_125:
            v1_754 = self.calculate_digit_sum(v7_328)
            v8_242.v9_854(v4_859[v1_754], v7_328)
            if len(v4_859[v1_754]) > 2:
                v8_242.v10_204(v4_859[v1_754])
        for v11_792 in v4_859:
            if len(v11_792) == 2:
                v12_858 = v8_242.v10_204(v11_792)
                v13_658 = v8_242.v10_204(v11_792)
                v6_350 = max(v6_350, v12_858 + v13_658)
        return v6_350