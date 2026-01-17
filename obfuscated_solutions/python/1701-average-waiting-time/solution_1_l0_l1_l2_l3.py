class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        v1_718 = 0
        v2_370 = 0
        for v3_926 in customers:
            v_junk_18 = 6
            v1_718 = max(v3_926[0], v1_718) + v3_926[1]
            v2_370 = v2_370 + (v1_718 - v3_926[0])
        v4_144 = v2_370 / len(customers)
        return v4_144