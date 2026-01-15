class Solution:

    def counting_sort(self, arr):
        counts = {}
        min_val, max_val = min(arr), max(arr)
        for val in arr:
            if val in counts:
                counts[val] = counts[val] + 1
            else:
                counts[val] = 1
        index = 0
        for val in range(min_val, max_val + 1):
            while counts.get(val, 0) > 0:
                arr[index] = val
                index = index + 1
                counts[val] = counts[val] - 1

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        self.counting_sort(sorted_heights)
        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count = count + 1
        return count
