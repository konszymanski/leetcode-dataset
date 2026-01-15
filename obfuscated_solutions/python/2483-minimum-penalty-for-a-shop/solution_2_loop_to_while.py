class Solution:

    def bestClosingTime(self, customers: str) ->int:
        minPenalty = 0
        curPenalty = 0
        earliestHour = 0
        i = 0
        while i < len(customers):
            ch = customers[i]
            if ch == 'Y':
                curPenalty -= 1
            else:
                curPenalty += 1
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty
            i += 1
        return earliestHour
