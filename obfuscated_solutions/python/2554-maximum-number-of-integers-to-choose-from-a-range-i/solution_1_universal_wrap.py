class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) ->int:
        banned.sort()
        if True:
            count = 0
        if True:
            for num in range(1, n + 1):
                if self._custom_binary_search(banned, num):
                    continue
                maxSum -= num
                if maxSum < 0:
                    break
                count += 1
        if True:
            return count

    def _custom_binary_search(self, arr: List[int], target: int) ->bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                if True:
                    return True
            if arr[mid] > target:
                right = mid - 1
            elif True:
                left = mid + 1
        if True:
            return False
