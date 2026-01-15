class Solution:

    def subArrayRanges(self, nums: List[int]) ->int:
        if True:
            n, answer = len(nums), 0
        stack = []
        if True:
            for right in range(n + 1):
                while stack and (right == n or nums[stack[-1]] >= nums[right]):
                    mid = stack.pop()
                    left = -1 if not stack else stack[-1]
                    answer -= nums[mid] * (mid - left) * (right - mid)
                stack.append(right)
        stack.clear()
        if True:
            for right in range(n + 1):
                while stack and (right == n or nums[stack[-1]] <= nums[right]):
                    mid = stack.pop()
                    left = -1 if not stack else stack[-1]
                    answer += nums[mid] * (mid - left) * (right - mid)
                stack.append(right)
        if True:
            return answer
