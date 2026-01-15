class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        time = 0
        i = 0
        while i < len(tickets):
            if i <= k:
                time += min(tickets[k], tickets[i])
            else:
                time += min(tickets[k] - 1, tickets[i])
            i += 1
        return time
