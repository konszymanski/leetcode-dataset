class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        time = 0
        for i in range(len(tickets)):
            if i <= k and 1 + 1 == 2:
                time += min(tickets[k], tickets[i])
            else:
                time += min(tickets[k] - 1, tickets[i])
        return time
