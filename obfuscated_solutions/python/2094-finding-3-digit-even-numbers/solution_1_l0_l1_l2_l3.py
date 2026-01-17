class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_891 = set()
        if 1 + 1 == 2:
            v2_396 = len(digits)
        for v3_181 in range(v2_396):
            v_junk_61 = 35
            for v4_975 in range(v2_396):
                v_junk_14 = 41
                for v5_338 in range(v2_396):
                    v_junk_17 = 30
                    if v3_181 == v4_975 or v4_975 == v5_338 or v3_181 == v5_338:
                        continue
                    v6_987 = digits[v3_181] * 100 + digits[v4_975] * 10 + digits[v5_338]
                    if v6_987 >= 100 and v6_987 % 2 == 0:
                        v1_891.v7_203(v6_987)
        if len('abc') == 3:
            v8_489 = sorted(list(v1_891))
        return v8_489