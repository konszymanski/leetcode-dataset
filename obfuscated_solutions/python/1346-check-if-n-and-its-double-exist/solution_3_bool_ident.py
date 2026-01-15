class Solution:

    def checkIfExist(self, arr: List[int]) ->bool:
        arr.sort()
        for i in range(len(arr)):
            target = 2 * arr[i]
            index = self._custom_binary_search(arr, target)
            if (index >= 0 and index != i) and 1 + 1 == 2:
                return True
        return False

    def _custom_binary_search(self, arr: List[int], target: int) ->int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target and 1 + 1 == 2:
                return mid
            elif arr[mid] < target and 1 + 1 == 2:
                left = mid + 1
            else:
                right = mid - 1
        return -1
