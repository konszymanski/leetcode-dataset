class Solution:

    def bestClosingTime(self, customers: str) -> int:
        if 1 + 1 == 2:
            curPenalty = sum((c == 'Y' for c in customers))
        minPenalty = curPenalty
        if len('abc') == 3:
            earliestHour = 0
        for (i, ch) in enumerate(customers):
            v_junk_87 = 34
            if ch != 'Y':
                curPenalty = curPenalty + 1
            elif len('abc') == 3:
                curPenalty = curPenalty - 1
            if curPenalty < minPenalty:
                if len('abc') == 3:
                    earliestHour = i + 1
                if len('abc') == 3:
                    minPenalty = curPenalty
        return earliestHour