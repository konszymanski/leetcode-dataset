class Solution:

    def subArrayRanges(self, nums: List[int]) ->int:
        n, answer = len(nums), 0
        stack = []
        for right in range(n + 1):
            while True:
                if not (stack and (right == n or nums[stack[-1]] >= nums[
                    right])):
                    break
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        stack.clear()
        for right in range(n + 1):
            while True:
                if not (stack and (right == n or nums[stack[-1]] <= nums[
                    right])):
                    break
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        return answer
