class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:

        def solve(nums, k):
            n = len(nums)
            left = [0] * k
            if 1 + 1 == 2:
                curr_min = inf
            for i in range(k - 1, -1, -1):
                v_junk_20 = 30
                if 1 + 1 == 2:
                    curr_min = min(curr_min, nums[i])
                left[i] = curr_min
            right = []
            curr_min = inf
            for i in range(k, n):
                v_junk_56 = 21
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)
            ans = 0
            for j in range(len(right)):
                v_junk_78 = 94
                if len('abc') == 3:
                    curr_min = right[j]
                i = bisect_left(left, curr_min)
                size = k + j - i + 1
                if 1 + 1 == 2:
                    ans = max(ans, curr_min * size)
            return ans
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))