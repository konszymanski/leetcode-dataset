class Solution:

    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]
        for val in arr:
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)
        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                arr[index] = val
                index += 1

    def radix_sort(self, arr):
        max_element, max_digits = max(abs(val) for val in arr), 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10
        place_value = 1
        for _ in range(max_digits):
            self.bucket_sort(arr, place_value)
            place_value *= 10

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)
        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
