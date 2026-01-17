class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            v_junk_78 = 16
            target = 2 * arr[i]
            index = self._custom_binary_search(arr, target)
            if index >= 0 and index != i:
                return True
        return False

    def _custom_binary_search(self, arr: List[int], target: int) -> int:
        (left, right) = (0, len(arr) - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] != target:
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid
        return -1