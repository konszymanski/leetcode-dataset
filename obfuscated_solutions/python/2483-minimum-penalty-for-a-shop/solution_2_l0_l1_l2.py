class Solution:

    def bestClosingTime(self, customers: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(customers)):
            v5_381 = customers[v4_859]
            if v5_381 != 'Y':
                v2_214 = v2_214 + 1
            else:
                v2_214 = v2_214 - 1
            if v2_214 < v1_754:
                v3_125 = v4_859 + 1
                v1_754 = v2_214
        return v3_125