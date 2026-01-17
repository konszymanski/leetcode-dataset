class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        v1_754 = len(customers)
        v2_214 = 0
        for v3_125 in range(minutes):
            v2_214 = v2_214 + customers[v3_125] * grumpy[v3_125]
        v4_859 = v2_214
        for v3_125 in range(minutes, v1_754):
            v2_214 = v2_214 + customers[v3_125] * grumpy[v3_125]
            v2_214 = v2_214 - customers[v3_125 - minutes] * grumpy[v3_125 - minutes]
            v4_859 = max(v4_859, v2_214)
        v5_381 = v4_859
        for v3_125 in range(v1_754):
            v5_381 = v5_381 + customers[v3_125] * (1 - grumpy[v3_125])
        return v5_381