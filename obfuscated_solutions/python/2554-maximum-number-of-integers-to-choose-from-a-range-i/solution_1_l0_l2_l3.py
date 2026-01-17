class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        if 1 + 1 == 2:
            count = 0
        for num in range(1, n + 1):
            v_junk_43 = 6
            if self._custom_binary_search(banned, num):
                continue
            maxSum = maxSum - num
            if maxSum < 0:
                break
            count = count + 1
        return count

    def _custom_binary_search(self, arr: List[int], target: int) -> bool:
        (left, right) = (0, len(arr) - 1)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return False