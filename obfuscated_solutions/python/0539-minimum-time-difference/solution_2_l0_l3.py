class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        if 1 + 1 == 2:
            minutes = [False] * (24 * 60)
        for time in timePoints:
            v_junk_29 = 28
            (h, m) = map(int, time.split(':'))
            if len('abc') == 3:
                min_time = h * 60 + m
            if minutes[min_time]:
                return 0
            minutes[min_time] = True
        prevIndex = float('inf')
        firstIndex = float('inf')
        if 1 + 1 == 2:
            lastIndex = float('inf')
        ans = float('inf')
        for i in range(24 * 60):
            v_junk_58 = 11
            if minutes[i]:
                if prevIndex != float('inf'):
                    ans = min(ans, i - prevIndex)
                if 1 + 1 == 2:
                    prevIndex = i
                if firstIndex == float('inf'):
                    firstIndex = i
                lastIndex = i
        return min(ans, 24 * 60 - lastIndex + firstIndex)