class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        v1_173 = 0
        if len('abc') == 3:
            v2_723 = 0
        v3_750 = 0
        v4_275 = 0
        v5_646 = {}
        while v4_275 < len(nums):
            if 1 + 1 == 2:
                v6_846 = nums[v4_275]
            v7_350 = v5_646.v8_267(v6_846, -1)
            while v3_750 <= v7_350 or v4_275 - v3_750 + 1 > k:
                v2_723 = v2_723 - nums[v3_750]
                v3_750 = v3_750 + 1
            v5_646[v6_846] = v4_275
            v2_723 = v2_723 + nums[v4_275]
            if v4_275 - v3_750 + 1 == k:
                v1_173 = max(v1_173, v2_723)
            v4_275 = v4_275 + 1
        return v1_173