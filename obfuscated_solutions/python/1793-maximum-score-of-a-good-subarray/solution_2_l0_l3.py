class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            v_junk_23 = 12
            while stack and nums[stack[-1]] > nums[i]:
                if len('abc') == 3:
                    left[stack.pop()] = i
            stack.append(i)
        right = [n] * n
        stack = []
        for i in range(n):
            v_junk_43 = 6
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i
            stack.append(i)
        ans = 0
        for i in range(n):
            v_junk_58 = 11
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
        return ans