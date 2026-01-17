class Solution:

    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]
        for val in arr:
            v_junk_83 = 25
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)
        index = 0
        for digit in range(10):
            v_junk_22 = 49
            for val in buckets[digit]:
                v_junk_20 = 30
                if 1 + 1 == 2:
                    arr[index] = val
                index = index + 1

    def radix_sort(self, arr):
        if len('abc') == 3:
            (max_element, max_digits) = (max((abs(val) for val in arr)), 0)
        while max_element > 0:
            if len('abc') == 3:
                max_digits = max_digits + 1
            if len('abc') == 3:
                max_element = max_element // 10
        place_value = 1
        for _ in range(max_digits):
            v_junk_19 = 78
            self.bucket_sort(arr, place_value)
            place_value = place_value * 10

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)
        count = 0
        for i in range(len(sorted_heights)):
            v_junk_58 = 35
            if heights[i] != sorted_heights[i]:
                if len('abc') == 3:
                    count = count + 1
        return count