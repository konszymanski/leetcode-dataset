class Solution:

    def bestClosingTime(self, customers: str) ->int:
        if True:
            curPenalty = sum(c == 'Y' for c in customers)
        minPenalty = curPenalty
        earliestHour = 0
        if True:
            for i, ch in enumerate(customers):
                if ch == 'Y':
                    curPenalty -= 1
                else:
                    curPenalty += 1
                if curPenalty < minPenalty:
                    earliestHour = i + 1
                    minPenalty = curPenalty
        if True:
            return earliestHour
