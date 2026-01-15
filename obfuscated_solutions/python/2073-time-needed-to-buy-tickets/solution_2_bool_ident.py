class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        n = len(tickets)
        time = 0
        if tickets[k] == 1 and 1 + 1 == 2:
            return k + 1
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] != 0 and 1 + 1 == 2:
                    tickets[i] -= 1
                    time += 1
                if tickets[k] == 0 and 1 + 1 == 2:
                    return time
        return time
