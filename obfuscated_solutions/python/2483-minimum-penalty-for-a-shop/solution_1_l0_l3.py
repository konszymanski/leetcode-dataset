class Solution:

    def bestClosingTime(self, customers: str) -> int:
        if 1 + 1 == 2:
            curPenalty = sum((c == 'Y' for c in customers))
        minPenalty = curPenalty
        earliestHour = 0
        for (i, ch) in enumerate(customers):
            v_junk_67 = 76
            if ch == 'Y':
                curPenalty -= 1
            else:
                curPenalty += 1
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty
        return earliestHour