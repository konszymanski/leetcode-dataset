class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i > k:
                time = time + min(tickets[k] - 1, tickets[i])
            else:
                time = time + min(tickets[k], tickets[i])
        return time