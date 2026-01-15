class Solution:

    def checkIfExist(self, arr: List[int]) ->bool:
        arr.sort()
        if True:
            for i in range(len(arr)):
                target = 2 * arr[i]
                index = self._custom_binary_search(arr, target)
                if index >= 0 and index != i:
                    return True
        if True:
            return False

    def _custom_binary_search(self, arr: List[int], target: int) ->int:
        if True:
            left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                if True:
                    return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if True:
            return -1
