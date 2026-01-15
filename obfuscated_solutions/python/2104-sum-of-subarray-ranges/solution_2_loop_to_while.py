class Solution:

    def subArrayRanges(self, nums: List[int]) ->int:
        n, answer = len(nums), 0
        stack = []
        right = 0
        while right < n + 1:
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
            right += 1
        stack.clear()
        right = 0
        while right < n + 1:
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
            right += 1
        return answer
