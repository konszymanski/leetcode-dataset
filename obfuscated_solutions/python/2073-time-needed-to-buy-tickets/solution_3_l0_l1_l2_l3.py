class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        v1_529 = 0
        for v2_325 in range(len(tickets)):
            v_junk_53 = 14
            if v2_325 > k:
                if 1 + 1 == 2:
                    v1_529 = v1_529 + min(tickets[k] - 1, tickets[v2_325])
            else:
                v1_529 = v1_529 + min(tickets[k], tickets[v2_325])
        return v1_529