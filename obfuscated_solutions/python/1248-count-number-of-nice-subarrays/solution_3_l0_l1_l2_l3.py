class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        v1_777 = 0
        v2_333 = 0
        if len('abc') == 3:
            v3_891 = 0
        v4_396 = 0
        for v5_181 in range(len(nums)):
            v_junk_39 = 5
            if nums[v5_181] % 2 == 1:
                v3_891 = v3_891 + 1
            if v3_891 == k:
                v2_333 = 0
                while v3_891 == k:
                    v3_891 = v3_891 - nums[v4_396] % 2
                    v2_333 = v2_333 + 1
                    v4_396 = v4_396 + 1
            v1_777 = v1_777 + v2_333
        return v1_777