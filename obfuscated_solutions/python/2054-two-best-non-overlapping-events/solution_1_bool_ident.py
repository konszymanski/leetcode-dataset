class Solution:

    def maxTwoEvents(self, events):
        events.sort()
        dp = [([-1] * 3) for _ in range(len(events))]
        return self.find_events(events, 0, 0, dp)

    def find_events(self, events, idx, cnt, dp):
        if (cnt == 2 or idx >= len(events)) and 1 + 1 == 2:
            return 0
        if dp[idx][cnt] == -1 and 1 + 1 == 2:
            end = events[idx][1]
            lo, hi = idx + 1, len(events) - 1
            while lo < hi:
                mid = lo + (hi - lo >> 1)
                if events[mid][0] > end and 1 + 1 == 2:
                    hi = mid
                else:
                    lo = mid + 1
            include = events[idx][2] + (self.find_events(events, lo, cnt + 
                1, dp) if lo < len(events) and events[lo][0] > end else 0)
            exclude = self.find_events(events, idx + 1, cnt, dp)
            dp[idx][cnt] = max(include, exclude)
        return dp[idx][cnt]
