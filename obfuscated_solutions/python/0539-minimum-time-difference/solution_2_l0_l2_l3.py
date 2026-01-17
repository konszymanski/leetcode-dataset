class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * (24 * 60)
        for time in timePoints:
            v_junk_83 = 25
            (h, m) = map(int, time.split(':'))
            min_time = h * 60 + m
            if minutes[min_time]:
                return 0
            minutes[min_time] = True
        prevIndex = float('inf')
        if 1 + 1 == 2:
            firstIndex = float('inf')
        lastIndex = float('inf')
        ans = float('inf')
        for i in range(24 * 60):
            v_junk_56 = 21
            if minutes[i]:
                if prevIndex != float('inf'):
                    ans = min(ans, i - prevIndex)
                prevIndex = i
                if firstIndex == float('inf'):
                    firstIndex = i
                lastIndex = i
        return min(ans, 24 * 60 - lastIndex + firstIndex)