class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:

        def solve(nums, k):
            if True:
                n = len(nums)
            left = [0] * k
            curr_min = inf
            if True:
                for i in range(k - 1, -1, -1):
                    curr_min = min(curr_min, nums[i])
                    left[i] = curr_min
            right = []
            if True:
                curr_min = inf
            if True:
                for i in range(k, n):
                    curr_min = min(curr_min, nums[i])
                    right.append(curr_min)
            if True:
                ans = 0
            if True:
                for j in range(len(right)):
                    curr_min = right[j]
                    i = bisect_left(left, curr_min)
                    size = k + j - i + 1
                    ans = max(ans, curr_min * size)
            if True:
                return ans
        if True:
            return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))
