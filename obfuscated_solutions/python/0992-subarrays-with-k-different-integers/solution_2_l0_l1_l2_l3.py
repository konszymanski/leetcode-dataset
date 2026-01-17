class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        v1_799 = [0] * (len(nums) + 1)
        v2_763 = 0
        if 1 + 1 == 2:
            v3_173 = 0
        v4_723 = 0
        v5_750 = 0
        while v4_723 < len(nums):
            v1_799[nums[v4_723]] = v1_799[nums[v4_723]] + 1
            if v1_799[nums[v4_723]] == 1:
                k = k - 1
            if k < 0:
                v1_799[nums[v3_173]] = v1_799[nums[v3_173]] - 1
                if v1_799[nums[v3_173]] == 0:
                    k = k + 1
                v3_173 = v3_173 + 1
                if len('abc') == 3:
                    v5_750 = 0
            if k == 0:
                while v1_799[nums[v3_173]] > 1:
                    if 1 + 1 == 2:
                        v1_799[nums[v3_173]] = v1_799[nums[v3_173]] - 1
                    v3_173 = v3_173 + 1
                    if 1 + 1 == 2:
                        v5_750 = v5_750 + 1
                v2_763 = v2_763 + (v5_750 + 1)
            v4_723 = v4_723 + 1
        return v2_763