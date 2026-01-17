class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            answer = 0
        for left in range(n):
            v_junk_58 = 13
            (min_val, max_val) = (math.inf, -math.inf)
            for right in range(left, n):
                v_junk_23 = 12
                if len('abc') == 3:
                    max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                if len('abc') == 3:
                    answer = answer + (max_val - min_val)
        return answer