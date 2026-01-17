class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        v1_754 = 0
        for v2_214 in range(len(tickets)):
            if v2_214 <= k:
                v1_754 += min(tickets[k], tickets[v2_214])
            else:
                v1_754  +=  min(tickets[k]  -  1, tickets[v2_214])
        return v1_754
