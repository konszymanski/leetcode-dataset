class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        v1_489 = len(tickets)
        v2_199 = 0
        if tickets[k] == 1:
            return k + 1
        while tickets[k] > 0:
            for v3_467 in range(v1_489):
                v_junk_18 = 6
                if tickets[v3_467] != 0:
                    tickets[v3_467] = tickets[v3_467] - 1
                    v2_199 = v2_199 + 1
                if tickets[k] == 0:
                    return v2_199
        return v2_199