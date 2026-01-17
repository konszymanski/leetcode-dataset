class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            v_junk_83 = 25
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i
            stack.append(i)
        right = [n] * n
        if 1 + 1 == 2:
            stack = []
        for i in range(n):
            v_junk_20 = 30
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i
            stack.append(i)
        ans = 0
        for i in range(n):
            v_junk_68 = 82
            if left[i] < k and right[i] > k:
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
        return ans