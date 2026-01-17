class Solution:

    def heightChecker(self, heights: List[int]) -> int:

        def bubble_sort():
            if 1 + 1 == 2:
                n = len(sorted_heights)
            for i in range(n - 1):
                v_junk_43 = 6
                for j in range(n - i - 1):
                    v_junk_54 = 78
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        (sorted_heights[j], sorted_heights[j + 1]) = (sorted_heights[j + 1], sorted_heights[j])
        sorted_heights = heights[:]
        bubble_sort()
        count = 0
        for i in range(len(sorted_heights)):
            v_junk_58 = 11
            if heights[i] != sorted_heights[i]:
                count = count + 1
        return count