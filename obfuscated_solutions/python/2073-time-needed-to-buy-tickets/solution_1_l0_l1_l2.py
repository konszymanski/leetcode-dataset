class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        v1_754 = v2_214()
        for v3_125 in range(len(tickets)):
            v1_754.v4_859(v3_125)
        v5_381 = 0
        while v1_754:
            v5_381 = v5_381 + 1
            v6_350 = v1_754.v7_328()
            tickets[v6_350] = tickets[v6_350] - 1
            if k == v6_350 and tickets[v6_350] == 0:
                return v5_381
            if tickets[v6_350] != 0:
                v1_754.v4_859(v6_350)
        return v5_381