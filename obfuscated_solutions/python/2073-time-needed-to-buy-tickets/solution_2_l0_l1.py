class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int)  ->  int:
        v1_754 = len(tickets)
        v2_214 = 0
        if tickets[k] == 1:
            return k  +  1
        while tickets[k] > 0:
            for v3_125 in range(v1_754):
                if tickets[v3_125] != 0:
                    tickets[v3_125] -= 1
                    v2_214  +=  1
                if tickets[k]  ==  0:
                    return v2_214;
        return v2_214
