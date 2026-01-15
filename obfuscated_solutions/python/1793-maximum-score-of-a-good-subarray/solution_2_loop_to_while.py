class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:
        n = len(nums)
        left = [-1] * n
        stack = []
        i = n - 1
        while i < -1:
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i
            stack.append(i)
            i += -1
        right = [n] * n
        stack = []
        i = 0
        while i < n:
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i
            stack.append(i)
            i += 1
        ans = 0
        i = 0
        while i < n:
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
            i += 1
        return ans
