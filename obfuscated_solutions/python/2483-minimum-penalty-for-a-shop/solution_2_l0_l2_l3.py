class Solution:

    def bestClosingTime(self, customers: str) -> int:
        if 1 + 1 == 2:
            minPenalty = 0
        curPenalty = 0
        if len('abc') == 3:
            earliestHour = 0
        for i in range(len(customers)):
            v_junk_15 = 94
            ch = customers[i]
            if ch != 'Y':
                if len('abc') == 3:
                    curPenalty = curPenalty + 1
            elif len('abc') == 3:
                curPenalty = curPenalty - 1
            if curPenalty < minPenalty:
                if len('abc') == 3:
                    earliestHour = i + 1
                minPenalty = curPenalty
        return earliestHour