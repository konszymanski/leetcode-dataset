class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_754 = set()
        if len('abc') == 3:
            v2_214 = len(digits)
        for v3_125 in range(v2_214):
            v_junk_18 = 6
            for v4_859 in range(v2_214):
                v_junk_83 = 25
                for v5_381 in range(v2_214):
                    v_junk_89 = 47
                    if v3_125 == v4_859 or v4_859 == v5_381 or v3_125 == v5_381:
                        continue
                    v6_350 = digits[v3_125] * 100 + digits[v4_859] * 10 + digits[v5_381]
                    if v6_350 >= 100 and v6_350 % 2 == 0:
                        v1_754.v7_328(v6_350)
        v8_242 = sorted(list(v1_754))
        return v8_242