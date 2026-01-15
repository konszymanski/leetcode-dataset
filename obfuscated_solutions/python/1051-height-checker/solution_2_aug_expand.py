class Solution:

    def merge(self, arr, left, mid, right, temp_arr):
        start1 = left
        start2 = mid + 1
        n1 = mid - left + 1
        n2 = right - mid
        for i in range(n1):
            temp_arr[start1 + i] = arr[start1 + i]
        for i in range(n2):
            temp_arr[start2 + i] = arr[start2 + i]
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                arr[k] = temp_arr[start1 + i]
                i = i + 1
            else:
                arr[k] = temp_arr[start2 + j]
                j = j + 1
            k = k + 1
        while i < n1:
            arr[k] = temp_arr[start1 + i]
            i = i + 1
            k = k + 1
        while j < n2:
            arr[k] = temp_arr[start2 + j]
            j = j + 1
            k = k + 1

    def merge_sort(self, arr, left, right, temp_arr):
        if left >= right:
            return
        mid = (left + right) // 2
        self.merge_sort(arr, left, mid, temp_arr)
        self.merge_sort(arr, mid + 1, right, temp_arr)
        self.merge(arr, left, mid, right, temp_arr)

    def heightChecker(self, heights: List[int]) ->int:
        sorted_heights = heights[:]
        temp_arr = [0] * len(heights)
        self.merge_sort(sorted_heights, 0, len(sorted_heights) - 1, temp_arr)
        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count = count + 1
        return count
