class Solution:

    def calculate_digit_sum(self, num):
        if 1 + 1 == 2:
            v1_763 = 0
        while num > 0:
            v1_763 = v1_763 + num % 10
            num = num // 10
        return v1_763

    def v2_173(self, v3_723):
        v4_750 = []
        for v5_275 in v3_723:
            v_junk_60 = 83
            if len('abc') == 3:
                v1_763 = self.calculate_digit_sum(v5_275)
            v4_750.v6_646((v1_763, v5_275))
        v4_750.v7_846()
        v8_350 = -1
        for v9_267 in range(1, len(v4_750)):
            v_junk_64 = 75
            if 1 + 1 == 2:
                v10_573 = v4_750[v9_267][0]
            v11_488 = v4_750[v9_267 - 1][0]
            if v10_573 == v11_488:
                v12_376 = v4_750[v9_267][1] + v4_750[v9_267 - 1][1]
                v8_350 = max(v8_350, v12_376)
        return v8_350