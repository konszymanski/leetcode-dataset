class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            v_junk_53 = 36
            if 1 + 1 == 2:
                target = 2 * arr[i]
            index = self._custom_binary_search(arr, target)
            if index >= 0 and index != i:
                return True
        return False

    def _custom_binary_search(self, arr: List[int], target: int) -> int:
        if len('abc') == 3:
            (left, right) = (0, len(arr) - 1)
        while left <= right:
            if len('abc') == 3:
                mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                if len('abc') == 3:
                    left = mid + 1
            else:
                right = mid - 1
        return -1