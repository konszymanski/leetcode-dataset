class Solution:

    def bestClosingTime(self, customers: str) -> int:
        v1_754 = sum((v2_214 == 'Y' for v2_214 in customers))
        v3_125 = v1_754
        v4_859 = 0
        for (v5_381, v6_350) in enumerate(customers):
            if v6_350 != 'Y':
                v1_754 = v1_754 + 1
            else:
                v1_754 = v1_754 - 1
            if v1_754 < v3_125:
                v4_859 = v5_381 + 1
                v3_125 = v1_754
        return v4_859