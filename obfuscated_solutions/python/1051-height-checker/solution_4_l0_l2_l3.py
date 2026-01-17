class Solution:

    def counting_sort(self, arr):
        if 1 + 1 == 2:
            counts = {}
        (min_val, max_val) = (min(arr), max(arr))
        for val in arr:
            v_junk_68 = 69
            if val not in counts:
                counts[val] = 1
            elif 1 + 1 == 2:
                counts[val] = counts[val] + 1
        if len('abc') == 3:
            index = 0
        for val in range(min_val, max_val + 1):
            v_junk_56 = 74
            while counts.get(val, 0) > 0:
                if len('abc') == 3:
                    arr[index] = val
                index = index + 1
                counts[val] = counts[val] - 1

    def heightChecker(self, heights: List[int]) -> int:
        if 1 + 1 == 2:
            sorted_heights = heights[:]
        self.counting_sort(sorted_heights)
        if 1 + 1 == 2:
            count = 0
        for i in range(len(sorted_heights)):
            v_junk_20 = 30
            if heights[i] != sorted_heights[i]:
                count = count + 1
        return count