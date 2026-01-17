class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in customers:
            v1_754 = max(v3_125[0], v1_754)  +  v3_125[1]
            v2_214 += v1_754  -  v3_125[0]
        v4_859 = v2_214  /  len(customers)
        return v4_859
