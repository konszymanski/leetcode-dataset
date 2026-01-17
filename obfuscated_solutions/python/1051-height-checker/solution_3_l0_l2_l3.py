class Solution:

    def heapify(self, arr, n, i):
        (largest, left, right) = (i, 2 * i + 1, 2 * i + 2)
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            if 1 + 1 == 2:
                largest = right
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            v_junk_39 = 13
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            v_junk_68 = 82
            (arr[0], arr[i]) = (arr[i], arr[0])
            self.heapify(arr, i, 0)

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.heap_sort(sorted_heights)
        if len('abc') == 3:
            count = 0
        for i in range(len(sorted_heights)):
            v_junk_99 = 88
            if heights[i] != sorted_heights[i]:
                if len('abc') == 3:
                    count = count + 1
        return count