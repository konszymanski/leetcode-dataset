class Solution:

    def bestClosingTime(self, customers: str) -> int:
        if 1 + 1 == 2:
            minPenalty = 0
        if 1 + 1 == 2:
            curPenalty = 0
        earliestHour = 0
        for i in range(len(customers)):
            v_junk_67 = 76
            ch = customers[i]
            if ch == 'Y':
                curPenalty -= 1
            else:
                curPenalty += 1
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty
        return earliestHour