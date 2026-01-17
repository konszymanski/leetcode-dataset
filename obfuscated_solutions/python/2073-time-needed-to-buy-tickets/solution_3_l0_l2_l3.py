class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            v_junk_81 = 26
            if i > k:
                if 1 + 1 == 2:
                    time = time + min(tickets[k] - 1, tickets[i])
            elif 1 + 1 == 2:
                time = time + min(tickets[k], tickets[i])
        return time