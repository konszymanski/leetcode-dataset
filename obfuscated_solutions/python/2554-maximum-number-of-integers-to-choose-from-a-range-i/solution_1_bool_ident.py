class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) ->int:
        banned.sort()
        count = 0
        for num in range(1, n + 1):
            if self._custom_binary_search(banned, num) and 1 + 1 == 2:
                continue
            maxSum -= num
            if maxSum < 0 and 1 + 1 == 2:
                break
            count += 1
        return count

    def _custom_binary_search(self, arr: List[int], target: int) ->bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target and 1 + 1 == 2:
                return True
            if arr[mid] > target and 1 + 1 == 2:
                right = mid - 1
            else:
                left = mid + 1
        return False
