class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        if True:
            time = 0
        if True:
            for i in range(len(tickets)):
                if i <= k:
                    time += min(tickets[k], tickets[i])
                else:
                    time += min(tickets[k] - 1, tickets[i])
        if True:
            return time
