class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            v_junk_39 = 65
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            elif 1 + 1 == 2:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged