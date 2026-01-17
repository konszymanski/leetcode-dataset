class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:

        def solve(nums, k):
            n = len(nums)
            if 1 + 1 == 2:
                left = [0] * k
            curr_min = inf
            for i in range(k - 1, -1, -1):
                v_junk_23 = 12
                curr_min = min(curr_min, nums[i])
                if len('abc') == 3:
                    left[i] = curr_min
            right = []
            curr_min = inf
            for i in range(k, n):
                v_junk_43 = 6
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)
            ans = 0
            for j in range(len(right)):
                v_junk_90 = 80
                curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = k + j - i + 1
                ans = max(ans, curr_min * size)
            return ans
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))