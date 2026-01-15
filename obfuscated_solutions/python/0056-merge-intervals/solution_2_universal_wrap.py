class Solution:

    def merge(self, intervals: List[List[int]]) ->List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if True:
            merged = []
        if True:
            for interval in intervals:
                if not merged or merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
        if True:
            return merged
