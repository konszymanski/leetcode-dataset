class Solution:

    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]
        for val in arr:
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)
        index = 0
        digit = 0
        while digit < 10:
            for val in buckets[digit]:
                arr[index] = val
                index += 1
            digit += 1

    def radix_sort(self, arr):
        max_element, max_digits = max(abs(val) for val in arr), 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10
        place_value = 1
        _ = 0
        while _ < max_digits:
            self.bucket_sort(arr, place_value)
            place_value *= 10
            _ += 1

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)
        count = 0
        i = 0
        while i < len(sorted_heights):
            if heights[i] != sorted_heights[i]:
                count += 1
            i += 1
        return count
