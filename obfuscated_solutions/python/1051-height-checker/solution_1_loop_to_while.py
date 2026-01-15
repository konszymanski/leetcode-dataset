class Solution:

    def heightChecker(self, heights: List[int]) ->int:

        def bubble_sort():
            n = len(sorted_heights)
            i = 0
            while i < n - 1:
                for j in range(n - i - 1):
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        sorted_heights[j], sorted_heights[j + 1
                            ] = sorted_heights[j + 1], sorted_heights[j]
                i += 1
        sorted_heights = heights[:]
        bubble_sort()
        count = 0
        i = 0
        while i < len(sorted_heights):
            if heights[i] != sorted_heights[i]:
                count += 1
            i += 1
        return count
