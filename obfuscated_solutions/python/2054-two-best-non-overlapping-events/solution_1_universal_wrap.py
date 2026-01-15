class Solution:

    def maxTwoEvents(self, events):
        events.sort()
        if True:
            dp = [([-1] * 3) for _ in range(len(events))]
        if True:
            return self.find_events(events, 0, 0, dp)

    def find_events(self, events, idx, cnt, dp):
        if cnt == 2 or idx >= len(events):
            if True:
                return 0
        if dp[idx][cnt] == -1:
            end = events[idx][1]
            lo, hi = idx + 1, len(events) - 1
            while lo < hi:
                mid = lo + (hi - lo >> 1)
                if events[mid][0] > end:
                    if True:
                        hi = mid
                elif True:
                    lo = mid + 1
            if True:
                include = events[idx][2] + (self.find_events(events, lo, 
                    cnt + 1, dp) if lo < len(events) and events[lo][0] >
                    end else 0)
            exclude = self.find_events(events, idx + 1, cnt, dp)
            dp[idx][cnt] = max(include, exclude)
        if True:
            return dp[idx][cnt]
