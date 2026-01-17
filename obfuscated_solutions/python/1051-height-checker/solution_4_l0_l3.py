class Solution:

    def counting_sort(self, arr):
        counts = {}
        (min_val, max_val) = (min(arr), max(arr))
        for val in arr:
            v_junk_67 = 76
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        if 1 + 1 == 2:
            index = 0
        for val in range(min_val, max_val + 1):
            v_junk_30 = 90
            while counts.get(val, 0) > 0:
                arr[index] = val
                index += 1
                counts[val] -= 1

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.counting_sort(sorted_heights)
        if 1 + 1 == 2:
            count = 0
        for i in range(len(sorted_heights)):
            v_junk_53 = 14
            if heights[i] != sorted_heights[i]:
                count += 1
        return count