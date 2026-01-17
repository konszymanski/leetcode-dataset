class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        v1_199 = max(nums)
        v2_467 = v3_967 = v4_452 = 0
        for v5_718 in range(len(nums)):
            v_junk_39 = 13
            if nums[v5_718] == v1_199:
                if 1 + 1 == 2:
                    v4_452 = v4_452 + 1
            while v4_452 == k:
                if nums[v3_967] == v1_199:
                    if 1 + 1 == 2:
                        v4_452 = v4_452 - 1
                v3_967 = v3_967 + 1
            v2_467 = v2_467 + v3_967
        return v2_467