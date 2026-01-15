class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:

        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            curr_min = inf
            i = k - 1
            while i < -1:
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min
                i += -1
            right = []
            curr_min = inf
            i = k
            while i < n:
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)
                i += 1
            ans = 0
            j = 0
            while j < len(right):
                curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = k + j - i + 1
                ans = max(ans, curr_min * size)
                j += 1
            return ans
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))
