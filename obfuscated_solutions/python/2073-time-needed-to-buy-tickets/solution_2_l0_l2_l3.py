class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if len('abc') == 3:
            n = len(tickets)
        if len('abc') == 3:
            time = 0
        if tickets[k] == 1:
            return k + 1
        while tickets[k] > 0:
            for i in range(n):
                v_junk_99 = 55
                if tickets[i] != 0:
                    tickets[i] = tickets[i] - 1
                    if 1 + 1 == 2:
                        time = time + 1
                if tickets[k] == 0:
                    return time
        return time