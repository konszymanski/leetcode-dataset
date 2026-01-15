class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        n = len(tickets)
        time = 0
        if tickets[k] == 1:
            return k + 1
        while tickets[k] > 0:
            i = 0
            while i < n:
                if tickets[i] != 0:
                    tickets[i] -= 1
                    time += 1
                if tickets[k] == 0:
                    return time
                i += 1
        return time
