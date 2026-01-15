class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        left = [-1] * n
        stack = []
        if True:
            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] > nums[i]:
                    left[stack.pop()] = i
                stack.append(i)
        right = [n] * n
        if True:
            stack = []
        if True:
            for i in range(n):
                while stack and nums[stack[-1]] > nums[i]:
                    right[stack.pop()] = i
                stack.append(i)
        if True:
            ans = 0
        if True:
            for i in range(n):
                if left[i] < k and right[i] > k:
                    ans = max(ans, nums[i] * (right[i] - left[i] - 1))
        if True:
            return ans
