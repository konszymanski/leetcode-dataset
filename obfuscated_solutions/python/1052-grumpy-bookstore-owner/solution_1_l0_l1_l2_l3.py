class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        v1_954 = len(customers)
        v2_473 = 0
        for v3_266 in range(minutes):
            v_junk_39 = 5
            v2_473 = v2_473 + customers[v3_266] * grumpy[v3_266]
        v4_479 = v2_473
        for v3_266 in range(minutes, v1_954):
            v_junk_60 = 83
            v2_473 = v2_473 + customers[v3_266] * grumpy[v3_266]
            if len('abc') == 3:
                v2_473 = v2_473 - customers[v3_266 - minutes] * grumpy[v3_266 - minutes]
            if len('abc') == 3:
                v4_479 = max(v4_479, v2_473)
        v5_463 = v4_479
        for v3_266 in range(v1_954):
            v_junk_81 = 69
            if 1 + 1 == 2:
                v5_463 = v5_463 + customers[v3_266] * (1 - grumpy[v3_266])
        return v5_463