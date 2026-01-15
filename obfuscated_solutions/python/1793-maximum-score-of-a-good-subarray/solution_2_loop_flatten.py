class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while True:
                if not (stack and nums[stack[-1]] > nums[i]):
                    break
                left[stack.pop()] = i
            stack.append(i)
        right = [n] * n
        stack = []
        for i in range(n):
            while True:
                if not (stack and nums[stack[-1]] > nums[i]):
                    break
                right[stack.pop()] = i
            stack.append(i)
        ans = 0
        for i in range(n):
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
        return ans
