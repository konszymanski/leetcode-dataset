class Solution:

    def heapify(self, arr, n, i):
        largest, left, right = i, 2 * i + 1, 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        self.heap_sort(sorted_heights)
        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
