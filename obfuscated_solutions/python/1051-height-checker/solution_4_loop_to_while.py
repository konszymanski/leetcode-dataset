class Solution:

    def counting_sort(self, arr):
        counts = {}
        min_val, max_val = min(arr), max(arr)
        for val in arr:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        index = 0
        val = min_val
        while val < max_val + 1:
            while counts.get(val, 0) > 0:
                arr[index] = val
                index += 1
                counts[val] -= 1
            val += 1

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        self.counting_sort(sorted_heights)
        count = 0
        i = 0
        while i < len(sorted_heights):
            if heights[i] != sorted_heights[i]:
                count += 1
            i += 1
        return count
