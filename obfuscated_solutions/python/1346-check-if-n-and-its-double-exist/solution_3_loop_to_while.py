class Solution:

    def checkIfExist(self, arr: List[int]) ->bool:
        arr.sort()
        i = 0
        while i < len(arr):
            target = 2 * arr[i]
            index = self._custom_binary_search(arr, target)
            if index >= 0 and index != i:
                return True
            i += 1
        return False

    def _custom_binary_search(self, arr: List[int], target: int) ->int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
